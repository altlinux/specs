Name: qmpdclient
Version: 1.1.3
Release: alt2.qa2

Summary: Qt4-based mpd client
License: %gpl2plus
Group: Sound
Url: http://bitcheese.net/wiki/QMPDClient

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

# git://github.com/Voker57/qmpdclient-ne.git
Source0: %name-%version.tar
Patch0: qmpdclient-1.1.3-patch-DSO.patch

BuildRequires(pre): rpm-build-licenses libqt4-devel >= 4.4.0
BuildPreReq: gcc-c++ unzip cmake

Requires: libqt4-core >= 4.4.0
BuildRequires: desktop-file-utils
#Suggests: notification-daemon

%description
QMPDClient is an easy to use MPD client written in Qt 4.

%prep
%setup
%patch0 -p1
sed -i 's,/home/h/Projects/qmpdclient/qmpdclient/icons/qmpdclient22.png,%_iconsdir/hicolor/22x22/apps/%name.png,' \
	src/notifications_dbus.cpp
sed -i 's,Icon=%{name}64.png,Icon=%name,' %name.desktop

%build
%cmake
%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD
for i in 16 22 48 64; do
    install -pD -m644 icons/qmpdclient$i.png %buildroot%_iconsdir/hicolor/${i}x$i/apps/%name.png
done
install -pD -m644 icons/svg/qmpdclient.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

mkdir -p %buildroot%_datadir/QMPDClient/{iconsets,styles}/
tar xf Rodent.tar.gz -C %buildroot%_datadir/QMPDClient/iconsets/
unzip -q qmpdclient_silk_iconsets.zip -d %buildroot%_datadir/QMPDClient/iconsets/
rm -f %buildroot%_datadir/QMPDClient/iconsets/Readme.txt
rm -f %buildroot%_datadir/QMPDClient/iconsets/*/[Tt]humbs.db
install -pD -m644 Rain.css %buildroot%_datadir/QMPDClient/styles/

rm -f %buildroot%_iconsdir/%{name}64.png
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Network \
	--remove-category=Music \
	--add-category=AudioVideo \
	--add-category=Audio \
	--add-category=Player \
	%buildroot%_desktopdir/qmpdclient.desktop

%files
%_bindir/*
%_datadir/QMPDClient/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%doc AUTHORS Changelog INSTALL README THANKSTO

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2.qa2
- Fixed build

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.3-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qmpdclient
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Aug 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.1.3-alt2
- 1.1.3-7-ge7add82

* Mon Jun 07 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.3-alt1
- 1.1.3
- build with latest gcc again

* Mon Feb 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.2-alt2
- 1.1.2-36-gc5fa754

* Sat Nov 07 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.2-alt1
- 1.1.2
- fix Icon= in the desktop file, do not install qmpdclient64.png

* Wed Sep 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.1-alt4
- 1.1.1-5-g589ba0a
- replace libqt4 requirement with libqt4-core one

* Sun Aug 23 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.1-alt3
- build with gcc 4.3

* Tue Aug 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.1-alt2
- 1.1.1-4-g5d08dfc

* Sun Aug 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.1-alt1
- 1.1.1-1-g7c38e25

* Thu Feb 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt1
- qmpdclient-ne 1.1.0

* Wed Feb 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.1.0-alt0.1
- qmpdclient-ne 1f991a22 (1.1.0-pre)
- remove obsolete files

* Sat Dec 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.9-alt2
- update to git://github.com/Voker57/qmpdclient-ne.git 8cff43cd

* Thu May 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Fri Jan 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.8-alt2
- add Russian translation
- fix icon path for dbus notifier
- add styles and iconsets from official site

* Sun Jul 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Dec 21 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Tue Dec 19 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.6.2-alt2
- use optflags (drool@)
- install and package bundled icons

* Sat Oct 21 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.6.2-alt1
- 1.0.6.2

* Fri Oct 13 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.6.1-alt1
- 1.0.6.1

* Sat Sep 30 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.5-alt1
- initial build
