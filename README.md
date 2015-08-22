# Gould

Creating an API for [Dominon’s Smart Pricing Plan](https://www.dom.com/residential/dominion-virginia-power/ways-to-save/smart-pricing-plan/).

The current rate data, output by Gould, is provided at [`http://api.openva.com/dominion/rates.json`](http://api.openva.com/dominion/rates.json). It is updated at 5:00 PM ET daily.

Dominion provides [a rate card as a PDF](https://www.dom.com/library/domcom/pdfs/virginia-power/smart-pricing-plan/spp-combined.pdf) and a [day classification calendar](https://www.dom.com/residential/dominion-virginia-power/ways-to-save/smart-pricing-plan/smart-pricing-plan-day-classification-calendar) that provides a power-rate classification one day ahead (updated at 4 PM), but no machine-readable data to allow action to be taken automatically using this information.

This is software that determines that classification, and provides an API to enable that classification to be identified and acted upon programmatically (e.g., bt IFTTT, Nest, etc.)

The project is named for [Frank Jay Gould](https://en.wikipedia.org/wiki/Frank_Jay_Gould), the founder of the Virginia Railway & Power Company, later renamed Virginia Electric and Power Company, and today named Dominion.
