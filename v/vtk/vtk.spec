%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define ver 9.5
%define soname 1

Name: vtk
Version: %ver.2
Release: alt4
Summary: The Visualization Toolkit, an Object-Oriented Approach to 3D Graphics
License: BSD-3-Clause
Group: Development/Tools
Url: https://www.vtk.org/

VCS: https://gitlab.kitware.com/vtk/vtk.git
Source: %name-%version.tar

# Remote modules
Source100: %name-%version-MomentInvariants.tar
Source101: %name-%version-vtkDICOM.tar

Patch1: vtk-9.3.0-alt-python-install-path.patch
Patch2: vtk-9.1.0-alt-dont-fetch-remote-modules.patch
Patch3: vtk-9.1.0-alt-compile-flags.patch
Patch4: vtk-9.4.2-alt-fmt-12.patch
Patch5: vtk-9.5.2-alt-numpy2-in1d.patch
Patch6: vtk-9.5.2-alt-streamtracer-use-after-free.patch
Patch7: vtk-9.5.2-fix-gdal-conversion.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /usr/bin/sqlite3
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-graph-parallel-devel
BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: jsoncpp-devel
BuildRequires: libGLEW-devel
BuildRequires: libGLU-devel
BuildRequires: libXt-devel
BuildRequires: libXxf86misc-devel
BuildRequires: libarchive-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libavformat-devel
BuildRequires: libbfd-devel
BuildRequires: libbrotli-devel
BuildRequires: libcgns-devel
BuildRequires: libdc1394-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: libexpat-devel
BuildRequires: libfmt-devel
BuildRequires: libfreetype-devel
BuildRequires: libftgl220-devel
BuildRequires: libgdal-devel
BuildRequires: libgl2ps-devel
BuildRequires: libgsl-devel
BuildRequires: libgsm-devel
BuildRequires: libharu-devel
BuildRequires: libhdf5-devel
BuildRequires: libimlxx-devel
BuildRequires: libjpeg-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: libnetcdf-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libopenmotif-devel
BuildRequires: libopenslide-devel
BuildRequires: libpcre2-devel
BuildRequires: libpng-devel
BuildRequires: libpostproc-devel
BuildRequires: libproj-devel
BuildRequires: libpugixml-devel
BuildRequires: libsqlite3-devel
BuildRequires: libswscale-devel
BuildRequires: libtag-devel
BuildRequires: libtheora-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: libxml2-devel
BuildRequires: nlohmann-json-devel
BuildRequires: python3-devel
BuildRequires: python3-module-PyQt5-devel
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-sip-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-tools-devel
BuildRequires: tk-devel
BuildRequires: zlib-devel

%description
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

%package -n libMomentInvariants%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): MomentInvariant
Group: System/Libraries

%description -n libMomentInvariants%ver
This package contains shared library of VTK: MomentInvariant.

%package -n libvtkChartsCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ChartsCore
Group: System/Libraries

%description -n libvtkChartsCore%ver
This package contains shared library of VTK: ChartsCore.

%package -n libvtkCommonArchive%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonArchive
Group: System/Libraries

%description -n libvtkCommonArchive%ver
This package contains shared library of VTK: CommonArchive.

%package -n libvtkCommonColor%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonColor
Group: System/Libraries

%description -n libvtkCommonColor%ver
This package contains shared library of VTK: CommonColor.

%package -n libvtkCommonComputationalGeometry%ver
Summary: Shared library CommonComputationalGeometry from Visualization Toolkit
Group: System/Libraries

%description -n libvtkCommonComputationalGeometry%ver
This package contains shared library of VTK: CommonComputationalGeometry.

%package -n libvtkCommonCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonCore
Group: System/Libraries

%description -n libvtkCommonCore%ver
This package contains shared library of VTK: CommonCore.

%package -n libvtkCommonDataModel%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonDataModel
Group: System/Libraries

%description -n libvtkCommonDataModel%ver
This package contains shared library of VTK: CommonDataModel.

%package -n libvtkCommonExecutionModel%ver
Summary: Shared library CommonExecutionModel from Visualization Toolkit (VTK)
Group: System/Libraries

%description -n libvtkCommonExecutionModel%ver
This package contains shared library of VTK: CommonExecutionModel.

%package -n libvtkCommonMath%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonMath
Group: System/Libraries

%description -n libvtkCommonMath%ver
This package contains shared library of VTK: CommonMath.

%package -n libvtkCommonMisc%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonMisc
Group: System/Libraries

%description -n libvtkCommonMisc%ver
This package contains shared library of VTK: CommonMisc.

%package -n libvtkCommonSystem%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonSystem
Group: System/Libraries

%description -n libvtkCommonSystem%ver
This package contains shared library of VTK: CommonSystem.

%package -n libvtkCommonTransforms%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): CommonTransforms
Group: System/Libraries

%description -n libvtkCommonTransforms%ver
This package contains shared library of VTK: CommonTransforms.

%package -n libvtkDICOM%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): DICOM
Group: System/Libraries

%description -n libvtkDICOM%ver
This package contains shared library of VTK: DICOM.

%package -n libvtkDICOMParser%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): DICOMParser
Group: System/Libraries

%description -n libvtkDICOMParser%ver
This package contains shared library of VTK: DICOMParser.

%package -n libvtkDomainsChemistry%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): DomainsChemistry
Group: System/Libraries

%description -n libvtkDomainsChemistry%ver
This package contains shared library of VTK: DomainsChemistry.

%package -n libvtkDomainsChemistryOpenGL2_%ver
Summary: Shared library DomainsChemistryOpenGL2 from Visualization Toolkit
Group: System/Libraries

%description -n libvtkDomainsChemistryOpenGL2_%ver
This package contains shared library of VTK: DomainsChemistryOpenGL2.

%package -n libvtkDomainsMicroscopy%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): DomainsMicroscopy
Group: System/Libraries

%description -n libvtkDomainsMicroscopy%ver
This package contains shared library of VTK: DomainsMicroscopy.

%package -n libvtkGeovisCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): GeovisCore
Group: System/Libraries

%description -n libvtkGeovisCore%ver
This package contains shared library of VTK: GeovisCore.

%package -n libvtkGeovisGDAL%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): GeovisGDAL
Group: System/Libraries

%description -n libvtkGeovisGDAL%ver
This package contains shared library of VTK: GeovisGDAL.

%package -n libvtkIOAMR%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOAMR
Group: System/Libraries

%description -n libvtkIOAMR%ver
This package contains shared library of VTK: IOAMR.

%package -n libvtkIOAsynchronous%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOAsynchronous
Group: System/Libraries

%description -n libvtkIOAsynchronous%ver
This package contains shared library of VTK: IOAsynchronous.

%package -n libvtkIOCGNSReader%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCGNSReader
Group: System/Libraries

%description -n libvtkIOCGNSReader%ver
This package contains shared library of VTK: IOCGNSReader.

%package -n libvtkIOCONVERGECFD%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCONVERGECFD
Group: System/Libraries

%description -n libvtkIOCONVERGECFD%ver
This package contains shared library of VTK: IOCONVERGECFD.

%package -n libvtkIOCellGrid%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCellGrid
Group: System/Libraries

%description -n libvtkIOCellGrid%ver
This package contains shared library of VTK: IOCellGrid.

