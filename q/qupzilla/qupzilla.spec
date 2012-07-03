# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

Name: qupzilla
Version: 1.1.8
Release: alt1

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW

Url: http://qupzilla.com
# Sources are available on github
# git clone https://github.com/nowrep/QupZilla.git qupzilla && cd qupzilla
# git archive v1.1.8 --prefix=qupzilla-1.1.8/ | bzip2 > ../qupzilla-1.1.8.tar.bz2
Source: %name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Mar 13 2012
# optimized out: fontconfig libgst-plugins libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-sql libqt4-webkit libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ phonon-devel

BuildRequires: libqt4-devel >= 4.7

%description
QupZilla is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%prep
%setup
# remove BUILDTIME usage from build
sed -i '/static const QString BUILDTIME/d' src/app/qupzilla.h
sed -i '/QupZilla::BUILDTIME/d' -i \
	src/other/aboutdialog.cpp \
	src/app/commandlineoptions.cpp \
	src/app/qupzilla.cpp \
	src/network/qupzillaschemehandler.cpp

%build
export USE_WEBGL="true"
# enables better oxygen icons in Preferences.
export KDE="true"
pushd src
echo "CONFIG += debug" >> src.pro
qmake-qt4
%make_build

%install
make -C src INSTALL_ROOT=%buildroot install

%files
%doc AUTHORS FAQ TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%_datadir/%name/locale
%_datadir/%name/themes

%changelog
* Tue Mar 13 2012 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- initial build for ALT Linux Sisyphus (based on opensuse package)
- considerable cleanup of otherwise quite nice spec
- buildreq

* Tue Feb 14 2012 fisiu@opensuse.org
- Update to 1.1.8:
  + new translations: Swedish, Serbian and Traditional Chinese
  + option to use external download manager
  + import/export passwords into xml file
  + option to change user agent
  + support for JavaScript Popup windows
  + allow changing background in Speed Dial
  + many bugfixes, details in Changelog file
- Drop qupzilla-1.1.5-remove-date-time.patch: sed'ed in .spec
* Sun Jan  8 2012 fisiu@opensuse.org
- Update to 1.1.5:
  + new translations: Portuguese, French, Greek
  + add support for js printing with window.print()
  + improved commandline options
  + improved performance of history delete
  + many bugfixes
- Rebase remove_date-time.patch
* Thu Dec 22 2011 fisiu@opensuse.org
- Add fedora and mandriva items
* Mon Dec 19 2011 fisiu@opensuse.org
- Upstream update to 1.1.0:
  + speed dial
  + import bookmarks from html file
  + option to turn on XSS Auditing
  + many bugfixes
- Set variable KDE to "true" to enable better integration
  (atm only incons, nepomuk is planned)
* Tue Nov  1 2011 fisiu@opensuse.org
- enable webgl only for openSUSE >= 12.1
* Tue Nov  1 2011 fisiu@opensuse.org
- initial package
