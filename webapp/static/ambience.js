"use strict";
(() => {
  const video = document.querySelector("#city-video");
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

  async function syncPlayback() {
    if (reducedMotion.matches || document.hidden) {
      video.pause();
      return;
    }
    if (!video.getAttribute("src")) video.src = video.dataset.src;
    video.defaultPlaybackRate = 0.5;
    video.playbackRate = 0.5;
    try {
      await video.play();
    } catch {
      // Keep the still background if the browser blocks autoplay.
    }
  }

  video.addEventListener("playing", () => {
    video.parentElement.classList.add("is-ready");
  });
  video.addEventListener("error", () => {
    video.parentElement.classList.remove("is-ready");
  });
  reducedMotion.addEventListener("change", syncPlayback);
  document.addEventListener("visibilitychange", syncPlayback);
  syncPlayback();
})();