%package -n libvtkIOCesium3DTiles%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCesium3DTiles
Group: System/Libraries

%description -n libvtkIOCesium3DTiles%ver
This package contains shared library of VTK: IOCesium3DTiles.

%package -n libvtkIOChemistry%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOChemistry
Group: System/Libraries

%description -n libvtkIOChemistry%ver
This package contains shared library of VTK: IOChemistry.

%package -n libvtkIOCityGML%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCityGML
Group: System/Libraries

%description -n libvtkIOCityGML%ver
This package contains shared library of VTK: IOCityGML.

%package -n libvtkIOCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOCore
Group: System/Libraries

%description -n libvtkIOCore%ver
This package contains shared library of VTK: IOCore.

%package -n libvtkIOERF%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOERF
Group: System/Libraries

%description -n libvtkIOERF%ver
This package contains shared library of VTK: IOERF.

%package -n libvtkIOEnSight%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOEnSight
Group: System/Libraries

%description -n libvtkIOEnSight%ver
This package contains shared library of VTK: IOEnSight.

%package -n libvtkIOEngys%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOEngys
Group: System/Libraries

%description -n libvtkIOEngys%ver
This package contains shared library of VTK: IOEngys.

%package -n libvtkIOExodus%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOExodus
Group: System/Libraries

%description -n libvtkIOExodus%ver
This package contains shared library of VTK: IOExodus.

%package -n libvtkIOExport%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOExport
Group: System/Libraries

%description -n libvtkIOExport%ver
This package contains shared library of VTK: IOExport.

%package -n libvtkIOExportGL2PS%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOExportGL2PS
Group: System/Libraries

%description -n libvtkIOExportGL2PS%ver
This package contains shared library of VTK: IOExportGL2PS.

%package -n libvtkIOExportPDF%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOExportPDF
Group: System/Libraries

%description -n libvtkIOExportPDF%ver
This package contains shared library of VTK: IOExportPDF.

%package -n libvtkIOFDS%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOFDS
Group: System/Libraries

%description -n libvtkIOFDS%ver
This package contains shared library of VTK: IOFDS.

%package -n libvtkIOFLUENTCFF%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOFLUENTCFF
Group: System/Libraries

%description -n libvtkIOFLUENTCFF%ver
This package contains shared library of VTK: IOFLUENTCFF.

%package -n libvtkIOGDAL%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOGDAL
Group: System/Libraries

%description -n libvtkIOGDAL%ver
This package contains shared library of VTK: IOGDAL.

%package -n libvtkIOGeometry%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOGeometry
Group: System/Libraries

%description -n libvtkIOGeometry%ver
This package contains shared library of VTK: IOGeometry.

%package -n libvtkIOHDF%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOHDF
Group: System/Libraries

%description -n libvtkIOHDF%ver
This package contains shared library of VTK: IOHDF.

%package -n libvtkIOIOSS%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOIOSS
Group: System/Libraries

%description -n libvtkIOIOSS%ver
This package contains shared library of VTK: IOIOSS.

%package -n libvtkIOImage%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOImage
Group: System/Libraries

%description -n libvtkIOImage%ver
This package contains shared library of VTK: IOImage.

%package -n libvtkIOImport%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOImport
Group: System/Libraries

%description -n libvtkIOImport%ver
This package contains shared library of VTK: IOImport.

%package -n libvtkIOInfovis%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOInfovis
Group: System/Libraries

%description -n libvtkIOInfovis%ver
This package contains shared library of VTK: IOInfovis.

%package -n libvtkIOLSDyna%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOLSDyna
Group: System/Libraries

%description -n libvtkIOLSDyna%ver
This package contains shared library of VTK: IOLSDyna.

%package -n libvtkIOLegacy%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOLegacy
Group: System/Libraries

%description -n libvtkIOLegacy%ver
This package contains shared library of VTK: IOLegacy.

%package -n libvtkIOLANLX3D%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOLANLX3D
Group: System/Libraries

%description -n libvtkIOLANLX3D%ver
This package contains shared library of VTK: IOLANLX3D.

%package -n libvtkIOMINC%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOMINC
Group: System/Libraries

%description -n libvtkIOMINC%ver
This package contains shared library of VTK: IOMINC.

%package -n libvtkIOMotionFX%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOMotionFX
Group: System/Libraries

%description -n libvtkIOMotionFX%ver
This package contains shared library of VTK: IOMotionFX.

%package -n libvtkIOMovie%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOMovie
Group: System/Libraries

%description -n libvtkIOMovie%ver
This package contains shared library of VTK: IOMovie.

%package -n libvtkIONetCDF%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IONetCDF
Group: System/Libraries

%description -n libvtkIONetCDF%ver
This package contains shared library of VTK: IONetCDF.

%package -n libvtkIOOggTheora%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOOggTheora
Group: System/Libraries

%description -n libvtkIOOggTheora%ver
This package contains shared library of VTK: IOOggTheora.

%package -n libvtkIOPLY%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOPLY
Group: System/Libraries

%description -n libvtkIOPLY%ver
This package contains shared library of VTK: IOPLY.

%package -n libvtkIOParallel%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOParallel
Group: System/Libraries

%description -n libvtkIOParallel%ver
This package contains shared library of VTK: IOParallel.

%package -n libvtkIOParallelXML%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOParallelXML
Group: System/Libraries

%description -n libvtkIOParallelXML%ver
This package contains shared library of VTK: IOParallelXML.

%package -n libvtkIOSQL%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOSQL
Group: System/Libraries

%description -n libvtkIOSQL%ver
This package contains shared library of VTK: IOSQL.

%package -n libvtkIOSegY%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOSegY
Group: System/Libraries

%description -n libvtkIOSegY%ver
This package contains shared library of VTK: IOSegY.

%package -n libvtkIOTecplotTable%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOTecplotTable
Group: System/Libraries

%description -n libvtkIOTecplotTable%ver
This package contains shared library of VTK: IOTecplotTable.

%package -n libvtkIOVeraOut%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOVeraOut
Group: System/Libraries

%description -n libvtkIOVeraOut%ver
This package contains shared library of VTK: IOVeraOut.

%package -n libvtkIOVideo%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOVideo
Group: System/Libraries

%description -n libvtkIOVideo%ver
This package contains shared library of VTK: IOVideo.

%package -n libvtkIOXML%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOXML
Group: System/Libraries

%description -n libvtkIOXML%ver
This package contains shared library of VTK: IOXML.

%package -n libvtkIOXMLParser%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): IOXMLParser
Group: System/Libraries

%description -n libvtkIOXMLParser%ver
This package contains shared library of VTK: IOXMLParser.

%package -n libvtkImagingColor%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingColor
Group: System/Libraries

%description -n libvtkImagingColor%ver
This package contains shared library of VTK: ImagingColor.

%package -n libvtkImagingCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingCore
Group: System/Libraries

%description -n libvtkImagingCore%ver
This package contains shared library of VTK: ImagingCore.

%package -n libvtkImagingFourier%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingFourier
Group: System/Libraries

%description -n libvtkImagingFourier%ver
This package contains shared library of VTK: ImagingFourier.

%package -n libvtkImagingGeneral%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingGeneral
Group: System/Libraries

%description -n libvtkImagingGeneral%ver
This package contains shared library of VTK: ImagingGeneral.

