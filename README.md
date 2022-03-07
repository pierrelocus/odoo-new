# odoo-new
This repository is a little toolbox to create new files useful in Odoo development : python / xml files with skelton of models, views, cron, system parameter, ... in Odoo

## Installation

git clone git@github.com:pierrelocus/odoo-new

sudo chmod +x odoo-new/odoo-new

sudo cp odoo-new/odoo-new /usr/bin

## Usage

odoo-new [xml|py] [view|cron|param|model|wizard] [model.name]

e.g.

    odoo-new py model sale.order

    odoo-new xml view sale.order
