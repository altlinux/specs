%define brand alt
%define Brand ALT
%define theme server-v
%define Theme Server-V
%define codename Actinoform
%define status %nil
%define status_en %nil
%define flavour %brand-%theme

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 1
%define design_graphics_abi_bugfix 0

%define data_cur_dir %_datadir/branding-data-current

%define _unpackaged_files_terminate_build 1

Name: branding-%flavour
Version: 10.1
Release: alt5
Url: https://basealt.ru

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
BuildRequires: design-bootloader-source >= 5.0-alt2
BuildRequires: cpio
%endif
BuildRequires: fonts-ttf-dejavu fonts-ttf-google-droid-sans

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc fribidi

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name ALT Virtualization Server %version%status_en
%define distro_name_ru Альт Сервер Виртуализации %version%status

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
Provides: design-bootloader-livecd-%theme = %EVR
Provides: design-bootloader-%theme = %EVR
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
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme = %EVR
Provides: branding-alt-%theme-browser-qt = %EVR
Provides: branding-altlinux-%theme-browser-qt = %EVR
Provides: alterator-icons design-alterator
Provides: design-alterator-%theme = %EVR

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop design-altertor-browser-server branding-altlinux-backup-server-alterator
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
В данном пакете находятся необходимые графические элементы для дистрибутива
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
BuildArch: noarch
Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPLv2+
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

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

#bootloader
%pre bootloader
%ifarch %ix86 x86_64
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
%endif
%ifarch %ix86 x86_64 aarch64
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:
%endif

%post bootloader
%ifarch %ix86 x86_64 aarch64
ln -snf %theme/message /boot/splash/message
LANG="C"
SYSTEMD_I18N="/etc/locale.conf"
SYSV_I18N="/etc/sysconfig/i18n"
if [ -f "$SYSTEMD_I18N" ] ; then
    . $SYSTEMD_I18N
elif [ -f "$SYSV_I18N" ] ; then
    . $SYSV_I18N
fi
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
%endif

%ifarch %ix86 x86_64 aarch64
%preun bootloader
[ "$1" -eq 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    rm -f /boot/splash/message
%endif

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
%endif
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
[ "$1" -eq 1 ] || exit 0
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

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
* Fri Feb 03 2023 Andrew A. Vasilyev <andy@altlinux.org> 10.1-alt5
- new slides from annaos@basealt.ru

* Wed Nov 09 2022 Andrew A. Vasilyev <andy@altlinux.org> 10.1-alt4
- import contents of indexhtml from Alexey Osotov

* Tue May 17 2022 Alexey Shabalin <shaba@altlinux.org> 10.1-alt3
- not provides /etc/os-release

* Wed Mar 30 2022 Andrew A. Vasilyev <andy@altlinux.org> 10.1-alt2
- use locale.conf if systemd installed, no dependency on startup package

* Tue Mar 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 10.1-alt1
- version 10.1

* Sat Nov 20 2021 Alexey Shabalin <shaba@altlinux.org> 10-alt1
- release up

* Fri Nov 12 2021 Alexey Shabalin <shaba@altlinux.org> 10-alt0.3
- add slideshow

* Tue Oct 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 10-alt0.2
- colors and styles from Workstation and Education

* Mon Oct 25 2021 Alexey Shabalin <shaba@altlinux.org> 10-alt0.1
- version 10

* Mon Aug 02 2021 Alexey Shabalin <shaba@altlinux.org> 9.2-alt2
- Revert "Don't change license and *-release files during update"
- indexhtml: update copyright years
- Do not obsolete packages itself without version
- Increase alternative version of design-current and design-browser-qt
  for resolve duplicate provides

* Tue May 18 2021 Andrew A. Vasilyev <andy@altlinux.org> 9.2-alt1
- version 9.2

* Wed Oct 14 2020 Alexey Shabalin <shaba@altlinux.org> 9.1-alt3
- define codename as Altostratus

* Wed Sep 16 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.1-alt2
- fix "the package obsoletes itself" error

* Wed May 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.1-alt1
- version 9.1

* Tue Mar 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0-alt4
- minimize buttons border

* Mon Mar 16 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0-alt3
- AWizardFace QPushButton min-width

* Thu Dec 12 2019 Alexey Shabalin <shaba@altlinux.org> 9.0-alt2
- en: Server Virtualization -> Virtualization Server

* Fri Dec 06 2019 Alexey Shabalin <shaba@altlinux.org> 9.0-alt1
- initial build as server-v flavour (based on server)

