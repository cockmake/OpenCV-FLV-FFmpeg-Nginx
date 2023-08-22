<template>
  <div>
    <video
      id="videoElement"
      controls
      height="480"
      width="640"
      autoplay>浏览器不支持</video>
  </div>
</template>

<script setup lang="js">
import {onMounted, ref} from "vue"
import flvjs from 'flv.js';
const flvPlayer = ref(null);
onMounted(() => {
  let videoElement = document.getElementById('videoElement');
  flvPlayer.value = flvjs.createPlayer(
    {
      type: 'flv',
      url: 'http://127.0.0.1:81/live?port=1935&app=live&stream=make', //你的url地址
      hasAudio: false,
    }
  );
  // flvPlayer.value.on(flvjs.Events.METADATA_ARRIVED, ()=>{
  //   console.log('加载完成')
  //   flvPlayer.value.play();
  // })
  flvPlayer.value.attachMediaElement(videoElement);
  flvPlayer.value.load();
})
</script>

<style scoped>

</style>