%package -n libvtkImagingHybrid%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingHybrid
Group: System/Libraries

%description -n libvtkImagingHybrid%ver
This package contains shared library of VTK: ImagingHybrid.

%package -n libvtkImagingMath%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingMath
Group: System/Libraries

%description -n libvtkImagingMath%ver
This package contains shared library of VTK: ImagingMath.

%package -n libvtkImagingMorphological%ver
Summary: Shared library ImagingMorphological from Visualization Toolkit (VTK)
Group: System/Libraries

%description -n libvtkImagingMorphological%ver
This package contains shared library of VTK: ImagingMorphological.

%package -n libvtkImagingOpenGL2_%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingOpenGL2
Group: System/Libraries

%description -n libvtkImagingOpenGL2_%ver
This package contains shared library of VTK: ImagingOpenGL2.

%package -n libvtkImagingSources%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingSources
Group: System/Libraries

%description -n libvtkImagingSources%ver
This package contains shared library of VTK: ImagingSources.

%package -n libvtkImagingStatistics%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingStatistics
Group: System/Libraries

%description -n libvtkImagingStatistics%ver
This package contains shared library of VTK: ImagingStatistics.

%package -n libvtkImagingStencil%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ImagingStencil
Group: System/Libraries

%description -n libvtkImagingStencil%ver
This package contains shared library of VTK: ImagingStencil.

%package -n libvtkInfovisBoostGraphAlgorithms%ver
Summary: Shared library InfovisBoostGraphAlgorithms from Visualization Toolkit
Group: System/Libraries

%description -n libvtkInfovisBoostGraphAlgorithms%ver
This package contains shared library of VTK: InfovisBoostGraphAlgorithms.

%package -n libvtkInfovisCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): InfovisCore
Group: System/Libraries

%description -n libvtkInfovisCore%ver
This package contains shared library of VTK: InfovisCore.

%package -n libvtkInfovisLayout%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): InfovisLayout
Group: System/Libraries

%description -n libvtkInfovisLayout%ver
This package contains shared library of VTK: InfovisLayout.

%package -n libvtkInteractionImage%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): InteractionImage
Group: System/Libraries

%description -n libvtkInteractionImage%ver
This package contains shared library of VTK: InteractionImage.

%package -n libvtkInteractionStyle%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): InteractionStyle
Group: System/Libraries

%description -n libvtkInteractionStyle%ver
This package contains shared library of VTK: InteractionStyle.

%package -n libvtkInteractionWidgets%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): InteractionWidgets
Group: System/Libraries

%description -n libvtkInteractionWidgets%ver
This package contains shared library of VTK: InteractionWidgets.

%package -n libvtkParallelCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ParallelCore
Group: System/Libraries

%description -n libvtkParallelCore%ver
This package contains shared library of VTK: ParallelCore.

%package -n libvtkParallelDIY%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ParallelDIY
Group: System/Libraries

%description -n libvtkParallelDIY%ver
This package contains shared library of VTK: ParallelDIY.

%package -n libvtkTestingCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): TestingCore
Group: System/Libraries

%description -n libvtkTestingCore%ver
This package contains shared library of VTK: TestingCore.

%package -n libvtkTestingRendering%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): TestingRendering
Group: System/Libraries

%description -n libvtkTestingRendering%ver
This package contains shared library of VTK: TestingRendering.

%package -n libvtkViewsContext2D%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ViewsContext2D
Group: System/Libraries

%description -n libvtkViewsContext2D%ver
This package contains shared library of VTK: ViewsContext2D.

%package -n libvtkViewsCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ViewsCore
Group: System/Libraries

%description -n libvtkViewsCore%ver
This package contains shared library of VTK: ViewsCore.

%package -n libvtkViewsInfovis%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ViewsInfovis
Group: System/Libraries

%description -n libvtkViewsInfovis%ver
This package contains shared library of VTK: ViewsInfovis.

%package -n libvtkWebCore%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): WebCore
Group: System/Libraries

%description -n libvtkWebCore%ver
This package contains shared library of VTK: WebCore.

%package -n libvtkWebGLExporter%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): WebGLExporter
Group: System/Libraries

%description -n libvtkWebGLExporter%ver
This package contains shared library of VTK: WebGLExporter.

%package -n libvtkWrappingTools%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): WrappingTools
Group: System/Libraries

%description -n libvtkWrappingTools%ver
This package contains shared library of VTK: WrappingTools.

%package -n libvtkexodusII%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): exodusII
Group: System/Libraries

%description -n libvtkexodusII%ver
This package contains shared library of VTK: exodusII.

%package -n libvtkglad%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): glad
Group: System/Libraries

%description -n libvtkglad%ver
This package contains shared library of VTK: glad.

%package -n libvtkioss%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): ioss
Group: System/Libraries

%description -n libvtkioss%ver
This package contains shared library of VTK: ioss.

%package -n libvtkkissfft%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): kissfft
Group: System/Libraries

%description -n libvtkkissfft%ver
This package contains shared library of VTK: kissfft.

%package -n libvtkloguru%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): loguru
Group: System/Libraries

%description -n libvtkloguru%ver
This package contains shared library of VTK: loguru.

%package -n libvtkmetaio%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): metaio
Group: System/Libraries

%description -n libvtkmetaio%ver
This package contains shared library of VTK: metaio.

%package -n libvtksys%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): sys
Group: System/Libraries

%description -n libvtksys%ver
This package contains shared library of VTK: sys.

%package -n libvtktoken%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): token
Group: System/Libraries

%description -n libvtktoken%ver
This package contains shared library of VTK: token.

%package -n libvtkverdict%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): verdict
Group: System/Libraries

%description -n libvtkverdict%ver
This package contains shared library of VTK: verdict.

%package -n libvtkfilters%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): filters
Group: System/Libraries

%description -n libvtkfilters%ver
This package contains shared libraries of VTK filters.

%package -n libvtkrendering%ver
Summary: Shared libraries of The Visualization Toolkit (VTK): rendering
Group: System/Libraries

%description -n libvtkrendering%ver
This package contains shared libraries of VTK rendering.

%package -n libvtk-devel
Summary: Development files of The Visualization Toolkit (VTK)
Group: Development/C++
Requires: vtk = %EVR
Requires: vtk-python3 = %EVR
Requires: libvtk%ver-python3 = %EVR
Requires: python3-module-vtk = %EVR
Requires: python3-module-vtk-tests = %EVR
Requires: nlohmann-json-devel
%ifnarch %arm
Requires: vtk-qt5 = %EVR
%endif
# Following dependencies are duplicates from build dependencies
Requires: qt5-base-devel
Requires: qt5-declarative-devel
Requires: libfreetype-devel
Requires: eigen3-devel
Requires: libdouble-conversion-devel
Requires: python3-devel
Requires: libxml2-devel
Requires: libgdal-devel
Requires: libGLEW-devel
Requires: libarchive-devel
Requires: libcgns-devel
Requires: libfmt-devel
Conflicts: libvtk6.1-devel
Conflicts: libvtk6.2-devel
Conflicts: libvtk8.1-devel
Conflicts: libvtk8.2-devel

%description -n libvtk-devel
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains development files of VTK.

