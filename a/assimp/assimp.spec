%define major   5
%define minor   4

%def_without docs
%def_without examples

Name: assimp
Version: 5.4.1
Release: alt1
Summary: Library to import various 3D model formats into applications
Group: Graphics
# Assimp is BSD
# Bundled contrib/clipper is Boost
# Bundled contrib/Open3DGC is MIT
# Bundled contrib/openddlparser is MIT
# Bundled contrib/stb_image is MIT
# Bundled contrib/unzip is zlib
# Bundled contrib/zip is unlicense
# Bundled contrib/zlib is zlib
License: BSD and MIT and Boost and unlicense and zlib
Url: https://github.com/assimp/assimp

# Github releases include nonfree models, source tarball must be re-generated
# using assimp_generate_tarball.sh
Source0: %name-%version-free.tar
Source1: assimp_generate_tarball.sh

# Un-bundle libraries that are provided by the distribution.
# Also fixes FTBFS: https://github.com/assimp/assimp/issues/4334
Patch0: assimp-5.4.0-alt-unbundle.patch

BuildRequires: boost-complete
BuildRequires: cmake
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(minizip)
BuildRequires: pkgconfig(poly2tri)
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(stb)
BuildRequires: libutf8cpp-devel
%if_with docs
BuildRequires: /usr/bin/doxygen swig
%endif
%if_with examples
BuildRequires: libGLU-devel libGLUT-devel libglvnd-devel
%endif
BuildRequires: gcc-c++ python3-devel rpm-build-python3 unzip zip

BuildRequires:  pkgconfig(polyclipping)
BuildRequires:  rapidjson-devel

%description
Assimp, the Open Asset Import Library, is a free library to import various
well-known 3D model formats into applications. Assimp aims to provide a full
asset conversion pipeline for use in game engines and real-time rendering
systems, but is not limited to these applications.

This package contains the assimp binary, a tool to work with various formats.

%package -n lib%name%major
Summary: Library to import various 3D model formats into applications
Group: System/Libraries
Provides: lib%name = %EVR

%description -n lib%name%major
Assimp, the Open Asset Import Library, is a free library to import various
well-known 3D model formats into applications. Assimp aims to provide a full
asset conversion pipeline for use in game engines and real-time rendering
systems, but is not limited to these applications.

%package -n lib%name-devel
Summary: Header files and development libraries for assimp
Group: Development/C++
Provides: %name-devel = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains the header files and development libraries for assimp.
You need to install it if you want to develop programs using assimp.

%prep
%setup
%patch0 -p2

# Get rid of bundled libs so we can't accidentally build against them
rm -rf contrib/android-cmake
#rm -rf contrib/clipper
rm -rf contrib/draco
rm -rf contrib/gtest
rm -rf contrib/poly2tri
rm -rf contrib/pugixml
rm -rf contrib/rapidjson
rm -rf contrib/stb
rm -rf contrib/unzip
rm -rf contrib/utf8cpp
#rm -rf contrib/zip
rm -rf contrib/zlib

%build
# mike@
%ifarch %e2k
# as of lcc 1.25.20
%add_optflags -Wno-error=maybe-uninitialized
%endif
%cmake \
%if_with docs
  -DASSIMP_BUILD_DOCS:BOOL=ON \
%else
  -DASSIMP_BUILD_DOCS:BOOL=OFF \
%endif
%if_with examples
  -DASSIMP_BUILD_SAMPLES:BOOL=ON \
%else
  -DASSIMP_BUILD_SAMPLES:BOOL=OFF \
%endif
  -DASSIMP_BUILD_ZLIB:BOOL=OFF \
  -DASSIMP_BUILD_ASSIMP_TOOLS:BOOL=ON \
  -DASSIMP_BUILD_TESTS:BOOL=OFF

%cmake_build

%install
%cmake_install

%files
%_bindir/%name

%files -n lib%name%major
%doc Readme.md LICENSE CREDITS CHANGES
%_libdir/lib%name.so.%major
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_libdir/cmake/%name-%major.%minor
%_pkgconfigdir/%name.pc

%changelog
* Fri May 24 2024 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt1
- 5.4.1.

* Mon Apr 08 2024 L.A. Kostis <lakostis@altlinux.ru> 5.4.0-alt1
- 5.4.0.
- cleanup .spec and patches.

* Mon Dec 18 2023 L.A. Kostis <lakostis@altlinux.ru> 5.3.1-alt1
- 5.3.1.
- Rebase/cleanup all patches.
- BR: cleanup
- BR: enable system rapidjson and polyclipping
- Remove mga cruft.

* Wed Nov 22 2023 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt2
- use stb instead of stbi (which is unmaintained and has security bugs).
- update BR.

* Thu Apr 14 2022 Igor Vlasenko <viy@altlinux.org> 5.2.2-alt1_3
- update by mgaimport

* Fri Jan 14 2022 Igor Vlasenko <viy@altlinux.org> 5.1.5-alt1_1
- new version + e2k support

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_5
- fixed build

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_4
- update by mgaimport

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_2
- update by mgaimport

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_3
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_2
- converted for ALT Linux by srpmconvert tools
