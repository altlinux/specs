Name: skipstone
Version: 1.0.1
Release: alt2

Summary: Simple WebKit-based web browser
License: GPL
Group: Networking/WWW

Url: http://www.muhri.net/skipstone
Source0: %url/%name-%version.tar.gz
Source1: skipstone.desktop
Patch0: skipstone-0.9.7-alt-defaults.patch
Patch1: skipstone-1.0.0-alt-script.patch
Patch2: skipstone-1.0.1-alt-webkit.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Apr 02 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libXext-devel libXfixes-devel libXrender-devel libatk-devel libcairo-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libgtk+2-devel libpango-devel libsoup-devel pkg-config
BuildRequires: libXcomposite-devel libXcursor-devel libXdamage-devel libXi-devel libXinerama-devel libXrandr-devel libwebkitgtk2-devel

%define skipdatadir %_datadir/%name
%define skipplugdir %_libdir/%name/plugins

%description
SkipStone is a simple Gtk+ web browser

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed -i \
	-e 's,/usr/local,%prefix,g' \
	-e 's,WebKitGtk,webkit-1.0,g' \
	config.webkit
pushd src
%make -f Makefile.webkit
popd
ln src/skipstone-bin-webkit .

# muhri seems to have only experimented with webkit
# without actually removing gtkmozembed.h
#pushd plugins/
#make
#popd

%install
install -d %buildroot{%_bindir,%skipplugdir}
install -d %buildroot%skipdatadir/{icons,pixmaps/default}
install -p -m755 src/skipdownload %buildroot%_bindir/
install -p -m755 src/skipstone-bin-webkit %buildroot%_bindir/%name
install -p -m644 icons/* %buildroot%skipdatadir/icons/
install -p -m644 pixmaps/* %buildroot%skipdatadir/pixmaps/default/

#pushd plugins/
#install -p -m755 AutoComplete/AutoComplete.so %buildroot%skipplugdir/
#install -p -m755 FavIcon/FavIcon.so %buildroot%skipplugdir/
#install -p -m755 HistorySideBar/HistorySideBar.so %buildroot%skipplugdir/
#install -p -m755 Launcher/Launcher.so %buildroot%skipplugdir/
#install -p -m755 NewButton/NewButton.so %buildroot%skipplugdir/
#install -p -m755 SearchToolBar/SearchToolBar.so %buildroot%skipplugdir/
#install -p -m755 Throbber/Throb.so %buildroot%skipplugdir/
#install -p -m755 Up/Up.so %buildroot%skipplugdir/
#install -p -m755 Zoomer/SkipZoomer.so %buildroot%skipplugdir/
#install -p -m644 NewButton/new.png %buildroot%skipdatadir/pixmaps/default/
#popd

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_libdir/%name/*
%_desktopdir/*
%skipdatadir/
%skipplugdir/

# TODO:
# - figure out why skipdownload skips download (double free)
# - proper distro browser integration, if any?
# - try to build against webkit?

%changelog
* Sat Apr 02 2011 Michael Shigorin <mike@altlinux.org> 1.0.1-alt2
- built against webkitgtk2
  + fixed FTBFS
  + had to drop plugins (gtkmozembed-specific)
  + dropped shell wrapper as well

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1
- applied repocop patch

* Thu Jun 19 2008 Michael Shigorin <mike@altlinux.org> 1.0.0-alt4
- fixed wrapper not to run any crap named skipstone-bin in current dir
  (#16090)

* Sat Jun 14 2008 Michael Shigorin <mike@altlinux.org> 1.0.0-alt3
- moved skipstone-bin to %_libdir/%name/ (#16009)

* Fri Apr 18 2008 Michael Shigorin <mike@altlinux.org> 1.0.0-alt2
- built against seamonkey again
- fix build (sort of)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1.qa1
- NMU (by repocop): the following fixes applied:
  + update_menus for skipstone

* Wed Feb 20 2008 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0
- built against firefox

* Sun Jan 20 2008 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- built for ALT Linux (this epoch)
  + based on upstream spec
    - *heavy* spec cleanup
  + added PLD *.desktop
- happy birthday AEN :)

