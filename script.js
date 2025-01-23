const mapImage = document.querySelector('.map-image');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  const imagePosition = mapImage.offsetTop;

  if (scrollPosition >= imagePosition - window.innerHeight * 0.5) {
    mapImage.classList.add('visible');
  } else {
    mapImage.classList.remove('visible');
  }
});

// Wait for the DOM to fully load
// document.addEventListener("DOMContentLoaded", () => {
//     // Select all videos with the class 'hover-play'
//     const videos = document.querySelectorAll(".hover-play");
  
//     // Add event listeners for mouseenter and mouseleave
//     videos.forEach((video) => {
//       // Play the video on hover
//       video.addEventListener("mouseenter", () => {
//         video.play();
//       });
  
//       // Pause the video when the mouse leaves
//       video.addEventListener("mouseleave", () => {
//         video.pause();
//         video.currentTime = 0; // Reset video to the start
//       });
//     });
//   });  


// Select all video elements
const videos = document.querySelectorAll("video");

// Add event listeners for each video
videos.forEach((video) => {
  // Play the video on mouseover
  video.addEventListener("mouseover", () => {
    video.play();
  });

  // Pause the video on mouseout
  video.addEventListener("mouseout", () => {
    video.pause();
    video.currentTime = 0; // Reset the video to the start if desired
  });
});