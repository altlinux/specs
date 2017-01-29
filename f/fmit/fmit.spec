Name: fmit
Version: 1.1.11
Release: alt1

Summary: Free Music Instrument Tuner

License: GPL
Group: Sound
Url: http://gillesdegottex.github.io/fmit/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gillesdegottex/fmit/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: git-core i586-libxcb python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope  ruby ruby-stdlibs
# Automatically added by buildreq on Fri Jul 29 2016
# optimized out: gcc-c++ libGL-devel libgpg-error libjson-c libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-svg libqt5-widgets libstdc++-devel python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-xmlpatterns-devel
BuildRequires: libalsa-devel libfftw3-devel libportaudio2-devel qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel

BuildRequires: desktop-file-utils

%description
Free Music Instrument Tuner. Features:
Error history
Volume history
Wave shape
Harmonic ratios
Microtonal tuning (with Scala file support)
Discrete Fourier Transform view
JACK, OSS, ALSA, Portaudio support

%prep
%setup

%build
mkdir BUILD
cd BUILD
qmake-qt5 "CONFIG+=acs_qt acs_alsa acs_portaudio" "PREFIX=%prefix" ../fmit.pro

%make_build

%install
cd BUILD
%makeinstall_std INSTALL_ROOT=%buildroot
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	%buildroot%_desktopdir/fmit.desktop

%files
%doc README.txt
%_bindir/%name
%_datadir/%name/
# FIXME: add macro for appdata
%_datadir/appdata/fmit.appdata.xml
%_iconsdir/hicolor/*/apps/fmit.*
%_desktopdir/%name.desktop

%changelog
* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt1
- new version 1.1.11 (with rpmrb script)

* Fri Jul 29 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- new version 1.1.8 (with rpmrb script)

* Thu Mar 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt2
- fix packing

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1
- new version 1.0.12

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.99.5-alt1
- new version 0.99.5 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.99.2-alt1
- new version 0.99.2 (with rpmrb script)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.98.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for fmit
  * postclean-03-private-rpm-macros for the spec file

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.98.1-alt1
- new version (0.98.1) import in git
- build without OSS and Jack support (does not build with newest libjack)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.97.7-alt2
- update buildreq

* Sun May 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.97.7-alt1
- initial build for ALT Linux Sisyphus

* Wed May 23 2007 jeff <moe@blagblagblag.org> - 0.97.5-0blag.fc6
- BLAG'd
- Quick/dirty changes to spec just so i could start using the thing.

* Fri May 18 2007 Toni Graffy <toni@links2linux.de> - 0.97.5-0.pm.1
- update to 0.97.5
* Fri May 11 2007 Toni Graffy <toni@links2linux.de> - 0.97.4-0.pm.1
- update to 0.97.4
* Thu Apr 12 2007 Toni Graffy <toni@links2linux.de> - 0.97.0-0.pm.1
- update to 0.97.0
* Wed Dec 06 2006 Toni Graffy <toni@links2linux.de> - 0.96.7-0.pm.1
- update to 0.96.7
* Mon Sep 18 2006 Toni Graffy <toni@links2linux.de> - 0.96.5-0.pm.1
- build for packman
* Thu Feb 16 2006 - oc2pus@arcor.de 0.96.5-0.oc2pus.1
- update to 0.96.5
* Sat Jan 28 2006 - oc2pus@arcor.de 0.96.4-0.oc2pus.1
- update to 0.96.4
* Tue Dec 06 2005 - oc2pus@arcor.de 0.95.1-0.oc2pus.1
- update to 0.95.1
* Fri Nov 18 2005 - oc2pus@arcor.de 0.95.0-0.oc2pus.2
- update to 0.95.0
* Sun Nov 13 2005 - oc2pus@arcor.de 0.91.3-0.oc2pus.1
- update to 0.91.3
* Wed Jun 01 2005 - oc2pus@arcor.de 0.91.2-0.oc2pus.1
- update to 0.91.2
- changed group to Productivity/Multimedia/Sound/Utilities
* Sat Apr 02 2005 - oc2pus@arcor.de 0.9.9-0.oc2pus.1
- initial release of rpm
