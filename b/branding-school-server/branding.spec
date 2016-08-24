%define brand school
%define Brand School
%define theme server
%define Theme Server
%define codename Aquila chrysaetos
%define variants altlinux-backup-server altlinux-desktop altlinux-gnome-desktop altlinux-kdesktop altlinux-lite altlinux-lxdesktop altlinux-office-desktop altlinux-office-server altlinux-school-server altlinux-sisyphus altlinux-spt altlinux-tablet altlinux-workbench informika-schoolmaster ivk-chainmail lxde-desktop lxde-school-lite Platform6-server-light school-junior school-lite school-master school-server school-teacher school-terminal simply-linux sisyphus-server-light altlinux-centaurus
%define status %nil
%define status_en %nil
%define distro_name ALT Linux 7.0.5%status_en School Server
%define distro_name_ru Альт Линукс 7.0.5%status Школьный Сервер

%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Name: branding-%brand-%theme
Version: 7.0.5
Release: alt2
BuildArch: noarch

BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu fonts-ttf-google-droid-sans
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%description
Distro-specific packages with design and texts for %distro_name.

%description -l ru_RU.UTF-8
Пакеты оформления для дистрибутива %distro_name_ru.

%package bootloader
Group:   System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux) 
License: GPLv2+

PreReq:    coreutils
Provides:  design-bootloader-system-%brand-%theme design-bootloader-livecd-%brand-%theme design-bootloader-%brand-%theme branding-alt-%brand-%theme-bootloader
Obsoletes: design-bootloader-system-%brand-%theme design-bootloader-livecd-%brand-%theme design-bootloader-%brand-%theme branding-alt-%brand-%theme-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

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
Summary:  Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива %distro_name_ru
License:  Distributable
Group:    System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
PreReq:   plymouth

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootsplash ";done )

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
Provides: design-alterator-browser-%brand-%theme  branding-alt-%brand-%theme-browser-qt branding-altlinux-%brand-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%brand-%theme
Obsoletes:  branding-alt-%brand-%theme-browser-qt branding-altlinux-%brand-%theme-browser-qt

# lexicographically first of the village
Conflicts: branding-sisyphus-server-light-alterator

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-alterator ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-altlinux-backup-server-alterator
PreReq(post,preun): alternatives >= 0.2 alterator

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

Provides: design-graphics-%brand-%theme  branding-alt-%brand-%theme-graphics
Obsoletes:  branding-alt-%brand-%theme-graphics design-graphics-%brand-%theme
Provides: design-graphics = 12.0.0

PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )

%description graphics
This package contains some graphics for %distro_name design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
%distro_name_ru.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-5.0 altlinux-release-5.1 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary:  %distro_name release file
Summary(ru_RU.UTF-8): Описание дистрибутива %distro_name_ru
License:  GPL
Group:    System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%brand-%theme  branding-alt-%brand-%theme-release
Obsoletes: %obsolete_list  branding-alt-%brand-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distro_name release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание дистрибутива %distro_name_ru.

%package notes
BuildArch: noarch
Provides:  alt-license-theme = %version alt-notes-%brand-%theme
Obsoletes: alt-license-%brand-%theme alt-notes-%brand-%theme
Summary:   Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива %distro_name_ru
License:   Distributable
Group:     Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-office-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения
для дистрибутива %distro_name_ru.

%package kde4-settings
BuildArch: noarch
Summary: KDE4 settings for %distro_name
License: Distributable
Group:   Graphical desktop/KDE
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-kde4-settings ";done )
PreReq: %name-graphics

%description kde4-settings
KDE4 settings for %distro_name

%package fvwm-settings

BuildArch: noarch
Summary: FVWM2 settings for %distro_name
License: Distributable
Group:   Graphical desktop/FVWM based
Requires: altlinux-freedesktop-menu-gnomish-menu
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-fvwm-settings ";done )

%description fvwm-settings
FVWM2 settings for %distro_name

%package mate-settings

BuildArch: noarch
Summary: MATE settings for %distro_name
License: Distributable
Group:   Graphical desktop/GNOME
Requires: gksu
Requires: dconf
Requires: gtk3-theme-clearlooks-phenix
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )
PreReq(post): lightdm-gtk-greeter
PreReq(post): libgio

