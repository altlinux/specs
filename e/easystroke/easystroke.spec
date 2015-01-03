# SPEC file for easystroke
#

Name:     easystroke
Version:  0.6.0
Release:  alt2.1

Summary: a gesture-recognition application for X11

Group:    Accessibility
License:  ICS License
URL:      https://github.com/thjaeger/easystroke
#URL:      http://sourceforge.net/projects/easystroke/
Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.5.5.1-alt-desktop.patch
Patch2:  %name-0.5.5.1-alt-debuginfo.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sun Apr 14 2013
# optimized out: at-spi2-atk boost-devel fontconfig fontconfig-devel glib2-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libat-spi2-core libatk-devel libatkmm-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+3-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-server perl-Encode perl-Locale-gettext pkg-config xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: boost-devel-headers gcc-c++ git-core help2man intltool libXtst-devel libdbus-glib-devel libgtkmm3-devel ruby ruby-stdlibs xorg-sdk

BuildRequires: librsvg-utils


%description
easystroke is a gesture-recognition application for X11.
It aims to be highly configurable while at the same time
providing an intuitive user interface. It was designed
primarily for use on a Tablet PC, but it also works well
with a mouse.

%prep
%setup  -n %name-%version
%patch0 -p1

%patch1
%patch2 -p2

%build
%make PREFIX=%_exec_prefix
%make man


%install
%make DESTDIR=%buildroot PREFIX=%_exec_prefix install

mkdir -p %buildroot%_man1dir
install -m 0755 %name.1 %buildroot%_man1dir/

mkdir -p -- %buildroot%_miconsdir %buildroot%_niconsdir %buildroot%_liconsdir
/usr/bin/rsvg-convert -w 16 -h 16 -f png -o %buildroot%_miconsdir/%name.png -- %name.svg
/usr/bin/rsvg-convert -w 32 -h 32 -f png -o %buildroot%_niconsdir/%name.png -- %name.svg
/usr/bin/rsvg-convert -w 48 -h 48 -f png -o %buildroot%_liconsdir/%name.png -- %name.svg

%find_lang %name

%files -f %name.lang
%doc changelog LICENSE

%_bindir/%name
%_man1dir/%name.*

%_desktopdir/%name.desktop

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.6.0-alt2.1
- rebuild with boost 1.57.0

* Sat Sep 20 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0-alt2
- Fix desktop file

* Sun Jun 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.99.2-alt1
- New version

* Sun Feb 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.6-alt1
- New version

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5.1-alt1.3
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5.1-alt1.2
- Rebuilt with Boost 1.51.0
- Enabled debuginfo

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5.1-alt1.1
- Rebuilt with Boost 1.49.0

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.5.1-alt1
- Initial build for ALT Linux Sisyphus

