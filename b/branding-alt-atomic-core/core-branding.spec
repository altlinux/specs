# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/core-branding to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define brand alt
%define theme atomic
%define Variant Core
%define variant core
%define altbranch sisyphus
%define flavour %brand-%theme
%define flavour_core %flavour-core
%define pname ALT Atomic
%define bugtracker https://altlinux.space/alt-atomic/core/issue
%define docpage https://atomic.alt-gnome.ru/

Name: branding-alt-atomic-core
Version: 20260312
Release: alt1

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later
URL: https://atomic.alt-gnome.ru/
VCS: https://altlinux.space/alt-atomic/core-branding.git

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
%branding_add_conflicts %flavour_core release

%description release
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

%files release
%_sysconfdir/*-release
%_prefix/lib/os-release

%changelog
* Thu Mar 12 2026 Vladimir Romanov <rirusha@altlinux.org> 20260312-alt1
- Cleaned requires.
- Replace requires on pam-limits-desktop with pam-limits-off.

* Thu Sep 25 2025 Vladimir Vaskov <rirusha@altlinux.org> 20250925-alt1
- Initial build.