%description mate-settings
MATE settings for %distro_name

%package xfce-settings
Summary: default settings for Xfce 4.6 for %distro_name
License: Distributable
Group: Graphical desktop/XFce
Requires: PolicyKit-gnome
Requires: etcskel gtk3-theme-clearlooks-phenix
Requires: gnome-icon-theme icon-theme-simple-sl
Requires: branding-%brand-%theme-graphics
Obsoletes: xfce-settings-lite xfce-settings-school-lite
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-xfce-settings ";done )
Conflicts: xfce-settings-simply-linux

%description xfce-settings
This package contains default settings for Xfce 4.6 for %distro_name.

%package slideshow
Summary: Slideshow for %distro_name installer
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива %distro_name_ru
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )
BuildArch: noarch

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
Provides: indexhtml indexhtml-%brand-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server
Conflicts: branding-altlinux-backup-server-indexhtml

Requires: xdg-utils 
Requires: docs-school-server
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

%description menu
Menu for %distro_name

%package system-settings
Summary: Some system settings for Simply Linux
License: GPLv2+
Group: System/Base
# Really we need lightdm only, but it can pull another greeter.
Requires: lightdm-gtk-greeter

%description system-settings
Some system settings for Simply Linux.

%prep
%setup -n branding

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Brand %Theme' BRAND_FNAME='%brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME_RU='%distro_name_ru' PRODUCT_NAME='%distro_name' CODENAME='%codename' X86='%x86' ./configure
make

%install
%makeinstall

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
mkdir -p %buildroot/%_niconsdir
install graphics/icons/slinux.png %buildroot/%_niconsdir/slinux.png
install graphics/icons/mini/slinux.png %buildroot/%_iconsdir/altlinux.png
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd

install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
%_datadir/design/current	%_datadir/design/%theme	10
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%distro_name" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
install -pD -m644 components/systemd/os-release %buildroot%_sysconfdir/os-release

#notes
pushd notes
%makeinstall
popd
ln -s license.ru.html %buildroot%_datadir/alt-notes/license.uk.html

