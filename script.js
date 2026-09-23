const artworks = [
  {
    img: "images/no_signal.jpg",
    link: "https://x.com/NeoRu18436"
  },
  {
    img: "images/dino.jpg",
    link:"https://x.com/Dino_illus"
  },
  {
    img: "images/low_energy.jpg",
    link: "https://x.com/nemupanart"
    },
  {
    img: "images/whatever_you_were.jpg",
    link: "https://x.com/mothidss"
  },
  {
    img: "images/dooby_oru.jpg",
    link: "https://x.com/orobou"
  },
   {
    img: "images/ralsei.jpg",
    link: "https://x.com/Not_Merritz"
  },
  {
    img: "images/tana.jpg",
    link: "https://x.com/LubyPiercing"
  },
  {
    img: "images/eddie.png",
    link: "https://www.instagram.com/kaybebop_/?hl=en"
  },
  {
    img: "images/tama.jpeg",
    link: "https://x.com/tama00001234"
  },
  {
    img: "images/bunnies.jpg",
    link: "https://x.com/yura_inaho"
  }
];



const today = new Date();
const index = today.getDate() % artworks.length;

// Set image
document.getElementById("daily-image").src = artworks[index].img;

// Set link
document.getElementById("daily-link").href = artworks[index].link;






// STATUS

async function loadLatestStatus() {
    try {
        // Replace with your actual GitHub raw URL
        const response = await fetch('https://raw.githubusercontent.com/Mcbuckets24/Status-Tracker/main/statuses.json?' + Date.now());
        const statuses = await response.json();

        if (statuses.length > 0) {
            const latest = statuses[0]; // First item is most recent

            document.getElementById('statusText').textContent = latest.status;

            //const timestamp = new Date(latest.timestamp);
            //document.getElementById('statusTimestamp').textContent =
                //`Updated: ${timestamp.toLocaleDateString()} ${timestamp.toLocaleTimeString()}`;
        }
    } catch (error) {
        console.error('Error loading status:', error);
        document.getElementById('statusText').textContent = 'Failed to load status';
    }
}

loadLatestStatus();
// Auto-refresh every 5 minutes
setInterval(loadLatestStatus, 300000);