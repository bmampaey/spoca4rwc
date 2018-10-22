1. What are FT_ objects
1. What is in the "name" property in FT_objects
1. The root object is FT_CoronalHole, so I can only submit those
1. How to create update read delete objects in the DB (curl -s -S -v -H "Content-Type: application/json" -X POST --data @fname.json http://solrwc2:8888/message)
1. How do link works in the JSON: integer, string or FT
1. Why there is 2 links from CoronalHole to CoronalHoleDetection and 1 link from CoronalHoleDetection to CoronalHole
1. Is FT\_\_CoronalHoleDetection__SPOCA\_CoronalHole_ a many 2 many table
1. For Provider do I use '+Provider_KSO', why does it starts with a + sign
1. In SPOCA_CoronalHole, why are Min, Max, Median, etc. arrays
1. In SPOCA_CoronalHole, a channel property is missing (image on which the stats where computed)
1. In CoronalHoleDetection there is no date, but there is one in _HeliographicCoordinate
1. In \_SolarSurface_Area:
  1. is the surface "on the sun" or "as seen from the observer"
  1. Mm vs Arcsec
  1. Why not Mm² and Arcsec²
  1. Unit of the error
1. Why don't we specify tracking relations between CoronalHoleDetection
1. In CoronalHole, is the BeginTime the time it was first observed + How to update the EndTime
