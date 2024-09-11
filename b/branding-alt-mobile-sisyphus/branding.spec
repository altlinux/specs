# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define theme mobile-sisyphus
%define Theme Mobile Sisyphus
%define brand alt
%define Brand ALT
%define codename phoenix
%define flavour %brand-%theme

Name: branding-%flavour
Version: 2024.08
Release: alt2

Url: https://www.altlinux.org/ALT_Mobile

BuildRequires(pre): rpm-macros-branding

BuildRequires: libalternatives-devel
BuildRequires: distro-licenses

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later

%define Brand_ru Альт
%define distro_name %Brand Mobile Sisyphus
%define distro_name_ru %Brand_ru Мобайл Сизиф
%define branding_data_dir %_datadir/branding-data-current
%define altbranch %_priority_distbranch

%define status %nil
%define status_en %nil

%description
Distro-specific packages with design and texts

# argh
%define design_graphics_abi_epoch 0
%define design_graphics_abi_major 12
%define design_graphics_abi_minor 0
%define design_graphics_abi_bugfix 0

%define provide_list altlinux fedora redhat system
%define obsolete_list altlinux-release fedora-release redhat-release

# alterantives weights
%define artworks_weight 4

%package release
Summary: %distro_name release file
Group: System/Configuration/Other
BuildArch: noarch
Requires: alt-os-release
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme branding-alt-%theme-release
Obsoletes: %obsolete_list
Conflicts: altlinux-release-%altbranch
%branding_add_conflicts %flavour release

%description release
%distro_name %version release file.

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Summary: Distribution license and release notes
License: Distributable
Group: Documentation
BuildArch: noarch
%branding_add_conflicts %flavour notes

%description notes
Distribution license and release notes.

%package bootsplash
Summary: Theme for splash animations during bootup
License: GPL-3.0-or-later
Group:  System/Configuration/Boot and Init
BuildArch: noarch
Provides: plymouth-theme-%theme plymouth(system-theme)
Requires: plymouth-plugin-script
Requires: plymouth
Requires: plymouth-theme-bgrt-alt
%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process, displayed via Plymouth

%package graphics
Summary: design for ALT
License: GPL-3.0-or-later
Group: Graphics
BuildArch: noarch

# FIXME: have a closer look at kdesktop flavour's spec
Provides: design-graphics = 12.0.0
Provides: design-graphics-%theme branding-alt-%theme-graphics
Provides: design-graphics = %design_graphics_abi_major.%design_graphics_abi_minor.%design_graphics_abi_bugfix
Obsoletes: design-graphics-%theme
Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics
Conflicts: design-graphics-default

%description graphics
This package contains some graphics for ALT design.

%package indexhtml
BuildArch: noarch
Summary:  HTML welcome page for %distro_name
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива %distro_name_ru
License:  distributable
Group:    System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
%branding_add_conflicts %flavour indexhtml

%description indexhtml
%distro_name welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива
%distro_name_ru.

%package phosh-settings
Summary: Distribution settings for Phosh
License: GPL-3.0-or-later
Group: Graphical desktop/Other
BuildArch: noarch
%branding_add_conflicts %flavour phosh-settings
Conflicts: phosh-background-settings

%description phosh-settings
Distribution settings for Phosh.

%prep
%setup -n branding

%build
autoconf
THEME=%theme NAME='%Theme' BRAND_FNAME='%Brand' BRAND_FNAME_RU='%Brand_ru' BRAND='%brand' STATUS_EN=%status_en STATUS=%status VERSION=%version PRODUCT_NAME='%distro_name' PRODUCT_NAME_RU='%distro_name_ru' CODENAME=%codename URL='%url' BRANCH='%altbranch' ./configure
#LC_ALL=en_US.UTF-8 make

%install
#makeinstall

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
{
	[ -n "%Brand" ] && echo -n "%Brand"
	[ -n "%Theme" ] && echo -n " %Theme"
	[ -n "%version" ] && echo -n " %version"
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

mkdir -p %buildroot/%prefix/lib/
install -pD -m644 systemd/os-release %buildroot/%prefix/lib/os-release

# graphics
mkdir -p %buildroot/%_datadir/design/%theme/icons
install -pD -m644 images/system-logo.png %buildroot/%_datadir/design/%theme/icons

mkdir -p %buildroot/%_datadir/design/backgrounds/
install -m644 images/background-*.png images/lockscreen-*.png \
	%buildroot/%_datadir/design/backgrounds/

install -d %buildroot/etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme %artworks_weight
%_datadir/design-current	%_datadir/design/%theme	%artworks_weight
%_datadir/design/current	%_datadir/design/%theme	%artworks_weight
__EOF__

# indexhtml
pushd indexhtml
%makeinstall
popd

# notes
pushd notes
%makeinstall
popd
ln -s /usr/share/license/GPL-3.0-or-later %buildroot/%_datadir/alt-notes/LICENSE

# phosh settings
cp -ar phosh/* %buildroot/

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=bgrt-alt/" /etc/plymouth/plymouthd.conf

%post indexhtml
%_sbindir/indexhtml-update

%files release
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%_datadir/alt-notes/*

%files bootsplash

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*

%files phosh-settings
%_sysconfdir/dconf/db/local.d/00_background
%_sysconfdir/skel/.config/gtk-3.0/gtk.css

%changelog
* Wed Sep 11 2024 Anton Midyukov <antohami@altlinux.org> 2024.08-alt2
- release: add missing conflicts with altlinux-release-%%altbranch

* Fri Aug 16 2024 Anton Midyukov <antohami@altlinux.org> 2024.08-alt1
- Bump version
- Fix space in /etc/altlinux-release

* Tue Jun 25 2024 Anton Midyukov <antohami@altlinux.org> 2024.06-alt1
- images: images: update background, lockscreen (Thanks Semen Fomchenkov)

* Fri Jun 14 2024 Anton Midyukov <antohami@altlinux.org> 2024.04-alt4
- indexhtml: add postcript for run indexhtml-update

* Thu Jun 13 2024 Anton Midyukov <antohami@altlinux.org> 2024.04-alt3
- indexhtml: install fonts

* Sat Jun 08 2024 Anton Midyukov <antohami@altlinux.org> 2024.04-alt2
- Add indexhtml

* Wed Apr 24 2024 Anton Midyukov <antohami@altlinux.org> 2024.04-alt1
- initial build
