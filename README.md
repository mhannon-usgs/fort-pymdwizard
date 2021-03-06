[![Build Status](https://travis-ci.org/talbertc-usgs/fort-pymdwizard.svg?branch=master)](https://travis-ci.org/talbertc-usgs/fort-pymdwizard)
[![Hackage](https://coveralls.io/repos/github/talbertc-usgs/fort-pymdwizard/badge.svg?branch=master)](https://coveralls.io/github/talbertc-usgs/fort-pymdwizard?branch=master)

<img width="250" align="right" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/USGS_logo_green.svg/500px-USGS_logo_green.svg.png"/>



pymdwizard: Standalone version of the Metadata Wizard
===========================================================================================

The  is a useful tool designed to facilitate FGDC  
metadata creation for spatial and non-spatial datasets.  It is a cross-platform desktop application
built using an open-source Python architecture.  

It provides several tools to automate the creation of high quality 
metadata records including:

* Auto-population of sections with information extracted from the dataset being documented.
    - Spatial Data Organization
    - Spatial Reference
    - Entity and Attribute
* Supports a variety of common data formats for introspection including 
    - CSV
    - Excel worksheets
    - Database tables
    - Shapefiles
    - GeoTiffs
    - File geodatabase feature classes.
* Automate creation of sections from existing web-services
    - Contact information (for USGS affiliates)
    - Taxonomic information from ITIS
    - keywords from USGS controlled vocabularies
* Built in validator which highlights any missing or error elements directly on the GUI and in a printable report suitable for metadata review.
* Drag-and-Drop integration with other tools including XML-Notepad and text editors.
* Built in help documentation which guides users through common and detailed questions about metadata.

![Alt text](docs/screenshot.png?raw=true "Screen shot")

This project is modeled off of the original [Metadata Wizard](https://github.com/dignizio-usgs/MDWizard_Source), which was designed as a toolbox in ArcMap, and required an ESRI installation.



----
Disclaimer:
-----------

Although this software program has been used by the U.S. Geological Survey (USGS), no warranty, expressed or implied, is made by the USGS or the U.S. Government as to the accuracy and functioning of the program and related program material nor shall the fact of distribution constitute any such warranty, and no responsibility is assumed by the USGS in connection therewith.