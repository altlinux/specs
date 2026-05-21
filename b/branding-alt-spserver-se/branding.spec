%define brand alt
%define Brand ALT
%define theme spserver-se
%define Theme SP Server
# NB: it'd be not noarch anymore on a shared girar instance
#ifarch %e2k
#define LKNV 11102-01
#else
%define LKNV 11103-01
#endif
%define altbranch %_priority_distbranch
%define status %nil
%define status_en ALPHA
%define flavour %brand-%theme

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 11.0
Release: alt0.50
URL: https://altsp.su

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt6-base-devel

BuildRequires: ImageMagick fontconfig bc

BuildRequires: distro-licenses >= 1.3.2

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-2.0-or-later

%define distro_name SP Server
%define Brand_ru Альт 
%define distro_name_ru СП Сервер

%description
Distro-specific packages with design and texts for %Brand %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %Brand_ru %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (grub2)
BuildArch: noarch
License: GPL-2.0-or-later

Requires(pre):    coreutils
Provides:  design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme
%branding_add_conflicts %flavour bootloader

%define grub_normal white/black
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo for %Brand %distro_name.
Suitable for both grub2.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (grub2)
для дистрибутива %Brand_ru %distro_name_ru.

%package bootsplash
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %Brand_ru %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
BuildArch: noarch
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
Requires: plymouth-theme-bgrt-alt
Requires(pre):   plymouth

%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process for %Brand %distro_name
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива
%Brand_ru %distro_name_ru.

%package alterator
Summary: Design for alterator for %Brand %distro_name
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива %Brand_ru %distro_name_ru
License: GPL-2.0-or-later
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt 

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-altlinux-backup-server-alterator
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for  %Brand %distro_name.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива %Brand_ru %distro_name_ru.

%package graphics
Summary: Design for %Brand %distro_name
Summary(ru_RU.UTF-8): Тема для дистрибутива %Brand_ru %distro_name_ru
License: Different licenses
Group: Graphics
BuildArch: noarch
Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  design-graphics-%theme
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
This package contains some graphics for %Brand %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%Brand_ru %distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary: %Brand %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %Brand_ru %distro_name_ru
License:  GPL-2.0-or-later
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list
%branding_add_conflicts %flavour release
Conflicts: altlinux-release-sisyphus altlinux-release-p9 altlinux-release-p10
Requires: alt-os-release

%description release
%Brand %distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %Brand_ru %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %Brand_ru %distro_name_ru
License:   Distributable
Group:     Documentation
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %Brand_ru %distro_name_ru.

%package slideshow
Summary: Slideshow for %Brand %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %Brand_ru %distro_name_ru
License: Distributable
Group: System/Configuration/Other 
BuildArch: noarch
%branding_add_conflicts %flavour slideshow

%description slideshow
Slideshow for %Brand %distro_name installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике 
дистрибутива %Brand_ru %distro_name_ru.

%package indexhtml
BuildArch: noarch
Summary:  HTML welcome page for %Brand %distro_name
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива %Brand_ru %distro_name_ru
License:  distributable
Group:    System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop
%branding_add_conflicts %flavour indexhtml

Requires(post): indexhtml-common

%description indexhtml
%Brand %distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%Brand_ru %distro_name_ru.

%prep
%setup -n branding
cp /usr/share/distro-licenses/ALT_SP_License/license.{all,ru}.html.in notes/

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND='%Brand' BRAND_RU='%Brand_ru' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' LKNV='%LKNV' BRANCH='%altbranch' ./configure
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
subst "s/Theme=.*/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf

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
#_datadir/plymouth/themes/%theme/*
#_pixmapsdir/system-logo.png

%files release
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%dir %data_cur_dir
%data_cur_dir/alt-notes
%exclude %_datadir/alt-notes/livecd-*
%_datadir/alt-notes/release-notes.*
%ghost %config(noreplace) %_datadir/alt-notes/license.*.html

%files slideshow
%_sysconfdir/alterator/slideshow.conf
%_datadir/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*
%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%changelog
* Thu May 21 2026 Anton Midyukov <antohami@altlinux.org> 11.0-alt0.50
- Initial new branding from alt-sp-server.
