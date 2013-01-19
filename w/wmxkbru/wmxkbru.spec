# spec by Konstantin Kogan <kostyalamer at yandex.ru>

Name: wmxkbru
Version: 1.2.2
Release: alt1
Summary: wmxkbru showns and controls XKB groups (only ru or en) for Window Maker
Summary(ru_RU.UTF-8): показывает и переключает раскладки клавиатуры (только ru/en)
License: GPL2
Group: Graphical desktop/Window Maker

%define __prefix /usr
URL: http://www.geocities.com/wmalms/#WMXKB
Source: %name-%version.tar.gz
Source1: %name.menu

Requires: WindowMaker >= 0.60.0

# Automatically added by buildreq on Sun Jun 13 2010
BuildRequires: imake libXext-devel libXpm-devel

%description
wmxkbru showns and controls XKB groups (only ru or en) for Window Maker.

%prep
%setup

%build
%configure --with-rpm --prefix=%{__prefix}
make

%install
make BINDIR=%buildroot%_bindir install

mkdir -p %buildroot%_datadir/pixmaps/wmxkb/
install -m 644 pixmaps/*.xpm %buildroot%_datadir/pixmaps/wmxkb/
install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%doc %_datadir/pixmaps/wmxkb
%_datadir/pixmaps/wmxkb/*.xpm
%_menudir/*

%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

* Mon Mar 20 2006 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-4
- changed prefix pat to /usr.

* Fri Mar 04 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-3
- changed pixmaps to /usr/X11R6/share/pixmaps/wmxkb.

* Fri Feb 18 2005 J. Krebs <rpm_speedy@yahoo.com> - 1.2.2-2
- src.rpm script barfed under Fedora. Tweaked it.

* Thu Jun 17 2004 Michael Glickman <wmalms@yahoo.com>
- v 1.2.2
- Bug fixes: image selection with flexy group
-            no crash if too many groups are defined
-            fixed RPM installation script

* Tue Feb 03 2004 Michael Glickman <wmalms@yahoo.com>
- v 1.2.1
- Minor bug fix: eliminate colon(:) from symbol names
- Default docking with PWM 

* Wed Dec 10 2003 Michael Glickman <wmalms@yahoo.com>
- v 1.2.0
- Support for group-specific images (e.g.country flags)
- Custom background images

* Wed Oct 29 2003 Michael Glickman <wmalms@yahoo.com>
- v 1.1.0
- Support for BlackBox and clones
- Extended windowMode option
- IconTitle (-ititle) parameter
- A neater xkb bug work arround (thanks to Ivan Pascal)

* Fri Oct 10 2003 Michael Glickman <wmalms@yahoo.com>
- RPM release



