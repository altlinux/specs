# SPEC file for KeePass
#

%define real_name    KeePassX

Name:     keepassx
Version:  0.4.4
Release:  alt2

Summary: KeePassX Password Safe - light-weight cross-platform password manager
Summary(ru_RU.UTF-8): простой кросс-платформенный менеджер паролей KeePassX Password Safe

Group:    Networking/Other
License:  %gpl2only
URL:      http://sourceforge.net/projects/keepassx/
# URL: http://keepass.sourceforge.net/

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %real_name-%version.tar

Patch0:  %name-0.4.0-desktop.patch
Patch1:  %name-0.4.3-ru_translation.patch
Patch2:  %name-0.4.3-headers_fix.patch

Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png


AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Jul 02 2021
# optimized out: gcc-c++ kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libglvnd-devel libqt5-core libqt5-gui libqt5-widgets libqt5-xml libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel ruby ruby-stdlibs sh4
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kwallet-devel qt5-multimedia-devel qt5-phonon-devel qt5-script-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

BuildRequires: desktop-file-utils qt5-tools


%description
KeePassX  is  a cross platform port  of the windows  application
"Keepass Password Safe". It is an OpenSource password safe which
helps you to manage your passwords in an easy and secure way. It
uses a highly encrypted database locked with one master key.

KeePassX saves many different information: user names, passwords,
urls, comments and  file attachments in one single database.  The
entries could be  sorted in groups, with user-defined  titles and
icons specified for each entry or group. Also KeePassX  offers an 
utility for secure password generation.

The complete database is always encrypted either with AES  (alias
Rijndael) or  Twofish  encryption algorithm using  a 256 bit key.
The database format  of KeePassX  is compatible with the one used
in KeePass Password Safe.

%description -l ru_RU.UTF-8
KeePassX  -  кроссплатформенный порт  программы "Keepass Password
Safe" для Windows, менеджер паролей с открытым исходным кодом. Он
упрощает  управление  различными паролями,  сохраняя их в единой,
защищаемой одним мастер-ключом, базе данных.

KeePassX может сохранять в записях  различную информацию, включая
имена пользователей, пароли, URL, файловые вложения и комментарии.
Записи можно  организовать в группы,  с задаваемыми пользователем
именами и пиктограммами для каждой группы или записи.  В KeePassX
также входит утилита для создания надёжных паролей.

База  с паролями всегда хранится защищённой с использованием 
алгоритмов AES (Rijndael) или Twofish с длиной ключа 256 бит. 
Формат базы данных совместим с KeePass Password Safe.


%prep
%setup  -n %name-%version
%patch0
%patch1
%patch2

mv -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%qmake_qt5 PREFIX=%buildroot%prefix
%make
./translations_release.sh

%install
sed -i 's@AppDir+"/../share/keepassx/license.html"@"%_datadir/keepassx/license.html"@g' src/dialogs/AboutDlg.cpp
sed -i 's@AppDir+"/../share/doc/keepassx/index.html"@"%_datadir/keepassx/doc/index.html"@g' src/mainwindow.cpp

mkdir -p -- %buildroot%_datadir
cp -a -- share/{applications,keepassx,mime,mimelnk,pixmaps} %buildroot%_datadir

install -pDm 0755 src/src  %buildroot%_bindir/%{name}

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%doc changelog
%doc --no-dereference COPYING

%_bindir/%name
%_datadir/keepassx*

%_desktopdir/%name.desktop
%_pixmapsdir/%{name}*

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*

%_datadir/mime/packages/%{name}.xml
%_datadir/mimelnk/application/x-keepass.desktop


%changelog
* Fri Jul 02 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.4.4-alt2
- Build with QT5

* Tue Jan 05 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.4-alt1
- New version: security fixes
- Fix CVE-2015-8378: Canceling XML export operation creates export as ".xml"

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3-alt3
- Removing freedesktop-desktop-file-proposed-patch repocop patch

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3-alt2
- Fix build with GCC 4.7

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for keepassx
  * postclean-03-private-rpm-macros for the spec file

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3-alt1
- New version 0.4.3

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1-alt1
- New version 0.4.1

* Thu Jun 04 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.0-alt1
- New version 0.4.0
- Fix typos in russian translation

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.4-alt1
- New version 0.3.4

* Sat Jul 19 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.1-alt1
- New version 0.3.1 (closes #16343)
- Add pre-scaled icons

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.2-alt3
- Fix desktop file (#12022)
- Fix typo in package description
- Spec file cleanup

* Mon Jul 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.2-alt2
- Fix location of qmake

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.2-alt1
- First build for ALT Linux Sisyphus

* Tue Jun 13 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.1-alt0.3
- Fix help file locations

* Tue Jun 13 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.1-alt0.2
- Fix desktop file and icon locations

* Sun Jun 11 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.1-alt0.1
- Adding desktop file and icon

* Wed Jun 07 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.1-alt0
- Initial build

