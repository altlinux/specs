%define variants altlinux-backup-server altlinux-desktop altlinux-gnome-desktop altlinux-kdesktop altlinux-lite altlinux-lxdesktop altlinux-office-desktop altlinux-office-server altlinux-school-server altlinux-sisyphus altlinux-spt altlinux-tablet altlinux-workbench informika-schoolmaster ivk-chainmail lxde-desktop lxde-school-lite Platform6-server-light school-junior school-lite school-master school-server school-teacher school-terminal simply-linux sisyphus-server-light altlinux-centaurus

%define theme chainmail
%define Theme Chainmail
%define codename none
%define brand ivk
%define Brand IVK
%define status альфа
%define status_en alpha

Name: branding-%brand-%theme
Version: 2.99
Release: alt6
BuildArch: noarch

BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

Packager: Stanislav Ievlev <inger@altlinux.org>

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts

%define grub_normal white/light-blue
%define grub_high black/light-gray

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
BuildArch: noarch
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme
Requires: plymouth-plugin-script
PreReq: plymouth

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootsplash ";done )
%description bootsplash
This package contains graphics for boot process, displayed via Plymouth

%package alterator
Summary: Design for alterator for %Brand %Theme 
License: GPL
Group: System/Configuration/Other
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt 

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-browser-qt ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server 
PreReq(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme 

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme
PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )

%description graphics
This package contains some graphics for ALT design.


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary: %distribution %Theme release file
Group: System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes

%package slideshow

Summary: Slideshow for %Brand %version %Theme installer
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml

Summary: %name -- ALT Linux html welcome page
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server

Requires: xdg-utils 
Requires(post): indexhtml-common

%description indexhtml
ALT Linux index.html welcome page.

%prep
%setup -n branding


%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version ./configure 
make

%install
%makeinstall

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
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
echo "%distribution %version %Theme %status_en (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

#notes
pushd notes
%makeinstall
popd

