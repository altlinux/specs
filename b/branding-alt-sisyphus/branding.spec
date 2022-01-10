# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define theme sisyphus
%define Theme Sisyphus
%define codename sisyphus
%define brand alt
%define Brand ALT
%define flavour %brand-%theme
%define distro_name Regular

Name: branding-%flavour
Version: 20220110
Release: alt1

Url: http://en.altlinux.org

BuildRequires(pre): rpm-macros-branding

BuildRequires: cpio fonts-ttf-dejavu

BuildRequires: qt5-base-devel
BuildRequires: libalternatives-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel
BuildRequires: fribidi

%define Theme Sisyphus
%define status unstable
%define status_en unstable

# argh
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPLv2+

%description
Distro-specific packages with design and texts

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for grub2, lilo and syslinux
License: GPL

%ifarch %ix86 x86_64
BuildRequires: gfxboot >= 4
%endif #ifarch
BuildRequires: design-bootloader-source >= 5.0-alt2
Requires: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-altlinux-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-altlinux-%theme-bootloader
%branding_add_conflicts %flavour bootloader

%define grub_normal white/black
%define grub_high black/white

%description bootloader
Here you find the graphical boot logo.
Suitable for grub2, lilo and syslinux.

%package bootsplash
Summary: Theme for splash animations during bootup
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: plymouth-theme-%theme plymouth(system-theme)
BuildArch: noarch
Requires: plymouth-plugin-script
Requires: plymouth
%branding_add_conflicts %flavour bootsplash
Conflicts: system-logo

%description bootsplash
This package contains graphics for boot process, displayed via Plymouth

%package alterator
Summary: Design for alterator for %Brand %Theme
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Provides: design-alterator-browser-%theme branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes: branding-altlinux-%theme-browser-qt

