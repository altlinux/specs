%define _unpackaged_files_terminate_build 1
%define soname 1

Name: itk
Version: 5.0
Release: alt2.rc1

Group: System/Libraries
Summary: Toolkit for N-dimensional scientific image processing, segmentation, and registration.
License: ASL 2.0
Url: http://www.itk.org/

# https://github.com/InsightSoftwareConsortium/ITK
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake
BuildRequires: gdcm-devel castxml graphviz libhdf5-devel 
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libxml2-devel
BuildRequires: python-devel
BuildRequires: libvxl-devel libvtk8.1-devel qt5-webkit-devel zlib-devel
BuildRequires: libblas-devel liblapack-devel libnetcdf-devel jsoncpp-devel
BuildRequires: libexpat-devel dcmtk 

BuildRequires: vtk8.1-python libfftw3-devel libgtest-devel eigen3
BuildRequires: libminc-devel
BuildRequires: libniftilib-devel

%define _description \
The Insight Toolkit (ITK) is an open-source, cross-platform toolkit for \
N-dimensional scientific image processing, segmentation, and registration. \
Segmentation is the process of identifying and classifying data found in a  \
digitally sampled representation. Typically the sampled representation is an  \
image acquired from such medical instrumentation as CT or MRI scanners. \
Registration is the task of aligning or developing correspondences between \
data. For example, in the medical environment, a CT scan may be aligned with  \
a MRI scan in order to combine the information contained in both.

%description %_description

%package -n lib%name%soname
Summary: Shared libraries files for ITK
Group: System/Libraries
%description -n lib%name%soname
This package contains ITK shared libraries.
%_description

%package -n lib%name-devel
Summary: Development files for ITK
Group: Development/C++
Requires: lib%name%soname = %EVR
%description -n lib%name-devel
This package contains development files for ITK.
%_description

%package examples
Summary: Examples for ITK
Group: Development/Tools
Requires: lib%name%soname = %EVR
%description examples
This package contains source code of ITK examples.
%_description

%package doc
Summary: Documentation for ITK
Group: Documentation
BuildArch: noarch
%description doc 
This package contains documentation for ITK.
%_description

%prep
%setup
%patch -p1

# Save an unbuilt copy of the Example's sources for %%doc
mkdir itk-examples
cp -a Examples itk-examples

# Delete unused third party sources
rm -rf Modules/ThirdParty/Expat/src/
rm -rf Modules/ThirdParty/GDCM/src/
rm -rf Modules/ThirdParty/MINC/src/libminc/
rm -rf Modules/ThirdParty/MINC/src/CMakeLists.txt
rm -rf Modules/ThirdParty/HDF5/src/itkhdf5/
rm -rf Modules/ThirdParty/HDF5/src/CMakeLists.txt
rm -rf Modules/ThirdParty/HDF5/src/README.md
rm -rf Modules/ThirdParty/JPEG/src/itkjpeg/
rm -rf Modules/ThirdParty/JPEG/src/CMakeLists.txt
rm -rf Modules/ThirdParty/PNG/src/itkpng/
rm -rf Modules/ThirdParty/PNG/src/CMakeLists.txt
rm -rf Modules/ThirdParty/TIFF/src/itktiff/
rm -rf Modules/ThirdParty/TIFF/src/CMakeLists.txt
rm -rf Modules/ThirdParty/ZLIB/src/itkzlib/
rm -rf Modules/ThirdParty/ZLIB/src/CMakeLists.txt
rm -rf Modules/ThirdParty/VNL/src/

%build
%cmake \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DCMAKE_CXX_FLAGS:STRING="-std=gnu++11 %{optflags}" \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DBUILD_TESTING=OFF \
       -DBUILD_EXAMPLES:BOOL=ON \
       -DBUILD_DOCUMENTATION:BOOL=OFF \
       -DITK_BUILD_DEFAULT_MODULES:BOOL=ON \
       -DITK_WRAP_PYTHON:BOOL=OFF \
       -DITK_WRAP_JAVA:BOOL=OFF \
       -DITK_INSTALL_LIBRARY_DIR=%_lib/ \
       -DITK_INSTALL_INCLUDE_DIR=include/%name \
       -DITK_INSTALL_PACKAGE_DIR=%_lib/cmake/%name/ \
       -DITK_INSTALL_RUNTIME_DIR:PATH=%_bindir \
       -DITK_INSTALL_DOC_DIR=share/doc/%name/ \
       -DITK_USE_KWSTYLE:BOOL=OFF \
       -DITK_FORBID_DOWNLOADS=ON \
       -DModule_ITKReview:BOOL=ON \
       -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
       -DITK_USE_FFTWD=ON \
       -DITK_USE_FFTWF=ON \
       -DITK_USE_SYSTEM_DCMTK=ON \
       -DITK_USE_SYSTEM_EXPAT=ON \
       -DITK_USE_SYSTEM_FFTW=ON \
       -DITK_USE_SYSTEM_GDCM=ON \
       -DITK_USE_SYSTEM_MINC=ON \
       -DITK_USE_SYSTEM_HDF5=ON \
       -DITK_USE_SYSTEM_JPEG=ON \
       -DITK_USE_SYSTEM_PNG=ON \
       -DITK_USE_SYSTEM_TIFF=ON \
       -DITK_USE_SYSTEM_ZLIB=ON \
       -DITK_USE_SYSTEM_VXL=ON \
       -DDO_NOT_INSTALL_ITK_TEST_DRIVER=ON \
    %nil
%cmake_build

%install
%cmakeinstall_std
# Delete unused test driver
rm -f BUILD/bin/itkTestDriver

install -D -m755 -t %buildroot%_libdir/%name-examples/ BUILD/bin/*

%files -n lib%name%soname
%_libdir/lib*.so.%soname

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/%name/
%_libdir/cmake/

%files examples
%doc itk-examples/Examples/
%_libdir/%name-examples/

%files doc
%doc %_docdir/%name/

%changelog
* Wed Mar 27 2019 Slava Aseev <ptrnine@altlinux.org> 5.0-alt2.rc1
- Switch on build examples

* Thu Feb 14 2019 Slava Aseev <ptrnine@altlinux.org> 5.0-alt1.rc1
- Initial build for ALT

