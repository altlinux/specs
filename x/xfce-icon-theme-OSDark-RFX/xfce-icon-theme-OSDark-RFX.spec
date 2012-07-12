Name:		xfce-icon-theme-OSDark-RFX
Summary:	OSDark-RFX is a icon theme for XFCE
Version:	20120211
Release:	alt1
License:	GPLv2+
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://xfce-look.org/content/show.php/OSDark+RFX?content=139893

Source0:	OSDark-20120211.tar.bz2
Source1:	OSDark-blue-20120211.tar.bz2
Source2:	OSDark-green-20120211.tar.bz2
Group:		Graphical desktop/XFce

Patch0:		OSDark-alt_red_name.diff

BuildArch:	noarch

%description
This package provides the Xfce icons themes.
Here it is final version of OSDark RFX (Remake For Xfce) of OSDark icon theme by gmaster.

%package -n %name-red
Summary: Xfce OSDark-RFX red icons theme.
Group: Graphical desktop/XFce
Provides: %name

%description -n %name-red
Xfce OSDark-RFX red icons theme.

%package -n %name-blue
Summary: Xfce OSDark-RFX blue icons theme.
Group: Graphical desktop/XFce
Provides: %name

%description -n %name-blue
Xfce OSDark-RFX blue icons theme.

%package -n %name-green
Summary: Xfce OSDark-RFX green icons theme.
Group: Graphical desktop/XFce
Provides: %name

%description -n %name-green
Xfce OSDark-RFX green icons theme.

%prep
%setup -c
tar xjf %SOURCE1
tar xjf %SOURCE2
%patch0 -p1

%install
mkdir -p %buildroot%_iconsdir

cp -a ./OSDark %buildroot%_iconsdir/OSDark-red
cp -a ./OSDark-blue %buildroot%_iconsdir/OSDark-blue
cp -a ./OSDark-green %buildroot%_iconsdir/OSDark-green

%files -n %name-red
%dir %_iconsdir/OSDark-red
%_iconsdir/OSDark-red/*

%files -n %name-blue
%dir %_iconsdir/OSDark-blue
%_iconsdir/OSDark-blue/*

%files -n %name-green
%dir %_iconsdir/OSDark-green
%_iconsdir/OSDark-green/*

%changelog
* Thu Jul 12 2012 Motsyo Gennadi <drool@altlinux.ru> 20120211-alt1
- initial build for ALT Linux
