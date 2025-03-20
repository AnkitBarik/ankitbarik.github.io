#!/bin/bash
sed -i "s/actions\/cache@v3/actions\/cache@v4/" *
sed -i "s/actions\/configure-pages@v3/actions\/configure-pages@v5/" *
sed -i "s/actions\/deploy-pages@v2/actions\/deploy-pages@v4/" *
sed -i "s/actions\/upload-pages-artifact@v2/actions\/upload-pages-artifact@v3/" *
sed -i "s/peaceiris\/actions-hugo@v2/peaceiris\/actions-hugo@v3/" *

