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
 * __SPoCA/classes/constants.h__: Constants for the compilation of the programs
