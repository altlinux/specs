%define _unpackaged_files_terminate_build 1

Name: alt-workstation-10-11-upgrade
Version: 1.2.0
Release: alt1

Summary: A simple tool for ALT Workstation upgrade from 10 to 11
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://altlinux.space/alt-gnome/alt_workstation_10-11_upgrade
VCS: https://altlinux.space/alt-gnome/alt_workstation_10-11_upgrade

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

%add_python3_path %_bindir %_prefix/libexec

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-python3

%description
%summary.

%prep
%setup

%build
%meson --libexecdir=libexec
%meson_build

%install
%meson_install

%files
%_sbindir/alt-workstation-10-11-upgrade
%_prefix/libexec/alt-workstation-10-11-upgrade-finish
%_sysconfdir/xdg/autostart/alt-workstation-10-11-upgrade-finish.desktop
%python3_sitelibdir_noarch/alt_workstation_10_11_upgrade/

%changelog
* Mon Mar 02 2026 Alexey Volkov <qualimock@altlinux.org> 1.2.0-alt1
- new version 1.2.0 (closes: 57917, 58055, 58056, 58057)

* Thu Feb 26 2026 Alexey Volkov <qualimock@altlinux.org> 1.1.1-alt1
- new version 1.1.1 (closes: 57916, 57917)

* Sat Feb 14 2026 Alexey Volkov <qualimock@altlinux.org> 1.1.0-alt1
- new version 1.1.0 (closes: 57489)

* Tue Feb 3 2026 Alexey Volkov <qualimock@altlinux.org> 1.0.1-alt1
- new version 1.0.1 (closes: 57727, 57489)

* Wed Jan 28 2026 Alexey Volkov <qualimock@altlinux.org> 1.0.0-alt1
- new version 1.0.0 (closes: 57489)

* Wed Jan 14 2026 Alexey Volkov <qualimock@altlinux.org> 0.2.0-alt1
- initial build for ALT
