%define brand etersoft
%define Brand Etersoft
%define theme ximper
%define Theme Ximper
%define codename Alice
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
Version: 0.8
Release: alt1
Url: https://ximperlinux.ru

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
BuildRequires: cpio fonts-ttf-dejavu fonts-otf-abattis-cantarell
BuildRequires: design-bootloader-source >= 5.0-alt2 fribidi
%endif

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%define distro_name Ximper Linux %version%status_en
%define distro_name_ru Ximper Linux %version%status

%description
Distro-specific packages for %distro_name.

%description -l ru_RU.UTF-8
Пакеты для дистрибутива %distro_name_ru.

%package apt-conf
BuildArch: noarch
Summary: A set of apt configuration files for %distro_name
License: GPL-2.0-or-later
Group: System/Configuration/Packaging

%branding_add_conflicts %flavour apt-conf
%description apt-conf
This package contains default apt configuration for %distro_name.

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
BuildArch: noarch
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme plymouth(system-theme)
%define plymouth_theme bgrt
Requires: plymouth-theme-bgrt
Requires: plymouth-plugin-script
Requires: plymouth-plugin-label
Requires: fonts-ttf-dejavu
Requires(pre,postun): plymouth

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
%branding_add_conflicts %flavour graphics

Requires(post,preun): alternatives >= 0.2


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

%package gnome-settings
BuildArch: noarch
Summary:   GNOME settings for %distro_name
License:   Distributable
Group:     Graphical desktop/GNOME
AutoReqProv: no
%branding_add_conflicts %flavour gnome-settings

%description gnome-settings
GNOME settings for %distro_name

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

%package backgrounds
Group: Graphics
Summary: Backgrounds for %distro_name
License: CC-BY-NC-SA-3.0+
BuildArch: noarch
%branding_add_conflicts %flavour backgrounds

%description backgrounds
This package contains backgrounds for %distro_name.


%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' ./configure
make

%install
%makeinstall
find %buildroot -name \*.in -delete

mkdir -p %buildroot/%_datadir/install3

#apt-conf
mkdir -p %buildroot%_sysconfdir/apt/sources.list.d
install ximper.list %buildroot%_sysconfdir/apt/sources.list.d/ximper.list


mkdir -p %buildroot/%_datadir/glib-2.0/schemas
install gnome-settings-gschema/ximper-linux.gschema.override %buildroot%_datadir/glib-2.0/schemas/ximper-linux.gschema.override

mkdir -p %buildroot%_sysconfdir/skel/.config/Kvantum
install  skel/skel/.config/Kvantum/kvantum.kvconfig %buildroot%_sysconfdir/skel/.config/Kvantum/kvantum.kvconfig

mkdir -p %buildroot%_sysconfdir/skel/.config/environment.d
install  skel/skel/.config/environment.d/qt.conf %buildroot%_sysconfdir/skel/.config/environment.d/qt.conf

install pixmaps/ximperlinux.svg %buildroot%_pixmapsdir/ximperlinux.svg

#backgrounds
install -pD -m644 -t %buildroot%_datadir/wallpapers/ximper/ ximperwallpapers/*
./imgtognome.sh %buildroot%_datadir/wallpapers/ximper/
mkdir -p %buildroot%_datadir/gnome-background-properties
mv %buildroot%_datadir/wallpapers/ximper/ximper.xml %buildroot%_datadir/gnome-background-properties/

#bootloader
%ifarch %ix86 x86_64
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:
%endif

%post bootloader
[ "$1" -eq 1 ] || exit 0
%ifarch %ix86 x86_64
ln -snf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
%endif
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%ifarch %ix86 x86_64
%preun bootloader
[ "$1" -eq 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    rm -f /boot/splash/message
%endif

#%post indexhtml
#%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
%endif
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
sed -i "s/Theme=.*/Theme=%plymouth_theme/" /etc/plymouth/plymouthd.conf ||:

#notes
%post notes
if ! [ -e %_datadir/alt-notes/license.all.html ]; then
	cp -a %data_cur_dir/alt-notes/license.*.html %_datadir/alt-notes/
fi

%post gnome-settings
glib-compile-schemas /usr/share/glib-2.0/schemas/

%files apt-conf
%config(noreplace) %_sysconfdir/apt/sources.list.d/ximper.list

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_pixmapsdir/ximperlinux.svg

%files backgrounds
%_datadir/wallpapers/ximper
%_datadir/gnome-background-properties/ximper.xml

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

%files gnome-settings
%_datadir/glib-2.0/schemas/ximper-linux.gschema.override
%_sysconfdir/skel/.config/environment.d/qt.conf
%_sysconfdir/skel/.config/Kvantum/kvantum.kvconfig

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
#%_desktopdir/*
#%_datadir/kf5/kio_desktop/DesktopLinks/indexhtml.desktop
#%attr(0755,root,root) %_datadir/Desktop/indexhtml.desktop
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.png

%changelog
* Wed Aug 30 2023 Roman Alifanov <ximper@altlinux.org> 0.8-alt1
- Initial build for Sisyphus. (Forked from branding-alt-server)
