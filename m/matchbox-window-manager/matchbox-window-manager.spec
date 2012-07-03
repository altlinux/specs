Name: matchbox-window-manager
Version: 1.2
Release: alt2
Summary: Window manager for the Matchbox Desktop
License: GPLv2+
Group: Graphical desktop/Other
Url: http://projects.o-hand.com/matchbox/
Packager: Aleksey Lim <alsroot@altlinux.org>

Source: http://matchbox-project.org/sources/%name/%version/%name-%version.tar.bz2

BuildPreReq: libmatchbox-devel >= %version-%release
BuildPreReq: pkgconfig
BuildPreReq: expat-devel
BuildPreReq: libXfixes-devel
BuildPreReq: libXcursor-devel
BuildPreReq: pango-devel
BuildPreReq: libpng-devel
BuildPreReq: libjpeg-devel

#BuildRequires:  startup-notification-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%prep
%setup -v

%build
%configure \
	--enable-keyboard \
	--enable-expat \
	--enable-pango
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_datadir/matchbox
%_datadir/themes/*
%_sysconfdir/*
%doc AUTHORS README ChangeLog COPYING

%changelog
* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 1.2-alt2
- fix %files warnings

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 1.2-alt1
- first build for ALT Linux Sisyphus
