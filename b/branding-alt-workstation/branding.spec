%define brand alt
%define Brand ALT
%define theme workstation
%define Theme Workstation
%define codename unknown
%define status alpha
%define status_en alpha
%define flavour %brand-%theme

%define gtk_theme BlueMenta
%define icon_theme Papirus

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

#alterantives weights
%define alterator_browser_weight 53
%define artworks_weight 000012000053

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 10.900
Release: alt1
Url: https://basealt.ru

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

# for licenses
BuildRequires: distro-licenses

BuildRequires: ImageMagick fontconfig bc

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_version %version

%define distro_base_name ALT Workstation
%define distro_base_name_ru Альт Рабочая станция

%define distro_name %distro_base_name %distro_version%status_en
%define distro_name_ru %distro_base_name_ru %distro_version%status

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux) 
License: GPLv2+

Requires(pre):    coreutils
Provides:  design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme
%branding_add_conflicts %flavour bootloader

%define grub_normal white/dark-gray
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo for %distro_name.
Suitable for both lilo and syslinux.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (lilo и syslinux) 
для дистрибутива %distro_name_ru.

%package bootsplash
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
BuildArch: noarch
Provides: plymouth-theme-%theme
Requires: plymouth
Requires: plymouth-theme-bgrt-alt
Requires: plymouth-plugin-label
Requires: fonts-ttf-dejavu


%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process for %distro_name
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива
%distro_name_ru.

%package alterator
Summary: Design for alterator for %distro_name
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива %distro_name_ru
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt 

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-altlinux-backup-server-alterator
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %distro_name.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива %distro_name_ru.

%package graphics
Summary: Design for %distro_name
Summary(ru_RU.UTF-8): Тема для дистрибутива %distro_name_ru
License: Different licenses
Group: Graphics
BuildArch: noarch
Provides: design-graphics-%theme
Obsoletes: design-graphics-%theme
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPLv2+
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Requires: pam-limits-desktop
Requires: alt-os-release

%description release
%distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %distro_name_ru
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes
Conflicts: alt-notes-school-server

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %distro_name_ru.

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: dconf
# Specified themes
Requires: icon-theme-ePapirus
Requires: icon-theme-Papirus
Requires: icon-theme-Papirus-Dark
Requires: icon-theme-Papirus-Light
Requires: mate-themes
Requires: theme-mate-windows
Requires: x-cursor-theme-jimmac
#
%branding_add_conflicts %flavour mate-settings
%branding_add_conflicts %flavour graphics
Requires(post): lightdm-gtk-greeter
Requires(post): libgio
# To avoid install check conflicts
Requires: %name-graphics = %EVR
Conflicts: installer-feature-lightdm-stage3 < 0.1.0-alt1
# Due to /usr/share/install3/lightdm-gtk-greeter.conf
Conflicts: branding-simply-linux-system-settings
Conflicts: lxde-settings-lxdesktop < 0.3.2-alt2

%description mate-settings
MATE settings for %distro_name

%package slideshow
Summary: Slideshow for %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %distro_name_ru
License: Distributable
Group: System/Configuration/Other 
BuildArch: noarch
%branding_add_conflicts %flavour slideshow

%description slideshow
Slideshow for %distro_name installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике 
дистрибутива %distro_name_ru.

%package indexhtml
BuildArch: noarch
Summary:  HTML welcome page for %distro_name
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива %distro_name_ru
License:  distributable
Group:    System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop
%branding_add_conflicts %flavour indexhtml

Requires: xdg-utils
Requires: docs-alt-%theme
Requires: shared-desktop-icons
Requires: menu-icons-default
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%prep
%setup -n branding
%ifarch %e2k
# cf. rm#115880
sed -i 's,#alt-workstation,&-e2k,' indexhtml/index-*.html.in
%endif

