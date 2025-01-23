// Select all video elements inside the cards
const videos = document.querySelectorAll('video');

// Add event listeners to each video
videos.forEach(video => {
  video.addEventListener('mouseenter', () => {
    video.play();  // Play the video when hovered
  });

  video.addEventListener('mouseleave', () => {
    video.pause();  // Pause the video when mouse leaves
    video.currentTime = 0;  // Reset the video to the first frame
  });
});

