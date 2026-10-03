const assert = require('node:assert/strict');
require('../static/plan-api.js');
(async () => {
  const originalFetch = global.fetch;
  const originalTimeout = global.setTimeout;
  const body = {blocks:['arrival'],profile:{citizenship:'italian'},story:'generic goals'};
  const plan = {ai_generated:true,steps:[{id:'arrival--orientation'}]};
  let calls, waits;
  const response = (status, data) => ({ok:status===200,status,json:async()=>data});
  async function scenario(sequence) {
    calls=[];waits=[];
    global.fetch=async (url,options)=>{
      calls.push({url,body:options.body});const item=sequence.shift();
      if(item instanceof Error)throw item;
      return item;
    };
    global.setTimeout=(fn,ms)=>{waits.push(ms);fn();};
    return StudyPlanAPI.generate(body);
  }
  try {
    assert.deepEqual(await scenario([response(502,null),response(200,plan)]),plan);
    assert.equal(calls.length,2);assert.deepEqual(calls[0],calls[1]);assert.deepEqual(waits,[2000]);
    assert.deepEqual(await scenario([new TypeError('Failed to fetch'),response(200,plan)]),plan);
    assert.equal(calls.length,2);
    assert.deepEqual(await scenario([response(503,{message:'Application failed to respond'}),response(200,plan)]),plan);
    assert.equal(calls.length,2);
    await assert.rejects(scenario([response(504,null),response(504,null)]),/PLAN_CONNECTION_INTERRUPTED/);
    assert.equal(calls.length,2);
    await assert.rejects(scenario([new TypeError('Failed to fetch'),new TypeError('Failed to fetch')]),/PLAN_CONNECTION_INTERRUPTED/);
    assert.equal(calls.length,2);
    for(const [status,detail] of [[502,'PLAN_GENERATION_FAILED'],[502,'CLAUDE_REQUEST_FAILED'],[503,'CLAUDE_NOT_CONFIGURED'],[429,'CHAT_LIMIT_REACHED'],[422,'PLAN_NEEDS_ANSWERS']]) {
      await assert.rejects(scenario([response(status,{detail})]),new RegExp(detail));
      assert.equal(calls.length,1);assert.equal(waits.length,0);
    }
    console.log('PASS: interrupted AI requests recover once with identical input; application errors and budgets never retry');
  } finally {global.fetch=originalFetch;global.setTimeout=originalTimeout;}
})().catch(error=>{console.error(error);process.exit(1)});