cp -a /usr/share/distro-licenses/ALT_Product_License/license.ru.html.in notes/
cp -a /usr/share/distro-licenses/ALT_Product_License/license.all.html.in notes/

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%distro_version PRODUCT_BASE_NAME_RU='%distro_base_name_ru' PRODUCT_BASE_NAME='%distro_base_name' PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' GTK_THEME='%gtk_theme' ICON_THEME='%icon_theme' ALTERATOR_BROWSER_WEIGHT=%alterator_browser_weight ARTWORKS_WEIGHT='%artworks_weight' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

%post bootloader
[ "$1" -eq 1 ] || exit 0
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
if [ "$1" -eq 1 ]; then
	subst "s/Theme=.*/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf
else
	subst "s/Theme=workstation/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf
fi

%post mate-settings
[ "$1" -eq 1 ] || exit 0
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
#_iconsdir/hicolor/*/apps/alt-%theme.png

%files bootsplash

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files mate-settings
%_sysconfdir/skel/.config/
%_sysconfdir/skel/.gtkrc-2.0
%_datadir/glib-2.0/schemas/*.gschema.override
%_datadir/install3/*

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%changelog
* Wed Sep 18 2024 Mikhail Efremov <sem@altlinux.org> 10.900-alt1
- release: Set codename to unknown.
- indexhtml: Update "Software Repository" link.
- indexhtml: Use English page for "Software Repository" link.
- indexhtml: Fix links.
- bootsplash: Use bgrt-alt plymouth theme.
- build: Replace convert with magick.
- bootloader: Drop gfxboot support.
- Set status to alpha.

* Wed Feb 14 2024 Mikhail Efremov <sem@altlinux.org> 10.2-alt1
- slideshow: Fix Telegram link.
- indexhtml: Fix Telegram link.
- indexhtml: Add mail lists link.

* Tue Dec 26 2023 Mikhail Efremov <sem@altlinux.org> 10.1.990-alt1
- all: Bump distro version to 10.1.990.

* Mon Dec 04 2023 Mikhail Efremov <sem@altlinux.org> 10.1.900-alt1
- mate-settings: Don't use user background in the lightdm-gtk-greeter.
- notes: Always update licenses.
- notes: Use licenses from distro-licenses package.

* Thu Nov 02 2023 Michael Shigorin <mike@altlinux.org> 10.1-alt4.1
- E2K: link to platform-specific distribution manual (rm#115880)

* Tue Dec 20 2022 Mikhail Efremov <sem@altlinux.org> 10.1-alt4
- all: Bump distro version to 10.1

* Tue Dec 13 2022 Mikhail Efremov <sem@altlinux.org> 10.1-alt3
- all: Set distro version to 10.0.920.
- indexhtml: Substitute product base name.
- indexhtml: Update index.html page.
- Drop fake changelog entry.

* Thu Oct 06 2022 Mikhail Efremov <sem@altlinux.org> 10.1-alt2
- Add fake changelog entry and bump release.
- alterator: Add logo_48.png to browser-qt rcc.
- notes: Use https everywhere.
- indexhtml: Fix bugzilla.altllinux.org link.
- indexhtml: Use https everywhere.

* Wed Aug 17 2022 Mikhail Efremov <sem@altlinux.org> 10.0.910-alt1
- slideshow: Replace broken Youtube QR-code with Yandex.Zen.
- bootsplash: more narrow and short progressbar (by Andrey Cherepanov).
- indexhtml: Fix background colour for distro name.
- indexhtml: Show distro name on index.html.
- indexhtml: Update social networks banners (closes: #43552).

* Wed Jul 13 2022 Mikhail Efremov <sem@altlinux.org> 10.0.900-alt1
- indexhtml: Fix basealt.ru links.
- indexhtml: Add Yandex.Zen link.
- indexhtml: Drop Facebook link.
- Lighten the background of list boxes (closes: 41514) (by Paul Wolneykien).
- Fix: Don't specify extra horizontal margins for inputs in
  alterator-listbox tables (by Paul Wolneykien).
- Fix: Don't restrict the width of the top panel buttons (by Paul Wolneykien).

* Mon Dec 06 2021 Mikhail Efremov <sem@altlinux.org> 10.0-alt2
- bootloader: Fix grub colors.
- bootsplash: Don't set GRUB_WALLPAPER.

* Thu Dec 02 2021 Mikhail Efremov <sem@altlinux.org> 10.0-alt1
- Bump version.

* Thu Nov 18 2021 Mikhail Efremov <sem@altlinux.org> 9.990-alt1
- indexhtml: Year auto-substitution (by Anton V. Boyarshinov).
- slideshow: Fix English slide 14.

* Thu Nov 11 2021 Mikhail Efremov <sem@altlinux.org> 9.930-alt1
- slideshow: Add English slides.
- slideshow: Update Russian slides.

* Tue Oct 26 2021 Mikhail Efremov <sem@altlinux.org> 9.920-alt1
- slideshow: Create empty Slides-en directory if needed.
- slideshow: Drop old p9 English slides.
- alterator: Add icons from Education 10.
- slideshow: Update Russian slideshow for WS10.
- alterator: Set black labels and titles.
- bootloader: Update grub colors.
- bootloader: Update gfxboot colors.
- mate-settings: Don't conflict with lxde-settings-lxdesktop >=
  0.3.2-alt2.
- alterator: fix alterator-browser-qt theme: bold selection and
  group, darkorange for progressbar (by Andrey Cherepanov).
- alterator: adapt css for brand colors (by Andrey Cherepanov).
- alterator: Add help button.
- alterator: Update theme.
- release: Fix /etc/*-release files packaging.

* Wed Oct 13 2021 Mikhail Efremov <sem@altlinux.org> 9.911-alt2
- notes: Add conflict with alt-notes-school-server.
- mate-settings: Add conflict with lxde-settings-lxdesktop.

* Wed Oct 06 2021 Mikhail Efremov <sem@altlinux.org> 9.911-alt1
- bootsplash: New progressbar from alt-education.

* Tue Oct 05 2021 Mikhail Efremov <sem@altlinux.org> 9.910-alt1
- Drop alpha status.
- Update images.
- Update progressbar.
- os-release.in: Add BUILD_ID.
- Package /etc/altlinux-release again.
- Package /usr/lib/os-relese.
- Set codename Autolycus.

* Thu Sep 23 2021 Mikhail Efremov <sem@altlinux.org> 9.900-alt1
- Set status to alpha.
- Set codename to unknown.
- Bump version.

* Tue Jul 27 2021 Mikhail Efremov <sem@altlinux.org> 9.2-alt1
- Bump version.

* Thu Jul 15 2021 Mikhail Efremov <sem@altlinux.org> 9.1.991-alt1
- Bump version.

* Tue Jun 29 2021 Mikhail Efremov <sem@altlinux.org> 9.1.990-alt1
- Bump version.

* Thu Jun 10 2021 Mikhail Efremov <sem@altlinux.org> 9.1.910-alt1
- Bump version.

* Tue May 25 2021 Mikhail Efremov <sem@altlinux.org> 9.1.900-alt1
- graphics: Fix duplicate alternatives.
- mate-settings: Conflict with branding-simply-linux-system-settings.
- alterator: Fix duplicate alternatives.

* Mon Nov 23 2020 Mikhail Efremov <sem@altlinux.org> 9.1-alt2
- bootloader,graphics,release: Drop self provides/obsoletes.
- alterator,release: Fix license tag.

* Fri Jul 17 2020 Mikhail Efremov <sem@altlinux.org> 9.1-alt1
- Bump version.

* Thu Jul 02 2020 Mikhail Efremov <sem@altlinux.org> 9.0.990-alt1
- Bump version.

* Wed Jun 10 2020 Mikhail Efremov <sem@altlinux.org> 9.0.920-alt1
- Use getalt.org as download link.

* Thu Jun 04 2020 Mikhail Efremov <sem@altlinux.org> 9.0.910-alt1
- Bump version.

* Wed Apr 29 2020 Mikhail Efremov <sem@altlinux.org> 9.0.900-alt1
- mate-settings: Drop gksu.

* Fri Oct 18 2019 Mikhail Efremov <sem@altlinux.org> 9.0-alt1
- Drop redundant empty %%description section.
- bootloader: Fix %%preun script.
- mate-settings: Add keyboard layout and full date to LightDM.
- mate-settings: Don't touch lightdm-gtk-greeter.conf at all.
- mate-settings: Get rid of gnome-settings.
- cleanup: Don't use internal rpm macros.
- all: Don't touch config files during package update.
- BR: Drop libGConf-devel.
- BR: Require fribidi on x86 only.
- bootsplash,bootloader: Package grub and plymouth themes on
  all arches.
- build: Install grub and plymouth themes on all arches.
- mate-settings: Use BlueMenta theme.
- Use design-bootloader-source on x86 only.

* Wed Oct 02 2019 Mikhail Efremov <sem@altlinux.org> 8.991-alt1
- Bump version.

* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 8.990-alt2
- Rename slides/ -> Slides/.

* Fri Sep 13 2019 Mikhail Efremov <sem@altlinux.org> 8.990-alt1
- Add English slides for ALT Workstation 9.
- Add Russian slides for ALT Workstation 9.

* Fri Aug 09 2019 Mikhail Efremov <sem@altlinux.org> 8.940-alt1
- Bump version.

* Fri Jul 26 2019 Andrey Cherepanov <cas@altlinux.org> 8.920-alt2
- Set for installer widescreen background.
- Use common icon with BaseALT logo for indexhtml.
- Make progressbar label brighter.

* Thu Jul 11 2019 Mikhail Efremov <sem@altlinux.org> 8.920-alt1
- Set codename Laertes.
- mate-settings: Use theme-mate-windows.

* Thu Jul 04 2019 Mikhail Efremov <sem@altlinux.org> 8.910-alt1
- mate-settings: Use TraditionalOk theme.
- mate-setting: Don't use non-existent window theme.
- notes: Replace license.all.html.in with English page.

* Tue Jun 18 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt2
- mate-settings: Require graphics subpackage.
- mate-settings: Add conflicts with *-graphics subpackages.

* Wed Jun 05 2019 Mikhail Efremov <sem@altlinux.org> 8.900-alt1
- mate-settings: Package all files in /etc/skel/.
- Don't try to install non-existent icons.
- Drop alt-education-*.png icons.
- Use BaseALT logo in the alterator web interface.
- mate-settings: Package Trolltech.conf.
- Drop menu subpackage.
- Drop system-settings subpackage.
- Drop {kde4,xfce,fvwm}-settings.
- Use _unpackaged_files_terminate_build.
- Don't change license and *-release files during update.
- Change spec for ALT Workstation.
- Update images for Workstation.

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 8.90-alt1
- Alpha version of ALT Education 9.0.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.2
- Add Droid fonts used in XFCE.
- Remove overrided desktop file for system-config-printer.
- Fix menu on window key.
- Add xfce4-clipman.desktop.
- Replace standard XFCE menu by Whisker menu, mixer plugin by pulseaudio plugin.
- Simplify panel in XFCE.
- Remove Simply Linux logo and wallpapers.

* Fri May 12 2017 Andrey Cherepanov <cas@altlinux.org> 8.2-alt0.M80P.1
- New release
- Use pam-limits-desktop instead of own limits rules
- Remove altlinux.ru from files

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 8.1-alt0.M80P.1
- Increase release number

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.5.M80P.1
- Complete Russian localization of menu
- Update indexhtml: fix URLs of official site sections URL and books location

* Mon Sep 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.4.M80P.1
- Use bright Education icon suitable both for light and dark backgrounds
- Rename kde4-settings to kde-settings, package Konsole profile and
  disable nm-applet.desktop autostart in KDE

* Tue Aug 30 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.3.M80P.1
- Set yellow labels for gfxboot
- Use predefined boot.png with logo for grub
- Set bright color for menubar in grub

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.2.M80P.1
- Do not require polkit-gnome
- Set SimpleSL icon theme in XFCE settings

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.2
- Rebuild with conflict with branding-xalt-kworkstation

* Fri Jul 22 2016 Andrey Cherepanov <cas@altlinux.org> 8.0-alt0.1.M80P.1
- Initial build
