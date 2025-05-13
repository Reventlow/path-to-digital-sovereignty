# Fase 2: Planlægningsfase

## Fasedefinition

I denne fase er truslen om licens- eller tjenesteafbrydelse stadig usandsynlig, men vurderes som tilstrækkeligt realistisk til, at der bør udarbejdes kontingensplaner og tekniske overvejelser. Formålet er at dokumentere og analysere vores afhængighed af amerikansk-baserede teknologier og forberede strategier til at kunne håndtere en potentiel afbrydelse.

## Overordnede handlinger

### System- og tjenesteidentifikation

- Identificere alle kritiske systemer og tjenester afhængige af amerikanske leverandører (Microsoft, Apple, Google, Cisco m.fl.)

### Juridisk og teknisk vurdering

- Vurdere juridiske og tekniske muligheder for erstatning eller afkobling

### Udkast til migreringsplaner

- Udarbejde udkast til migreringsplaner for (inklusive øvrige afhængigheder, værktøjer og systemnære komponenter):

  - Operativsystemer
  - Kontorpakker
  - E-mail og kalender
  - Autentificering og adgangsstyring
  - Cloud-lagring og samarbejdsværktøjer
  - Netværksudstyr, telefoni og mobile løsninger (inkl. vurdering af afhængighed af Apple og Android enheder og mulige alternativer som Fairphone, /e/OS eller Linux-baserede systemer)
  - Backup-løsninger og lagring
  - Databaser
  - DNS
  - Firmwareopdateringer (BIOS, UEFI, drivere og anden enhedsnær software med afhængighed af producentens infrastruktur)
  - Øvrige specialiserede applikationer afhængigt af organisationens behov, f.eks.:

    - AI-værktøjer
    - Grafisk software
    - Videoredigering
    - Overvågning og adgangskontrol
    - CAD-software
    - Social media-værktøjer (EU-venlige alternativer)

## Teknologiske alternativer (eksempler)

> **Bemærkning:** Enkelte af de foreslåede løsninger har oprindelse i USA (f.eks. Keycloak, FreeIPA, Jitsi, GitLab CE, Ansible, Puppet), men er fuldt open source og kan selvhostes uden afhængighed af kommercielle tjenester eller licensbindinger. De er medtaget i kraft af deres robusthed, modenhed og uafhængighed i driftsmiljøer. Målet er ikke fuldstændig isolation, men reduktion af kritisk afhængighed.

- **Operativsystem:** Linux Mint, Debian eller Arch i testmiljø
- **Kontorpakke:** LibreOffice, OnlyOffice eller Collabora
- **E-mail:** Dovecot + Postfix, evt. i kombination med Nextcloud Kalender og Kontakter
- **AD/Azure AD:** Keycloak og FreeIPA
- **Cloud/SharePoint:** Nextcloud
- **Kommunikation (Teams):** Jitsi og Matrix
- **GitHub:** Gitea eller selvhostet GitLab CE
- **SCCM:** Ansible, shell-scripts eller Puppet
- **ERP/Navision:** Odoo, Dolibarr, Tryton
- **Database:** PostgreSQL, MariaDB, MySQL (alle open source og EU-venlige)
- **Backup-løsninger:** BorgBackup, Restic, Duplicity, eller Veeam med lokal lagring
- **Mobile enheder:** Fairphone med /e/OS eller Ubuntu Touch, PinePhone, Librem 5

## Kommunikation

Etablering af en klar kommunikationsplan er central i denne fase og skal sikre, at information om planen, dens formål og forløb bliver kommunikeret effektivt og rettidigt til alle interessenter.

Kommunikationen bør:

- Udformes som en plan for internt og eksternt beredskab
- Understøtte gennemsigtighed og tillid til planens formål og metode
- Muliggøre videndeling og samarbejde med andre organisationer og open-source-miljøer
- Formidle opdateringer løbende gennem passende kanaler
- Publicering af planen i open source-format (f.eks. via GitHub), med henblik på at styrke gennemsigtighed og tillid til planens formål og metode. Dette vil samtidig gøre det muligt for andre organisationer at kommentere, genbruge og bidrage til indholdet på tværs af sektorer og landegrænser.
- Starte kontakt til andre organisationer og open-source-miljøer for videndeling og fælles udvikling

## Arbejdsgruppe

Det anbefales at oprette en tværfaglig arbejdsgruppe med repræsentanter fra relevante dele af organisationen. Denne gruppe skal understøtte koordinering, forankring og fremdrift i planens arbejde.

Arbejdsgruppen bør:

- Bestå af:

  - Styregruppe
  - Økonomiansvarlige
  - Implementeringsansvarlige
  - Supportfunktioner
  - Kompetenceudviklingsansvarlige
  - Ansvarlige for intern kommunikation

- Have ansvar for:

  - Løbende afstemning med ledelse og nøglepersoner
  - Indsamling af feedback fra brugere og medarbejdere
  - Vurdering af behov for eksternt samarbejde og koordinering
  - Forberedelse af kulturskift og organisatorisk forankring

## Output fra denne fase

### Dokumenterede kontingensplaner

- Dokumenterede kontingensplaner for alle hovedsystemer, herunder for hver løsning:

  - Valg af alternativ og begrundelse
  - Implementeringskrav (teknisk og organisatorisk)
  - Migrationsmuligheder og -metoder (eksportfunktioner, scripting, manuel overførsel eller nyopsætning fra bunden)
  - IT-kompetenceudvikling: krav til opkvalificering eller behov for outsourcing
  - Slutbruger-kompetenceudvikling: træning og support
  - Budgetovervejelser: estimater for licens, hardware og drift
  - Tidsforbrug og estimeret implementeringshorisont

### Pilotprojekter

- Pilotprojekter defineret og eventuelt igangsat, herunder:

  - Opsætning af sandkassemiljø til test af FOSS-løsninger uden produktionseksponering
  - For hvert pilotprojekt bør følgende defineres:

    - Hvad måles og testes?
    - Hvilke konkrete spørgsmål ønskes besvaret?
    - Hvor længe kører forsøget?
    - Hvilke systemer og brugergrupper indgår?
    - Hvem evaluerer og dokumenterer erfaringerne?

### Licens- og afhængighedskortlægning

- Klarlæggelse af licensforhold og afhængigheder, herunder:

  - Hvilke systemer kræver løbende licensvalidering?
  - Hvilke systemer påvirkes indirekte, hvis licens eller adgang til et andet system ophører?
  - Er der afhængigheder til cloud-baserede login-, aktiverings- eller valideringstjenester?
  - Hvor hurtigt forventes forskellige systemer at stoppe med at fungere ved licensafbrydelse?
  - Hvilke systemer har nødlicens, offline-funktionalitet eller lokale fallback-muligheder?

### Kompetenceudvikling

- Overblik over nødvendige kompetenceudviklingsområder (f.eks. Linux, Ansible, e-mailadministration)

## Risikostyring i forhold til fokus i denne fase

- Ingen akutte handlinger tages endnu
- Fokus på dokumentation, analyse og samarbejde
- Planen evalueres og opdateres løbende ved ændring i trusselsbilledet
