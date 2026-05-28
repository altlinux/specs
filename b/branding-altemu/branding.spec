# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define theme altemu
%define Theme ALTEMU
%define brand alt
%define Brand ALT
%define codename houhou
%define flavour %theme

Name: branding-%flavour
Version: 2026.05
Release: alt1

Url: https://www.altlinux.org/AltEMU

BuildRequires(pre): rpm-macros-branding

BuildRequires: libalternatives-devel
BuildRequires: distro-licenses

Source: branding.tar

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later

%define Brand_ru Альт
%define distro_name ALTEMU Sisyphus
%define distro_name_ru АЛЬТЭМУ Сизиф
%define branding_data_dir %_datadir/branding-data-current

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif

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
%define artworks_weight 2

%package release
Summary: %distro_name release file
Group: System/Configuration/Other
BuildArch: noarch
Requires: alt-os-release
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme branding-%theme-release
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
Requires: plymouth-plugin-two-step
Requires: plymouth
Requires: plymouth-theme-altemu
%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process, displayed via Plymouth

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

%package altemu-settings
Summary: Distribution settings for ALTEMU
License: GPL-3.0-or-later
Group: Graphical desktop/Other
BuildArch: noarch
%branding_add_conflicts %flavour phosh-settings

%description altemu-settings
Distribution settings of Sway window manager for altemu.

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

# indexhtml
pushd indexhtml
%makeinstall
popd

# notes
pushd notes
%makeinstall
popd
ln -s /usr/share/license/GPL-3.0-or-later %buildroot/%_datadir/alt-notes/LICENSE

# altemu settings
cp -ar altemu-settings/etc/skel %buildroot/%_sysconfdir

#bootsplash
%post bootsplash
subst "s/Theme=.*/Theme=altemu/" /etc/plymouth/plymouthd.conf

%post indexhtml
%_sbindir/indexhtml-update

%files release
%_sysconfdir/buildreqs/packages/ignore.d/*
%_sysconfdir/*-release
%prefix/lib/os-release

%files notes
%_datadir/alt-notes/*

%files bootsplash

%files indexhtml
%ghost %_defaultdocdir/indexhtml/index.html
%_defaultdocdir/indexhtml/*
%_desktopdir/*

%files altemu-settings
%_sysconfdir/skel/.sway/config
%_sysconfdir/skel/storage/roms/README.md


%changelog
* Thu May 28 2026 Artyom Bystrov <arbars@altlinux.org> 2026.05-alt1
- Update version
- index pages update

* Fri Sep 26 2025 Artyom Bystrov <arbars@altlinux.org> 2025.09-alt2
- Minor cleanup
- Add storage directory

* Thu Sep  4 2025 Artyom Bystrov <arbars@altlinux.org> 2025.09-alt1
- Bump version
- Fix plymouth theme name

* Mon May  5 2025 Artyom Bystrov <arbars@altlinux.org> 2025.05-alt1
- Bump version
- New branding for ALTEMU

* Thu Apr 24 2025 Artyom Bystrov <arbars@altlinux.org> 2025.04-alt4
- sway-settings: update configs for waybar
- change on-screen keyboard from squeekboard to wvkbd
- add lower bar with "close app", "menu" and "power" buttons
- add number of indicators in tray - bluetooth, modem and WiFi

* Wed Apr 23 2025 Artyom Bystrov <arbars@altlinux.org> 2025.04-alt3
- sway-settings: new set of settings and config files for alt-mobile-sway

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 2025.04-alt2
- phosh-settings: replace gtk.css with gsettings override

* Wed Apr 02 2025 Anton Midyukov <antohami@altlinux.org> 2025.04-alt1
- phosh-settings: fix override settings for phosh >= 0.46.0

* Fri Feb 21 2025 Oleg Shchavelev <oleg@altlinux.org> 2025.02-alt2
- phosh-settings: set accent color to orange using gschema overrides

* Wed Feb 12 2025 Oleg Shchavelev <oleg@altlinux.org> 2025.02-alt1
- Bump version
- images: added lockscreen image with a resolution of 4096x4096 pixels
- phosh-settings: remove tweaks phosh-applist-background settings in gtk.css
- phosh-settings: update lockscreen background image in gtk.css
- images: update the background image has been changed to a new one,
  and the dark version of the new image is now used for dark modes
- phosh-settings: optimize branding background, disable camera privacy
  and add gschema override
- phosh-settings: add wallpapers-alt-mobile dependency

* Wed Jan 29 2025 Anton Midyukov <antohami@altlinux.org> 2025.01-alt1
- Bump version
- phosh-settings: add gsettings override for disable camera privacy

* Wed Dec 11 2024 Anton Midyukov <antohami@altlinux.org> 2024.12-alt1
- Bump version

* Wed Sep 25 2024 Anton Midyukov <antohami@altlinux.org> 2024.09-alt1
- Bump version
- Fix Russian name
- indexhtml: use @PRODUCT_NAME@ and /@PRODUCT_NAME_RU@ instead @BRAND@ @NAME@

* Tue Sep 17 2024 Anton Midyukov <antohami@altlinux.org> 2024.08-alt3
- fix build, when rpm macros _priority_distbranch is not defined

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
