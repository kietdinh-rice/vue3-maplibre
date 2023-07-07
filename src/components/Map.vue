<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"
      ><img
        src="https://api.maptiler.com/resources/logo.svg"
        alt="MapTiler logo"
    /></a>
    <div class="map" ref="mapContainer"></div>
  </div>
</template>

<script>
  import { Map, NavigationControl } from "maplibre-gl";
  import { shallowRef, onMounted, onUnmounted, markRaw } from "vue";
  import ctaData from '@/assets/CTA.geojson'
  export default {
    name: "Map",

    setup() {
      const mapContainer = shallowRef(null);
      const map = shallowRef(null);

      

      onMounted(async () => {

        const apiKey = "JahzWSoMkHlhAV2kk3Nn"; // K's account

        const initialState = { lng: -95.428421, lat: 29.829907, zoom: 9.5 };

        map.value = markRaw(
          new Map({
            container: mapContainer.value,
            style: `https://api.maptiler.com/maps/backdrop/style.json?key=${apiKey}`,
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom,
          })
        );
        map.value.addControl(new NavigationControl(), "top-right");

        // new Marker({color: "#FF0000"})
        //   .setLngLat([-95.358421,29.749907])
        //   .addTo(map.value);

        var hoveredCTAId = null;
        map.value.on("load", function () {
          map.value.addSource("ctas", {
            "type": "geojson",
            "data": ctaData,
          });

          // The feature-state dependent fill-opacity expression will render the hover effect
          // when a feature's hover state is set to true.
          map.value.addLayer({
            "id": "cta-fills",
            "type": "fill",
            "source": "ctas",
            "layout": {},
            "paint": {
              "fill-color": "#627BC1",
              "fill-opacity": [
                "case",
                ["boolean", ["feature-state", "hover"], false],
                1,
                0.5,
              ],
            },
          });

          map.value.addLayer({
            "id": "cta-borders",
            "type": "line",
            "source": "ctas",
            "layout": {},
            "paint": {
              "line-color": "#627BC1",
              "line-width": 1,
            },
          });

          // When the user moves their mouse over the state-fill layer, we'll update the
          // feature state for the feature under the mouse.
          map.value.on("mousemove", "cta-fills", function (e) {
            if (e.features.length > 0) {
              if (hoveredCTAId) {
                map.value.setFeatureState(
                  { source: "ctas", id: hoveredCTAId },
                  { hover: false }
                );
              }
              hoveredCTAId = e.features[0].properties.OBJECTID;
              map.value.setFeatureState(
                { source: "ctas", id: hoveredCTAId },
                { hover: true }
              );
            }
          });

          // When the mouse leaves the state-fill layer, update the feature state of the
          // previously hovered feature.
          map.value.on("mouseleave", "cta-fills", function () {
            if (hoveredCTAId) {
              map.value.setFeatureState(
                { source: "ctas", id: hoveredCTAId },
                { hover: false }
              );
            }
            hoveredCTAId = null;
          });
        });

      });

      onUnmounted(() => {
        map.value?.remove();
      });

      return {
        map,
        mapContainer,
      };
    },
  };
</script>

<style scoped>
  @import "~maplibre-gl/dist/maplibre-gl.css";

  .map-wrap {
    position: relative;
    margin-top: 40px;
    width: 100%;
    height: calc(
      100vh - 77px
    ); /* calculate height of the screen minus the heading */
  }

  .map {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  .watermark {
    position: absolute;
    left: 10px;
    bottom: 10px;
    z-index: 999;
  }
</style>
