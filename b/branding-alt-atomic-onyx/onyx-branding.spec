# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/onyx-branding to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define brand alt
%define theme atomic-onyx
%define altbranch sisyphus
%define flavour %brand-%theme
%define pname ALT Atomic Onyx
%define bugtracker https://altlinux.space/alt-atomic/onyx/issue

Name: branding-alt-atomic-onyx
Version: 20240822
Release: alt1

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later
Url: https://atomic.alt-gnome.ru/
Vcs: https://altlinux.space/alt-atomic/onyx-branding.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-branding
BuildRequires: meson

%description
%summary.

%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release

%package release
Summary: %pname release files
Group: System/Configuration/Other

BuildArch: noarch

Requires: alt-atomic-icons
Requires: pam-limits-desktop
Requires: alt-os-release
Provides: %(for n in %provide_list; do echo -n "$n-release = %EVR "; done) altlinux-release-%theme
Obsoletes: %obsolete_list
Conflicts: altlinux-release-%altbranch
%branding_add_conflicts %flavour release

%description release
%summary.

%package gnome-settings
Summary: %pname settings for GNOME
Group: Graphical desktop/GNOME

BuildArch: noarch

Requires: dconf
Requires: %name-graphics = %EVR
Requires(post): libgio
# From ALT Workstation branding
Conflicts: installer-feature-lightdm-stage3 < 0.1.0-alt1
Conflicts: branding-simply-linux-system-settings
Conflicts: lxde-settings-lxdesktop < 0.3.2-alt2
%branding_add_conflicts %flavour gnome-settings

%description gnome-settings
%summary.

%package bootsplash
Summary: Theme for splash animations during bootup
Group: System/Configuration/Boot and Init

BuildArch: noarch

Provides: plymouth-theme-%theme = %EVR
Requires: icon-theme-alt-atomic-onyx
Requires: plymouth
Requires: plymouth-theme-bgrt
Requires: plymouth-plugin-label
Requires: fonts-ttf-dejavu
%branding_add_conflicts %flavour bootsplash

%description bootsplash
This package contains graphics for boot process for %pname
(needs console splash screen enabled).
release

%package graphics
Summary: This package contains some graphics for %pname design.
Group: Graphics

BuildArch: noarch

Requires: alt-atomic-icons

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour graphics

%description graphics
%summary.

%prep
%setup

%build
%meson \
    -Dname='%pname' \
    -Dtheme=%theme \
    -Dbranch=%altbranch \
    -Dbrand=%brand \
    -Dhomepage=%url \
    -Dbugtracker=%bugtracker
%meson_build

%install
%meson_install

%post bootsplash
[ "$1" -eq 1 ] || exit 0
plymouth-set-default-theme bgrt

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release

%files bootsplash

%files graphics

%files gnome-settings
%_datadir/glib-2.0/schemas/*.override

%changelog
* Fri Aug 22 2025 Vladimir Vaskov <rirusha@altlinux.org> 20240822-alt1
- Initial build.