#kde4-settings
pushd kde4-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde4
cp -a kde4/* %buildroot%_sysconfdir/skel/.kde4/
mkdir -p %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
install -m 644 menu/* %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/
popd

#kde3-settings
pushd kde3-settings
mkdir -p %buildroot%_sysconfdir/skel/.kde
cp -a kde/* %buildroot%_sysconfdir/skel/.kde/
mkdir -p %buildroot%_sysconfdir/skel/.kde/share
mkdir -p %buildroot%_sysconfdir/skel/.kde/share/config
mkdir -p %buildroot%_sysconfdir/skel/.kde/share/apps
cp -a config/* %buildroot%_sysconfdir/skel/.kde/share/config/
cp -a apps/* %buildroot%_sysconfdir/skel/.kde/share/apps/
popd

#kde3-splash
pushd kde3-styles-splash
mkdir -p "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme"
install -m 644 *.jpg "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
install -m 644 *.png "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
install -m 644 *.rc "%buildroot/%_datadir/apps/ksplash/Themes/ALTLinux%Theme/"
popd

#gnome-settings
%define XdgThemeName %Brand %Theme
pushd gnome-settings
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
install -m 644 gtkrc '%buildroot/%_datadir/themes/%XdgThemeName/gtk-2.0'
mkdir -p '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1'
install -m 644 metacity-theme-1.xml '%buildroot/%_datadir/themes/%XdgThemeName/metacity-1/'
install -m 644 index.theme '%buildroot/%_datadir/themes/%XdgThemeName/'
mkdir -p '%buildroot/etc/gnome/xdg/menus/applications-merged/'
install -m 644 applications.menu '%buildroot/etc/gnome/xdg/menus/applications-merged/'
mkdir -p '%buildroot/etc/xdg/menus/'
install -m 644 settings.menu '%buildroot/etc/xdg/menus/'
cp -a skel/.gconf  '%buildroot/etc/skel/'
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/*  %buildroot/usr/share/install2/slideshow/

#xfce-settings
pushd xfce-settings
mkdir -p %buildroot/etc/skel/.config/xfce4/desktop
mkdir -p %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
mkdir -p %buildroot/etc/skel/.config/xfce4/panel
mkdir -p %buildroot/etc/skel/.config/xfce4-session
mkdir -p %buildroot/etc/skel/.config/autostart
mkdir -p %buildroot/etc/skel/.local/share/applications
mkdir -p %buildroot/etc/skel/Templates
install -m 644 etcskel/Templates/* %buildroot/etc/skel/Templates/
install -m 644 etcskel/.config/xfce4/helpers.rc %buildroot/etc/skel/.config/xfce4/
install -m 644 etcskel/.config/xfce4/desktop/* %buildroot/etc/skel/.config/xfce4/desktop
install -m 644 etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/* %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
install -m 644 etcskel/.config/xfce4/panel/* %buildroot/etc/skel/.config/xfce4/panel
install -m 644 etcskel/.config/xfce4-session/* %buildroot/etc/skel/.config/xfce4-session/
install -m 644 etcskel/.config/autostart/*  %buildroot/etc/skel/.config/autostart
install -m 644 etcskel/.local/share/applications/*  %buildroot/etc/skel/.local/share/applications
install -m 644 etcskel/.wm-select %buildroot/etc/skel/
install -m 644 etcskel/.Xdefaults %buildroot/etc/skel/

mkdir -p  %buildroot/usr/share/xfce4/backdrops
install -m 644 ../graphics/backgrounds/default.png %buildroot/usr/share/xfce4/backdrops
install -m 644 ../graphics/backgrounds/xdm.png %buildroot/usr/share/xfce4/backdrops
mkdir -p  '%buildroot/usr/share/themes/ALTLinux-%Theme/gtk-2.0'
install -m 644 themes/ALTLinux/gtk-2.0/* '%buildroot/usr/share/themes/ALTLinux-%Theme/gtk-2.0/'
install -m 644 themes/ALTLinux/*.png '%buildroot/usr/share/themes/ALTLinux-%Theme/'

mkdir -p %buildroot/%_bindir
install -m 755 bin/* %buildroot/%_bindir

mkdir -p %buildroot/etc/sysconfig/ 
install -m 644 xinitrc %buildroot/etc/sysconfig/xinitrc.xfce
popd

#bootloader
%pre bootloader
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
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

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

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files bootsplash
%_datadir/plymouth/themes/%theme/*

%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files slideshow
/usr/share/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/img
%_desktopdir/indexhtml.desktop

%changelog
* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 2.99-alt6
- plymouth: Fix background scaling
- Fix colors of tree widgets in alterator-browser-qt
- Fix link color of help messages in Alterator web interface

* Tue Sep 09 2014 Andrey Cherepanov <cas@altlinux.org> 2.99-alt5
- [alterator] Make links in error messages more visible

* Fri Aug 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.99-alt4
- Fix file name appearance for input[type="file"]

* Fri Jul 25 2014 Andrey Cherepanov <cas@altlinux.org> 2.99-alt3
- [grub] Set color for selected menu item background similar gfxboot as
  pixmap `selected_blob_c.png`
- [browser-qt] Return old Chainmail colors, but use Clearlooks theme

* Thu Jul 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.99-alt2
- Use Alterator colors and Clearlooks theme from Centaurus
- Decorate progressbar in Alterator as stripped bar
- [ahttpd] Solid background for error message
- [grub] Use colors from bootloader

* Tue Jun 10 2014 Andrey Cherepanov <cas@altlinux.org> 2.99-alt1
- Prepare for new version
- Support Plymouth and grub2
- Fix password placeholder symbol and background position in installer
- Fix background for tooltips and progress bars
- Fix color for gfxboot popup menu labels
- Remove slides from slideshow
- Spec cleanup

* Wed Feb 17 2010 Mikhail Efremov <sem@altlinux.org> 2.0-alt16
- drop 'alpha' status.

* Tue Nov 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt15
- update CSS styles for progressbar widget and widgets in disabled state

* Wed Oct 28 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt14
- add CSS styles for dialog
- replace some explicit corner setup with ui-round-corner class

* Fri Oct 23 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt13
- change default install dir for indexhtml packages (updated patch from azol@)
- use unified local documentation link (updated patch from azol@)

* Tue Oct 13 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt12
- add classes for selection inside table.alterator-listbox

* Mon Oct 12 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt11
- add classes for color rows in table.alterator-listbox

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt10
- add classes: close-dialog-button, help-button, and resizeable
- add svg image for close-dialog-button

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt9
- add svg images and style for page navigation buttons

* Tue Sep 22 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt8
- fix style for progress bar.

* Fri Sep 18 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt7
- add style for clock
- redesign indexhtml component

* Tue Sep 08 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt6
- add style for accordion

* Tue Sep 01 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt5
- use jpeg for background image instead of png (problem with IE 8 and Firefox 3.5.1)

* Mon Aug 31 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- update indexhtml

* Fri Aug 28 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- new pictures from ksenia@
- fix and improve web design

* Fri Aug 21 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- update web design

* Tue Aug 18 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- Initial build