# Used by:
# - gdcm
# - opencascade
%package -n rpm-macros-vtk
Summary: Macros for packages depended by Visualization Toolkit (VTK)
Group: Development/C++
BuildArch: noarch

%description -n rpm-macros-vtk
This package contain file with macros for building packages depended by VTK.


%package python3
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: vtk = %EVR
Requires: libvtk%ver-python3 = %EVR
Requires: python3-module-vtk = %EVR
Conflicts: vtk6.1-python
Conflicts: vtk6.2-python
Conflicts: vtk8.1-python
Conflicts: vtk8.2-python
Conflicts: vtk8.2-python3

%description python3
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n libvtk%ver-python3
Summary: The Visualization Toolkit (VTK) Python shared libraries
Group: System/Libraries

%description -n libvtk%ver-python3
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains Python shared libraries of VTK.

%package -n python3-module-vtk
Summary: The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: libvtk%ver-python3 = %EVR
%add_python3_req_skip GDK
%add_python3_req_skip gtk
%add_python3_req_skip gtk.gtkgl
%add_python3_req_skip gtkgl
%add_python3_req_skip pygtk
%add_python3_req_skip vtk.vtkCommonCore
%add_python3_req_skip vtk.vtkFiltersGeometry
%add_python3_req_skip vtk.vtkRenderingCore
%add_python3_req_skip vtk.vtkWebCore
%add_python3_req_skip vtk.web
%add_python3_req_skip vtk.web.camera
%add_python3_req_skip vtk.web.query_data_model
%add_python3_req_skip vtkParallelPython
%add_python3_req_skip wslink.websocket
%py3_requires PyQt5
Provides: python3-module-vtk8.2 = %EVR
Obsoletes: python3-module-vtk8.2 < %EVR
Conflicts: python3-module-vtk8.2 < %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/vtkmodules/web/wslink.py

%description -n python3-module-vtk
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package provides Python bindings to VTK.

%package -n python3-module-vtk-tests
Summary: Tests for The Visualization Toolkit (VTK) Python bindings
Group: Development/Python3
Requires: python3-module-vtk = %EVR
Provides: python3-module-vtk8.2-tests = %EVR
Obsoletes: python3-module-vtk8.2-tests < %EVR
Conflicts: python3-module-vtk8.2-tests < %EVR

%description -n python3-module-vtk-tests
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains tests for Python bindings to VTK.

%package examples
Summary: The Visualization Toolkit (VTK) examples
Group: Development/Tools
BuildArch: noarch
Requires: vtk = %EVR
%add_python3_req_skip numeric

%description examples
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK examples.

%package qt5
Summary: The Visualization Toolkit (VTK) QML plugin
Group: System/Libraries

%description qt5
VTK is an open-source software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms (e.g.,
surface reconstruction, implicit modelling, decimation) and rendering techniques
(e.g., hardware-accelerated volume rendering, LOD control).

This package contains VTK QML plugin.

%prep
%setup -a100 -a101
%autopatch -p1

%ifarch %e2k
sed -i -E 's/(std::vector<.*(pointList_|transforms_))\{\}/\1={}/' \
	ThirdParty/ioss/vtkioss/Ioss_{Field,CoordinateFrame}.h
sed -i 's/large_power_of_5\[\] = {/large_power_of_5[5] = {/' \
	ThirdParty/fast_float/vtkfast_float/vtkfast_float/bigint.h
sed -i '/#define vtkOpenFOAMReader_h/a #include "vtkUnsignedCharArray.h"' \
	IO/Geometry/vtkOpenFOAMReader.h
%endif

# apply build timestamp
CMake/vtkVersion.bash -f

# remove bundled libraries
rm -rf \
   ThirdParty/AutobahnPython/vtkAutobahn \
   ThirdParty/Twisted/vtkTwisted \
   ThirdParty/ZopeInterface/vtkZopeInterface \
   ThirdParty/constantly/vtkconstantly \
   ThirdParty/expat/vtkexpat \
   ThirdParty/freetype/vtkfreetype \
   ThirdParty/gl2ps/vtkgl2ps \
   ThirdParty/hdf5/vtkhdf5 \
   ThirdParty/hyperlink/vtkhyperlink \
   ThirdParty/incremental/vtkincremental \
   ThirdParty/jpeg/vtkjpeg \
   ThirdParty/jsoncpp/vtkjsoncpp \
   ThirdParty/libharu/vtklibharu \
   ThirdParty/libxml2/vtklibxml2 \
   ThirdParty/lz4/vtklz4 \
   ThirdParty/netcdf/vtknetcdf \
   ThirdParty/oggtheora/vtkoggtheora \
   ThirdParty/png/vtkpng \
   ThirdParty/tiff/vtktiff \
   ThirdParty/txaio/vtktxaio \
   ThirdParty/zlib/vtkzlib \
   #

%build
PATH=$PATH:%_qt5_bindir

export PYTHON=%__python3
%add_optflags -I%_includedir/gsl
%add_optflags -DHAVE_SYS_TIME_H -DHAVE_SYS_TYPES_H -DHAVE_SYS_SOCKET_H
%add_optflags -D__USE_LARGEFILE64 -DH5_HAVE_SIGSETJMP -D__USE_POSIX
%add_optflags -DH5_HAVE_SETJMP_H
%add_optflags -D_FILE_OFFSET_BITS=64

%ifarch %e2k
# ld: failed to set dynamic section sizes: memory exhausted
%add_optflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
%add_optflags -fno-lto
%endif

# remote module flags go last
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_SKIP_BUILD_RPATH=OFF \
	-DCMAKE_BUILD_RPATH_USE_ORIGIN=ON \
	-DCMAKE_INSTALL_QMLDIR=%_qt5_qmldir \
	-DVTK_BUILD_DOCUMENTATION=OFF \
	-DVTK_BUILD_EXAMPLES=OFF \
	-DVTK_BUILD_TESTING=OFF \
	-DVTK_EXTRA_COMPILER_WARNINGS=ON \
	-DVTK_GROUP_ENABLE_Imaging:STRING=YES \
	-DVTK_GROUP_ENABLE_Rendering:STRING=YES \
	-DVTK_GROUP_ENABLE_StandAlone:STRING=YES \
	-DVTK_GROUP_ENABLE_Views:STRING=YES \
	-DVTK_GROUP_ENABLE_Web:STRING=YES \
	-DCMAKE_INSTALL_LICENSEDIR:PATH=share/doc/vtk-%ver/licenses \
	-DVTK_MODULE_ENABLE_VTK_CommonArchive:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_DomainsMicroscopy:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_GeovisGDAL:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_ImagingOpenGL2:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_InfovisBoost:STRING=YES \
	-DVTK_MODULE_ENABLE_VTK_InfovisBoostGraphAlgorithms:STRING=YES \
%ifarch %arm
	-DVTK_GROUP_ENABLE_Qt:STRING=NO \
%else
	-DVTK_GROUP_ENABLE_Qt:STRING=YES \
