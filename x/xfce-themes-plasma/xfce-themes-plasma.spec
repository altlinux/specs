Name:		xfce-themes-plasma
Summary:	Xfce Gtk+-2.0, Gtk+-3.0 and xfwm4 Plasma themes.
Version:	1.3
Release:	alt1
Epoch:		1
License:	GPLv2+
Url:		http://xfce-look.org/content/show.php/Plasma+Bolt%2C+Fire%2C+Shock?content=158436
Source:		158436-plasma-bundle.tar.gz
Group:		Graphical desktop/XFce
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildArch:	noarch

%description
This package provides the Xfce Gtk+-2.0, Gtk+-3.0 and xfwm4 Plasma themes.
This is an ' old school ' black (and I mean ' BLACK ') theme modified from
DarkMint/DarkCold4 by originalseed.

%package -n %name-Bolt
Summary: Xfce Plasma Bolt theme.
Group: Graphical desktop/XFce
Requires:	xfwm4 libgtk+2
Provides: %name

%description -n %name-Bolt
Xfce Gtk+-2.0, Gtk+-3.0 and xfwm4 Plasma Bolt theme.

%package -n %name-Fire
Summary: Xfce Plasma Fire theme.
Group: Graphical desktop/XFce
Requires:	xfwm4 libgtk+2
Provides: %name

%description -n %name-Fire
Xfce Gtk+-2.0, Gtk+-3.0 and xfwm4 Plasma Fire theme.

%package -n %name-Shock
Summary: Xfce Plasma Shock theme.
Group: Graphical desktop/XFce
Requires:	xfwm4 libgtk+2
Provides: %name

%description -n %name-Shock
Xfce Gtk+-2.0, Gtk+-3.0 and xfwm4 Plasma Shock theme.

%prep
%setup -c

%install
mkdir -p %buildroot%_datadir/themes
cp -a "./Plasma Bolt" %buildroot%_datadir/themes/Plasma_Bolt
cp -a "./Plasma Fire" %buildroot%_datadir/themes/Plasma_Fire
cp -a "./Plasma Shock" %buildroot%_datadir/themes/Plasma_Shock

%files -n %name-Bolt
%dir %_datadir/themes/Plasma_Bolt
%_datadir/themes/Plasma_Bolt/*

%files -n %name-Fire
%dir %_datadir/themes/Plasma_Fire
%_datadir/themes/Plasma_Fire/*

%files -n %name-Shock
%dir %_datadir/themes/Plasma_Shock
%_datadir/themes/Plasma_Shock/*

%changelog
* Sat Apr 05 2014 Motsyo Gennadi <drool@altlinux.ru> 1:1.3-alt1
- 1.3

* Wed Feb 05 2014 Motsyo Gennadi <drool@altlinux.ru> 1.05-alt1.1
- fix build

* Wed Feb 05 2014 Motsyo Gennadi <drool@altlinux.ru> 1.05-alt1
- 1.05

* Tue Jun 19 2012 Motsyo Gennadi <drool@altlinux.ru> 0.96-alt1
- initial build for ALT Linux
