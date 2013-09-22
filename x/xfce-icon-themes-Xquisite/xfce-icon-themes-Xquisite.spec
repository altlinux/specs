Name:		xfce-icon-themes-Xquisite
Summary:	Xquisite is a icon theme for XFCE
Version:	0.4.6
Release:	alt1
License:	Creative Commons
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://xfce-look.org/content/show.php/Xquisite?content=69735

Source0:	Xquisite.tbz
Group:		Graphical desktop/XFce

BuildArch:	noarch

%description
This package provides the Xfce icons themes.
An icon theme based on prior Exquisites and modified from various sources, this time more set up around Xfce.

%prep
%setup -c

%install
mkdir -p %buildroot%_iconsdir

cp -a ./Xquisite %buildroot%_iconsdir/Xquisite

%files
%dir %_iconsdir/Xquisite
%_iconsdir/Xquisite/*

%changelog
* Sun Sep 22 2013 Motsyo Gennadi <drool@altlinux.ru> 0.4.6-alt1
- initial build for ALT Linux
