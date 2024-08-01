%define _unpackaged_files_terminate_build 1

# documentation build sometimes generates non-identical files
%def_without docs

# TODO: remove later this fix for documentation
#%%define _cmake__builddir BUILD

%define openjpeg2_sover 2
%define ver_maj 3
%define sover 3.5
%define libvxl libvxl%ver_maj

Name: libvxl
Version: 3.5.0
Release: alt2

Group: System/Libraries
Summary: C++ Libraries for Computer Vision Research and Implementation
License: BSD
Url: https://vxl.github.io/

VCS: https://github.com/vxl/vxl.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: gcc-c++ cmake libdcmtk-devel dcmtk libtiff-devel libjpeg-devel libssl-devel rpm-build-ninja
BuildRequires: libpng-devel libxml2-devel libgeotiff-devel
%if_with docs
BuildRequires: doxygen /usr/bin/dot texi2html
%endif

%define _description \
VXL (the Vision-something-Libraries) is a collection of C++ libraries designed \
for computer vision research and implementation. It was created from TargetJr \
and the IUE with the aim of making a light, fast and consistent system. VXL is \
written in ANSI/ISO C++ and is designed to be portable over many platforms.

%description 
%_description

%package -n %libvxl
Summary: Shared libraries for VXL
Group: System/Libraries
# dcmtk required, because its contains DICOM tags list
Requires: dcmtk

%description -n %libvxl 
This package contains shared libraries for VXL.
%_description

%package devel
Summary: Headers for VXL
Group: Development/C++
Conflicts: libvpl-devel

%description devel 
This package contains development files for VXL.
%_description

%if_with docs
%package doc
Summary: Documentation for VXL
Group: Documentation
BuildArch: noarch

%description doc 
This package contains documentation for VXL.
%_description
%endif

%prep
%setup
%patch1 -p1
%ifarch %e2k
sed -i 's/-fno-gcse/-Wall/' v3p/netlib/CMakeLists.txt
%endif

%build
%cmake -GNinja \
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
%if_with docs
    -DVXL_BUILD_DOCUMENTATION=ON \
%endif
    -DVXL_LEGACY_FUTURE_REMOVE:BOOL=OFF \
    %nil

%ninja_build -C "%_cmake__builddir"

%if_with docs
%ninja_build -C "%_cmake__builddir" build_doxygen_doc
%endif

%install
%ninja_install -C "%_cmake__builddir"

%files -n %libvxl
%_libdir/lib*.so.%sover
%_libdir/lib*.so.%sover.*
%_libdir/libopenjpeg2.so.%openjpeg2_sover.*
%dir %_datadir/vxl/

%files devel
%_libdir/lib*.so
%_includedir/vxl/
%_datadir/vxl/cmake/

%if_with docs
%files doc
%doc %_cmake__builddir/doxy/html
%endif

%changelog
* Thu Aug 01 2024 Anton Farygin <rider@altlinux.ru> 3.5.0-alt2
- libvxl-devel: Added conflicts with libvpl-devel (Closes: #50978)

* Tue Feb 27 2024 Michael Shigorin <mike@altlinux.org> 3.5.0-alt1.1
- E2K: avoid lcc-unsupported option (ilyakurdyukov@)

* Mon Apr 17 2023 Elizaveta Morozova <morozovaes@altlinux.org> 3.5.0-alt1
- New version
- Build using ninja-build
- Include DCMTK-3.6.4 API update

* Wed Sep 22 2021 Slava Aseev <ptrnine@altlinux.org> 2.0.2-alt4
- Include missing "limits" std header

* Fri May 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt3
- Backported from upstream changes required by new ITK.
- Fixed build with new cmake macros.
- Disabled building documentation.

* Tue Jul 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt2
- Fixed generated header installation.
- Enabled deprecated functions.

* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 2.0.2-alt1
- Initial build for ALT
