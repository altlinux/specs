Name: wildmidi
Version: 0.2.3.5
Release: alt1
Summary: WildMidi Open Source Midi Sequencer
Group: Sound

License: GPLv3+
Url: http://wildmidi.sourceforge.net
Source: %name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sat Aug 07 2010 (-bi)
BuildRequires: libalsa-devel chrpath

Requires: timidity-instruments

%description
WildMidi is a software midi play which has a core softsynth library that can be use with other applications.

%prep
%setup -n %name-%version

%build
%configure --disable-static --without-arch --disable-werror
%make
chrpath -d src/.libs/libWildMidi.so
chrpath -d src/.libs/wildmidi

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/*
%_man5dir/*

%define libname lib%name

%package -n %libname
Summary: Library for wildmidi
Group: System/Libraries
License: LGPLv3+

%description -n %libname
This package contains library files for wildmidi

%files -n %libname
%_libdir/*.so.*

%define develname lib%name-devel

%package -n %develname
Summary: Development files for wildmidi
Group: Development/Other
Requires: %libname = %version
License: LGPLv3+

%description -n %develname
This package contains development files for wildmidi

%files -n %develname
%_libdir/*.so
%_includedir/*.h
%_man3dir/*.3*

%changelog
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
