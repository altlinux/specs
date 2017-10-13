# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++ libGL-devel libGLU-devel swig unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name assimp
%define major   3
%define minor   3
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           assimp
Version:        3.3.1
Release:        alt1_2
Summary:        Library to import various 3D model formats into applications
Group:          Graphics
License:        BSD
URL:            http://www.assimp.org
Source0:        https://github.com/assimp/assimp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         assimp-3.3.1-mga-fdr-system-poly2tri-clipper.patch
Patch1:         assimp-3.3.1-mga-system-unzip.patch
# Fix library and include paths in assimp-config.cmake
# Fixes rhbz#1263698, not submitted upstream
# Rehashed to 3.3.1
Patch2:         0001-Assimp-cmake-provider-fix.patch
Patch10:        assimp-3.3.1-install-pkgconfig.patch
# Upstream backports:
# Collada morph animation
Patch100:       0001-Morph-animation-support-for-collada.patch
# Generate doc from CMakeFiles
Patch101:       0001-Enable-doxygen-been-properly-used-from-cmake-build-a.patch

BuildRequires:  boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  ccmake cmake ctest
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(poly2tri)
# assimp 3.1 seems not to build with the most recent version of polyclipping
#BuildRequires:  pkgconfig(polyclipping)
BuildRequires:  pkgconfig(zlib)
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
%doc doc/AssimpDoc_Html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}-%{major}.%{minor}
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%package        doc
Summary:        Assimp documentation
Group:          Documentation
BuildArch:      noarch

%description    doc
This package contains the Assimp documentation.

%files          doc
%{_docdir}/%{name}-%{version}/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch100 -p1
%patch101 -p1

# Get rid of bundled libs so we can't accidently build against them
#rm -rf contrib/clipper
rm -rf contrib/cppunit-1.12.1
rm -rf contrib/poly2tri
rm -rf contrib/unzip
rm -rf contrib/zlib

dos2unix CHANGES CREDITS LICENSE Readme.md

%build
%{mageia_cmake} -DASSIMP_BUILD_TESTS:BOOL=NO \
       -DASSIMP_LIB_INSTALL_DIR:PATH=%{_libdir} \
       -DASSIMP_BIN_INSTALL_DIR=%{_bindir} \
       -DASSIMP_INCLUDE_INSTALL_DIR=%{_includedir} \
       -DBUILD_DOCS=ON \
       -DHTML_OUTPUT=%{name}-%{version} \
       -DCMAKE_INSTALL_DOCDIR=%{_docdir} \
       -DPOLY2TRI_LIB_PATH:PATH=%{_libdir} \
       -DPOLY2TRI_INCLUDE_PATH:PATH=%{_includedir}/poly2tri
# To use system polyclipping if assimp ever becomes compatible:
#       -DCLIPPER_LIB_PATH:PATH=%%{_libdir} \
#       -DCLIPPER_INCLUDE_PATH:PATH=%%{_includedir}/polyclipping
%make_build

%install
%makeinstall_std -C build


%changelog
* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_2
- update by mgaimport

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_3
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_2
- converted for ALT Linux by srpmconvert tools

