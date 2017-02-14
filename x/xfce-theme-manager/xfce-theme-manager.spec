%global		pkgname Xfce-Theme-Manager
Name:		xfce-theme-manager
Version:	0.3.8
Release:	alt1
Summary:	A theme manager for Xfce
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Graphical desktop/XFce
License:	GPLv3
Url:		http://xfce-look.org/content/show.php?content=149647
Source0:	http://keithhedger.hostingsiteforfree.com/zips/xfcethememanager/%pkgname-%version.tar.gz

Patch0: %name-0.2.4-desktop.patch
Patch1: %name-0.2.3-fix-strip-debug.patch

# Automatically added by buildreq on Thu Feb 07 2013 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstartup-notification libstdc++-devel libxfce4util-devel pkg-config xorg-xproto-devel
BuildRequires: desktop-file-utils gcc-c++ libXcursor-devel libxfce4ui-devel

%description
A theme manager allowing easy configuration of themes,
window borders, controls, icons and cursors for Xfce

%prep
%setup -n  %pkgname-%version
%patch0 -p1
# #%patch1 -p1

%build
%configure
%make_build
# # CXXFLAGS="%optflags -Wunused -Wunused-function -Wno-unused-result -lXcursor -lgthread-2.0 `pkg-config --cflags --libs glib-2.0` `pkg-config --cflags --libs gdk-2.0` `pkg-config --cflags --libs gtk+-2.0` -DGTK_DISABLE_DEPRECATED -DGTK_DISABLE_SINGLE_INCLUDES -DGDK_DISABLE_DEPRECATED -DGSEAL_ENABLE `pkg-config --cflags --libs libxfce4ui-1` -DGOT_LIBXFCEUI"

%install
make install DESTDIR=%buildroot PREFIX=%prefix

find %buildroot -name 'xfce-theme-manager' | xargs chmod 0755

%files
# #%doc README* ChangeLog* gpl-3.0.txt
%dir %_datadir/%pkgname
%_bindir/%name
%_desktopdir/%pkgname.desktop
%_pixmapsdir/%name.png
%_datadir/%pkgname/*
%_man1dir/%name.*
%_mandir/es/man1/%name.*
%_mandir/de/man1/%name.*
%_mandir/fr/man1/%name.*
%_mandir/pl/man1/%name.*

%changelog
* Tue Feb 14 2017 Motsyo Gennadi <drool@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Sun Sep 22 2013 Motsyo Gennadi <drool@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Thu Feb 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.2.4-alt1
- build for ALT Linux from FC19 package
