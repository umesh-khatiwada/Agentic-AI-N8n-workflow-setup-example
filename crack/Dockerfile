FROM docker.n8n.io/n8nio/n8n:latest

USER root

RUN sed -i "s/getValue(feature) {/getValue(feature) {return undefined;/g" /usr/local/lib/node_modules/n8n/dist/license.js && \
    sed -i "s/isAPIDisabled() {/isAPIDisabled() {return false;/g" /usr/local/lib/node_modules/n8n/dist/license.js && \
    sed -i "s/isLicensed(feature) {/isLicensed(feature) {if (feature == 'feat\:showNonProdBanner') {return false} else {return true};/g" /usr/local/lib/node_modules/n8n/dist/license.js && \
    sed -i "s/getPlanName() {/getPlanName() {return 'Entreprise';/g" /usr/local/lib/node_modules/n8n/dist/license.js && \
    sed -i "s/async renew() {/async renew() {return;/g" /usr/local/lib/node_modules/n8n/dist/license.js

USER node

LABEL crack=true
LABEL crack.author="Ibaraki Douji"