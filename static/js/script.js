// function searchEntries() {
//     let input = document.getElementById("search").value.toLowerCase();
//     let entries = document.querySelectorAll(".entry");
  
//     entries.forEach(entry => {
//       let app = entry.getAttribute("data-app").toLowerCase();
//       entry.style.display = app.includes(input) ? "block" : "none";
//     });
// }

// function searchEntries() {
//   let input = document.getElementById("search").value.trim().toLowerCase();
//   let entries = document.querySelectorAll(".entry");

//   entries.forEach(entry => {
//       let app = entry.getAttribute("data-app");
      
//       // Check if data-app exists and is not empty
//       if (app && app.trim() !== "") {
//           let appValue = app.toLowerCase();
//           entry.style.display = appValue.includes(input) ? "block" : "none";
//       } else {
//           // Hide empty entries
//           entry.style.display = "none";
//       }
//   });
// }

function searchEntries() {
  let input = document.getElementById("search").value.trim().toLowerCase();

  let allCards = document.querySelectorAll(".card");

  allCards.forEach(card => {
    const entries = card.querySelectorAll(".entry");
    let hasVisibleEntry = false;

    entries.forEach(entry => {
      const app = entry.getAttribute("data-app");

      if (app && app.trim().toLowerCase().includes(input)) {
        entry.style.display = "block";
        hasVisibleEntry = true;
      } else {
        entry.style.display = "none";
      }
    });

    // Show or hide the entire card based on whether it has visible entries
    card.style.display = hasVisibleEntry ? "block" : "none";
  });
}



function toggleEditForm(key) {
    const form = document.getElementById("editForm-" + key);
    form.style.display = form.style.display === "none" ? "block" : "none";
}

 // Toggle form visibility
const formToggle = document.getElementById('formToggle');
const formFields = document.getElementById('formFields');
const toggleIcon = document.getElementById('toggleIcon');
 
formToggle.addEventListener('click', function() {
  formFields.classList.toggle('show');
     
    // Rotate icon
    if (formFields.classList.contains('show')) {
        toggleIcon.style.transform = 'rotate(180deg)';
    } else {
        toggleIcon.style.transform = 'rotate(0)';
    }
});


// Function to copy text from the .text-copy element to clipboard using document.execCommand()
function copyToClipboard() {
  // Get the text from the .text-copy element
  const textToCopy = document.querySelector(".text-copy").textContent;

  // Create a temporary textarea element
  const tempInput = document.createElement("textarea");
  tempInput.value = textToCopy;
  document.body.appendChild(tempInput);
  tempInput.select();  // Select the text
  document.execCommand("copy");  // Copy the text to clipboard
  document.body.removeChild(tempInput);  // Remove the temporary textarea

  // Show the tooltip with "Copied!" message
  const tooltip = document.querySelector(".copy-link .tooltip");
  tooltip.textContent = "Copied!";
  tooltip.classList.add("show-tooltip");

  // Reset the tooltip text after 1.5 seconds
  setTimeout(() => {
      tooltip.textContent = "Copy";
      tooltip.classList.remove("show-tooltip");
  }, 1500);
}

// Trigger the function when the copy link is clicked
document.querySelector(".copy-link").onclick = function(event) {
  event.preventDefault();  // Prevent default anchor behavior
  copyToClipboard();  // Call the copy function
};


document.getElementById('formToggle').addEventListener('click', () => {
  const fields = document.getElementById('formFields');
  const icon = document.getElementById('toggleIcon');
  fields.style.display = (fields.style.display === 'none' || fields.style.display === '') ? 'block' : 'none';
  icon.classList.toggle('fa-chevron-down');
  icon.classList.toggle('fa-chevron-up');
});

// Disable right click
document.addEventListener('contextmenu', event => event.preventDefault());

// Block common devtools keys
document.addEventListener('keydown', function(e) {
  if (
    e.key === "F12" || 
    (e.ctrlKey && e.shiftKey && ["I", "J", "C"].includes(e.key)) ||
    (e.ctrlKey && e.key === "U")
  ) {
    e.preventDefault();
  }
});

// Detect if DevTools is open
(function() {
  const threshold = 160;
  setInterval(() => {
    const devtools = window.outerWidth - window.innerWidth > threshold || 
                     window.outerHeight - window.innerHeight > threshold;
    if (devtools) {
      document.body.innerHTML = "<h1>DevTools is not allowed</h1>";
    }
  }, 1000);
})();