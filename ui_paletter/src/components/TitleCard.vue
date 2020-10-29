<template>
  <div class="title">
    <div id="particles-js"></div>
    <div class="title_header">
      <p class="title_mp">MOVING</p>
      <p class="title_mp">PALETTES</p>
      <p>
        A cinemagraphic collage generator. Relax, browse, and add custom
        palettes however you like.
      </p>
    </div>
    <section class="title_scroll">
      <vs-button icon color="#ffffff" transparent @click="scrollDown">
        <i class="bx bx-chevron-down icon"></i>
      </vs-button>
    </section>
  </div>
</template>

<script>
import "particles.js";
export default {
  name: "TitleCard",
  mounted() {
    this.initParticles();
  },
  methods: {
    initParticles() {
      window.particlesJS("particles-js", {
        particles: {
          number: { value: 400, density: { enable: true, value_area: 800 } },
          color: { value: "#fff" },
          shape: {
            type: "circle",
            stroke: { width: 0, color: "#000000" },
            polygon: { nb_sides: 5 },
            image: { src: "img/github.svg", width: 100, height: 100 },
          },
          opacity: {
            value: 0.35,
            random: true,
            anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false },
          },
          size: {
            value: 10,
            random: true,
            anim: { enable: false, speed: 40, size_min: 0.1, sync: false },
          },
          line_linked: {
            enable: false,
            distance: 500,
            color: "#ffffff",
            opacity: 0.4,
            width: 2,
          },
          move: {
            enable: true,
            speed: 3,
            direction: "top-right",
            random: true,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: { enable: false, rotateX: 600, rotateY: 1200 },
          },
        },
        interactivity: {
          detect_on: "canvas",
          events: {
            onhover: { enable: true, mode: "bubble" },
            onclick: { enable: true, mode: "repulse" },
            resize: true,
          },
          modes: {
            grab: { distance: 400, line_linked: { opacity: 0.5 } },
            bubble: {
              distance: 300,
              size: 1,
              duration: 0.3,
              opacity: 1,
              speed: 3,
            },
            repulse: { distance: 200, duration: 0.4 },
            push: { particles_nb: 4 },
            remove: { particles_nb: 2 },
          },
        },
        retina_detect: true,
      });
    },
    scrollDown(e) {
      this.$emit("scroll-down", e, "just do it");
    },
  },
};
</script>

<style scoped>
#particles-js {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
}

.title {
  position: relative;
  height: inherit;
  display: flex;
  justify-content: left;
  align-items: center;

  background: linear-gradient(
    230deg,
    #fcac73,
    #a5c482,
    #8fc2e0,
    #b26c96,
    #b17960,
    #dbc1b6
  );
  background-size: 1200% 1200%;
  -webkit-animation: GradientShift 45s ease infinite;
  -moz-animation: GradientShift 45s ease infinite;
  -o-animation: GradientShift 45s ease infinite;
  animation: GradientShift 45s ease infinite;
}

.title_header {
  margin-left: 4rem;
}

.title_header p {
  color: white;
  text-align: left;
  margin: 0px;
}

.title_header p:last-child {
  padding-left: 0.5rem;
  padding-top: 1rem;
  font-style: italic;
  line-height: 1.25rem;
  max-width: 25rem;
  text-shadow: 0 0 2px #ffffff;
}

.title_mp {
  font-size: 7vw;
  font-weight: bold;
  text-shadow: 0 0 4px #ffffff;

  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-family: "Source Sans Pro", sans-serif;
  animation: reveal 3000ms ease-in-out forwards 200ms,
    glow 2500ms linear infinite 2000ms;
}

.title_mp span {
  font-size: 5rem;
}

.title_scroll {
  position: absolute;
  bottom: 0;
  left: calc(50% - 3rem);

  animation-duration: 2s;
  animation-iteration-count: infinite;
  transform-origin: bottom;
  animation-name: bounce-2;
  animation-timing-function: ease;
}

.icon {
  font-size: 3rem;
  text-shadow: 0 0 6px #ffffff;
}

@media only screen and (max-width: 768px) {
  /* For mobile phones: */
  .title_header {
    margin-left: 2rem;
  }

  .title_mp {
    font-size: 10vw;
    font-weight: bold;
    text-shadow: 0 0 4px #ffffff;

    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-family: "Source Sans Pro", sans-serif;
    animation: reveal 3000ms ease-in-out forwards 200ms,
      glow 2500ms linear infinite 2000ms;
  }

  .title_header p:last-child {
    padding-left: 0.5rem;
    padding-top: 1rem;
    font-style: italic;
    line-height: 1.25rem;
    max-width: 20rem;
    text-shadow: 0 0 2px #ffffff;
  }
}

@keyframes bounce-2 {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0);
  }
}

@-webkit-keyframes GradientShift {
  0% {
    background-position: 0% 66%;
  }
  50% {
    background-position: 100% 35%;
  }
  100% {
    background-position: 0% 66%;
  }
}
@-moz-keyframes GradientShift {
  0% {
    background-position: 0% 66%;
  }
  50% {
    background-position: 100% 35%;
  }
  100% {
    background-position: 0% 66%;
  }
}
@-o-keyframes GradientShift {
  0% {
    background-position: 0% 66%;
  }
  50% {
    background-position: 100% 35%;
  }
  100% {
    background-position: 0% 66%;
  }
}
@keyframes GradientShift {
  0% {
    background-position: 0% 66%;
  }
  50% {
    background-position: 100% 35%;
  }
  100% {
    background-position: 0% 66%;
  }
}
@keyframes reveal {
  80% {
    letter-spacing: 4px;
  }
  100% {
    background-size: 300% 300%;
  }
}
@keyframes glow {
  40% {
    text-shadow: 0 0 8px #ffffff;
  }
}
</style>
