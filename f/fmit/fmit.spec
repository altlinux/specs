Name: fmit
Version: 0.98.1
Release: alt1.qa1

Summary: Free Music Instrument Tuner

License: GPL
Group: Sound
Url: http://home.gna.org/fmit/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.gna.org/fmit/%name-%version-Source.tar

# Automatically added by buildreq on Sun Jan 02 2011
BuildRequires: ccmake gcc-c++ libXScrnSaver-devel libXau-devel libXcomposite-devel libXdmcp-devel libXmu-devel libXpm-devel libXtst-devel libXv-devel libXxf86misc-devel libalsa-devel libfftw3-devel libfreeglut-devel libxkbfile-devel qt3-designer
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
%setup -n %name-%version-Source

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
%_desktopdir/%name.desktop

%changelog
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
