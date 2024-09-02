Name: tuxguitar
Version: 1.6.4
Release: alt2

Summary: A multitrack guitar tablature editor and player
License: LGPL-2.0+
Group: Sound

Url: https://www.tuxguitar.app/
VCS: https://github.com/helge17/tuxguitar

Source0: %name-%version.tar
Source1: vendors-%version.tar
Source2: tuxguitar.sh

Requires: java-17-openjdk
Requires: javapackages-filesystem
BuildRequires: java-17-openjdk-devel java-headless
BuildRequires: javapackages-filesystem maven glibc libfluidsynth-devel
BuildRequires: libjack-devel libalsa-devel soundfont2-default gcc-c++
BuildRequires: lilv-devel musl-devel libconfig-devel libsuil-devel
BuildRequires: qt5-base-devel libfreetype-devel
BuildRequires: libxcbutil-devel libXdmcp-devel libxcbutil-cursor-devel
BuildRequires: libxcbutil-keysyms-devel libxkbcommon-x11-devel libpango-devel
BuildRequires: libgtkmm2-devel libgtkmm3-devel libstdc++-devel

ExclusiveArch: x86_64

%description
TuxGuitar is a guitar tablature editor with player support through midi.
It can display scores and multitrack tabs. It can open GP3, GP3 and GP5
files.

With TuxGuitar, you will be able to compose music using the following features:
* Tablature editor
* Score Viewer
* Multitrack display
* Autoscroll while playing
* Note duration management
* Various effects (bend, slide, vibrato, hammer-on/pull-off)
* Support for triplets (5,6,7,9,10,11,12)
* Repeat open and close
* Time signature management
* Tempo management
* Imports and exports gp3,gp4 and gp5 files

%prep
%setup -n vendors-%version -b 1
%setup -n %name-%version

%build
pushd desktop/build-scripts/tuxguitar-linux-swt
mvn -P native-modules package -Dmaven.repo.local=../../../vendors/m2-repository
popd

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%name-%version/
mkdir -p %buildroot/%_libdir/%name-%version/

install -pm 755 %SOURCE2 %buildroot/%_bindir/tuxguitar

cp -r desktop/build-scripts/tuxguitar-linux-swt/target/tuxguitar-9.99-SNAPSHOT-linux-swt/dist/ %buildroot/%_datadir/%name-%version/
cp -r desktop/build-scripts/tuxguitar-linux-swt/target/tuxguitar-9.99-SNAPSHOT-linux-swt/share/ %buildroot/%_datadir/%name-%version/
cp -r desktop/build-scripts/tuxguitar-linux-swt/target/tuxguitar-9.99-SNAPSHOT-linux-swt/lib/ %buildroot/%_libdir/%name-%version/

# desktop files
install -dm 755 %buildroot/%_datadir/applications
sed 's/Icon=tuxguitar/Icon=\/usr\/share\/icons\/hicolor\/96x96\/apps\/tuxguitar.png/g' %buildroot/%_datadir/%name-%version/share/applications/tuxguitar.desktop > %buildroot/%_datadir/applications/tuxguitar.desktop

# icon
install -dm 755 %buildroot/%_iconsdir/hicolor/96x96/apps/
install -pm 644 desktop/TuxGuitar/share/skins/Lavender/icon.png %buildroot/%_iconsdir/hicolor/96x96/apps/tuxguitar.png

# mime-type icons
install -dm 755 %buildroot/%_iconsdir/hicolor/96x96/mimetypes
install -pm 644 desktop/TuxGuitar/share/skins/Lavender/icon.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-tuxguitar.png
install -pm 644 desktop/TuxGuitar/share/skins/Lavender/icon.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-gtp.png
install -pm 644 desktop/TuxGuitar/share/skins/Lavender/icon.png %buildroot/%_iconsdir/hicolor/96x96/mimetypes/audio-x-ptb.png

desktop-file-install --dir %buildroot/%_datadir/applications --delete-original %buildroot/%_datadir/applications/tuxguitar.desktop

