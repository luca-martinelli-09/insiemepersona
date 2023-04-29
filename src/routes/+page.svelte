<script lang="ts">
  import InsiemePerSonaLogo from "$lib/components/logos/InsiemePerSonaLogo.svelte";
  import ViviamoSonaLogo from "$lib/components/logos/ViviamoSonaLogo.svelte";
  import Icon from "@iconify/svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  const posts = data.posts;
</script>

<section>
  <main class="flex flex-col gap-12 md:gap-20">
    <div class="flex justify-center gap-2 md:gap-5 w-full">
      <ViviamoSonaLogo size={250} class="h-auto w-full lg:w-auto" />
      <InsiemePerSonaLogo size={250} class="h-auto w-full lg:w-auto" />
    </div>
    <div class="flex flex-col gap-16 items-center">
      <h1 class="title text-center">Ripartiamo dalle<br /><span class="green font-medium">persone</span></h1>
      <div class="flex flex-col w-full justify-center md:flex-row gap-2">
        <a class="button primary" href="/chi-siamo">Conosci i candidati</a>
        <a class="button gap-3" href="/programma-amministrativo.pdf" target="_blank" rel="noopener noreferrer">
          <span class="text-3xl"><Icon icon="solar:download-minimalistic-linear" /></span>
          <span>Le nostre idee</span>
        </a>
      </div>
      <div class="flex gap-2 text-3xl">
        <a href="https://www.facebook.com/viviamosona" target="_blank" rel="noopener noreferrer"><Icon icon="mdi:facebook" /></a>
        <a href="http://instagram.com/viviamosona" target="_blank" rel="noopener noreferrer"><Icon icon="mdi:instagram" /></a>
      </div>
    </div>
  </main>
</section>

<section class="items-stretch flex-col py-0 min-h-0">
  <main class="py-0 md:pt-20">
    <h4 class="title text-center">
      Il nostro modo di amministrare parte dalla presenza sul territorio, dall'<strong class="green">ascolto</strong>, dalla <strong class="green">concretezza</strong> nel cercare soluzioni a istanze
      reali della nostra comunità, con la <strong class="green">competenza</strong> di chi è abituato a risolvere problemi, con la <strong class="green">passione</strong>
      e l'<strong class="green">impegno</strong> che da sempre spendiamo nel volontariato civico.
    </h4>
  </main>
  <img src="/bg/foto-gruppo.webp" class="mt-10 md:mt-20" alt="Foto di gruppo" />
</section>

<section class="items-stretch min-h-0">
  <img src="/cv/gianfranco-dalla-valentina/gianfranco-dalla-valentina.webp" alt="Azioni nei primi 100 giorni" class="side hidden lg:block" />
  <main class="pills">
    <h2 class="title">Azioni nei primi <span class="green">100 giorni</span></h2>

    <ul class="pills">
      <li><p><strong>Manutenzione</strong> di tutte le <strong>strade</strong> e dei <strong>marciapiedi</strong>.</p></li>
      <li><p><strong>Manutenzione</strong> di tutti gli <strong>impianti sportivi</strong>.</p></li>
      <li><p><strong>Manutenzione</strong> di tutte le <strong>aree verdi</strong> pubbliche.</p></li>
    </ul>
  </main>
</section>

<section class="items-stretch">
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Lugagnano</span></h2>

    <ol class="pills">
      <li><p><strong>Riqualificare</strong> il centro anche attraverso la realizzazione di nuovi parcheggi.</p></li>
      <li><p><strong>Creare</strong> una rete di ciclabili che colleghino tutto il paese.</p></li>
      <li><p><strong>Credere</strong> nelle potenzialità delle associazioni, e progettare una sede per le associazioni socio-assistenziali (Sos e Dono).</p></li>
      <li><p><strong>Creare</strong> un polo sportivo per tutti gli sport e per tutte le persone.</p></li>
      <li><p><strong>Difendere l'ambiente</strong> (no ad alcun ampliamento della discarica Cà di Capri).</p></li>
    </ol>
  </main>
  <img src="/bg/lugagnano.webp" alt="5 passi per ripartire a Lugagnano" class="side" />
