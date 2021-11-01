Name: adplay
Version: 1.8.1
Release: alt1
License: GPL
Group: Sound
Url: https://adplug.github.io/
Summary: AdLib music player for the command line
# https://github.com/adplug/adplay-unix
Source: %name-%version.tar
Source44: %name.watch

# Automatically added by buildreq on Sat Jan 05 2008
BuildRequires: gcc-c++ libadplug-devel libalsa-devel libao-devel

%description
AdPlay/UNIX is AdPlug's UNIX console-based frontend. AdPlug is a free,
universal OPL2 audio playback library. AdPlay/UNIX supports the full range
of AdPlug's file format playback features. Despite this, at the moment, only
emulated OPL2 output is supported by AdPlay/UNIX, but this on a wide range
of output devices.

%prep
%setup

%build
%autoreconf
%configure --sharedstatedir=%_datadir \
	--disable-output-oss \

%make_build

%install
%makeinstall

%files
%doc README NEWS TODO AUTHORS ChangeLog
%_bindir/adplay
%_man1dir/adplay.1*

%changelog
* Mon Oct 18 2021 Ildar Mulyukov <ildar@altlinux.ru> 1.8.1-alt1
- new upstream URL
- add `loop` option PR

* Fri Dec 04 2015 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1
- rebuild with libbinio

* Sun Sep 09 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.7-alt1
- new version

* Sat Jan 05 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.6-alt1
- 1st version for Sisyphus

* Tue Mar  4 2003 Götz Waschk <waschk@linux-mandrake.com> 1.3-1
- requires new adplug libraries
- fix group for RH standard
- new version

* Tue Nov 26 2002 Götz Waschk <waschk@linux-mandrake.com> 1.2-1
- initial package
