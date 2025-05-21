document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', function() {
    document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
    this.classList.add('active');
  });
});

document.querySelector('.contact-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  // Should include code like this to submit to /api/messages
  fetch('/api/messages', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      name: nameInput.value,
      email: emailInput.value,
      message: messageInput.value
    })
  })
});
document.addEventListener('mousemove', function(e) {
  const bubble = document.getElementById('cursor-bubble');
  bubble.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
});
// Add this to your style.css for smooth animations
```css:c%3A%2FUsers%2Fritis%2FOneDrive%2Fportfolio%2Fstyle.css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(20px); }
}
```


