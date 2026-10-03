"use strict";
(() => {
  const video = document.querySelector("#city-video");
  const toggle = document.querySelector("#ambience-toggle");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  let wantsMotion = !reducedMotion.matches;

  function updateControl() {
    const playing = !video.paused;
    const english = document.documentElement.lang === "en";
    const label = english
      ? playing ? "Pause background" : "Play background"
      : playing ? "Ferma lo sfondo" : "Anima lo sfondo";
    toggle.dataset.playing = String(playing);
    toggle.setAttribute("aria-label", label);
    toggle.title = label;
  }

  async function syncPlayback() {
    if (!wantsMotion || document.hidden) {
      video.pause();
      return;
    }
    if (!video.getAttribute("src")) video.src = video.dataset.src;
    video.defaultPlaybackRate = 0.5;
    video.playbackRate = 0.5;
    try {
      await video.play();
    } catch {
      // Keep the poster and let the user start playback if autoplay is blocked.
      updateControl();
    }
  }

  video.addEventListener("playing", () => {
    video.parentElement.classList.add("is-ready");
    updateControl();
  });
  video.addEventListener("pause", updateControl);
  video.addEventListener("error", () => {
    video.parentElement.classList.remove("is-ready");
    toggle.hidden = true;
  });
  toggle.addEventListener("click", () => {
    wantsMotion = video.paused;
    syncPlayback();
  });
  reducedMotion.addEventListener("change", () => {
    wantsMotion = !reducedMotion.matches;
    syncPlayback();
  });
  document.addEventListener("visibilitychange", syncPlayback);
  new MutationObserver(updateControl).observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["lang"],
  });
  toggle.hidden = false;
  updateControl();
  syncPlayback();
})();
