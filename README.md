# Test technique Geoptis : Platform Engineer (DevOps & IA)

Candidate : Fatma Bouzid

## Plan
- [x] Étape 0 : mise en place
- [x] Étape 1 : Déployer une application Node.js simple
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

## Étape 1 : Déployer une application Node.js simple

J'ai créé une petite application Node.js avec Express qui expose une route `GET /` et retourne `Hello from Geoptis test`.

J'ai créé une image Docker à partir d'un `Dockerfile`, puis je l'ai chargée dans le cluster kind avec `kind load docker-image`.

Côté Kubernetes, j'ai créé un `Deployment` avec 3 replicas ainsi qu'un `Service` de type `ClusterIP`.

Les 3 pods sont bien en état `Running` et le Service possède bien les 3 endpoints.

J'ai ensuite testé l'accès à l'application depuis le cluster avec une requête HTTP et obtenu :

`Hello from Geoptis test`

### Ce que j'en retiens

J'ai mieux compris le fonctionnement d'un Deployment Kubernetes avec plusieurs replicas, ainsi que le rôle d'un Service pour permettre l'accès aux pods.

J'ai également appris à vérifier l'état des pods, les endpoints d'un Service et à tester la communication entre les ressources du cluster.