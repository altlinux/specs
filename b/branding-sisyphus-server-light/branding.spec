%define Theme Server Light
%define codename Collybia confluens
%define brand sisyphus
%define Brand Sisyphus
%define variants altlinux-kdesktop altlinux-desktop altlinux-office-desktop altlinux-office-server altlinux-lite altlinux-workbench school-master altlinux-gnome-desktop


Name: branding-%brand-server-light
Version: 1.1.5
Release: alt1
BuildArch: noarch

%define theme %name
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0
%define status r5
%define status_en r5

BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): libqt4-core
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig bc libGConf-devel

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for lilo and syslinux
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

%description bootloader
Here you find the graphical boot logo. Suitable for both lilo and syslinux.

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
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Provides: design-graphics-%theme  branding-alt-%theme-graphics design-graphics-kdesktop
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme design-graphics-kdesktop
PreReq(post,preun): alternatives >= 0.2

%description graphics
This package contains some graphics for ALT design.


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary: %distribution %Theme release file
Copyright: GPL
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

GRAPHICS_ALTPRIO=`printf '%%.3d%%.3d%%.3d%%.3d\n' %design_graphics_abi_epoch %design_graphics_abi_major %design_graphics_abi_minor %design_graphics_abi_bugfix`
install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/design-current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
%_datadir/design/current	%_datadir/design/%theme	$GRAPHICS_ALTPRIO
__EOF__


#release
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/ignore.d/
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

#indexhtml
%define _indexhtmldir %_defaultdocdir/indexhtml
pushd indexhtml
mkdir -p %buildroot{%_indexhtmldir/,%_desktopdir/}
cp -r * %buildroot%_indexhtmldir/
rm -f %buildroot%_indexhtmldir/*.in %buildroot%_indexhtmldir/indexhtml.desktop
touch %buildroot%_indexhtmldir/index.html
install -m644 indexhtml.desktop %buildroot%_desktopdir/
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



%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme

%files alterator
%config %_altdir/*.rcc
/usr/share/alterator-browser-qt/design/*.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*

%files slideshow
/usr/share/install2/slideshow

%files indexhtml
%ghost %_indexhtmldir/index.html
%_indexhtmldir/*
%_desktopdir/*

%changelog
* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 1.1.5-alt1
- version UP

* Fri Apr 01 2011 Anton Farygin <rider@altlinux.ru> 1.1.4-alt1
- fixed color theme in alterator-vm (thnx dkr@)

* Wed Feb 23 2011 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- color palette changed to B/W

* Wed Dec 01 2010 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- removed images from slideshow

* Wed Nov 24 2010 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- codename changed

* Wed Nov 10 2010 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- version UP

* Fri Dec 04 2009 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for Sisyphus, based on kdesktop branding
