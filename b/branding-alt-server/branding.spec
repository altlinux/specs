%define brand alt
%define Brand ALT
%define theme server
%define Theme Server
%define codename Mendelevium
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%def_enable flickfree

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 11.0
Release: alt6
Url: https://basealt.ru

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc
BuildRequires: distro-licenses >= 1.3.1

%if "%status" != "%nil" || "%status_en" != "%nil"
BuildRequires: fonts-ttf-dejavu
%endif

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name ALT Server %version%status_en
%define distro_name_ru Альт Сервер %version%status

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
Provides: design-bootloader-system-%theme = %EVR
Provides: design-bootloader-livecd-%theme = %EVR
Provides: design-bootloader-%theme = %EVR
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme
%branding_add_conflicts %flavour bootloader

%define grub_normal white/light-blue
%define grub_high black/light-gray

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
Provides: plymouth-theme-%theme = %EVR
%if_enabled flickfree
%define plymouth_theme bgrt-alt
Requires: plymouth-theme-bgrt-alt
%else
%define plymouth_theme %theme
%endif
Requires: plymouth-plugin-script
Requires(pre):   plymouth

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
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Provides: branding-alt-%theme-browser-qt = %EVR
Provides: branding-altlinux-%theme-browser-qt = %EVR
Provides: alterator-icons design-alterator
Provides: design-alterator-%theme = %EVR
Provides: design-alterator-browser-%theme = %EVR

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
Provides: design-graphics-%theme = %EVR
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
License:  GPL
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme = %EVR
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
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
%branding_add_conflicts %flavour mate-settings
%branding_add_conflicts %flavour graphics
Requires(post): lightdm-gtk-greeter
# To avoid install check conflicts
Requires: %name-graphics = %EVR
Conflicts: installer-feature-lightdm-stage3 < 0.1.0-alt1
# Due to /usr/share/install3/lightdm-gtk-greeter.conf
Conflicts: branding-simply-linux-system-settings
Conflicts: branding-alt-workstation-mate-settings
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

Requires: docs-alt-%theme
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%prep
%setup -n branding
cp /usr/share/distro-licenses/ALT_Server_License/license.{all,ru}.html.in notes/
%ifarch %e2k
# cf. rm#115880
sed -i 's,#alt-server,&-e2k,' indexhtml/index-*.html.in
%endif

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

mkdir -p %buildroot/%_datadir/install3
install mate-settings/lightdm-gtk-greeter.conf %buildroot/%_datadir/install3/lightdm-gtk-greeter.conf
mkdir -p %buildroot/%_datadir/mate-menu
install mate-settings/applications.list-themed %buildroot/%_datadir/mate-menu/applications.list-themed

#graphics
mkdir -p %buildroot/%_datadir/design/%theme
cp -a images/product-logo.png %buildroot/%_datadir/design/%theme/icons/system-logo.png

#bootloader
%ifarch %ix86 x86_64
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:
%endif

%post bootloader
[ "$1" -eq 1 ] || exit 0
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
%if_enabled flickfree
shell_config_del /etc/sysconfig/grub2 GRUB_THEME
%else
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
%endif

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
[ "$1" -eq 1 ] || exit 0
sed -i "s/Theme=.*/Theme=%plymouth_theme/" /etc/plymouth/plymouthd.conf ||:

#notes
%post notes
if ! [ -e %_datadir/alt-notes/license.all.html ]; then
	cp -a %data_cur_dir/alt-notes/license.*.html %_datadir/alt-notes/
fi

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
#_iconsdir/hicolor/*/apps/alt-%theme.png

