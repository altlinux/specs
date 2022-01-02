# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/doxygen gcc-c++ libGLU-devel libglvnd-devel python3-devel rpm-build-python3 swig unzip zip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name assimp
%define major   5
%define minor   1
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           assimp
Version:        5.1.0
Release:        alt1_1
Summary:        Library to import various 3D model formats into applications
Group:          Graphics
# Assimp is BSD
# Bundled contrib/clipper is Boost
# Bundled contrib/Open3DGC is MIT
# Bundled contrib/openddlparser is MIT
# Bundled contrib/stb_image is MIT
# Bundled contrib/unzip is zlib
# Bundled contrib/zip is unlicense
# Bundled contrib/zlib is zlib
License:        BSD and MIT and Boost and unlicense and zlib
URL:            https://github.com/assimp/assimp

# Github releases include nonfree models, source tarball must be re-generated
# using assimp_generate_tarball.sh
Source0:        %{name}-%{version}-free.tar.xz
Source1:        assimp_generate_tarball.sh

# Un-bundle libraries that are provided by the distribution.
Patch0:         assimp-5.1.0-mga-unbundle.patch

BuildRequires:  boost-complete
BuildRequires:  cmake
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(poly2tri)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  stbi-devel
BuildRequires:  libutfcpp-devel

# Incompatible - https://github.com/assimp/assimp/issues/788
#BuildRequires:  pkgconfig(polyclipping)
# Needs unstable git version we don't package yet
#BuildRequires:  rapidjson

Provides: bundled(polyclipping) = 4.8.8
Provides: bundled(open3dgc)
Provides: bundled(openddl-parser)
Provides: bundled(rapidjson)
# https://github.com/kuba--/zip
Provides: bundled(zip)
Source44: import.info

%description
Assimp, the Open Asset Import Library, is a free library to import various
well-known 3D model formats into applications. Assimp aims to provide a full
asset conversion pipeline for use in game engines and real-time rendering
systems, but is not limited to these applications.

This package contains the assimp binary, a tool to work with various formats.

%files
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%package -n     %{libname}
Summary:        Library to import various 3D model formats into applications
Group:          System/Libraries

%description -n %{libname}
Assimp, the Open Asset Import Library, is a free library to import various
well-known 3D model formats into applications. Assimp aims to provide a full
asset conversion pipeline for use in game engines and real-time rendering
systems, but is not limited to these applications.

%files -n       %{libname}
%doc Readme.md LICENSE CREDITS CHANGES
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n     %{devname}
Summary:        Header files and development libraries for assimp
Group:          Development/C++
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the header files and development libraries for assimp.
You need to install it if you want to develop programs using assimp.

%files -n       %{devname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}-%{major}.%{minor}
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1


# Get rid of bundled libs so we can't accidentally build against them
rm -rf contrib/android-cmake
#rm -rf contrib/clipper
rm -rf contrib/draco
rm -rf contrib/gtest
rm -rf contrib/poly2tri
rm -rf contrib/pugixml
#rm -rf contrib/rapidjson
rm -rf contrib/stb
rm -rf contrib/unzip
rm -rf contrib/utf8cpp
#rm -rf contrib/zip
rm -rf contrib/zlib

%build
%{mageia_cmake} \
  -DASSIMP_BUILD_TESTS=OFF

%mageia_cmake_build

%install
%mageia_cmake_install


%changelog
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

