# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/onyx-branding 

%define _unpackaged_files_terminate_build 1

%define brand alt
%define theme atomic
%define Variant Onyx
%define variant onyx
%define altbranch sisyphus
%define flavour %brand-%theme
%define flavour_onyx %flavour-onyx
%define pname ALT Atomic
%define bugtracker https://altlinux.space/alt-atomic/onyx/issue
%define docpage https://atomic.alt-gnome.ru/

Name: branding-alt-atomic-onyx
Version: 20260401
Release: alt1

# ptyxis doesn't support i586
ExcludeArch: i586

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later
URL: https://atomic.alt-gnome.ru/
VCS: https://altlinux.space/alt-atomic/onyx-branding.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-branding
BuildRequires: meson

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
%branding_add_conflicts %flavour_onyx release

%description release
%summary.

%package gnome-settings
Summary: %pname settings for GNOME
Group: Graphical desktop/GNOME

Requires: ptyxis
Requires: gnome-shell-extension-appindicator
Requires: gnome-shell-extension-clipboard-indicator
Requires: nautilus-open-any-terminal
Requires: dconf
Requires: %name-graphics = %EVR
Requires(post): libgio
# From ALT Workstation branding
Conflicts: installer-feature-lightdm-stage3 < 0.1.0-alt1
Conflicts: branding-simply-linux-system-settings
Conflicts: lxde-settings-lxdesktop < 0.3.2-alt2
%branding_add_conflicts %flavour_onyx gnome-settings

%description gnome-settings
%summary.

%package bootsplash
Summary: Theme for splash animations during bootup
Group: System/Configuration/Boot and Init

BuildArch: noarch

Requires: plymouth-theme-%theme
%branding_add_conflicts %flavour_onyx bootsplash

%description bootsplash
This package contains graphics for boot process for %pname
(needs console splash screen enabled).

%package graphics
Summary: This package contains some graphics for %pname design.
Group: Graphics

BuildArch: noarch

Requires: icon-theme-alt-atomic-onyx
Requires: wallpapers-alt-atomic-gnome

Requires(post,preun): alternatives >= 0.2
%branding_add_conflicts %flavour_onyx graphics

%description graphics
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

%post bootsplash
[ "$1" -eq 1 ] || exit 0
plymouth-set-default-theme %theme

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release

%files bootsplash

%files graphics

%files gnome-settings
%_datadir/glib-2.0/schemas/*.override

%changelog
* Wed Apr 01 2026 Vladimir Romanov <rirusha@altlinux.org> 20260401-alt1
- Added requires on ptyxis in gnome-settings subpackage.
- Added ExcludeArch for i586 (because of ptyxis).

* Fri Mar 13 2026 Vladimir Romanov <rirusha@altlinux.org> 20260313-alt1
- Replaced alt-atomic-icons with icon-theme-alt-atomic-onyx in graphics.

* Thu Mar 12 2026 Vladimir Romanov <rirusha@altlinux.org> 20260312-alt1
- Cleaned requires.
- Added requires on wallpapers-alt-atomic-gnome.
- Changed settings, move input-sources to image.
- Added flathub.alt-gnome.ru to gnome-software whitelist.
- Replaced req on pam-limits-desktop with pam-limits-off.

* Thu Sep 25 2025 Vladimir Vaskov <rirusha@altlinux.org> 20250925-alt1
- A more accurate ID was used in the release file.

* Tue Sep 02 2025 Vladimir Vaskov <rirusha@altlinux.org> 20250902-alt1
- Fixed typo in VARIANT and VARIANT_ID.
- Fixed version date (now it 2025 year).
- Whitelisted dl.flathub.org.
- Removed Ptyxis default settings.
- Fixed vendor in os-release, thx to David Sultaniiazov <x1z53@alt-gnome.ru>.

* Mon Aug 25 2025 Vladimir Vaskov <rirusha@altlinux.org> 20240825-alt1
- Added more fields to os-release:
  + ID_LIKE;
  + RELEASE_TYPE;
  + DOCUMENTATION_URL;
  + BUG_REPORT_URL;
  + VENDOR_NAME;
  + VENDOR_URL;
  + DEFAULT_HOSTNAME;
  + VARIANT;
  + VARIANT_ID.

* Fri Aug 22 2025 Vladimir Vaskov <rirusha@altlinux.org> 20240822-alt1
- Initial build.
