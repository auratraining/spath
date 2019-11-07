# spath

-Problem statement
Did you ever faced issues in reaching your friends house who stays in the same residential complex?  Where your GPS devices is does not work.
The application address the navigating problem within in indoors where GPS doesn't helps much.

For example showing floor plan and route map to your friends house, who is residing within your residential complex.  The Tower, Block, Floor, House numbers adds more confusion and results you to climb up/down many elevators in different towers.  The problem gets bigger if you are tyring from basement.  The GPS may not be available or does't help you.

The nature of the problem is applicable in many other locations
1. Residential layouts :  Delivery boys and kids, doodh wala's gets more confused in residential layouts.
2. Offie space : Locating meeting rooms, printers, seat location within your multi floored office location
3. Big shopping maals

- Solution : Building local static map overlays
Application uses the static built map to plot route map

Design:
1. Building static simple indoor map
   * Required to build a "standard" to represent location map in a simple text format
   * This standard is used to represe the local map of the floor
   * The static-map get fed into application
   Note: This required lot of thought before building standard 
      
2. Reading/loading/feeding static map to application
   * Loading the map and plotting graphical map
   
3. Create graph "path walk algorithm" to display route map.
   * Required to build "graph path walk algorithm" to build route map for source to destination
   
4. Plotting graphical map 
   * Plotting route map from static plan
   Note: Check the possibility using google maps if it supports to use staic maps
