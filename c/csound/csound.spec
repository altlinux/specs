%define _unpackaged_files_terminate_build 1
%define jsover 1
%define sover 6
%define _pluginsdir %_libdir/%name/plugins64-%sover.0

Name: csound
Version: 6.18.1
Release: alt5

Summary: A sound synthesis language and library
License: LGPL-2.1
Group: Sound
URL: https://csound.github.io/
VCS: https://github.com/csound/csound

Conflicts: extract
Conflicts: clearsilver

Source: %name-%version.tar
Patch0: cmakedir.patch

BuildRequires(pre): rpm-macros-java rpm-macros-cmake rpm-macros-python3
BuildRequires: rpm-build-java rpm-build-cmake rpm-build-python3
BuildRequires: CUnit-devel
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: java-devel
BuildRequires: ladspa_sdk
BuildRequires: liblo-devel
BuildRequires: libportaudio2-devel
BuildRequires: libportmidi-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: swig

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...

%package -n lib%name%sover
Group: System/Libraries
Summary: Lib files for %name

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Csound development files and libraries
Group: Development/C++
Provides: %name-devel = %EVR
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
Contains headers and libraries for developing applications that use Csound.

%package -n python3-module-%name
Summary: Python Csound development files and libraries
Group: Development/Python3
Requires: lib%name%sover = %EVR

%description -n python3-module-%name
Contains Python language bindings for developing Python applications that
use Csound.

%package java
Summary: Java Csound support
Group: System/Libraries
Requires: lib%name%sover = %EVR

%description java
Contains Java language bindings for developing and running Java
applications that use Csound.

%prep
%setup
%patch0 -p1

%build
%add_optflags -Wno-error=incompatible-pointer-types
%add_optflags -Wno-error=template-body

%cmake \
%if "%_lib" == "lib64"
    -DUSE_LIB64=ON \
%endif
    -DCMAKE_DIR=%_cmakedir
%cmake_build

%install
%cmakeinstall_std

mkdir -pv %buildroot%_javadir
mv -v %buildroot%_libdir/*.jar %buildroot%_javadir/

%find_lang %name%sover

%files -f %name%sover.lang
%doc COPYING
%_bindir/*
%_datadir/samples/*

%files -n lib%name%sover
%_libdir/libcsnd%sover.so.%sover.*
%_libdir/lib%{name}64.so.%sover.*
%dir %_pluginsdir
%_pluginsdir/lib*.so

%files -n lib%name-devel
%_includedir/%name/
%_libdir/libcsnd%sover.so
%_libdir/lib%{name}64.so
%_cmakedir/Csound/FindCsound.cmake

%files -n python3-module-%name
%python3_sitelibdir/ctcsound.py
%python3_sitelibdir/__pycache__/*.pyc

%files java
%_libdir/lib_jcsound.so.%jsover
%_libdir/lib_jcsound%sover.so
%_javadir/csnd6.jar

%changelog
* Thu Apr 23 2026 Artem Semenov <savoptik@altlinux.org> 6.18.1-alt5
- Dropped redundant workaround from the latest change. (thx Gleb Fotengauer-Malinovskiy)

* Wed Apr 22 2026 Artem Semenov <savoptik@altlinux.org> 6.18.1-alt4
- Fixed FTBFS after GCC 15

* Tue Jan 27 2026 Artem Semenov <savoptik@altlinux.org> 6.18.1-alt3
- Optemised build requires
- Packaged locales
- Added conflicts to extract clearsilver (Closes: 57669)

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 6.18.1-alt2
- Cleaned-up the spec

* Wed Dec 04 2024 Artem Semenov <savoptik@altlinux.org> 6.18.1-alt1
- Initial build for Sisyphus (thx Paul Wolneykien)
