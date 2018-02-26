# vim: set ft=spec: -*- rpm-spec -*-

%define azupdater_version 1.8.8

Name: vuze
Version: 4.2.0.2
Release: alt1

Summary: Powerful, full-featured, cross-platform bittorrent client
Group: Networking/File transfer
License: GPL
Url: http://azureus.sourceforge.net/

BuildArch: noarch

Packager: Sir Raorn <raorn@altlinux.ru>

Provides: azureus-plugin-azupdater = %azupdater_version
Provides: vuze-plugin-azupdater = %azupdater_version

Requires: java >= 1.6.0 eclipse-swt jakarta-commons-cli junit4 log4j

Obsoletes: azureus < 3.1.1.0
Provides: azureus = %version-%release

Source: %name-%version.tar
Source1: azupdater-%azupdater_version.tar

Source10: %name.desktop

Patch: %name-%version-%release.patch
Patch1: azupdater-%azupdater_version-%release.patch

# Automatically added by buildreq on Sun Dec 28 2008 (-bi)
BuildRequires: ant jpackage-1.6-compat jakarta-commons-cli junit4 log4j eclipse-swt ImageMagick-tools

BuildRequires: /proc

%description
Vuze (formerly Azureus) is a BitTorrent protocol implementation
that offers multiple torrent downloads, queuing/priority systems
(on torrents and files), start/stop seeding options, and instant
access to numerous pieces of information about your torrents.
It includes an embedded tracker that is easily set up and ready
to use.

%prep
%setup -a1
%patch -p1
pushd azupdater
%patch1 -p1
popd

%build
mkdir -p build/libs dist
ln -sf %_javadir/commons-cli.jar build/libs
ln -sf %_javadir/junit4.jar build/libs
ln -sf %_javadir/log4j.jar build/libs
ln -sf %_libdir/java/swt.jar build/libs

ANT_OPTS='-Xmx384m' ant

pushd azupdater
javac -source 1.5 -target 1.5 -g:lines,vars,source org/gudy/azureus2/update/Updater.java
jar -cf Updater.jar org/
popd

bzip2 ChangeLog.txt

%install
mkdir -p %buildroot{%_bindir,%_datadir/azureus/plugins/azupdater,%_liconsdir,%_miconsdir,%_niconsdir,%_desktopdir}
install -p -m644 dist/Azureus2.jar %buildroot%_datadir/azureus
install -p -m755 org/gudy/azureus2/platform/unix/startupScript %buildroot%_bindir/vuze
ln -sf vuze %buildroot%_bindir/azureus
pushd azupdater
install -p -m644 Updater.jar %buildroot%_datadir/azureus/plugins/azupdater
install -p -m644 plugin.properties %buildroot%_datadir/azureus/plugins/azupdater
popd

install -p -m644 %_sourcedir/vuze.desktop %buildroot%_desktopdir/vuze.desktop
install -p -m644 org/gudy/azureus2/ui/icons/a16.png %buildroot%_miconsdir/vuze.png
install -p -m644 org/gudy/azureus2/ui/icons/a32.png %buildroot%_niconsdir/vuze.png
convert -resize 48x48 org/gudy/azureus2/ui/icons/a64.png %buildroot%_liconsdir/vuze.png

%files
%doc ChangeLog.txt*
%_bindir/azureus
%_bindir/vuze
%_datadir/azureus
%_desktopdir/vuze.desktop
%_miconsdir/vuze.png
%_niconsdir/vuze.png
%_liconsdir/vuze.png

%changelog
* Sun May 31 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.0.2-alt1
- [4.2.0.2] (closes: #20250)
- Russian translations updated from http://azureus.narod.nnov.ru/russian.html

* Mon Jan 19 2009 Sir Raorn <raorn@altlinux.ru> 4.0.0.4-alt2
- Silenced complains about non-writable system plugin directory
- Russian translations updated from http://azureus.narod.nnov.ru/russian.html

* Sun Dec 28 2008 Sir Raorn <raorn@altlinux.ru> 4.0.0.4-alt1
- [4.0.0.4]
- Built with java 1.6 due to eclipse-swt
- Removed obsolete %%update_menus/%%clean_menus calls

* Sun Sep 21 2008 Sir Raorn <raorn@altlinux.ru> 3.1.1.0-alt1
- [3.1.1.0]
- Renamed to vuze

* Tue Jan 29 2008 Sir Raorn <raorn@altlinux.ru> 3.0.4.2-alt2
- Packaged azupdater plugin
- Added desktop entry and application icons

* Sun Jan 27 2008 Sir Raorn <raorn@altlinux.ru> 3.0.4.2-alt1
- Initial build

