%global _unpackaged_files_terminate_build 1

%define brand uzguard
%define Brand Uzguard
%define theme workstation
%define Theme Workstation
%define codename %nil
%define status alpha
%define status_en alpha
%define flavour %brand-%theme

%define gtk_theme Breeze-Education
%define kde_theme Breeze
%define icon_theme Papirus-Edu
%define window_theme Smoothwall-Breeze

# Enable compositing on ix86 and x86_64 only
%ifarch %ix86 x86_64
%define xfwm4_compositing true
%else
%define xfwm4_compositing false
%endif

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 1
%define design_graphics_abi_bugfix 0

Name: branding-%flavour
Version: 1.0
Release: alt0.2

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
BuildRequires: design-bootloader-source >= 7.3-alt1
BuildRequires: cpio
%endif

BuildRequires(pre): rpm-macros-branding
BuildRequires: libalternatives-devel
BuildRequires: qt5-base-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel fribidi

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-2.0+

%define distro_name Uzguard OS Workstation Idora %version%status_en
%define distro_name_ru Uzguard OS Workstation Idora %version%status_en
%define distro_logo uzguard-workstation-desktop

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux)
License: GPL-2.0

Requires(pre): coreutils
Provides:  design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
%branding_add_conflicts %flavour bootloader

%define grub_normal light-gray/black
%define grub_high white/dark-gray

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
Provides: plymouth-theme-%theme
Requires: plymouth-theme-bgrt-alt
Requires: plymouth-plugin-script
Requires: plymouth-plugin-label
Requires: fonts-ttf-dejavu
Requires(pre): plymouth

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
Requires: fonts-ttf-roboto

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
Provides: design-graphics-%theme
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
License:  Distributable
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
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

%package kde-settings
BuildArch: noarch
Summary: KDE settings for %distro_name (for KDE4 and KF5)
License: Distributable
Group:   Graphical desktop/KDE
Requires(pre): %name-graphics
Requires: %name-graphics = %EVR
Requires: kde5-konsole-colorscheme-SolarizedPastel
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
Requires: plasma5-breeze
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Requires: document-templates
Provides: branding-%flavour-kde4-settings = %version-%release
Obsoletes: branding-%flavour-kde4-settings < %version-%release
%branding_add_conflicts %flavour kde-settings
%branding_add_conflicts %flavour kde4-settings

%description kde-settings
KDE settings for %distro_name (for KDE4 and KF5)

%package xfce-settings
Summary: Default settings for XFCE for %distro_name
License: Distributable
Group: Graphical desktop/XFce
Requires: etcskel
Requires: fonts-ttf-liberation
Requires: fonts-ttf-google-droid-sans-mono
Requires: fonts-ttf-google-noto-sans
Requires: gnome-icon-theme
# Specified themes
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
Requires: xfwm4-theme-Smoothwall-Breeze
Requires(post): lightdm-gtk-greeter
# XFCE plugins
Requires: xfce4-whiskermenu-plugin
Requires: xfce4-pulseaudio-plugin
Requires: branding-%brand-%theme-graphics
Requires(pre): libgtk+2
%branding_add_conflicts %flavour xfce-settings

%description xfce-settings
XFCE settings for %distro_name

%package fvwm-settings
BuildArch: noarch
Summary: FVWM2 settings for %distro_name
License: Distributable
Group:   Graphical desktop/FVWM based
Requires: altlinux-freedesktop-menu-gnomish-menu
%branding_add_conflicts %flavour fvwm-settings

%description fvwm-settings
FVWM2 settings for %distro_name

%package mate-settings
BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: beesu
Requires: dconf
# Specified themes
Requires: papirus-icon-theme
Requires: gtk-theme-breeze-education
#
%branding_add_conflicts %flavour mate-settings
Requires(post): lightdm-gtk-greeter
Requires(post): libgio

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
%branding_add_conflicts %flavour indexhtml

Requires: xdg-utils
Requires: docs-alt-%theme
Requires: shared-desktop-icons
Requires(post): indexhtml-common

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%package menu
Summary: Menu for %distro_name
License: Distributable
Group: Graphical desktop/Other
Requires(pre): altlinux-freedesktop-menu-common
Requires: altlinux-freedesktop-menu-common
%branding_add_conflicts %flavour menu