%endif
	-DVTK_USE_EXTERNAL=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_fast_float=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_verdict=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_expat=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_exprtk=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_freetype=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_hdf5=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_ioss=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_jpeg=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libharu=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libproj=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_libxml2=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_lz4=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_netcdf=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_png=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_tiff=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_token=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_zlib=ON \
	-DVTK_MODULE_USE_EXTERNAL_VTK_utf8=OFF \
	-DVTK_MODULE_USE_EXTERNAL_VTK_pegtl=OFF \
	-DVTK_PYTHON_VERSION=3 \
	-DVTK_PYTHON_OPTIONAL_LINK=OFF \
	-DVTK_SMP_IMPLEMENTATION_TYPE="Sequential" \
	-DVTK_USE_X=ON \
	-DVTK_WRAP_PYTHON=ON \
	-DVTK_MODULE_ENABLE_VTK_ParallelMomentInvariants:STRING=NO \
	-DVTK_MODULE_ENABLE_VTK_MomentInvariants:STRING=YES \
	%nil

export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/%_lib
%cmake_build

%install
export LD_LIBRARY_PATH=$PWD/%_cmake__builddir/%_lib
%cmakeinstall_std

mkdir -p %buildroot%_rpmmacrosdir
cat << EOF > %buildroot%_rpmmacrosdir/vtk
%%vtk_soname %soname
%%vtk_version %ver
EOF

%files
%doc Copyright.txt README.md
%_datadir/doc/vtk-%ver/licenses
%_bindir/vtkParseJava-%ver
%_bindir/vtkWrapHierarchy-%ver
%_bindir/vtkWrapJava-%ver
%_bindir/vtkProbeOpenGLVersion-%ver
%_bindir/vtkWrapSerDes-%ver

%files -n rpm-macros-vtk
%_rpmmacrosdir/vtk

%files -n libMomentInvariants%ver
%_libdir/libMomentInvariants-%ver.so.%soname
%_libdir/libMomentInvariants-%ver.so.%ver

%files -n libvtkChartsCore%ver
%_libdir/libvtkChartsCore-%ver.so.%soname
%_libdir/libvtkChartsCore-%ver.so.%ver

%files -n libvtkCommonArchive%ver
%_libdir/libvtkCommonArchive-%ver.so.%soname
%_libdir/libvtkCommonArchive-%ver.so.%ver

%files -n libvtkCommonColor%ver
%_libdir/libvtkCommonColor-%ver.so.%soname
%_libdir/libvtkCommonColor-%ver.so.%ver

%files -n libvtkCommonComputationalGeometry%ver
%_libdir/libvtkCommonComputationalGeometry-%ver.so.%soname
%_libdir/libvtkCommonComputationalGeometry-%ver.so.%ver

%files -n libvtkCommonCore%ver
%_libdir/libvtkCommonCore-%ver.so.%soname
%_libdir/libvtkCommonCore-%ver.so.%ver

%files -n libvtkCommonDataModel%ver
%_libdir/libvtkCommonDataModel-%ver.so.%soname
%_libdir/libvtkCommonDataModel-%ver.so.%ver

%files -n libvtkCommonExecutionModel%ver
%_libdir/libvtkCommonExecutionModel-%ver.so.%soname
%_libdir/libvtkCommonExecutionModel-%ver.so.%ver

%files -n libvtkCommonMath%ver
%_libdir/libvtkCommonMath-%ver.so.%soname
%_libdir/libvtkCommonMath-%ver.so.%ver

%files -n libvtkCommonMisc%ver
%_libdir/libvtkCommonMisc-%ver.so.%soname
%_libdir/libvtkCommonMisc-%ver.so.%ver

%files -n libvtkCommonSystem%ver
%_libdir/libvtkCommonSystem-%ver.so.%soname
%_libdir/libvtkCommonSystem-%ver.so.%ver

%files -n libvtkCommonTransforms%ver
%_libdir/libvtkCommonTransforms-%ver.so.%soname
%_libdir/libvtkCommonTransforms-%ver.so.%ver

%files -n libvtkDICOM%ver
%_libdir/libvtkDICOM-%ver.so.%soname
%_libdir/libvtkDICOM-%ver.so.%ver

%files -n libvtkDICOMParser%ver
%_libdir/libvtkDICOMParser-%ver.so.%soname
%_libdir/libvtkDICOMParser-%ver.so.%ver

%files -n libvtkDomainsChemistry%ver
%_libdir/libvtkDomainsChemistry-%ver.so.%soname
%_libdir/libvtkDomainsChemistry-%ver.so.%ver

%files -n libvtkDomainsChemistryOpenGL2_%ver
%_libdir/libvtkDomainsChemistryOpenGL2-%ver.so.%soname
%_libdir/libvtkDomainsChemistryOpenGL2-%ver.so.%ver

%files -n libvtkDomainsMicroscopy%ver
%_libdir/libvtkDomainsMicroscopy-%ver.so.%soname
%_libdir/libvtkDomainsMicroscopy-%ver.so.%ver

%files -n libvtkGeovisCore%ver
%_libdir/libvtkGeovisCore-%ver.so.%soname
%_libdir/libvtkGeovisCore-%ver.so.%ver

%files -n libvtkGeovisGDAL%ver
%_libdir/libvtkGeovisGDAL-%ver.so.%soname
%_libdir/libvtkGeovisGDAL-%ver.so.%ver

%files -n libvtkIOAMR%ver
%_libdir/libvtkIOAMR-%ver.so.%soname
%_libdir/libvtkIOAMR-%ver.so.%ver

%files -n libvtkIOAsynchronous%ver
%_libdir/libvtkIOAsynchronous-%ver.so.%soname
%_libdir/libvtkIOAsynchronous-%ver.so.%ver

%files -n libvtkIOCGNSReader%ver
%_libdir/libvtkIOCGNSReader-%ver.so.%soname
%_libdir/libvtkIOCGNSReader-%ver.so.%ver

%files -n libvtkIOCONVERGECFD%ver
%_libdir/libvtkIOCONVERGECFD-%ver.so.%soname
%_libdir/libvtkIOCONVERGECFD-%ver.so.%ver

%files -n libvtkIOCellGrid%ver
%_libdir/libvtkIOCellGrid-%ver.so.%soname
%_libdir/libvtkIOCellGrid-%ver.so.%ver

%files -n libvtkIOCesium3DTiles%ver
%_libdir/libvtkIOCesium3DTiles-%ver.so.%soname
%_libdir/libvtkIOCesium3DTiles-%ver.so.%ver

%files -n libvtkIOChemistry%ver
%_libdir/libvtkIOChemistry-%ver.so.%soname
%_libdir/libvtkIOChemistry-%ver.so.%ver

%files -n libvtkIOCityGML%ver
%_libdir/libvtkIOCityGML-%ver.so.%soname
%_libdir/libvtkIOCityGML-%ver.so.%ver

%files -n libvtkIOCore%ver
%_libdir/libvtkIOCore-%ver.so.%soname
%_libdir/libvtkIOCore-%ver.so.%ver

%files -n libvtkIOERF%ver
%_libdir/libvtkIOERF-%ver.so.%soname
%_libdir/libvtkIOERF-%ver.so.%ver

%files -n libvtkIOEnSight%ver
%_libdir/libvtkIOEnSight-%ver.so.%soname
%_libdir/libvtkIOEnSight-%ver.so.%ver

%files -n libvtkIOEngys%ver
%_libdir/libvtkIOEngys-%ver.so.%soname
%_libdir/libvtkIOEngys-%ver.so.%ver

