%define brand alt
%define Brand ALT
%define theme spserver
%define Theme SP Server
%define codename cliff
%define LKNV 11100-01
%define BRANCH $(rpm --eval %_priority_distbranch)
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 10.1
Release: alt2
Url: https://altsp.su

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name ALT SP Server
%define distro_name_ru Альт СП Сервер

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (grub2)
BuildArch: noarch
License: GPLv2+

Requires(pre):    coreutils
Provides:  design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme
%branding_add_conflicts %flavour bootloader

%define grub_normal white/black
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo for %distro_name.
Suitable for both grub2.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (grub2)
для дистрибутива %distro_name_ru.

%package bootsplash
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
BuildArch: noarch
Provides: plymouth-theme-%theme
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
Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  design-graphics-%theme
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
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Conflicts: altlinux-release-sisyphus altlinux-release-p9 altlinux-release-p10
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

Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' LKNV='%LKNV' BRANCH=%BRANCH ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

#bootloader
%post bootloader
[ "$1" -eq 1 ] || exit 0
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
shell_config_set /etc/sysconfig/grub2 GRUB_BACKGROUND ''
# deprecated
shell_config_set /etc/sysconfig/grub2 GRUB_WALLPAPER ''

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
[ "$1" -eq 1 ] || exit 0
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf

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
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%_datadir/alt-notes/livecd-*
%_datadir/alt-notes/release-notes.*
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

#%%files slideshow
#/etc/alterator/slideshow.conf
#/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%changelog
* Tue Jan 24 2023 Anton Midyukov <antohami@altlinux.org> 10.1-alt2
- disable gfxboot for syslinux and slideshow for installer
- bootloader subpackage noarch again
- cleanup unused images
- update images
- add LKNV to os-release
- define BRANCH from %%_priority_distbranch

* Fri Nov 11 2022 Anton Midyukov <antohami@altlinux.org> 10.1-alt1
- version bump
- replace distro_name 'ALT 8 SP Server' with 'ALT SP Server'
- save BUILD_ID in /etc/os-release with alt-os-release
- indexhtml: update for new release
- indexhtml: do not require docs-alt-spworkstation
- do not create symlinks on documentation

* Fri Sep 02 2022 Anton Midyukov <antohami@altlinux.org> 8.4-alt3
- update Conflicts for release
- set black-white colours for grub
- disable GRUB_BACKGROUND, GRUB_WALLPAPER

* Wed Sep 29 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.4-alt2
- color scheme in browser-qt fixed

* Tue Sep 21 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.4-alt1
- version bump
- os-release updating

* Tue Sep 14 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.3-alt2
- design changed

* Thu Jul 15 2021 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.3-alt1
- version bump
- build fixed

* Mon Oct 26 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.2-alt4
- 'Next' button look fixed

* Fri Sep 25 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.2-alt3
- licenses replaced from c8.1

* Wed May 20 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.2-alt2
- bootmenu bar color fixed

* Wed May 13 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.2-alt1
- spserver version based on alt-server

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
