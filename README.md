# Pipeline to extract Coronal Hole from SDO/AIA 193Å images and submit the corresponding events to the RWC Event DB

The following python scripts are used to run the pipeline:
 * __AIA_CH_pipeline.py__: Run all following scripts and submit the events to the Event DB
 * __AIA_CH_spoca_jobs.py__: Run the programs classification.x, get_CH_map.x and tracking.x from the SPoCA suite, to create and track the Coronal Hole maps (CHMap)
 * __AIA_CH_event.py__: Extract the Coronal Hole events from a CHMap

The following python scripts are tools for the pipeline:
 * __AIA_quality.py__: Test the quality of a SDO/AIA FITS file
 * __event_db.py__: Allow to create, get and update events in the Event DB
 * __job.py__: Runs a program

The following python script is not part of the pipeline:
 * __AIA_CH_overlay_jobs__: Run the overlay.x program from the SPoCA suite, to create overlay of the CHMap on SDO/AIA and SDO/HMI images

All scripts contain at their top environment parameters to properly run without the need to specify them manually when executed.

Configuration files for the programs of the SPoCA suite:
 * __scripts/AIA_CH_classification.config__: Config file for the classification.x program
 * __scripts/AIA_CH_get_CH_map.config__: Config file for the get_CH_map.x program
 * __scripts/AIA_CH_tracking.config__: Config file for the tracking.x program
 * __scripts/AIA_CH_overlay.config__: Config file for the overlay.x program

The executables of the SPoCA suite can be compiled using the following Make files:
 * __SPoCA/classification.mk__: To compile SPoCA/bin/classification.x
 * __SPoCA/get_CH_map.mk__: To compile SPoCA/bin/get_CH_map.x
 * __SPoCA/tracking.mk__: To compile SPoCA/bin/tracking.x
 * __SPoCA/overlay.mk__: To compile SPoCA/bin/overlay.x (not used in the pipeline, see above)
 * __SPoCA/fits2png.mk__: To compile SPoCA/bin/fits2png.x (not used in the pipeline, useful to create png of the SDO FITS files)
 * __SPoCA/map2png.mk__: To compile SPoCA/bin/map2png.x (not used in the pipeline, useful to create png of the CHMap FITS files)
