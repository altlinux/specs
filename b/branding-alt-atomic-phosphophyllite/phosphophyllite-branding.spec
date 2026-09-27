# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/phosphophyllite-branding

%define _unpackaged_files_terminate_build 1

%define brand alt
%define theme atomic
%define Variant Phosphohpyllite
%define variant phosphophyllite
%define altbranch sisyphus
%define flavour %brand-%theme
%define flavour_phosphophyllite %flavour-phosphophyllite
%define pname ALT Atomic
%define bugtracker https://altlinux.space/alt-atomic/phosphophyllite/issues
%define docpage https://alt-atomic.org/

Name: branding-alt-atomic-phosphophyllite
Version: 20260925
Release: alt1

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later
URL: https://alt-atomic.org/
VCS: https://altlinux.space/alt-atomic/phosphophyllite-branding.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-branding
BuildRequires(pre): rpm-macros-ready-set
BuildRequires: meson
BuildRequires: pkgconfig(libready-set-0.14)

%description
%summary.

%package release
Summary: %pname release files
Group: System/Configuration/Other

BuildArch: noarch

Requires: alt-atomic-icons
Requires: pam-limits-off
Requires: alt-os-release
Provides: system-release = %EVR
Provides: altlinux-release = %EVR
Provides: altlinux-release-%theme = %EVR
Conflicts: altlinux-release-%altbranch
%branding_add_conflicts %flavour_phosphophyllite release

%description release
%summary.

%package gnome-settings
Summary: %pname settings for GNOME
Group: Graphical desktop/GNOME

Requires: dconf
Requires: %name-graphics = %EVR
Requires(post): libgio
Conflicts: branding-simply-linux-system-settings
%branding_add_conflicts %flavour_phosphophyllite gnome-settings

%description gnome-settings
%summary.

%package bootsplash
Summary: Theme for splash animations during bootup
Group: System/Configuration/Boot and Init

BuildArch: noarch

Requires: plymouth-theme-%theme
%branding_add_conflicts %flavour_phosphophyllite bootsplash

%description bootsplash
This package contains graphics for boot process for %pname
(needs console splash screen enabled).

%package graphics
Summary: This package contains some graphics for %pname design
Group: Graphics

BuildArch: noarch

Requires: icon-theme-alt-atomic-onyx
Requires: wallpapers-alt-atomic-gnome

%branding_add_conflicts %flavour_phosphophyllite graphics

%description graphics
%summary.

%package ready-set
Summary: This package contains ready-set config
Group: Other

Requires: ready-set-phrog
Requires: ready-set-plugin-language
Requires: ready-set-plugin-license-agreement
Requires: ready-set-plugin-keyboard
Requires: ready-set-plugin-network
Requires: ready-set-plugin-privacy
Requires: ready-set-plugin-date-and-time
Requires: ready-set-plugin-software
Requires: ready-set-plugin-user-passwdqc
Requires: ready-set-plugin-atomic-finalize

%branding_add_conflicts %flavour_phosphophyllite ready-set

%description ready-set
%summary.

%prep
%setup

%build
%meson \
  -Dname='%pname' \
  -Dpretty_name='%pname %Variant' \
  -Dtheme=%theme \
  -Dbranch=%altbranch \
  -Dbrand=%brand \
  -Dhomepage=%url \
  -Dbugtracker=%bugtracker \
  -Dflavour=%flavour \
  -Ddocpage=%docpage \
  -Dvariant=%Variant \
  -Dvariant_id=%variant \
  -Dversion=%version
%meson_build

%install
%meson_install
%find_lang %variant-branding

%post bootsplash
[ "$1" -eq 1 ] || exit 0
plymouth-set-default-theme %theme

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release

%files bootsplash

%files graphics

%files ready-set -f %variant-branding.lang
%__ready_set_datadir/config
%__ready_set_datadir/software/sources.d/flathub.yml

%files gnome-settings
%_datadir/glib-2.0/schemas/*.override

%changelog
* Fri Sep 25 2026 David Sultaniiazov <x1z53@altlinux.org> 20260925-alt1
- Initial build.
