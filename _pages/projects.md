---
layout: single
title: "Funding and Projects"
permalink: /projects/
author_profile: true
---

{% assign logos = "https://nwo.nl/|image003.jpg|NWO;https://lter-life.nl/en|image018.png|LTER-LIFE;https://envri.eu/|image021.png|ENVRI-Hub NEXT;https://oscars-project.eu/|image017.png|OSCARS;https://everse.software/|image022.jpg|EVERSE;https://blue-cloud.org/blue-cloud-2026|image016.jpg|Blue-Cloud 2026;https://www.lifewatch.eu/|image002.png|LifeWatch ERIC;https://biodt.eu/|image022.png|BioDT;http://envri.eu/envri-fair/|image006.jpg|ENVRI-FAIR;https://www.blue-cloud.org/|image007.png|Blue-Cloud;http://www.clarify-project.eu/|image008.png|CLARIFY;https://articonf.eu/|image005.jpg|ARTICONF;http://www.switchproject.eu/|image009.jpg|SWITCH;https://www.vre4eic.eu/|image011.png|VRE4EIC;http://www.envriplus.eu/|image014.jpg|ENVRIplus" | split: ";" %}
<div style="display:flex;flex-wrap:wrap;align-items:center;gap:18px 28px;margin-bottom:2em">
{% for l in logos %}{% assign p = l | split: "|" %}<a href="{{ p[0] }}" title="{{ p[2] }}"><img src="{{ '/images/' | append: p[1] | relative_url }}" alt="{{ p[2] }}" style="height:48px;width:auto"></a>
{% endfor %}
</div>

Current projects
======

### As UvA PI
1. NWO **[LTER-LIFE](https://lter-life.nl/en)** (a research infrastructure to develop Digital Twins of ecosystems in a changing world), Large-Scale Research Infrastructure (LSRI). Duration: August 2023 – August 2032.
2. EU Horizon Europe **[ENVRI-Hub NEXT](https://envri.eu/envri-community-contributes-to-envri-hub-next-advancing-interdisciplinary-environmental-research-data-access/)** (ENVironmental Research Infrastructures delivering an open access Hub and NEXT-level interdisciplinary research framework providing services for advancing science and society). Grant No. 101131141, [HORIZON-INFRA-2023-DEV-01](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-infra-2023-dev-01-01) call. Duration: 2024–2027.
3. EU Horizon Europe **[EVERSE](https://everse.software/)** (European Virtual Institute for Research Software Excellence). Grant No. 101129744, [HORIZON-INFRA-2023-EOSC-01-02](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-infra-2023-eosc-01-02) call. Duration: 2024–2027.
4. EU Horizon Europe **[OSCARS](https://oscars-project.eu/)** (Open Science Clusters' Action for Research and Society). Grant No. 101129751, HORIZON-INFRA-2023-EOSC-01 call. Duration: 2024–2027. (Third party via LifeWatch ERIC)
5. EU Horizon Europe **[Blue-Cloud 2026](https://blue-cloud.org/blue-cloud-2026)** (A federated European FAIR and Open Research Ecosystem for oceans, seas, and inland waters). Grant No. [101094227](https://cordis.europa.eu/project/id/101094227), [HORIZON-INFRA-2022-EOSC-01-03](https://cordis.europa.eu/programme/id/HORIZON_HORIZON-INFRA-2022-EOSC-01-03/en) call. Duration: January 2023 – June 2026.

### Participating via LifeWatch VLIC
6. EU Horizon Europe **[BMD](https://biodt.eu/)** (Biodiversity Meets Data). Grant No. [101057437](https://cordis.europa.eu/project/id/101094227), HORIZON-INFRA-2021-TECH-01-01 call. Duration: March 2025 – February 2028.

Finished projects
======

### As UvA PI
7. EU H2020 **[CLARIFY](http://www.clarify-project.eu/)** (CLoud ARtificial Intelligence For pathologY). Grant No. 860627, [H2020-MSCA-ITN-2019](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/msca-itn-2019) call. Duration: November 2019 – October 2023.
8. EU H2020 **[ENVRI-FAIR](https://envri.eu/home-envri-fair/)** (ENVironmental Research Infrastructures building Fair services Accessible for society, Innovation and Research). Grant No. 824068, [H2020-INFRAEOSC-2018-2](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/infraeosc-04-2018) call. Duration: January 2019 – December 2022.
9. EU H2020 **[Blue-Cloud](https://blue-cloud.org/)** (Piloting innovative services for Marine Research & the Blue Economy). [H2020-BG-2018-2020](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/bg-07-2019-2020). Grant No. 862409. Duration: November 2019 – October 2022.
10. EU H2020 **[ARTICONF](https://articonf.eu/)** (smART socIal media eCOsystem in a blockchaiN Federated environment). Grant No. 825134, [H2020-ICT-2018-2](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/ict-28-2018) call. Duration: January 2019 – December 2021.
11. EU H2020 **[ENVRIplus](https://www.envriplus.eu/)** (ENVironmental Research Infrastructures Providing shared soLUtions for Science and society). Leader of [the Data for Science Theme](http://www.envriplus.eu/wp-content/uploads/2015/08/Theme-2_Zhiming-Zhao.pdf). Grant No. 654182 ([INFRADEV-4-2014-2015](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/infradev-4-2014-2015)). Duration: May 2015 – April 2019.
12. EU H2020 **[VRE4EIC](https://vre4eic.ercim.eu/)** (A Europe-wide interoperable Virtual Research Environment to Empower multidisciplinary research communities and accelerate Innovation and Collaboration). Grant No. 676247, [H2020-EINFRA-2015-1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/einfra-9-2015). Duration: October 2015 – September 2018.
13. EU H2020 **[SWITCH](http://www.switchproject.eu/)** (Software Workbench for Interactive, Time Critical and Highly self-adaptive cloud applications). Grant No. 643963, [H2020-ICT 9-2014-1](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/ict-09-2014) call: Tools and methods for software development. Duration: February 2015 – January 2018.

### Participated via LifeWatch VLIC
14. EU Horizon Europe **[BioDT](https://biodt.eu/)** (Biodiversity Digital Twin for Advanced Modelling, Simulation and Prediction Capabilities). Grant No. [101057437](https://cordis.europa.eu/project/id/101094227), HORIZON-INFRA-2021-TECH-01-01 call. Duration: June 2022 – May 2025.

### Participated as developer in early projects
15. EU FP7 **[ENVRI](http://www.envri.eu/)**. Task leader, task 3.4: linking data and infrastructure — Common operations of Environmental Research Infrastructure (ENVRI). Grant No. 283465.