%files -n libvtkIOExodus%ver
%_libdir/libvtkIOExodus-%ver.so.%soname
%_libdir/libvtkIOExodus-%ver.so.%ver

%files -n libvtkIOExport%ver
%_libdir/libvtkIOExport-%ver.so.%soname
%_libdir/libvtkIOExport-%ver.so.%ver

%files -n libvtkIOExportGL2PS%ver
%_libdir/libvtkIOExportGL2PS-%ver.so.%soname
%_libdir/libvtkIOExportGL2PS-%ver.so.%ver

%files -n libvtkIOExportPDF%ver
%_libdir/libvtkIOExportPDF-%ver.so.%soname
%_libdir/libvtkIOExportPDF-%ver.so.%ver

%files -n libvtkIOFDS%ver
%_libdir/libvtkIOFDS-%ver.so.%soname
%_libdir/libvtkIOFDS-%ver.so.%ver

%files -n libvtkIOFLUENTCFF%ver
%_libdir/libvtkIOFLUENTCFF-%ver.so.%soname
%_libdir/libvtkIOFLUENTCFF-%ver.so.%ver

%files -n libvtkIOGDAL%ver
%_libdir/libvtkIOGDAL-%ver.so.%soname
%_libdir/libvtkIOGDAL-%ver.so.%ver

%files -n libvtkIOGeometry%ver
%_libdir/libvtkIOGeometry-%ver.so.%soname
%_libdir/libvtkIOGeometry-%ver.so.%ver

%files -n libvtkIOHDF%ver
%_libdir/libvtkIOHDF-%ver.so.%soname
%_libdir/libvtkIOHDF-%ver.so.%ver

%files -n libvtkIOIOSS%ver
%_libdir/libvtkIOIOSS-%ver.so.%soname
%_libdir/libvtkIOIOSS-%ver.so.%ver

%files -n libvtkIOImage%ver
%_libdir/libvtkIOImage-%ver.so.%soname
%_libdir/libvtkIOImage-%ver.so.%ver

%files -n libvtkIOImport%ver
%_libdir/libvtkIOImport-%ver.so.%soname
%_libdir/libvtkIOImport-%ver.so.%ver

%files -n libvtkIOInfovis%ver
%_libdir/libvtkIOInfovis-%ver.so.%soname
%_libdir/libvtkIOInfovis-%ver.so.%ver

%files -n libvtkIOLSDyna%ver
%_libdir/libvtkIOLSDyna-%ver.so.%soname
%_libdir/libvtkIOLSDyna-%ver.so.%ver

%files -n libvtkIOLegacy%ver
%_libdir/libvtkIOLegacy-%ver.so.%soname
%_libdir/libvtkIOLegacy-%ver.so.%ver

%files -n libvtkIOLANLX3D%ver
%_libdir/libvtkIOLANLX3D-%ver.so.%soname
%_libdir/libvtkIOLANLX3D-%ver.so.%ver

%files -n libvtkIOMINC%ver
%_libdir/libvtkIOMINC-%ver.so.%soname
%_libdir/libvtkIOMINC-%ver.so.%ver

%files -n libvtkIOMotionFX%ver
%_libdir/libvtkIOMotionFX-%ver.so.%soname
%_libdir/libvtkIOMotionFX-%ver.so.%ver

%files -n libvtkIOMovie%ver
%_libdir/libvtkIOMovie-%ver.so.%soname
%_libdir/libvtkIOMovie-%ver.so.%ver

%files -n libvtkIONetCDF%ver
%_libdir/libvtkIONetCDF-%ver.so.%soname
%_libdir/libvtkIONetCDF-%ver.so.%ver

%files -n libvtkIOOggTheora%ver
%_libdir/libvtkIOOggTheora-%ver.so.%soname
%_libdir/libvtkIOOggTheora-%ver.so.%ver

%files -n libvtkIOPLY%ver
%_libdir/libvtkIOPLY-%ver.so.%soname
%_libdir/libvtkIOPLY-%ver.so.%ver

%files -n libvtkIOParallel%ver
%_libdir/libvtkIOParallel-%ver.so.%soname
%_libdir/libvtkIOParallel-%ver.so.%ver

%files -n libvtkIOParallelXML%ver
%_libdir/libvtkIOParallelXML-%ver.so.%soname
%_libdir/libvtkIOParallelXML-%ver.so.%ver

%files -n libvtkIOSQL%ver
%_libdir/libvtkIOSQL-%ver.so.%soname
%_libdir/libvtkIOSQL-%ver.so.%ver

%files -n libvtkIOSegY%ver
%_libdir/libvtkIOSegY-%ver.so.%soname
%_libdir/libvtkIOSegY-%ver.so.%ver

%files -n libvtkIOTecplotTable%ver
%_libdir/libvtkIOTecplotTable-%ver.so.%soname
%_libdir/libvtkIOTecplotTable-%ver.so.%ver

%files -n libvtkIOVeraOut%ver
%_libdir/libvtkIOVeraOut-%ver.so.%soname
%_libdir/libvtkIOVeraOut-%ver.so.%ver

%files -n libvtkIOVideo%ver
%_libdir/libvtkIOVideo-%ver.so.%soname
%_libdir/libvtkIOVideo-%ver.so.%ver

%files -n libvtkIOXML%ver
%_libdir/libvtkIOXML-%ver.so.%soname
%_libdir/libvtkIOXML-%ver.so.%ver

%files -n libvtkIOXMLParser%ver
%_libdir/libvtkIOXMLParser-%ver.so.%soname
%_libdir/libvtkIOXMLParser-%ver.so.%ver

%files -n libvtkImagingColor%ver
%_libdir/libvtkImagingColor-%ver.so.%soname
%_libdir/libvtkImagingColor-%ver.so.%ver

%files -n libvtkImagingCore%ver
%_libdir/libvtkImagingCore-%ver.so.%soname
%_libdir/libvtkImagingCore-%ver.so.%ver

%files -n libvtkImagingFourier%ver
%_libdir/libvtkImagingFourier-%ver.so.%soname
%_libdir/libvtkImagingFourier-%ver.so.%ver

%files -n libvtkImagingGeneral%ver
%_libdir/libvtkImagingGeneral-%ver.so.%soname
%_libdir/libvtkImagingGeneral-%ver.so.%ver

%files -n libvtkImagingHybrid%ver
%_libdir/libvtkImagingHybrid-%ver.so.%soname
%_libdir/libvtkImagingHybrid-%ver.so.%ver

%files -n libvtkImagingMath%ver
%_libdir/libvtkImagingMath-%ver.so.%soname
%_libdir/libvtkImagingMath-%ver.so.%ver

%files -n libvtkImagingMorphological%ver
%_libdir/libvtkImagingMorphological-%ver.so.%soname
%_libdir/libvtkImagingMorphological-%ver.so.%ver

%files -n libvtkImagingOpenGL2_%ver
%_libdir/libvtkImagingOpenGL2-%ver.so.%soname
%_libdir/libvtkImagingOpenGL2-%ver.so.%ver

%files -n libvtkImagingSources%ver
%_libdir/libvtkImagingSources-%ver.so.%soname
%_libdir/libvtkImagingSources-%ver.so.%ver

%files -n libvtkImagingStatistics%ver
%_libdir/libvtkImagingStatistics-%ver.so.%soname
%_libdir/libvtkImagingStatistics-%ver.so.%ver

