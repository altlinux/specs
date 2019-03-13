%define _unpackaged_files_terminate_build 1 
%define sover 2
%define libvxl libvxl%sover

Name: libvxl
Version: 2.0.2
Release: alt1

Group: System/Libraries
Summary: C++ Libraries for Computer Vision Research and Implementation
License: BSD
Url: https://vxl.github.io/

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake libdcmtk-devel dcmtk libtiff-devel libjpeg-devel libssl-devel
BuildRequires: libpng-devel libxml2-devel libgeotiff-devel doxygen /usr/bin/dot texi2html

%define _description \
VXL (the Vision-something-Libraries) is a collection of C++ libraries designed \
for computer vision research and implementation. It was created from TargetJr \
and the IUE with the aim of making a light, fast and consistent system. VXL is \
written in ANSI/ISO C++ and is designed to be portable over many platforms.

%description 
%_description

# dcmtk required, because its contains DICOM tags list
%package -n %libvxl
Summary: Shared libraries for VXL
Requires: dcmtk
Group: System/Libraries
%description -n %libvxl 
This package contains shared libraries for VXL.
%_description

%package devel
Summary: Headers for VXL
Group: Development/C++
%description devel 
This package contains development files for VXL.
%_description

%package doc
Summary: Documentation for VXL
Group: Documentation
BuildArch: noarch
%description doc 
This package contains documentation for VXL.
%_description

%prep
%setup
%patch1 -p1
rm -rf v3p/{bzlib,dcmtk,geotiff,j2k,png,rply,tiff,zlib,jpeg}

%build
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DVXL_INSTALL_LIBRARY_DIR=%_libdir \
    -DVXL_INSTALL_ARCHIVE_DIR=%_libdir \
    -DVXL_FORCE_B3P_EXPAT:BOOL=OFF \
    -DVXL_FORCE_V3P_DCMTK:BOOL=OFF \
    -DVXL_FORCE_V3P_GEOTIFF:BOOL=OFF \
    -DVXL_FORCE_V3P_JPEG:BOOL=OFF \
    -DVXL_FORCE_V3P_PNG:BOOL=OFF \
    -DVXL_FORCE_V3P_TIFF:BOOL=OFF \
    -DVXL_FORCE_V3P_ZLIB:BOOL=OFF \
    -DVXL_USING_NATIVE_ZLIB=ON \
    -DVXL_USING_NATIVE_JPEG=ON \
    -DVXL_USING_NATIVE_PNG=ON \
    -DVXL_USING_NATIVE_TIFF=ON \
    -DVXL_USING_NATIVE_GEOTIFF=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DVNL_CONFIG_LEGACY_METHODS=ON \
    -DVXL_BUILD_DOCUMENTATION=ON \
    %nil
%cmake_build VERBOSE=1
%cmake_build build_doxygen_doc 

%install
%cmakeinstall_std

%files -n %libvxl
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%sover.*
%dir %_datadir/vxl/

%files devel
%_libdir/lib*.so
%_includedir/vxl/
%_datadir/vxl/cmake/

%files doc
%doc BUILD/doxy/html

%changelog
* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 2.0.2-alt1
- Initial build for ALT
