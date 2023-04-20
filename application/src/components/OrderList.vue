<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
<div class="order-list">
    <h1>Tellimused</h1>

    <!-- Siia tuleb mappida OrderListItemid 
    Koosta saateleht / Saada uuesti

    Läbi kasutajaliidese saab pärida tellimuse numbri järgi tellimuse infot ning näha tellimuse andmeid (tellimuse number, kliendikood, kliendi nimi, kuupäev ja tellimuse ridasid toote kood toote nimetus tellitud kogus).
    -->

    
    <table>
    <tr>
        <th>Tellimuse nr</th>
        <th>Kliendikood</th>
        <th>Kliendi nimi</th>
        <th>Kuupäev</th>
        <th>Nupp</th>
    </tr>
    <tr>
        <td>Nr1</td>
        <td>Kliendikood1</td>
        <td>Kliendinimi1</td>
        <td>01.02.2023</td>
        <td>Koosta saateleht / Vaata tellimust</td>
    </tr>
    </table>
  </div>
</template>

<style scoped>
/* h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.order-list h1,
.order-list h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .order-list h1,
  .order-list h3 {
    text-align: left;
  }
} */
</style>
