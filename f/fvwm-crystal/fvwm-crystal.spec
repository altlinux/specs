Name: fvwm-crystal
Version: 3.0.6
Release: alt2.1.1
License: GPL v2+
Group: Graphical desktop/FVWM based
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Summary: Desktop Environment

Source: http://download.berlios.de/fvwm-crystal/%name-%version.tar
Source1: fvwm-crystal.wmsession
Url: http://fvwm-crystal.berlios.de/
BuildRequires: fvwm-base
BuildArch: noarch

%description
FVWM-Crystal is a set of configuration files for F* Virtual Window
Manager (FVWM), which can create for you a good looking, very
functional desktop environment.

%prep
%setup -q

%install
export prefix=%buildroot/usr
make PREFIX=%buildroot%prefix install
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/10Fvwm-crystal
sed -i "s|%buildroot|/|g" %buildroot/%_bindir/*
rm -rf %buildroot/%_datadir/%name/fvwm/Applications/*

%files

%doc doc/* AUTHORS INSTALL COPYING NEWS README
%_bindir/*
%_datadir/%name/fvwm/Applications
%_datadir/%name/fvwm/colorsets
%_datadir/%name/fvwm/components
%_datadir/%name/fvwm/config
%_datadir/%name/fvwm/decorations
%_datadir/%name/fvwm/icons
%_datadir/%name/fvwm/locale
%_datadir/%name/fvwm/preferences
%_datadir/%name/fvwm/recipes
%_datadir/%name/fvwm/scripts
%_datadir/%name/fvwm/wallpapers
%_man1dir/*.gz
%_sysconfdir/X11/wmsession.d/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.6-alt2.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt2.1
- Rebuilt with python 2.6

* Thu May 14 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.6-alt2
- Packaged as noarch

* Tue Mar 31 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.6-alt1
- Initial for ALT (spec from PLD)
