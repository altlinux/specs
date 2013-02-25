Name:		rosa-launcher
Version:	2.0.0
Release:	alt1.r53.1
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.gz
Patch1:     %name-2.0.0-fix-plugin-path.patch
Patch2:     %name-2.0.0-fix-base-dir.patch
Patch3:     %name-2.0.0-fix-desktop-file.patch

Requires:	kde4base-workspace

BuildRequires(pre):	kde-common-devel
BuildRequires: gcc-c++
BuildRequires: kde4base-workspace-devel
BuildRequires: kde4base-devel
BuildRequires: soprano-backend-redland
BuildRequires: soprano
BuildRequires: qjson-devel

Provides:   simplywelcome = %version-%release

%description
ROSA Desktop Application Launcher.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%K4build

%install
%K4install
mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps/
install -m0644 assets/rosa-icon.png  %buildroot%_iconsdir/hicolor/128x128/apps/rosalauncher.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_K4lib/*.so
%_K4srv/*.desktop
%_libdir/libtimeframe.so
%_libdir/timeframe/*-timeframe-plugin.so
%_datadir/%name/*
%_iconsdir/hicolor/128x128/apps/rosalauncher.png
%lang(ar)      %_K4i18n/ar/LC_MESSAGES/*
%lang(de)      %_K4i18n/de/LC_MESSAGES/*
%lang(es)      %_K4i18n/es/LC_MESSAGES/*
%lang(et)      %_K4i18n/et/LC_MESSAGES/*
%lang(eu)      %_K4i18n/eu/LC_MESSAGES/*
%lang(fr)      %_K4i18n/fr/LC_MESSAGES/*
%lang(pt_BR)   %_K4i18n/pt_BR/LC_MESSAGES/*
%lang(ru)      %_K4i18n/ru/LC_MESSAGES/*
%lang(sl)      %_K4i18n/sl/LC_MESSAGES/*
%lang(sw)      %_K4i18n/sw/LC_MESSAGES/*
%lang(tr)      %_K4i18n/tr/LC_MESSAGES/*
%lang(zh_TW)   %_K4i18n/zh_TW/LC_MESSAGES/*

%changelog
* Mon Feb 25 2013 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.r53.1
- Add icon for plasmoid
- Fix desktop file

* Fri Feb 08 2013 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.r53
- New version 2.0.0-53

* Mon Nov 12 2012 Andrey Cherepanov <cas@altlinux.org> 0.34.12-alt1
- Initial build for ALT Linux distribution (thanks unihorn) (ALT #27487)

* Mon Sep 25 2012  Andrey Cherkinsky aka unihorn <unihorn@altlinux.ru> 1:0.34.12-alt1
- Initial build for ALT Linux distribution.
- Based on the spec of this src.rpm: http://rpm.pbone.net/index.php3?stat=26&dist=17&size=242551&name=rosa-launcher-0.34.12-1.src.rpm.
