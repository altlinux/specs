Name:		rosa-launcher
Version:	0.34.12
Release:	alt1
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.gz
Patch1:		kfileitem_h.patch
Patch2:		local-applet-config_h.patch
Patch3:		rosa-srarter-config_h.patch

Requires:	kde4base-workspace

BuildRequires(pre):	kde-common-devel
BuildRequires: gcc-c++
BuildRequires: kde4base-workspace-devel
BuildRequires: kde4base-devel
BuildRequires: soprano-backend-redland
BuildRequires: soprano

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

cd local-applet
%K4build

cd ../rosa-services-runner
%K4build

cd ../rosa-starter
%K4build
cd ..

%install
%K4install

cd local-applet
%K4install

cd ../rosa-services-runner
%K4install

cd ../rosa-starter
%K4install
cd ..

mkdir -p %buildroot%_datadir/locale/ru/LC_MESSAGES/ \
         %buildroot%_K4apps/plasma/plasmoids/rosastarter/ \
         %buildroot%_iconsdir/hicolor/128x128/apps/ \
         %buildroot%_K4apps/rosa-launcher/icons/buttons/ \
         %buildroot%_K4apps/rosa-launcher/extra/

cp -f local-applet/plasma-applet-rosa-launcher.desktop rosa-services-runner/plasma-runner-rosa-services.desktop rosa-starter/metadata.desktop rosa-starter/plasma-applet-rosastarter.desktop %buildroot%_K4srv

cp -f icons/buttons/* %buildroot%_K4apps/rosa-launcher/icons/buttons/
cp -f icons/rosalauncher.png %buildroot%_iconsdir/hicolor/128x128/apps/
cp -f icons/rosa-icon.png icons/mandriva-icon.png %buildroot%_K4apps/rosa-launcher/icons/

cp -f extra/checkos.sh %buildroot%_K4apps/rosa-launcher/extra/

cp -Rf locale/ %buildroot%_datadir

%find_lang %name

%files -f %name.lang
%_bindir/*
%_K4lib/*.so
%_K4srv/*.desktop
%_K4apps/rosa-launcher/*
%_iconsdir/hicolor/128x128/apps/rosalauncher.png
%lang(ar)      %_datadir/locale/ar/LC_MESSAGES/*
%lang(es)      %_datadir/locale/es/LC_MESSAGES/*
%lang(et)      %_datadir/locale/et/LC_MESSAGES/*
%lang(eu)      %_datadir/locale/eu/LC_MESSAGES/*
%lang(fr)      %_datadir/locale/fr/LC_MESSAGES/*
%lang(pt_BR)   %_datadir/locale/pt_BR/LC_MESSAGES/*
%lang(ru)      %_datadir/locale/ru/LC_MESSAGES/*
%lang(sl)      %_datadir/locale/sl/LC_MESSAGES/*
%lang(sw)      %_datadir/locale/sw/LC_MESSAGES/*
%lang(tr)      %_datadir/locale/tr/LC_MESSAGES/*
%lang(zh_TW)   %_datadir/locale/zh_TW/LC_MESSAGES/*

%changelog
* Mon Nov 12 2012 Andrey Cherepanov <cas@altlinux.org> 0.34.12-alt1
- Initial build for ALT Linux distribution (thanks unihorn) (ALT #27487)

* Mon Sep 25 2012  Andrey Cherkinsky aka unihorn <unihorn@altlinux.ru> 1:0.34.12-alt1
- Initial build for ALT Linux distribution.
- Based on the spec of this src.rpm: http://rpm.pbone.net/index.php3?stat=26&dist=17&size=242551&name=rosa-launcher-0.34.12-1.src.rpm.
