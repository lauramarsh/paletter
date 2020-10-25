<template>
    <div class="title">
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
export default {
  name: "TitleCard",
};
</script>

<style scoped>
.title {
  height: inherit;
  /* height: 100vh;
  width: 100vw; */
  display: flex;
  justify-content: left;
  align-items: center;

  /* background: linear-gradient(208deg, #fcac73, #9bbe74, #8fc2e0, #b26c96);
  background-size: 800% 800%;
  -webkit-animation: AnimationName 12s ease infinite;
  -moz-animation: AnimationName 12s ease infinite;
  -o-animation: AnimationName 12s ease infinite;
  animation: AnimationName 12s ease infinite; */

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

.title div {
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

/* @-webkit-keyframes AnimationName {
  0% {
    background-position: 0% 99%;
  }
  50% {
    background-position: 100% 2%;
  }
  100% {
    background-position: 0% 99%;
  }
}

@-moz-keyframes AnimationName {
  0% {
    background-position: 0% 99%;
  }
  50% {
    background-position: 100% 2%;
  }
  100% {
    background-position: 0% 99%;
  }
}

@-o-keyframes AnimationName {
  0% {
    background-position: 0% 99%;
  }
  50% {
    background-position: 100% 2%;
  }
  100% {
    background-position: 0% 99%;
  }
}

@keyframes AnimationName {
  0% {
    background-position: 0% 99%;
  }
  50% {
    background-position: 100% 2%;
  }
  100% {
    background-position: 0% 99%;
  }   
} */

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