%files -n libvtkImagingStencil%ver
%_libdir/libvtkImagingStencil-%ver.so.%soname
%_libdir/libvtkImagingStencil-%ver.so.%ver

%files -n libvtkInfovisBoostGraphAlgorithms%ver
%_libdir/libvtkInfovisBoostGraphAlgorithms-%ver.so.%soname
%_libdir/libvtkInfovisBoostGraphAlgorithms-%ver.so.%ver

%files -n libvtkInfovisCore%ver
%_libdir/libvtkInfovisCore-%ver.so.%soname
%_libdir/libvtkInfovisCore-%ver.so.%ver

%files -n libvtkInfovisLayout%ver
%_libdir/libvtkInfovisLayout-%ver.so.%soname
%_libdir/libvtkInfovisLayout-%ver.so.%ver

%files -n libvtkInteractionImage%ver
%_libdir/libvtkInteractionImage-%ver.so.%soname
%_libdir/libvtkInteractionImage-%ver.so.%ver

%files -n libvtkInteractionStyle%ver
%_libdir/libvtkInteractionStyle-%ver.so.%soname
%_libdir/libvtkInteractionStyle-%ver.so.%ver

%files -n libvtkInteractionWidgets%ver
%_libdir/libvtkInteractionWidgets-%ver.so.%soname
%_libdir/libvtkInteractionWidgets-%ver.so.%ver

%files -n libvtkParallelCore%ver
%_libdir/libvtkParallelCore-%ver.so.%soname
%_libdir/libvtkParallelCore-%ver.so.%ver

%files -n libvtkParallelDIY%ver
%_libdir/libvtkParallelDIY-%ver.so.%soname
%_libdir/libvtkParallelDIY-%ver.so.%ver

%files -n libvtkTestingCore%ver
%_libdir/libvtkTestingCore-%ver.so.%soname
%_libdir/libvtkTestingCore-%ver.so.%ver

%files -n libvtkTestingRendering%ver
%_libdir/libvtkTestingRendering-%ver.so.%soname
%_libdir/libvtkTestingRendering-%ver.so.%ver

%files -n libvtkViewsContext2D%ver
%_libdir/libvtkViewsContext2D-%ver.so.%soname
%_libdir/libvtkViewsContext2D-%ver.so.%ver

%files -n libvtkViewsCore%ver
%_libdir/libvtkViewsCore-%ver.so.%soname
%_libdir/libvtkViewsCore-%ver.so.%ver

%files -n libvtkViewsInfovis%ver
%_libdir/libvtkViewsInfovis-%ver.so.%soname
%_libdir/libvtkViewsInfovis-%ver.so.%ver

%files -n libvtkWebCore%ver
%_libdir/libvtkWebCore-%ver.so.%soname
%_libdir/libvtkWebCore-%ver.so.%ver

%files -n libvtkWebGLExporter%ver
%_libdir/libvtkWebGLExporter-%ver.so.%soname
%_libdir/libvtkWebGLExporter-%ver.so.%ver

%files -n libvtkWrappingTools%ver
%_libdir/libvtkWrappingTools-%ver.so.%soname
%_libdir/libvtkWrappingTools-%ver.so.%ver

%files -n libvtkexodusII%ver
%_libdir/libvtkexodusII-%ver.so.%soname
%_libdir/libvtkexodusII-%ver.so.%ver

%files -n libvtkglad%ver
%_libdir/libvtkglad-%ver.so.%soname
%_libdir/libvtkglad-%ver.so.%ver

%files -n libvtkioss%ver
%_libdir/libvtkioss-%ver.so.%soname
%_libdir/libvtkioss-%ver.so.%ver

%files -n libvtkkissfft%ver
%_libdir/libvtkkissfft-%ver.so.%soname
%_libdir/libvtkkissfft-%ver.so.%ver

%files -n libvtkloguru%ver
%_libdir/libvtkloguru-%ver.so.%soname
%_libdir/libvtkloguru-%ver.so.%ver

%files -n libvtkmetaio%ver
%_libdir/libvtkmetaio-%ver.so.%soname
%_libdir/libvtkmetaio-%ver.so.%ver

%files -n libvtksys%ver
%_libdir/libvtksys-%ver.so.%soname
%_libdir/libvtksys-%ver.so.%ver

%files -n libvtktoken%ver
%_libdir/libvtktoken-%ver.so.%soname
%_libdir/libvtktoken-%ver.so.%ver

%files -n libvtkverdict%ver
%_libdir/libvtkverdict-%ver.so.%soname
%_libdir/libvtkverdict-%ver.so.%ver

%files -n libvtkfilters%ver
%_libdir/libvtkFilters*-%ver.so.%soname
%_libdir/libvtkFilters*-%ver.so.%ver
%exclude %_libdir/libvtkFiltersPython*-%ver.so.%soname
%exclude %_libdir/libvtkFiltersPython*-%ver.so.%ver

%files -n libvtkrendering%ver
%exclude %_libdir/libvtkRenderingQt-%ver.so.%soname
%exclude %_libdir/libvtkRenderingQt-%ver.so.%ver
%_libdir/libvtkRendering*-%ver.so.%soname
%_libdir/libvtkRendering*-%ver.so.%ver

