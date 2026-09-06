const toast = document.querySelector(".toast");
const card = document.querySelector("[data-game-card]");
const counter = document.querySelector(".counter");
const games = [
  {
    title: "Minecraft",
    studio: "MOJANG STUDIOS",
    mode: "CREATIVE<br>MODE",
    platform: "PC",
    tags: ["Sandbox", "Adventure", "Survival"],
    description:
      "Build, explore, survive and unleash your creativity in a world made of blocks. Endless possibilities are waiting.",
    rating: "4.6",
    reviews: "2M+ reviews",
    image:
      "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?auto=format&fit=crop&w=1000&q=85",
  },
  {
    title: "Hades II",
    studio: "SUPERGIANT GAMES",
    mode: "WITCH<br>CRAFT",
    platform: "PC",
    tags: ["Action", "Roguelike", "Mythology"],
    description:
      "Battle beyond the Underworld using dark sorcery and legendary weapons in a stylish mythic adventure.",
    rating: "4.8",
    reviews: "128K+ reviews",
    image:
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1000&q=85",
  },
  {
    title: "No Man's Sky",
    studio: "HELLO GAMES",
    mode: "BEYOND<br>THE STARS",
    platform: "PC / MOBILE",
    tags: ["Exploration", "Sci-fi", "Survival"],
    description:
      "Chart your own course through an infinite universe of strange worlds, ancient ruins and new discoveries.",
    rating: "4.5",
    reviews: "310K+ reviews",
    image:
      "https://images.unsplash.com/photo-1446776877081-d282a0f896e2?auto=format&fit=crop&w=1000&q=85",
  },
  {
    title: "Stardew Valley",
    studio: "CONCERNEDAPE",
    mode: "FIND YOUR<br>WAY HOME",
    platform: "MOBILE",
    tags: ["Cozy", "Farming", "RPG"],
    description:
      "Turn an overgrown field into a thriving home, make friends and build a life at your own pace.",
    rating: "4.9",
    reviews: "890K+ reviews",
    image:
      "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=85",
  },
];
let currentGame = 0;
let savedGames = JSON.parse(localStorage.getItem("playnext-saved") || "[]");
let startX = 0;
let currentX = 0;
let isDragging = false;
let toastTimer;

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("show"), 2200);
}

function updateSavedLabel() {
  document.querySelector(".saved-label").textContent = savedGames.length
    ? `Saved ${savedGames.length}`
    : "Saved";
}

document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-toast]");
  if (button) showToast(button.dataset.toast);
});

document.querySelector(".scroll-button").addEventListener("click", () => {
  showToast("Drag right to save, left to pass");
});

function renderGame(game) {
  card
    .querySelector(".artwork")
    .style.setProperty("--game-image", `url("${game.image}")`);
  card.querySelector(".artwork-copy span").textContent = game.studio;
  card.querySelector(".artwork-copy strong").innerHTML = game.mode;
  card.querySelector(".platform-badge").innerHTML =
    `<span>▣</span> ${game.platform}`;
  card.querySelector(".tags").innerHTML = game.tags
    .map((tag) => `<span>${tag}</span>`)
    .join("");
  card.querySelector("h2").textContent = game.title;
  card.querySelector(".description").textContent = game.description;
  card.querySelector(".rating strong").textContent = game.rating;
  card.querySelector(".rating span:last-child").textContent = game.reviews;
  card.querySelector(".primary-button").dataset.toast = `Opening ${game.title}`;
  card.querySelector(".secondary-button").dataset.toast =
    `${game.title} details`;
  card.setAttribute(
    "aria-label",
    `Swipe card to save or dismiss ${game.title}`,
  );
  counter.innerHTML = `${String(currentGame + 1).padStart(2, "0")} <i>/</i> ${String(games.length).padStart(2, "0")}`;
}

function finishSwipe(direction) {
  const saved = direction === "right";
  const game = games[currentGame];
  if (
    saved &&
    !savedGames.some((savedGame) => savedGame.title === game.title)
  ) {
    savedGames.push({ title: game.title, image: game.image });
    localStorage.setItem("playnext-saved", JSON.stringify(savedGames));
    updateSavedLabel();
  }
  card.classList.add("is-swiping");
  card.style.transform = `translateX(${saved ? "120%" : "-120%"}) rotate(${saved ? "14deg" : "-14deg"})`;
  card.style.opacity = "0";

  setTimeout(() => {
    showToast(saved ? `${game.title} saved` : `${game.title} passed`);
    currentGame += 1;
    if (currentGame >= games.length) {
      card.innerHTML =
        '<div class="empty-state"><span>✦</span><h2>You\'re all caught up</h2><p>Come back soon for more games to discover.</p><button class="primary-button" type="button">Start over</button></div>';
      card.querySelector("button").addEventListener("click", () => {
        currentGame = 0;
        card.innerHTML = initialCardMarkup;
        renderGame(games[currentGame]);
      });
    } else {
      renderGame(games[currentGame]);
    }
    card.classList.remove("is-swiping");
    card.style.transform = "";
    card.style.opacity = "";
    card.animate(
      [
        { transform: "translateY(14px)", opacity: 0 },
        { transform: "translateY(0)", opacity: 1 },
      ],
      { duration: 360, easing: "ease-out" },
    );
  }, 420);
}

const initialCardMarkup = card.innerHTML;
card.addEventListener("pointerdown", (event) => {
  if (event.target.closest("button, a") || currentGame >= games.length) return;
  startX = event.clientX;
  currentX = startX;
  isDragging = true;
  card.classList.add("is-dragging");
  card.setPointerCapture(event.pointerId);
});
card.addEventListener("pointermove", (event) => {
  if (!isDragging) return;
  currentX = event.clientX;
  const delta = currentX - startX;
  card.style.transform = `translateX(${delta}px) rotate(${delta * 0.035}deg)`;
});
card.addEventListener("pointerup", () => {
  if (!isDragging) return;
  isDragging = false;
  card.classList.remove("is-dragging");
  const delta = currentX - startX;
  card.style.transform = "";
  if (Math.abs(delta) > 90) finishSwipe(delta > 0 ? "right" : "left");
});
card.addEventListener("pointercancel", () => {
  isDragging = false;
  card.classList.remove("is-dragging");
  card.style.transform = "";
});

renderGame(games[currentGame]);
updateSavedLabel();
