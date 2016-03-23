Name: fmit
Version: 1.0.12
Release: alt2

Summary: Free Music Instrument Tuner

License: GPL
Group: Sound
Url: http://gillesdegottex.github.io/fmit/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gillesdegottex/fmit/archive/v1.0.12.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sat Aug 03 2013
# optimized out: cmake cmake-modules fontconfig libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXcursor-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libstdc++-devel xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
BuildRequires: ccmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXres-devel libXxf86misc-devel libXxf86vm-devel libalsa-devel libfftw3-devel libfreeglut-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libxkbfile-devel phonon-devel qt4-designer

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
sed -i "s|share/mimelnk/application/|share/applications/|g" CMakeLists.txt
%cmake -DSOUNDSYSTEM_USE_JACK=OFF -DSOUNDSYSTEM_USE_OSS=OFF

cd BUILD
%make_build

%install
cd BUILD
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	%buildroot%_desktopdir/fmit.desktop

%files
%doc ChangeLog TODO
%_bindir/%name
%_datadir/%name/
# FIXME: add macro for appdata
%_datadir/appdata/fmit.appdata.xml
%_iconsdir/hicolor/*/apps/fmit.*
%_desktopdir/%name.desktop

%changelog
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
