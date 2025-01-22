
// document.addEventListener("DOMContentLoaded", () => {
//     const timeline = document.querySelector(".timeline");
//     const events = document.querySelectorAll(".timeline-event");
  
//     function animateTimeline() {
//       const viewportHeight = window.innerHeight;
  
//       events.forEach((event, index) => {
//         const rect = event.getBoundingClientRect();
//         const eventPosition = rect.top + rect.height / 2;
  
//         // Check if the event is in the viewport
//         if (eventPosition < viewportHeight) {
//           // Increase the blue line height
//           const progressHeight = (index + 1) / events.length * 100;
//           timeline.style.setProperty("--line-progress", progressHeight + "%");
  
//           // Highlight the current event
//           event.querySelector("::before").style.backgroundColor = "yellow";
//         }
//       });
//     }
  
//     window.addEventListener("scroll", animateTimeline);
//     animateTimeline(); // Run initially
//   });
  