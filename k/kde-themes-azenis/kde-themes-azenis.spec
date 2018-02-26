%define		sname azenis
%define		unpack tar -xf

Name:		kde-themes-azenis
Version:	1.1
Release:	alt4
Group:		Graphical desktop/KDE
Summary:	The Azenis themes for KDE
License:	GPL
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://kde-look.org/content/show.php/Azenis?content=77150
Source0:	%sname.tar.gz
Patch0:		%sname-cursor_name.diff
BuildArch:	noarch

%description
%name package contains the Azenis themes for Kbfx, KDM,
KDE splash (moodin engine), Dekorator, cursor theme,
wallpaper collection, TTF font

%package -n kbfx-themes-azenis
Summary: Azenis theme for Kbfx
Group: Graphical desktop/KDE
Requires: kbfx

%description -n kbfx-themes-azenis
Azenis theme for Kbfx

%package -n kbfx-themes-azenis_Alternet
Summary: Azenis Alternet theme for Kbfx
Group: Graphical desktop/KDE
Requires: kbfx

%description -n kbfx-themes-azenis_Alternet
Azenis Alternet theme for Kbfx

%package -n kdm-themes-azenis
Summary: Azenis theme for KDM
Group: Graphical desktop/KDE
Requires: kdmtheme kdebase-kdm

%description -n kdm-themes-azenis
Azenis theme for KDM

%package -n kde-style-azenis-kwin
Summary: Azenis Window Decorations
Group: Graphical desktop/KDE
Requires: dekorator

%description -n kde-style-azenis-kwin
Azenis Window Decorations

%package -n kde-styles-splash-azenis
Summary: Azenis theme for KDE splash
Group: Graphical desktop/KDE
Requires: kdebase-wm ksplash-engine-moodin

%description -n kde-styles-splash-azenis
Azenis theme for KDE splash (moodin engine)

%package -n kde-styles-splash-azenis_sys
Summary: Azenis_Sys theme for KDE splash
Group: Graphical desktop/KDE
Requires: kdebase-wm ksplash-engine-moodin

%description -n kde-styles-splash-azenis_sys
Azenis_Sys theme for KDE splash (moodin engine)

%package -n x-cursor-theme-azenis
Summary: Azenis cursors for Xorg
Group: System/X11

%description -n x-cursor-theme-azenis
This package contains Azenis cursors for Xorg

%package -n azenis-fonts-ttf
Summary: Unicode True Type fonts for Azenis theme
Group: System/Fonts/True type

%description -n azenis-fonts-ttf
This package contains unicode True Type fonts for Azenis theme

%package -n wallpapers-azenis
Summary: Azenis wallpapers collection
Group: Graphics

%description -n wallpapers-azenis
Azenis wallpapers collection

%package -n kicker-themes-azenis
Summary: Azenis background for Kicker
Group: Graphical desktop/KDE
Requires: kdebase-wm

%description -n kicker-themes-azenis
Azenis background for Kicker

%package -n %name-docs
Summary: Documentation for Azenis theme
Group: Documentation

%description -n %name-docs
This package contains HowTo (PDF format) for Azenis theme,
splash for OpenOffice and SuperKaramba themes

%package -n kde-colorscheme-azenis
Summary: Azenis color scheme for KDE
Group: Graphical desktop/KDE
Url: http://kde-look.org/content/show.php/Azenis+Custom+Color+Theme?content=82361
Source1: 82361-Azenis_Custom.kcsrc
Requires: kdebase-common

%description -n kde-colorscheme-azenis
Azenis color scheme for KDE

%package -n %name-full
Summary: Azenis themes full installation
Group: Graphical desktop/KDE
Requires: azenis-fonts-ttf = %version-%release
Requires: kbfx-themes-azenis = %version-%release
Requires: kbfx-themes-azenis_Alternet = %version-%release
Requires: kde-colorscheme-azenis = %version-%release
Requires: kde-style-azenis-kwin = %version-%release
Requires: kde-styles-splash-azenis = %version-%release
Requires: kde-styles-splash-azenis_sys = %version-%release
Requires: kde-themes-azenis-docs = %version-%release
Requires: kicker-themes-azenis = %version-%release
Requires: wallpapers-azenis = %version-%release
Requires: x-cursor-theme-azenis = %version-%release

%description -n %name-full
Virtual package for full Azenis themes installation

%prep
%setup -q -n Azenis
%unpack Azenis_Theme%version.tar.gz
pushd Azenis_Theme
cd ./CursorTheme/ && %unpack ./target.tar.gz && cd ..

%patch0 -p1

%build
pushd Azenis_Theme

cd Dekorator && %unpack Azenis_Dekorator-theme.tar.gz && cd ..
cd KBFX_menu && %unpack AzenisKbfxAlternet.tar.gz && %unpack AzenisKbfx.tar.gz && cd ..
cd KDE_Start_splash && %unpack Azenis.tar.gz && %unpack Azenis_Sys.tar.gz && cd ..
cd KDM_Login && %unpack AzenisKDM.tar.gz && cd ..

%install
pushd Azenis_Theme
rm -rf SuperKaramba/Azenis_KClock/KClock.theme~

