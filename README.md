# Test technique Geoptis : Platform Engineer (DevOps & IA)

Candidate : Fatma Bouzid

## Plan
- [x] Étape 0 : mise en place
- [ ] Étape 1 : Déployer une application Node.js simple
- [ ] Étape 2 : Empaqueter l'app en chart Helm
- [ ] Étape 3 : Premier déploiement GitOps avec ArgoCD
- [ ] Étape 4 : Monitoring et alerting
- [ ] Étape 5 (bonus) : Conception d'un script assisté par IA

## Étape 0 : mise en place

J'ai installé kind, créé mon cluster local (`geoptis-test`) et ce dépôt. Le nœud est bien `Ready`, donc tout est prêt pour la suite.

**Problèmes rencontrés**

J'ai eu deux soucis avec Docker Desktop : un plantage (réglé en le réinstallant), puis une erreur `no such host` quand il téléchargeait l'image de kind. Mon réseau marchait sous Windows, donc j'ai compris que le problème venait du DNS de Docker, et je lui ai donné un DNS public (1.1.1.1 et 8.8.8.8) dans ses réglages.

**Ce que j'en retiens**

kind fait tourner Kubernetes dans des conteneurs Docker, donc si Docker va mal, tout va mal. Et quand il y a un souci réseau, je commence par chercher si ça vient de Windows ou de Docker.