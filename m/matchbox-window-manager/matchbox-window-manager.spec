# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gconftool-2 /usr/bin/pkg-config libICE-devel libSM-devel libXext-devel libexpat-devel pkgconfig(gconf-2.0) pkgconfig(libstartup-notification-1.0) pkgconfig(xcomposite) pkgconfig(xdamage) pkgconfig(xrender)
# END SourceDeps(oneline)
Name: matchbox-window-manager
Version: 1.2
Release: alt3
Summary: Window manager for the Matchbox Desktop
License: GPLv2+
Group: Graphical desktop/Other
Url: http://matchbox-project.org/
Packager: Aleksey Lim <alsroot@altlinux.org>

#Source: http://matchbox-project.org/sources/%name/%version/%name-%version.tar.gz
Source0: http://ftp.de.debian.org/debian/pool/main/m/matchbox-window-manager/matchbox-window-manager_1.2-osso21.orig.tar
Source1: http://ftp.de.debian.org/debian/pool/main/m/matchbox-window-manager/matchbox-window-manager_1.2-osso21-1.debian.tar
Source2: %name.watch

BuildRequires: libmatchbox-devel >= %version
BuildRequires: pkgconfig
BuildRequires: expat-devel
BuildRequires: libXfixes-devel
BuildRequires: libXcursor-devel
BuildRequires: pango-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libxsettings-client-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package light
Summary: Standalone Matchbox Window manager for the installer or embedded use
Group: Graphical desktop/Other

%description light
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains even a more lightweight build of Matchbox,
sutable for installer or a minimal kiosk system.

%prep
%setup -q -a1
for patch in `cat debian/patches/series`; do
    patch -p1 < debian/patches/$patch
done

%build
cp -a %name %name-embedded
pushd %name
autoreconf -fisv
%configure \
	--enable-startup-notification \
	--enable-session \
	--enable-alt-input-wins \
	--enable-keyboard \
	--enable-expat \
	--enable-pango
%make_build
popd

# standalone binary for installer/resource limited system (debian udeb pkg)
# use: matchbox-window-manager -use_titlebar no -use_desktop_mode plain
pushd %name-embedded
autoreconf -fisv
%configure \
	   --disable-startup-notification --disable-expat \
	   --disable-keyboard --disable-xrm --disable-ping-protocol --enable-standalone

%make_build
popd

%install
mkdir -p %buildroot%_man1dir/
install -m 644 debian/matchbox-*.1 %buildroot%_man1dir/

pushd %name
%make_install DESTDIR=%buildroot install
popd
pushd %name-embedded
install -m755 ./src/matchbox-window-manager %buildroot%_bindir/matchbox-window-manager-light
popd

%files
%_bindir/matchbox-remote
%_bindir/matchbox-window-manager
%_man1dir/*
%_datadir/matchbox
%_datadir/themes/*
%_sysconfdir/*
%doc %name/{AUTHORS,README,ChangeLog,COPYING}

%files light
%_bindir/matchbox-window-manager-light

%changelog
* Sat Nov 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3
- updated url
- added debian patches
- added debian man pages
- updated build deps
- built with 
	--enable-startup-notification \
	--enable-session \
	--enable-alt-input-wins \
 - added light subpackage with minimal standalone build

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 1.2-alt2
- fix %files warnings

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 1.2-alt1
- first build for ALT Linux Sisyphus