%branding_add_conflicts %flavour alterator
Obsoletes: design-alterator-server design-alterator-desktop design-alterator-browser-desktop design-alterator-browser-server
Requires(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for %Brand %Theme

%package graphics
Summary: design for ALT
License: Different licenses
Group: Graphics
BuildArch: noarch

Provides: design-graphics-%theme branding-alt-%theme-graphics
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Obsoletes: branding-altlinux-%theme-graphics design-graphics-%theme
Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics
Conflicts: design-graphics-default

%description graphics
This package contains some graphics for ALT design.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release
Summary: %distribution %Theme release file
Group: System/Configuration/Other
BuildArch: noarch
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme branding-alt-%theme-release
Obsoletes: %obsolete_list
Conflicts: %conflicts_list
%branding_add_conflicts %flavour release

%description release
%distribution %version %Theme release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
BuildArch: noarch
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes

%package slideshow

Summary: Slideshow for %Brand %version %Theme installer
License: Distributable
Group: System/Configuration/Other
BuildArch: noarch
%branding_add_conflicts %flavour slideshow

%description slideshow
Slideshow for %Brand %version %Theme installer

%package indexhtml

Summary: ALT welcome page
License: distributable
Group: System/Base
BuildArch: noarch
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server
Conflicts: branding-sisyphus-server-light-indexhtml

%branding_add_conflicts %flavour indexhtml

Requires: xdg-utils
Requires(post): indexhtml-common

%description indexhtml
ALT index.html welcome page.

%package xfce-settings

Summary: XFCE settings for %Brand %version %Theme
License: Distributable
Group: Graphical desktop/XFce
%branding_add_conflicts %flavour xfce-settings

%description xfce-settings
XFCE settings for %Brand %version %Theme

%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME='%distro_name' CODENAME=%codename URL='%url' ./configure
LC_ALL=en_US.UTF-8 make

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
%_datadir/artworks	%_datadir/design/%theme 11	
%_datadir/design-current	%_datadir/design/%theme	11
%_datadir/design/current	%_datadir/design/%theme	11
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
{
	echo -n "%distribution"
	[ "%status_en" = "unstable" ] || echo -n " %version"	# FIXME: kludgery :-/
	[ -n "%Theme" ] && echo -n " %Theme"
	[ -n "%status_en" ] && {
		[ "%status_en" = "unstable" ] \
		&& echo -n " (unstable)" \
		|| echo -n " %status_en"
	}
	[ -n "%codename" ] && echo -n " (%codename)"
	echo
} >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done
install -pD -m644 components/systemd/os-release %buildroot%_sysconfdir/os-release

#notes
pushd notes
%makeinstall
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/* %buildroot/usr/share/install2/slideshow/

# xfce-settings
pushd xfce-settings
mkdir -p %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
mkdir -p %buildroot/etc/skel/.config/xfce4/panel
mkdir -p %buildroot/etc/skel/.config/autostart
cp -r etcskel/.config/xfce4/xfconf/xfce-perchannel-xml/* %buildroot/etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
cp -r etcskel/.config/xfce4/panel/* %buildroot/etc/skel/.config/xfce4/panel
cp -r etcskel/.config/autostart/* %buildroot/etc/skel/.config/autostart
popd

#bootloader
%pre bootloader
[ -s /usr/share/gfxboot/%theme ] && rm -fr /usr/share/gfxboot/%theme ||:

%post bootloader
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/%theme/theme.txt
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high
shell_config_set /etc/sysconfig/grub2 GRUB_BACKGROUND ''
# deprecated
shell_config_set /etc/sysconfig/grub2 GRUB_WALLPAPER ''

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%ifarch %ix86 x86_64
%_datadir/gfxboot/%theme
%endif #ifarch
/boot/grub/themes/%theme

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=%theme/" /etc/plymouth/plymouthd.conf

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
%_sysconfdir/*-release
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

%files xfce-settings
%_sysconfdir/skel/.config/xfce4
%_sysconfdir/skel/.config/autostart/*

%changelog
* Mon Jan 10 2022 Anton Midyukov <antohami@altlinux.org> 20220110-alt1
- drop old bootsplash support
- fix duplicate provides
- fix Requires tag for alternatives
- do not use fetch_color
- do not pack system-logo to %_pixmapsdir
- new bootsplash theme (based on Kworkstation)

* Wed Mar 10 2021 Anton Midyukov <antohami@altlinux.org> 20201124-alt3
- Fix missing conflicts

* Wed Nov 25 2020 Anton Midyukov <antohami@altlinux.org> 20201124-alt2
- Revert missing alternative

* Tue Nov 24 2020 Anton Midyukov <antohami@altlinux.org> 20201124-alt1
- Add support grub theme
- Change License Tag to GPLv2+
- Fix obsoletes itself
- Fix weight for alternatives

* Sat Oct 26 2019 Anton Midyukov <antohami@altlinux.org> 20191026-alt1
- bootsplash: add system-logo

* Mon Jun 24 2019 Anton Midyukov <antohami@altlinux.org> 20190624-alt1
- xfce-settings: replaced clipman and power-manager applets on tray
applications

* Tue Jun 18 2019 Anton Midyukov <antohami@altlinux.org> 20190618-alt1
- build bootloader and bootsplash for all ARCH
- change color blue to progress bar
- xfce-settings back in minimal
- browser-qt: transparent background for an inscription

* Sun Mar 03 2019 Anton Midyukov <antohami@altlinux.org> 20190303-alt1
- Cleanup plymouth theme (Closes: 36179)
- Use resources generator from Qt5
- Use _unpackaged_files_terminate_build
- drop kde3-settings
- drop kde4-settings
- drop gnome-settings and gnome-themes
- fix build for non-x86

* Mon Sep 25 2017 Michael Shigorin <mike@altlinux.org> 20170925-alt1
- don't require ksplash-engine-moodin (zerg@)

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 20170109-alt1
- os-release: better PRETTY_NAME (thanks snejok@) and VERSION
- notes: updated/fixed index pages

* Thu Dec 15 2016 Michael Shigorin <mike@altlinux.org> 20161215-alt1
- replaced license step icon
- downscaled slideshow images for 6x less space

* Sun Dec 11 2016 Michael Shigorin <mike@altlinux.org> 20161211-alt1
- indexhtml: fixed conflicts generation, dropped stopgap one;
  thanks Nikolay Ulyanitsky (closes: #32881)

* Wed Nov 30 2016 Michael Shigorin <mike@altlinux.org> 20161130-alt2
- indexhtml: stopgap conflict (*sigh*)

* Wed Nov 30 2016 Michael Shigorin <mike@altlinux.org> 20161130-alt1
- added missing Conflicts:
  (see also p8-starterkits 20130427-alt1.M70P.2)

* Tue Nov 29 2016 Michael Shigorin <mike@altlinux.org> 20161129-alt2
- updated logo as well
- fixed gfxboot help menu colour

* Tue Nov 29 2016 Michael Shigorin <mike@altlinux.org> 20161129-alt1
- updated branding: altlinux->basealt/alt
  (see also p8 starterkits)

* Tue Mar 15 2016 Michael Shigorin <mike@altlinux.org> 20160315-alt1
- fixed license (see also #31748)
  + copied from branding-altlinux-starterkit-p7-alt7.M70P.2

* Thu Nov 26 2015 Aleksey Avdeev <solo@altlinux.org> 20151126-alt1
- move themes to subpackages

* Tue Sep 02 2014 Michael Shigorin <mike@altlinux.org> 20140902-alt1
- updated company address

* Tue Apr 01 2014 Michael Shigorin <mike@altlinux.org> 20140401-alt1
- enabled mediachk by default

* Tue Feb 11 2014 Michael Shigorin <mike@altlinux.org> 20140211-alt1
- updated license agreement

* Wed Nov 27 2013 Michael Shigorin <mike@altlinux.org> 20130322-alt2
- fixed graphics subpackage provides
- added informika-schoolmaster to known variants

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 20130322-alt1
- rebuilt upon d-b-s with Kazakh translation

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 20130312-alt1
- tweaked wallpaper to avoid kde4/gnome3/mate/wmaker collisions

* Thu Mar 07 2013 Michael Shigorin <mike@altlinux.org> 20130307-alt1
- fixed broken image resolution/directory name match for kde4 splash
  (thanks zerg@)

* Mon Dec 31 2012 Michael Shigorin <mike@altlinux.org> 20121231-alt1
- fixed module link text colour in acc
- tweaked acc background color (was too white)

* Wed Dec 26 2012 Michael Shigorin <mike@altlinux.org> 20121226-alt1
- fixed background image position

* Thu Aug 02 2012 Michael Shigorin <mike@altlinux.org> 20110706-alt3
- *dropped* R: altlinux-menus (closes: #27585)

* Fri Jun 01 2012 Michael Shigorin <mike@altlinux.org> 20110706-alt2
- bootsplash subpackage provides plymouth(system-theme)

* Wed Jul 06 2011 Michael Shigorin <mike@altlinux.org> 20110706-alt1
- rebuilt against current design-bootloader-source
  (syslinux-3.86 support)

* Thu May 12 2011 Michael Shigorin <mike@altlinux.org> 20101228-alt2
- dropped R: altlinux-menus (closes: #25565)

* Tue Dec 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101228-alt1
- bootsplash->plymouth
- OO.o->libreoffice

* Thu Dec 09 2010 Michael Shigorin <mike@altlinux.org> 20101209-alt1
- initial Sisyphus-specific adaptation,
  including custom texts, background and colour scheme
- fixed alterator subpackage obsoletes (a typo) and conflicts (stale)
- minor spec cleanup

* Thu Jun 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt17
- ksplashrc added for kde4
- kde3-settings and splash for kde3 added (mex@)
- gnome-settngs added (mex@)

* Wed May 13 2009 Alexandra Panyukova <mex3@altlinux.ru> 5.0.0-alt16
- %%setup fixed from boyarsh@
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

* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

