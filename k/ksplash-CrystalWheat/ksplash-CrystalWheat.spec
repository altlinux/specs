Name: ksplash-CrystalWheat
Version: 1.0
Release: alt1
BuildArch: noarch
Summary: KDE splash Crystal Wheat

Packager: Lebedev Sergey <barabashka@altlinux.org>

License: GPL
Group: Graphical desktop/KDE
Url: http://kde-look.org/content/show.php/Crystal+Wheat?content=27894 

Source: %name-%version.tar.bz2
#Patch: %name-%version-%release.patch

BuildRequires: fontconfig freetype2 kde-settings kdelibs

%description
KDE splash Crystal Wheat by Leo Kent

%prep
%setup -q 

%install
mkdir -p %buildroot/%_datadir/apps/ksplash/Themes/CrystalWheat
install -m 644 *png %buildroot/%_datadir/apps/ksplash/Themes/CrystalWheat/
install -m 644 *rc %buildroot/%_datadir/apps/ksplash/Themes/CrystalWheat/

%files
%_datadir/apps/ksplash/Themes/*

%changelog
* Sun Nov 18 2007 Sergey Lebedev <barabashka@altlinux.ru> 1.0-alt1
- initial build

