%define _unpackaged_files_terminate_build 1

%define soname 2

Name: wildmidi
Version: 0.4.4
Release: alt1
Summary: WildMidi Open Source Midi Sequencer
Group: Sound

License: GPLv3+
Url: http://www.mindwerks.net/projects/wildmidi/
Source: %name-%version.tar

# Automatically added by buildreq on Tue May 20 2014 (-bi)
# optimized out: cmake-modules elfutils python-base
BuildRequires: cmake libalsa-devel libopenal-devel

Requires: timidity-instruments

%description
WildMidi is a software midi play which has a core softsynth library that can be use with other applications.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_man1dir/*
%_man5dir/*

%define libname lib%{name}%{soname}

%package -n %libname
Summary: Library for wildmidi
Group: System/Libraries
License: LGPLv3+
# Package qmmp-in-midi has broken requires for libwildmidi while actually this package is used.
# This provide is added in order to allow removing old library with CVE.
Provides: libwildmidi = %EVR

%description -n %libname
This package contains library files for wildmidi

%files -n %libname
%_libdir/*.so.%{soname}
%_libdir/*.so.%{soname}.*

%define develname lib%name-devel

%package -n %develname
Summary: Development files for wildmidi
Group: Development/Other
Requires: %libname = %EVR
Provides: %libname-devel = %EVR
License: LGPLv3+

%description -n %develname
This package contains development files for wildmidi

%files -n %develname
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*
%_libdir/cmake/WildMidi
%_man3dir/*.3*

%changelog
* Wed Aug 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.4-alt1
- Updated to upstream version 0.4.4.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 0.4.3-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Dec 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.3-alt1
- Updated to upstream version 0.4.3 (Fixes: CVE-2017-1000418).

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.3.8-alt1
- Autobuild version bump to 0.3.8

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Autobuild version bump to 0.3.7

* Tue May 20 2014 Fr. Br. George <george@altlinux.ru> 0.3.6-alt1
- Autobuild version bump to 0.3.6
- Build scheme and upstream hosting switch

* Fri Jan 20 2012 Fr. Br. George <george@altlinux.ru> 0.2.3.5-alt1
- Autobuild version bump to 0.2.3.5
- Fix build

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3.4-alt1.1
- Rebuilt for soname set-versions

* Sat Aug 07 2010 Motsyo Gennadi <drool@altlinux.ru> 0.2.3.4-alt1
- 0.2.3.4
- cleanup buildrequires
- remove MDV patch for timidity.conf (fix #23834)

* Wed Jul 14 2010 Fr. Br. George <george@altlinux.ru> 0.2.3.3-alt1
- Initial build from MDV
