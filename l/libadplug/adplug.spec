%define origname adplug
%define dbver 2006-07-07

Name: lib%origname
Version: 2.2.1
Release: alt2
Summary: AdLib sound player library
Url: http://adplug.sourceforge.net/
License: LGPL
Group: Sound
Source: http://sourceforge.net/projects/adplug/files/AdPlug%%20core%%20library/2.2.1/%origname-%version.tar
#.bz2
Source1: http://sourceforge.net/projects/adplug/files/Database/2006-07-06/adplugdb-%dbver.tar
#.gz

# Automatically added by buildreq on Sun Sep 09 2012 (-bi)
# optimized out: elfutils gnu-config libstdc++-devel pkg-config python-base
BuildRequires: chrpath gcc-c++ libbinio-devel

%if_enabled static
BuildPreReq: glibc-devel-static
%endif
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

%package devel
Group: Development/C++
Summary: Development files of AdPlug
Requires: %name = %version-%release

%description devel
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the C++ headers and documentation required for
building programs based on AdPlug.

%if_enabled static
%package devel-static
Group: Development/C++
Summary: Static library of AdPlug
Requires: %name-devel = %version-%release

%description devel-static
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the static library required for statically
linking applications based on AdPlug.

%endif #enabled static

%prep
%setup -n %origname-%version

%build
%add_optflags -fsigned-char
%configure --sharedstatedir=%_datadir
%make_build

%install
%makeinstall
chrpath -d %buildroot%_bindir/adplugdb

tar xf %SOURCE1
mkdir -p %buildroot%_datadir
cp -a %dbver %buildroot%_datadir/%origname

%files
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%_bindir/adplugdb
%_man1dir/adplugdb.1*
%_libdir/*.so.*
%_datadir/%origname

%files devel
%_includedir/%origname
%_libdir/*.so
%_pkgconfigdir/%origname.pc
%_infodir/%name.*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt2
- fixed build on arm arches

* Sat Dec 05 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1.1.1
- NMU: added BR: texinfo

* Fri Dec 04 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1.1
- rebuild with libbinio

* Sun Sep 09 2012 Ildar Mulyukov <ildar@altlinux.ru> 2.2.1-alt1
- new version
- spec cleanups

* Sat Jan 05 2008 Ildar Mulyukov <ildar@altlinux.ru> 2.1-alt1
- 1st version for Sisyphus
- build static libs if only --enabled static
- added adplugdb database version %dbver to %_datadir/%origname

* Tue Mar  4 2003 Götz Waschk <waschk@linux-mandrake.com> 1.4-1
- requires binio library
- fix groups for RH standard
- remove patches
- add adplugdb
- new version

* Tue Nov 26 2002 Götz Waschk <waschk@linux-mandrake.com> 1.3-1
- initial package
