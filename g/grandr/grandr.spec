Name: grandr
Version: 1.0.2
Release: alt3

Summary: RandR user interface using GTK+ libraries
License: MIT/X11
Group: System/X11

Url: http://cgit.freedesktop.org/xorg/app/%name/
Source: %name-%version.tar
Patch1: grandr-debian-01-fix-segfault-when-click-monitor.patch
Patch2: grandr-mandriva-synchronize-before-and-after-apply.patch


# Automatically added by buildreq on Tue Apr 10 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libXrender-devel libatk-devel libcairo-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libGConf-devel libXrandr-devel libgtk+2-devel

BuildRequires: xorg-util-macros

%description
%summary

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure 

%make_build LIBS="-lgthread-2.0 -lX11"

%install
%make DESTDIR=%buildroot install

%files
%doc README NEWS AUTHORS
%_bindir/*

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- DSO list completion

* Tue Apr 10 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix build

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build