# mime-type file
install -dm 755 %buildroot/%_datadir/mime/packages
install -pm 644 desktop/build-scripts/tuxguitar-linux-swt/target/tuxguitar-9.99-SNAPSHOT-linux-swt/share/mime/packages/tuxguitar.xml %buildroot/%_datadir/mime/packages/

%pretrans -p <lua>
path = "%{_iconsdir}/hicolor/96x96/apps/tuxguitar.png"
st = posix.stat(path)
if st and st.type == "directory" then
  if posix.stat(path .. "/icon.png") then
    os.remove(path .. "/icon.png")
  end
  os.remove(path)
end

%files
%doc AUTHORS LICENSE README.md
%_libdir/tuxguitar-%version
%_datadir/tuxguitar-%version
%_iconsdir/hicolor/*/*/*
%_datadir/applications/tuxguitar.desktop
%_datadir/mime/packages/*.xml
%_bindir/tuxguitar

%changelog
* Mon Sep 02 2024 Andrey Kovalev <ded@altlinux.org> 1.6.4-alt2
- fix update (closes: #51172)
- fix icon display

* Thu Aug 29 2024 Andrey Kovalev <ded@altlinux.org> 1.6.4-alt1
- update to 1.6.4 (closes: #51096)

* Mon Aug 12 2024 Andrey Kovalev <ded@altlinux.org> 1.6.3-alt2
- fix a bug with the icon display (closes: #51097)

* Fri Jul 19 2024 Andrey Kovalev <ded@altlinux.ru> 1.6.3-alt1
- update to 1.6.3

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt6
- fix build: add rpm-build-xdg

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt5
- fix build: drop libgcj-devel

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt4
- fix build: add libalsa-devel, libjack-devel

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.4
- NMU: corrected java dependencies

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.3
- NMU: corrected java dependencies

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.2
- NMU: corrected java dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3.1
- NMU: corrected java dependencies

* Mon Mar 19 2012 Michael Shigorin <mike@altlinux.org> 1.2-alt3
- rebuilt in current environment (closes: #21801)
- minor spec cleanup

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix CVE-2010-3385: insecure library loading (ALT bug #24333)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tuxguitar

* Thu Jan 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version 1.2 (with rpmrb script)
- add requires to eclipse-swt (ALT #24865)
- use Fedora's spec

* Thu Oct 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- subst /usr/lib with %_libdir (fix #21799)
- remove jpackage utils (fix #21521)

* Fri Sep 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version (1.0)
- rewrote spec, use external itext

* Sat May 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0rc4-alt1
- initial build for ALT Linux Sisyphus (thanks to SUSE for spec)

* Fri Apr 04 2008 Toni Graffy <toni@links2linux.de> - 1.0rc3-0.pm.1
- update to 1.0rc3
- changed BuildArch as this package contains two shared libs
- TuxGuitar-alsa is obsoleted now
* Mon Oct 29 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.2
- rebuild with new eclipse-swt-gtk2 package
* Wed Jan 31 2007 Toni Graffy <toni@links2linux.de> - 0.9.1-0.pm.1
- update to 0.9.1
* Tue Jan 30 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
* Wed Sep 27 2006 Toni Graffy <toni@links2linux.de> - 0.8-0.pm.1
- build for packman
- added itext.jar as internal lib
* Sat Sep 02 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.2
- rebuild, change in start-script for alsa-plugin
* Thu Aug 24 2006 oc2pus <oc2pus@arcor.de> - 0.8-0.oc2pus.1
- update to 0.8
* Mon Jul 17 2006 oc2pus <oc2pus@arcor.de> - 0.7-0.oc2pus.1
- update to 0.7
- switched to ant-build
- repacked without lib/* as tar.gz2
* Sun Jun 10 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.2
- corrected desktop-entry
* Sun May 28 2006 oc2pus <oc2pus@arcor.de> - 0.6-0.oc2pus.1
- update to 0.6
- added itext to dependencies
* Sat Apr 08 2006 oc2pus <oc2pus@arcor.de> - 0.5-0.oc2pus.1
- First packaged release 0.5
- repacked without swt.jar and native libs (jameica-swt3-gtk)
