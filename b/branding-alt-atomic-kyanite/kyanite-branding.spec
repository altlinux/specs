# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-atomic/kyanite-branding to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define brand alt
%define theme atomic
%define Variant Kyanite
%define variant kyanite
%define altbranch sisyphus
%define flavour %brand-%theme
%define flavour_kyanite %flavour-kyanite
%define pname ALT Atomic
%define bugtracker https://altlinux.space/alt-atomic/kyanite/issues
%define docpage https://atomic.alt-gnome.ru/

Name: branding-alt-atomic-kyanite
Version: 20260123
Release: alt1

Group: Graphics
Summary: System/Base
License: GPL-3.0-or-later
Url: https://atomic.alt-gnome.ru/
Vcs: https://altlinux.space/alt-atomic/kyanite-branding.git

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
%branding_add_conflicts %flavour_kyanite release

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
* Fri Jan 23 2026 Vladimir Romanov <rirusha@altlinux.org> 20260123-alt1
- Initial build.