%files bootsplash
%_datadir/plymouth/themes/%theme/*
%_pixmapsdir/system-logo.png

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%_datadir/alt-notes/livecd-*
%_datadir/alt-notes/release-notes.*
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

%files mate-settings
%_datadir/install3/lightdm-gtk-greeter.conf
%_datadir/mate-menu/applications.list-themed

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
* Thu Sep 26 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt6
- Stretch background image to entire installer window

* Tue Sep 24 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt5
- Change images to p11

* Thu Jul 25 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt4
- Add Chromium to the "Favorites" menu item

* Tue Jul 23 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt3
- Use bgrt-alt theme for plymouth (Closes: 41591)

* Thu Jul 18 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt2
- Add font for STATUS string

* Wed Jul 17 2024 Dmitry Terekhin <jqt4@altlinux.org> 11.0-alt1
- Add STATUS string to wallpaper
- Remove bootsplash and gfxboot

* Thu Feb 29 2024 Dmitry Terekhin <jqt4@altlinux.org> 10.2-alt3
- Fix different sizes of GUI elements (rm#125458 rm#125847)

* Thu Nov 02 2023 Michael Shigorin <mike@altlinux.org> 10.2-alt2.1
- E2K: link to platform-specific distribution manual (rm#115880)

* Thu Sep 28 2023 Dmitry Terekhin <jqt4@altlinux.org> 10.2-alt2
- updated licenses from distro-licenses
- use Basealt logo as a "steps list" button

* Tue Sep 19 2023 Dmitry Terekhin <jqt4@altlinux.org> 10.2-alt1
- update indexhtml URLs

* Tue Aug 29 2023 Dmitry Terekhin <jqt4@altlinux.org> 10.1-alt7
- copy licenses from distro-licenses

* Mon Aug 28 2023 Dmitry Terekhin <jqt4@altlinux.org> 10.1-alt6
- use the Basealt LLC logo for About system

* Thu Jan 19 2023 Dmitry Terekhin <jqt4@altlinux.org> 10.1-alt5
- update year for copyright to 2023
- set codename to Mendelevium

* Tue Nov 08 2022 Dmitry Terekhin <jqt4@altlinux.org> 10.1-alt4
- import contents of indexhtml from Alexey Osotov

* Mon Jun 27 2022 Dmitry Terekhin <jqt4@altlinux.org> 10.1-alt3
- add /usr/share/install3/lightdm-gtk-greeter.conf
  to change the keyboard layout in greeter
- remove wrong web links

* Tue May 17 2022 Alexey Shabalin <shaba@altlinux.org> 10.1-alt2
- add /etc/altlinux-release to package (fixed ALT#41741).
- update Provides.

* Tue Apr 19 2022 Paul Wolneykien <manowar@altlinux.org> 10.1-alt1
- Lighten the background of list boxes (closes: 41514).
- Fix: Don't specify extra horizontal margins for inputs in
  alterator-listbox tables.
- Fix: Don't restrict the width of the top panel buttons.

* Tue Nov 16 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 10.0-alt2
- year auto-substitution in (c)

* Mon Nov 15 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 10.0-alt1
- release up

* Fri Oct 29 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 10.0-alt0.3
- colors changed

* Fri Oct 15 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 10.0-alt0.2
- images and bootsplash fixed

* Thu Sep 16 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 10.0-alt0.1
- images and bootsplash changed

* Wed Mar 17 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.2-alt1
- version bump
- 'Next' button size fixed

* Thu Feb 11 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.1-alt4
- alternatives priorities changed

* Thu Jul  9 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.1-alt3
- product version fixed

* Tue Jun 23 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.1-alt2
- reduced black border for focused buttons

* Tue May 26 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.1-alt1
- version bump

* Thu Nov 14 2019 Alexey Shabalin <shaba@altlinux.org> 9.0-alt2
- sync spec with branding-alt-workstation
- Package system-logo.png for Plymouth
- add black border for focused buttons

* Thu Oct 17 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 9.0-alt1
- version set to 9.0

* Thu Sep  5 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.99-alt1
- dependence on xdg-utils in indexhtml removed

* Fri Aug 16 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.98-alt1
- unset "beta" status

* Tue Jul 23 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.95-alt1
- set status to beta

* Wed Jul 10 2019 Alexey Shabalin <shaba@altlinux.org> 8.91-alt1
- Replace license.all.html.in with English page
- Put status banner to NorthEast

* Fri Jun 14 2019 Alexey Shabalin <shaba@altlinux.org> 8.90-alt3
- update background4x3 with logo

* Thu Jun 13 2019 Alexey Shabalin <shaba@altlinux.org> 8.90-alt2
- Do not requires pam-limits-desktop (fixed ATL#36875)
- Drop settings for WM

* Wed May 29 2019 Alexey Shabalin <shaba@altlinux.org> 8.90-alt1
- Alpha version of ALT Server 9.0 (based on Education by cas@).

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
