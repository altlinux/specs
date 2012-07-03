%define theme lxdesktop
%define Theme LXDEsktop
%define codename Liliya
%define brand altlinux
%define Brand ALT Linux

Name: branding-%brand-%theme
Version: 6.0.0 
Release: alt7
BuildArch: noarch

BuildRequires: cpio fonts-ttf-dejavu fonts-ttf-droid
BuildRequires: design-bootloader-source >= 5.0-alt2
%ifnarch %arm
BuildRequires: cpio gfxboot >= 4 
%endif

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

%define status %nil
%define status_en %nil
%define variants altlinux-office-desktop altlinux-office-server altlinux-lite altlinux-workbench school-master altlinux-desktop altlinux-gnome-desktop

Packager: Anton V. Boyarshinov <boyarsh at altlinux dot org>

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Provides: branding-lxde-desktop-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Obsoletes: branding-lxde-desktop-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-bootloader ";done )

%define grub_normal white/black
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme branding-lxde-desktop-bootsplash
Obsoletes: branding-lxde-desktop-bootsplash
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
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt branding-lxde-desktop-alterator

Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-browser-qt ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server branding-lxde-desktop-alterator
PreReq(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics

Provides: design-graphics-%theme  branding-alt-%theme-graphics branding-lxde-desktop-graphics
Obsoletes: branding-alt-%theme-graphics design-graphics-%theme branding-lxde-desktop-graphics
Provides: design-graphics = 12.0.0
Provides: gnome-session-splash = %version-%release
PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-graphics ";done )

%description graphics
This package contains some graphics for ALT design.


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business

%package release
Summary: %distribution %Theme release file
Copyright: GPL
Group: System/Configuration/Other
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release branding-lxde-desktop-release
Obsoletes: %obsolete_list  branding-alt-%theme-release branding-lxde-desktop-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-release ";done )

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme branding-lxde-desktop-notes
Obsoletes: alt-license-%theme alt-notes-%theme branding-lxde-desktop-notes
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
Provides: branding-lxde-desktop-slideshow
Obsoletes: branding-lxde-desktop-slideshow
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml
Summary: %name -- ALT Linux html welcome page
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Provides: branding-lxde-desktop-indexhtml
Obsoletes: indexhtml-desktop indexhtml-Desktop branding-lxde-desktop-indexhtml

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

%package settings
Summary: LXDE settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/Other
Requires: fonts-ttf-dejavu
Requires: icon-theme-faenza
Requires: gtk2-themes-faenza
Requires: gtk2-themes-aurora
Requires: x-cursor-theme-Vanilla-DMZ-AA
Requires: lxde-lxterminal librsvg
Requires: lxde-common beesu
Requires: xdg-user-dirs xdg-user-dirs-gtk
Provides: lxde-settings branding-lxde-desktop-lxde-settings
Obsoletes: branding-lxde-desktop-lxde-settings lxde-settings-abstraction
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )

%description settings
LXDE settings for %Brand %version %Theme

%package lite-settings
Summary: LXDE-lite settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/Other
Requires: fonts-ttf-dejavu
Requires: icon-theme-faenza
Requires: gtk2-themes-faenza
Requires: gtk2-themes-aurora
Requires: x-cursor-theme-Bluecurve
Requires: lxde-common beesu
Requires: lxde-lxterminal librsvg
Requires: xdg-user-dirs xdg-user-dirs-gtk
Provides: lxde-settings branding-lxde-desktop-lxde-settings
Obsoletes: lxde-settings-abstraction-lite
Conflicts: %(for n in %variants ; do [ "$n" = %brand-%theme ] || echo -n "branding-$n-gnome-settings ";done )

%description lite-settings
LXDE-lite settings for %Brand %version %Theme

%package gdm-theme
Summary: GDM2-theme for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/GNOME
Requires: gdm2.20

%description gdm-theme
Simple theme based on Gnome Serenity GDM theme