%description menu
Menu for %distro_name

%package system-settings
BuildArch: noarch
Summary: Some system settings for %distro_name
License: GPL-2.0
Group: System/Base
# Really we need lightdm only, but it can pull another greeter.
Requires: lightdm-gtk-greeter
%branding_add_conflicts %flavour system-settings

%description system-settings
Some system settings for %distro_name.

%prep
%setup -n branding
%ifarch %e2k %ix86
# 2021: no chromium port available
grep -rl chromium xfce-settings/etcskel/.config/xfce4/panel |
	xargs -r -- sed -i 's,chromium,firefox,g;s,Chromium,Firefox,g'
%endif

%build
autoconf
THEME=%theme CTHEME=%Theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' PRODUCT_LOGO='%distro_logo' CODENAME='%codename' GTK_THEME='%gtk_theme' KDE_THEME='%kde_theme' ICON_THEME='%icon_theme' WINDOW_THEME='%window_theme' XFWM4_COMPOSITING='%xfwm4_compositing' ./configure
make

%install
%makeinstall

# Move os-release to /usr/lib
mkdir -p %buildroot%_libexecdir
mv %buildroot%_sysconfdir/os-release %buildroot%_libexecdir/os-release
touch %buildroot%_sysconfdir/os-release

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
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_del /etc/sysconfig/grub2 GRUB_THEME
shell_config_del /etc/sysconfig/grub2 GRUB_BACKGROUND
%endif

%ifarch %ix86 x86_64 aarch64
%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message
%endif

%post indexhtml
%_sbindir/indexhtml-update

%post system-settings
#chown _ldm:_ldm %_localstatedir/ldm/.pam_environment
sed -i '/pam_env\.so/ {
		/user_readenv/ b
		s/pam_env\.so/pam_env.so user_readenv=1/ }
' %_sysconfdir/pam.d/lightdm-greeter

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
/boot/splash/%theme
%endif
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
%ifarch %ix86 x86_64 aarch64
subst "s/Theme=.*/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf
%endif

%post mate-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

%post xfce-settings
subst 's/^#\?theme-name=.*/theme-name=%gtk_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?icon-theme-name=.*/icon-theme-name=%icon_theme/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?indicators=.*/indicators=~clock;~spacer;~host;~spacer;~session;~layout;~a11y;~power/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
subst 's/^#\?clock-format=.*/clock-format=%A, %x %H:%M/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
# Set gtk+2 theme for root too
grep -q '^gtk-theme-name' /etc/gtk-2.0/gtkrc || cat /etc/skel/.gtkrc-2.0 >> /etc/gtk-2.0/gtkrc

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*
%_sysconfdir/alterator/sysconfig/lang/langlist.ru_RU
%_sysconfdir/alterator/sysconfig/lang/langlist.uz_UZ

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
#_iconsdir/hicolor/*/apps/alt-%theme.svg

%files bootsplash
%_datadir/plymouth/themes/%theme/*
%_pixmapsdir/system-logo.png

%files release
%_sysconfdir/altlinux-release
%_sysconfdir/fedora-release
%_sysconfdir/redhat-release
%_sysconfdir/system-release
%ghost %_sysconfdir/os-release
%_libexecdir/os-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde-settings
%_datadir/kf5/konsole/%Theme.profile
/etc/skel/.config/autostart/nm-applet.desktop
/etc/skel/.config/k*
/etc/skel/.config/plasma*

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*.gschema.override

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
%exclude /etc/skel/.config/autostart/nm-applet.desktop
%exclude /etc/skel/.config/k*
%exclude /etc/skel/.config/plasma*
/etc/skel/.face
/etc/skel/.gconf
/etc/skel/.gtkrc-2.0
/etc/skel/.local
/etc/skel/.vimrc
/etc/skel/.recoll

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
#_iconsdir/hicolor/*/apps/alt-%theme-desktop.svg

%files menu
/usr/share/slinux-style
/etc/xdg/menus/applications-merged/50-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules
#config %_localstatedir/ldm/.pam_environment

%changelog
* Tue Apr 23 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.2
- kde-settings: make panel thinker and use all-application menubutton icon.
- menu: use computer icon for acc.
- alterator: package langlist for uz_UZ

* Mon Mar 25 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1
- New branding uzguard-workstation (alpha version).