#kde4-settings
pushd kde4-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde4
cp -a kde4/* %buildroot%_sysconfdir/skel/.kde4/
popd

#fwvm-settings
mkdir -p %buildroot/etc/skel
install -m 644 fvwm-settings/.fvwm2rc %buildroot/etc/skel/

#mate-settings
pushd mate-settings
install -m 644 -D 50_mate-background.gschema.override '%buildroot%_datadir/glib-2.0/schemas/50_mate-background.gschema.override'
install -m 644 -D 60_mate-theme.gschema.override '%buildroot%_datadir/glib-2.0/schemas/60_mate-theme.gschema.override'
install -m 644 -D Trolltech.conf '%buildroot%_sysconfdir/skel/.config/Trolltech.conf'
popd

mkdir -p %buildroot/etc/skel/XDG-Templates.skel/

cp -r xfce-settings/etcskel/* %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.config %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.local %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.gconf %buildroot/etc/skel/
cp -r xfce-settings/etcskel/.vimrc %buildroot/etc/skel/

install -m 644 xfce-settings/etcskel/.wm-select %buildroot/etc/skel/

mkdir -p %buildroot/usr/share/backgrounds/xfce/
cp -P xfce-settings/backgrounds/*.{jpg,png} %buildroot/usr/share/backgrounds/xfce/

install -pDm0755 xfce-settings/scripts/zdg-move-templates.sh %buildroot%_sysconfdir/X11/profile.d/zdg-move-templates.sh

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
mkdir -p %buildroot/etc/alterator
cp -a slideshow/*  %buildroot/usr/share/install2/slideshow/
install slideshow/slideshow.conf %buildroot/etc/alterator/
# Set English slideshow as default
#ln -s slides-en %buildroot/usr/share/install2/slideshow/slides

#indexhtml
%define _altdocsdir %_defaultdocdir/alt-docs
%define _indexhtmldir %_defaultdocdir/indexhtml
install components/indexhtml/*.html %buildroot%_defaultdocdir/indexhtml/
mkdir -p %buildroot%_defaultdocdir/indexhtml/images
install components/indexhtml/images/* %buildroot%_defaultdocdir/indexhtml/images/
#install -m644 components/indexhtml.desktop %buildroot%_desktopdir/

#menu
mkdir -p %buildroot/usr/share/slinux-style/applications
install menu/applications/* %buildroot/usr/share/slinux-style/applications/
mkdir -p %buildroot/etc/xdg/menus/xfce-applications-merged
cp menu/50-xfce-applications.menu %buildroot/etc/xdg/menus/xfce-applications-merged/
mkdir -p %buildroot/usr/share/desktop-directories
cp menu/altlinux-wine.directory %buildroot/usr/share/desktop-directories/

# system-settings
mkdir -p %buildroot/%_sysconfdir/polkit-1/rules.d/
cp -a system-settings/polkit-rules/*.rules %buildroot/%_sysconfdir/polkit-1/rules.d/
#install -Dm644 system-settings/ldm_pam_environment %buildroot%_localstatedir/ldm/.pam_environment

#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr  /usr/share/gfxboot/%theme ||:
[ -s /boot/splash/%theme ] && rm -fr  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
#shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%post system-settings
#chown _ldm:_ldm %_localstatedir/ldm/.pam_environment
sed -i '/pam_env\.so/ {
		/user_readenv/ b
		s/pam_env\.so/pam_env.so user_readenv=1/ }
' %_sysconfdir/pam.d/lightdm-greeter

%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

%post mate-settings
subst 's/#theme-name=/theme-name=Clearlooks-Phenix/' /etc/lightdm/lightdm-gtk-greeter.conf ||:
/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_niconsdir/slinux.png
%_iconsdir/altlinux.png

%files bootsplash
%_datadir/plymouth/themes/%theme/*
%exclude %_datadir/plymouth/themes/%theme/*.in

%files release
%_sysconfdir/*-release
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files kde4-settings
%_sysconfdir/skel/.kde4

%files fvwm-settings
%_sysconfdir/skel/.fvwm2rc

%files mate-settings
%_datadir/glib-2.0/schemas/*.gschema.override

%files xfce-settings
%_sysconfdir/X11/profile.d/zdg-move-templates.sh
/etc/skel/XDG-Templates.skel/
/etc/skel/.wm-select
/etc/skel/.config
/etc/skel/.local
/etc/skel/.gconf
/etc/skel/.vimrc
/usr/share/backgrounds/xfce/*
%_sysconfdir/skel/Templates/*

%files slideshow
/etc/alterator/slideshow.conf
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %_indexhtmldir/index.html
%_indexhtmldir/*
%_desktopdir/*

%files menu
/usr/share/slinux-style
/etc/xdg/menus/xfce-applications-merged/50-xfce-applications.menu
/usr/share/desktop-directories/altlinux-wine.directory

%files system-settings
%config %_sysconfdir/polkit-1/rules.d/*.rules
#%config %_localstatedir/ldm/.pam_environment

%changelog
* Wed Aug 24 2016 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt2
- Use full brand name (%brand-%theme) to prevent wrong replacement of
  branding with same %theme but different %brand

* Mon Apr 13 2015 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt0.M70P.2
- Update copyright years, fix VK group URL and update company address
- Fix button gluing in web interface
- Fix package name with Droid fonts
- Generate image for selection bar in GRUB menu from specified color

* Wed Jun 11 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt0.M70P.1
- Backport to p7 branch

* Wed Jun 11 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.5-alt1
- New release

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New release

* Fri Feb 14 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt3
- Set light blue background in rEFIt by set correct pixel color in top
  left corner of background image
- Remove abandoned web resource planet.altlinux.org from indexhtml

* Thu Feb 13 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt2
- Rebuild with updated gfxboot

* Wed Feb 05 2014 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- Fix license

* Tue Dec 24 2013 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- Release 7.0.2

* Tue Dec 17 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt5
- indexhtml requires docs-school-server
- beta version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt4
- Pack wide wallpaper and product logo
- Fix favicon and logo width in Alterator web-interface
- Fix bootloader colors
- Hide section border, simplify tooltips, turn off checkbox and
  radiobutton highlight in installer
- Replace Simply Linux logo by Platform Seven logo
- Simplify GRUB config

* Tue Dec 03 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt3
- Fix black color for selection background in Qt theme for Alterator
- Fix favicon and product logo width in ahttpd

* Mon Dec 02 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt2
- Fix selection color and note font in GRUB theme
- Set more bright color for bootloader
- Disable border around section and nice yellow captions for installer

* Tue Sep 10 2013 Andrey Cherepanov <cas@altlinux.org> 6.9.9-alt1
- Update branding for Seven platform

* Thu Apr 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt9
- kde3 settings removed

* Tue Sep 04 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt8
- Remove obsolete slideshow

* Mon Aug 20 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt7
- Fix grub2 console font

* Fri Aug 17 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt6
- Remove background from product logo
- Fix distro name
- Fix attribute name for meta http-equiv
- Fix grub background color

* Fri Jul 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt5
- autoboot from usb fixed

* Thu May 17 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt4
- Set appropriate product logo
- Modernize appearance of Alterator web interface

* Fri Apr 06 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt3
- images with informika logo added

* Thu Apr 05 2012 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt2
- Adapt indexhtml to use from httpd2
- Add gksu for apt-indicator in GNOME

* Thu Nov 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.0-alt1
- school server branding on top of centaurus one

* Thu Jun 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt17
- merge with desktop

* Wed May 13 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt16
- \%setup fixed from boyarsh@
- remove package name from .gear-rules from boyarsh@

* Fri Apr 24 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt15
- minor fixes of strange merge
- changes in alterator.css.in from inger@

* Fri Apr 17 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt14
- better quality background image for installer

* Thu Apr 16 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt13
- alterator.css = alterator.css+menu.css
- some strange results of merge fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt12
- gear-rules fixed

* Fri Apr 10 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt11
- web logo - white and smaller;
  labels on buttons - darker;
  disabled elements - lighter;

* Fri Apr 10 2009 Alxandra Panyukova <mex3@altlinux.ru> 5.0.0-alt10
- some misspells fixed

* Thu Apr 09 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt9
- darker text and new logo for web

* Thu Apr 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt8
- gradients and some colors in css fixed by mex3@

* Tue Apr 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt7
- fixes for installer design from mex3@ 

* Fri Apr 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt6
- default gray design from mex3@
- \%status_en intorduces for release file 

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt5
- logo in www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt4
- www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt3
- conflicts for -alterator subpackages added
- design for web alterator changed

* Mon Mar 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt2
- -browser-qt subpackage remaned to -alterator as it really is

* Fri Mar 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- addes \%status to altlinux-release
- images for verbose bootsplash mode from one source

* Wed Mar 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt24
- added versioned provides for indexhtml 

* Tue Mar 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt23
- indexhtml subpackage added 

* Mon Mar 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt22
- nepomukserverrc added into kde4 

* Wed Mar 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt21
- other images for browser-qt added
- gtkrcs added into kde4-settings
- plasma-applet-networkmanagenemt removed from kde4 by default
- conflicts bitween different brandings added

* Thu Mar 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt20
- steps icons added 

* Fri Feb 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- sample slideshow added

* Wed Feb 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- 1024x768 removed :D
- more transparent menu selection bar

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- 1024x768 added 
- fonts changed

* Thu Feb 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- not setup language in bootloader during install (when it is 'C') 

* Wed Feb 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- rebuild with new bootloader-source with support of real language change 

* Tue Feb 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- auto set default language for bootloader from /etc/sysconfig/i18n 

* Mon Feb 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- rebuild for fix oversized /boot/splash/message 

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- default language set to ru_RU for system boot 

* Wed Feb 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- fixed conflict of notes subpackage with itself 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- more kde4 settings from zerg@ 
- alternative and obsoletes for graphics added

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- rebuild with new translations 

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- added kde4-settings subpackage 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- added conflicts for notes 

* Mon Jan 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- xdm background fixed 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- added 'notes' subpackage 

* Thu Jan 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- fixed problem with owerwritten alternative 

* Wed Jan 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- release subpackage added 