</section>

<section class="items-stretch flex-col-reverse lg:flex-row">
  <img src="/bg/palazzolo.webp" alt="5 passi per ripartire a Palazzolo" class="side object-left" />
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Palazzolo</span></h2>

    <ol class="pills">
      <li><p><strong>Centro civico da completare</strong> con la farmacia e ambulatori, portando avanti un'azione concreta per dotare la frazione di un medico.</p></li>
      <li><p><strong>Centro civico</strong> da potenziare come spazio per i servizi del paese e per le Associazioni, portando avanti un'azione concreta per dotare la frazione di un medico.</p></li>
      <li><p><strong>Bosco</strong>: riqualificazione marciapiedi, strade e aree verdi.</p></li>
      <li><p><strong>Viabilità</strong>: portare avanti una progettualità per dotare il paese di percorsi ciclopedonali verso Sona e verso Bussolengo.</p></li>
      <li><p><strong>Area cani</strong>: realizzare un'area cani lungo la ciclabile, in modo che sia facilmente raggiungibile a tutti.</p></li>
    </ol>
  </main>
</section>

<section class="items-stretch">
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">San Giorgio</span></h2>

    <ol class="pills">
      <li>
        <p>
          <strong>Sicurezza</strong>: marciapiedi e sistemazione degli incroci stradali in <strong>via Gaburri</strong> e <strong>Tagliaferro</strong>.<br />
          Implementare il <strong>servizio di videosorveglianza</strong> nelle aree sensibili del territorio.
        </p>
      </li>
      <li><p><strong>Centro civico</strong> da potenziare come spazio per i servizi del paese e per le Associazioni, portando avanti un'azione concreta per dotare la frazione di un medico.</p></li>
      <li><p><strong>Sport</strong>: potenziare l'impianto sportivo per implementare la funzione di luogo del tempo libero per i nostri giovani e anziani.</p></li>
      <li><p><strong>Viabilità</strong>: censimento e mappatura delle strade vicinali con un piano di manutenzione annuale di tutte le strade pubbliche.</p></li>
      <li><p><strong>San Rocco</strong>: realizzazione di parcheggi e marciapiedi per il passaggio dei pedoni.</p></li>
    </ol>
  </main>
  <img src="/bg/san-giorgio.webp" alt="5 passi per ripartire a San Giorgio" class="side" />
</section>

<section class="items-stretch flex-col-reverse lg:flex-row">
  <img src="/bg/sona.webp" alt="5 passi per ripartire a Sona" class="side" />
  <main class="pills">
    <h2 class="title">5 passi per ripartire a <span class="green">Sona</span></h2>

    <ol class="pills">
      <li>
        <p>
          <strong>Riqualificazione</strong> del parco Fasoli (San Quirico) con implementazione di strutture per lo sport giovanile (calisthenics) e individuazione di uno spazio per le Associazioni del
          paese.
        </p>
      </li>
      <li>
        <p>
          <strong>Recupero del fabbricato</strong> nell'area retrostante la chiesa, per destinarlo (in accordo con la Parrocchia) a spazio per attività parrocchiali e sala prove per il Corpo Bandistico.
        </p>
      </li>
      <li><p><strong>Realizzare un percorso pedonale</strong> protetto su via Fusara e su via Piè di Colle sino alla loc. Valle.</p></li>
      <li><p><strong>Realizzare un anello ciclopedonale</strong> su via Val di Sandrà, dall'impianto di rugby fino alla loc. Valle.</p></li>
      <li>
        <p>
          <strong>Sicurezza</strong>: implementare il servizio di videosorveglianza nelle aree sensibili del paese, come dissuasore per la velocità e contro attraversamento del centro da parte di
          mezzi pesanti.
        </p>
      </li>
    </ol>
  </main>
</section>