# Kbfx
mkdir -p %buildroot%_datadir/apps/kbfx/skins/
cp -r KBFX_menu/AzenisKbfx %buildroot%_datadir/apps/kbfx/skins/Azenis
cp -r KBFX_menu/AzenisKbfxAlternet %buildroot%_datadir/apps/kbfx/skins/AzenisAlternet

# KDM
mkdir -p %buildroot%_datadir/apps/kdm/themes
cp -r KDM_Login/AzenisKDM %buildroot%_datadir/apps/kdm/themes/Azenis

# Dekorator
mkdir -p %buildroot%_datadir/apps/deKorator/themes
cp -r Dekorator/Azenis_Dekorator-theme %buildroot%_datadir/apps/deKorator/themes/Azenis-theme

# KDE splash (moodin!)
mkdir -p %buildroot%_datadir/apps/ksplash/Themes/
cp -r KDE_Start_splash/{Azenis,Azenis_Sys} %buildroot%_datadir/apps/ksplash/Themes/

# Cursors
mkdir -p %buildroot%_datadir/icons/Azenis
cp -r CursorTheme/target/* %buildroot%_datadir/icons/Azenis/

# TTF font
%__install -Dp -m 0644 Font/SAVEDBYZ.TTF %buildroot%_datadir/fonts/default/TrueType-val/SAVEDBYZ.ttf

# Wallpapers
mkdir -p %buildroot%_datadir/wallpapers
cp -r Wallpaper %buildroot%_datadir/wallpapers/Azenis

# Kicker
mkdir -p %buildroot%_datadir/apps/kicker/tiles
%__install -Dp -m 0644 Kicker/kicker_background.png %buildroot%_datadir/apps/kicker/wallpapers/kicker_background_azenis.png
cp Kicker/icon_background/*.png %buildroot%_datadir/apps/kicker/tiles/

# Color Scheme
%__install -Dp -m 0644 %SOURCE1 %buildroot%_datadir/apps/kdisplay/color-schemes/Azenis_Custom.kcsrc

popd Azenis_Theme

%files -n kbfx-themes-azenis
%dir %_datadir/apps/kbfx/skins/Azenis
%_datadir/apps/kbfx/skins/Azenis/*

%files -n kbfx-themes-azenis_Alternet
%dir %_datadir/apps/kbfx/skins/AzenisAlternet
%_datadir/apps/kbfx/skins/AzenisAlternet/*

# #%files -n kdm-themes-azenis
# #%dir %_datadir/apps/kdm/themes/Azenis
# #%_datadir/apps/kdm/themes/Azenis/*

%files -n kde-style-azenis-kwin
%dir %_datadir/apps/deKorator/themes/Azenis-theme
%dir %_datadir/apps/deKorator/themes/Azenis-theme/deco
%dir %_datadir/apps/deKorator/themes/Azenis-theme/masks
%dir %_datadir/apps/deKorator/themes/Azenis-theme/buttons
%dir %_datadir/apps/deKorator/themes/Azenis-theme/buttons/hover
%dir %_datadir/apps/deKorator/themes/Azenis-theme/buttons/normal
%dir %_datadir/apps/deKorator/themes/Azenis-theme/buttons/press
%_datadir/apps/deKorator/themes/Azenis-theme/masks/*
%_datadir/apps/deKorator/themes/Azenis-theme/deco/*
%_datadir/apps/deKorator/themes/Azenis-theme/buttons/*.png
%_datadir/apps/deKorator/themes/Azenis-theme/buttons/hover/*
%_datadir/apps/deKorator/themes/Azenis-theme/buttons/normal/*
%_datadir/apps/deKorator/themes/Azenis-theme/buttons/press/*

%files -n kde-styles-splash-azenis
%dir %_datadir/apps/ksplash/Themes/Azenis
%_datadir/apps/ksplash/Themes/Azenis/*

%files -n kde-styles-splash-azenis_sys
%dir %_datadir/apps/ksplash/Themes/Azenis_Sys
%_datadir/apps/ksplash/Themes/Azenis_Sys/*

%files -n x-cursor-theme-azenis
%dir %_datadir/icons/Azenis
%dir %_datadir/icons/Azenis/cursors
%_datadir/icons/Azenis/*.theme
%_datadir/icons/Azenis/cursors/*

%files -n azenis-fonts-ttf
%_datadir/fonts/default/TrueType-val/SAVEDBYZ.ttf

%files -n wallpapers-azenis
%dir %_datadir/wallpapers/Azenis
%_datadir/wallpapers/Azenis/*

%files -n kicker-themes-azenis
%_datadir/apps/kicker/wallpapers/*.png
%_datadir/apps/kicker/tiles/*.png

%files -n kde-colorscheme-azenis
%_datadir/apps/kdisplay/color-schemes/Azenis_Custom.kcsrc

%files -n %name-docs
%doc Azenis_Theme/HowTo.pdf Azenis_Theme/OpenOffice_Splash Azenis_Theme/SuperKaramba

%files -n %name-full

%changelog
* Mon Jan 17 2011 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt4
- build without kdm-themes-azenis

* Mon Oct 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt3
- fixed repocop warning (backup-file-in-package)

* Thu Sep 25 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt2
- fix unmet dependencies for %name-full

* Wed Sep 17 2008 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- initial build for ALT Linux