%prep
%setup -n branding

%ifnarch %arm
%define x86 boot
%else
%define x86 %nil
%endif

%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version X86='%x86' ./configure 
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

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/*  %buildroot/usr/share/install2/slideshow/

#lxdesktop-settings
mkdir -p %buildroot/%_datadir/%theme-settings
cp -ar lxde-settings/* %buildroot/%_datadir/%theme-settings

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme-settings << __EOF__
%_datadir/lxde %_datadir/%theme-settings 11
__EOF__

#lxdesktop-lite-settings
mkdir -p %buildroot/%_datadir/%theme-lite-settings
cp -ar lxde-settings-lite/* %buildroot/%_datadir/%theme-lite-settings

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme-lite-settings << __EOF__
%_datadir/lxde %_datadir/%theme-lite-settings 11
__EOF__

#gdm-theme
mkdir -p %buildroot%_datadir/gdm/themes/%theme
cp -ar gdm-theme/* %buildroot%_datadir/gdm/themes/%theme

#xdg-user-desktop-links.sh
mkdir -p %buildroot%_x11sysconfdir/profile.d
cp xdg-user-links-desktop.sh %buildroot%_x11sysconfdir/profile.d/

#xdg-user-dirs-gtk-update.sh
cp xdg-user-dirs-gtk-update.sh %buildroot%_x11sysconfdir/profile.d/

#added logout applications
mkdir -p %buildroot%_datadir/applications
cp lxsession-logout.desktop %buildroot%_datadir/applications/

#Theme to OpenBox
mkdir -p %buildroot%_datadir/themes/Aurora\ Black\ Glass/
cp -ar Aurora/* %buildroot%_datadir/themes/Aurora\ Black\ Glass/

#etcskel
mkdir -p %buildroot%_sysconfdir/skel/
cp -ar etcskel/.gnome2 %buildroot%_sysconfdir/skel/
cp -ar etcskel/.gnome-commander %buildroot%_sysconfdir/skel/
cp -ar etcskel/.config %buildroot%_sysconfdir/skel/
cp -ar etcskel/.mplayer %buildroot%_sysconfdir/skel/

#mime-default
install -D -m 644 mime-default/defaults-lxdesktop.list %buildroot/%_datadir/%theme-settings/applications/defaults.list
install -D -m 644 mime-default/defaults-lxdesktop.list %buildroot/%_datadir/%theme-lite-settings/applications/defaults.list


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
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%post settings
DESKDIR="/usr/share/applications/"
for dfile in uxterm xterm xkill
do
    if [ -f "$DESKDIR"/"$dfile".desktop ]
    then
	echo "Hidden=true" >> "$DESKDIR"/"$dfile".desktop
	else
	echo "Warning: $DESKDIR/$dfile.desktop not exist"
    fi
done

%post lite-settings
DESKDIR="/usr/share/applications/"
for dfile in uxterm xterm xkill
do
    if [ -f "$DESKDIR"/"$dfile".desktop ]
    then
    	echo "Hidden=true" >> "$DESKDIR"/"$dfile".desktop
	else
	echo "Warning: $DESKDIR/$dfile.desktop not exist"
    fi
done

%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%postun settings
DESKDIR="/usr/share/applications/"
for dfile in uxterm xterm xkill
do
    if [ -f "$DESKDIR"/"$dfile".desktop ]
	then
	grep -v "Hidden=true" "$DESKDIR"/"$dfile".desktop > "$TMPFILE"
	cat "$TMPFILE" > "$DESKDIR"/"$dfile".desktop
    fi
done
rm -f "$TMPFILE"

%postun lite-settings
DESKDIR="/usr/share/applications/"
for dfile in uxterm xterm xkill
do
    if [ -f "$DESKDIR"/"$dfile".desktop ]
        then
    	grep -v "Hidden=true" "$DESKDIR"/"$dfile".desktop > "$TMPFILE"
	cat "$TMPFILE" > "$DESKDIR"/"$dfile".desktop
    fi
done
rm -f "$TMPFILE"

%ifnarch %arm
%files bootloader
%dir /boot/grub/
%dir /boot/splash/
%dir /boot/grub/themes/
%dir %_datadir/gfxboot/
%_datadir/gfxboot/%theme
/boot/splash/%theme
/boot/grub/themes/%theme
%endif

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf
[ -f /etc/sysconfig/grub2 ] && \
      subst "s|GRUB_WALLPAPER=.*|GRUB_WALLPAPER=/usr/share/plymouth/themes/%theme/grub.jpg|" \
             /etc/sysconfig/grub2 ||:

%files alterator
%dir %_datadir/alterator-browser-qt/
%dir %_datadir/alterator-browser-qt/design/
%config %_altdir/*.rcc
%_datadir/alterator-browser-qt/design/*.rcc
%_datadir/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files bootsplash
%dir %_datadir/plymouth/themes/%theme/
%_datadir/plymouth/themes/%theme/*

%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%dir %_datadir/alt-notes/
%_datadir/alt-notes/*

%files slideshow
%dir %_datadir/install2
%_datadir/install2/slideshow

%define indexhtmldir %_defaultdocdir/indexhtml

%files indexhtml
%ghost %indexhtmldir/index.html
%indexhtmldir/index-*.html
%indexhtmldir/index.css
%indexhtmldir/images
%_desktopdir/indexhtml.desktop

%files settings
%config /etc/alternatives/packages.d/%theme-settings
%_datadir/%theme-settings
%_x11sysconfdir/profile.d/*
%_datadir/themes/*
%_datadir/applications/lxsession-logout.desktop
%_datadir/%theme-settings/applications/defaults.list
%_sysconfdir/skel/

%files lite-settings
%config /etc/alternatives/packages.d/%theme-lite-settings
%_datadir/%theme-lite-settings
%_x11sysconfdir/profile.d/*
%_datadir/themes/*
%_datadir/applications/lxsession-logout.desktop
%_datadir/%theme-lite-settings/applications/defaults.list
%_sysconfdir/skel/

%files gdm-theme
%_datadir/gdm/themes/*

%changelog
* Sun Mar 11 2012 Radik Usupov <radik@altlinux.org> 6.0.0-alt7
- Added tracker configs (#122)
- Changed grub2 theme (by Stranger573)
- Updated Openbox Theme (by Stranger573)

* Thu Mar 08 2012 Radik Usupov <radik@altlinux.org> 6.0.0-alt6
- Added PrtSc key to lxdesktop-lite (#114)
- Updated desktop font
- Fixed grub configuration (by Stranger573)

* Sun Feb 26 2012 Radik Usupov <radik@altlinux.org> 6.0.0-alt5
- Fixed status section

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 6.0.0-alt4
- Added lxdesktop slideshow (by twister5anna)
- Added new wallpapper (by Stranger573)
- Added config to gnome-mplayer (#107)
- Added screenshot key from the Openbox config (#114)
- Added screensaver key from the Openbox config (#28)
- Changed gdm theme
- Bootsplash update (by stranger573)
- Updated notes and indexhtml

* Tue Sep 27 2011 Radik Usupov <radik@altlinux.org> 6.0.0-alt3
- Changed plymouth theme
- Added folders to pcmanfm browser
- Added mime-defaults
- Added config files to gnome-commander
- Added lxdesktop slideshow
- Fixed lxpanel settings
- Added provides/obsoletes

* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 6.0.0-alt2
- Added logout button to lxpanel (#80)
- Replaced xdg-su by beesu (#78)
- Changed GDM theme (#69)
- Use Super on keyboard to open menu (#87)

* Sun Feb 20 2011 Radik Usupov <radik@altlinux.org> 6.0.0-alt1
- Initial build LXDEsktop branding (based on Centaurus branding)