%files -n libvtk-devel
%_libdir/*.so
%_includedir/vtk-%ver
%_libdir/cmake/vtk-%ver
%_libdir/vtk-%ver

%files examples
%doc Examples

%files python3
%_bindir/*python*
%_bindir/*Python*

%files -n libvtk%ver-python3
%_libdir/libvtk*Python*-%ver.so.%soname
%_libdir/libvtk*Python*-%ver.so.%ver

%files -n python3-module-vtk
%python3_sitelibdir/*
%exclude %python3_sitelibdir/__pycache__
%exclude %python3_sitelibdir/vtkmodules/test

%files -n python3-module-vtk-tests
%python3_sitelibdir/vtkmodules/test

%ifnarch %arm
%files qt5
%_libdir/libvtkGUISupportQtQuick-%ver.so.%soname
%_libdir/libvtkGUISupportQtQuick-%ver.so.%ver
%_libdir/libvtkGUISupportQtSQL-%ver.so.%soname
%_libdir/libvtkGUISupportQtSQL-%ver.so.%ver
%_libdir/libvtkGUISupportQt-%ver.so.%soname
%_libdir/libvtkGUISupportQt-%ver.so.%ver
%_libdir/libvtkRenderingQt-%ver.so.%soname
%_libdir/libvtkRenderingQt-%ver.so.%ver
%_libdir/libvtkViewsQt-%ver.so.%soname
%_libdir/libvtkViewsQt-%ver.so.%ver

%endif

%changelog
* Thu Jun 18 2026 Anton Farygin <rider@altlinux.org> 9.5.2-alt4
- fixed build with GDAL 3.13.1

* Fri May 08 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.5.2-alt3
- e2k build fix

* Sun Feb 02 2026 Anton Farygin <rider@altlinux.com> 9.5.2-alt2
- fixed vtkStreamTracer use-after-free in RequestData (InputData null guard)
- fixed numpy 2.x compatibility (numpy.in1d -> numpy.isin)
- disabled documentation build (removed doxygen, gnuplot, inkscape, texlive deps)
- removed docs subpackage
- added -fno-lto to fix build with LTO
- added CMAKE_SKIP_BUILD_RPATH and CMAKE_BUILD_RPATH_USE_ORIGIN flags
- fixed LD_LIBRARY_PATH in %%install for vtkWrapPythonInit to find libvtkWrappingTools

* Sun Jan 26 2026 Anton Farygin <rider@altlinux.com> 9.5.2-alt1
- 9.4.2 -> 9.5.2
- removed vtk-m submodule (no longer needed)
- removed patches merged upstream: fmt-11, findpoint, vtkparseproperties, netcdf
- removed QML plugin (no longer installed by upstream)
- added new subpackage libvtkIOLANLX3D

* Fri Sep 19 2025 Nazarov Denis <nenderus@altlinux.org> 9.4.2-alt1.1
- Fix build with fmt 12

* Sat Apr 05 2025 Anton Farygin <rider@altlinux.com> 9.4.2-alt1
- 9.4.1 -> 9.4.2

* Sat Mar 29 2025 Michael Shigorin <mike@altlinux.org> 9.4.1-alt3
- E2K: more workarounds to actually build slicer (ilyakurdyukov@).

* Fri Mar 07 2025 Constantin Sunzow <protvin@altlinux.org> 9.4.1-alt2
- Add macros subpackage.
- Update summaries.

* Wed Feb 19 2025 Constantin Sunzow <protvin@altlinux.org> 9.4.1-alt1
- Split libvtk to avoid debuginfo cpio size cap on e2k (thx cas@).
- Repackage Qt library files (ALT #52634).
- Remove unused BR (ALT #53114).
- E2K: spare memory used by ld.
- New version.

* Sun Oct 20 2024 Nazarov Denis <nenderus@altlinux.org> 9.3.0-alt1.2
- Fix build with fmt 11

* Mon Feb 26 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.3.0-alt1.1
- Fixed build for Elbrus.

* Wed Jan 24 2024 Anton Farygin <rider@altlinux.ru> 9.3.0-alt1
- 9.3.0

* Mon Sep 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 9.1.0-alt1.3
- NMU: fixed FTBFS on LoongArch

* Tue Jul  4 2023 Artyom Bystrov <arbars@altlinux.org> 9.1.0-alt1.2
- Fix build on GCC13

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 9.1.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jan 19 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 9.1.0-alt1
- Updated to upstream version 9.1.0.

* Thu Sep 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt6
- Renamed vtk-data package to vtk-data9.0.

* Thu Jun 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt5
- Fixed crash in uninitialized memory in OpenSlide wrapper (Closes: #40280, #40282).

* Wed Jun 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt4
- Updated build dependencies.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt3
- Added compatibility to p9.

* Thu May 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt2
- Built remote modules.
- Fixed 'duplicate target OpenSlide::OpenSlide' error using patch from upstream.
- Fixed build with new cmake macros.

* Tue May 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.1-alt1
- Updated to upstream version 9.0.1.

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt9
- Updated build dependencies.

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt8
- Fixed build with gcc-10 and new cmake.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 8.2.0-alt7
- NMU: fix build with freetype 2.10.3

* Fri Aug 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt6
- Fixed build with new qt version and architectures.

* Thu Mar 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt5
- fix packaging on armh arch

* Tue Feb 25 2020 Slava Aseev <ptrnine@altlinux.org> 8.2.0-alt4
- Fixed build with Python 3.8

* Mon Oct 07 2019 Vladislav Zavjalov <slazav@altlinux.org> 8.2.0-alt3
- Use internal libproj 4.4 instead of libproj 6.2.0

* Mon Jul 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.0-alt2
- Rebuilt with python-3.

* Wed May 15 2019 Slava Aseev <ptrnine@altlinux.org> 8.2.0-alt1
- Updated to upstream version 8.2.0.

* Thu Oct 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.1.1-alt3
- fixed build on armh

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt2
- Updated build dependencies.

* Mon Sep 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Wed Aug 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt4
- Rebuilt without openpdt.

* Sun Jun 24 2018 Anton Midyukov <antohami@altlinux.org> 6.2.0-alt3
- Rebuilt for aarch64
- Fix FTBFS

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2.qa1
- NMU: rebuilt against Tcl/Tk 8.6

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.2.0-alt2
- NMU: fixed build

* Fri Mar 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.2.0-alt1
- Version 6.2.0

* Tue May 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.0-alt1
- Version 6.1.0

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt2
- Fixed cmake files

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1
- Version 6.0.0

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt6
- Rebuilt with new python-module-sip

* Tue Jul 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt5
- Fixed build

* Thu Jun 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt4
- Rebuilt with new libhdf5

* Fri Apr 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt3
- Rebuilt without MPI

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt2
- Rebuilt with Boost 1.53.0

* Fri Feb 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.1-alt1
- Version 5.10.1

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt7
- Rebuilt with new qscintilla2

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt6
- Rebuilt with Boost 1.52.0

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt5
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt4
- Rebuilt with Boost 1.51.0 (thnx iv@)

* Wed Jun 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt3
- Rebuilt with OpenMPI 1.6

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt2
- Set soname version for libvtkQtPythonD.so

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10.0-alt1
- Version 5.10.0

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt12
- Fixed utils subpackage
- Set soname version for libvtkNetCDF_cxx.so
- Restored qt4-designer-plugin subpackage

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt11
- Fixed build with boost 1.49.0 (thnx iv@)

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt10
- Rebuilt with python-module-sip 4.13.2

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt9
- Built without OSMesa

* Mon Feb 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt8
- Fixed build with libav 0.8

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt7
- Rebuilt with python-module-sip 4.13.1

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt6
- Fixed file name: VTKTargets-reswithdebinfo.cmake ->
  VTKTargets-relwithdebinfo.cmake

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt5
- Fixed VTKTargets-reswithdebinfo.cmake (ALT #26650)

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt4
- Added necessary headers
- Fixed VTK_LIBRARY_DIRS (ALT #26650)

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt3
- Rebuilt with Boost 1.48.0

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt2
- Set directories of data files

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.8.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.8.0-alt1
- Version 5.8.0

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt2
- Rebuilt with libnetcdf7-mpi

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1
- Version 5.6.1

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt10
- Rebuilt with Boost 1.46.1

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt9
- Rebuilt with openmotif
- Added needed requirements

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt8
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt7
- Rebuilt with PostgreSQL 9.0

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt6
- Rebuilt for soname set-versions

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt5
- Fixed underlinking of libraries

* Wed Sep 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt4
- Do not use off screen calls (avoid segfault)

* Wed Sep 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt3
- Rebuilt with libmysqlclient.so.16

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt2
- Removed paths to buildroot

* Tue Jul 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.0-alt1
- Version 5.6.0

* Mon Mar 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt9
- Rebuilt with postgresql 8.4

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt8
- Changed requirement for python-module-%name: pygtkglext -> pygtkglext_git

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt7
- Rebuilt with new Boost (changed position of property_maps)
- Added some functionals (interfaces with addition packages)

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt6
- Rebuilt without python-module-Numeric

* Wed Jul 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt5
- Rebuild with python 2.6

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt4
- Enabled Python module

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt3
- Rebuild with changed libpng12

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt2
- Fixed directory layout for TCL wrappers

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.0-alt1
- Initial build for Sisyphus

