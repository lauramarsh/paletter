<template>
  <div class="title">
    <div id="particles-js"></div>
    <div>
      <p class="title_mp">M<span>OVING</span></p>
      <p class="title_mp">P<span>ALETTES</span></p>
      <p>
        A cinemagraphic collage generator. Relax, browse, add, and edit custom
        palettes however you like.
      </p>
    </div>
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
            value: 0.5,
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
            random: false,
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
              distance: 400,
              size: 4,
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
  -webkit-animation: AnimationName 45s ease infinite;
  -moz-animation: AnimationName 45s ease infinite;
  -o-animation: AnimationName 45s ease infinite;
  animation: AnimationName 45s ease infinite;
}

.title > div:first-child {
  /* width: inherit;
  height: inherit; */
}

.title > div:last-child {
  margin-left: 4rem;
}

.title p {
  color: white;
  text-align: left;
  margin: 0px;
}

.title p:last-child {
  padding-left: 0.5rem;
  padding-top: 1rem;
  font-style: italic;
  line-height: 1.25rem;
  max-width: 25rem;
}

.title_mp {
  font-size: 7rem;
  line-height: 5rem;
  font-weight: bold;
  letter-spacing: 5px;
}

.title_mp span {
  font-size: 5rem;
}

@-webkit-keyframes AnimationName {
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
@-moz-keyframes AnimationName {
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
@-o-keyframes AnimationName {
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
@keyframes AnimationName {
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
</style>
