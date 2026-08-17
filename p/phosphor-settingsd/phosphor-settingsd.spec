%define _unpackaged_files_terminate_build 1

Name: phosphor-settingsd
Version: 1.0
Release: alt2.git4af51a7.1

Summary: Interfaces to let the user configure

License: Apache-2.0
Group: System/Configuration/Other
Url: https://www.openbmc.org/
Vcs: https://github.com/openbmc/phosphor-settingsd.git

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)
BuildRequires: cereal-devel
BuildRequires: python3-module-yaml
BuildRequires: python3-module-mako
BuildRequires: sdbusplus-tools

%description
Settings management system for OpenBMC
that provides a framework for storing, validating,
and retrieving configuration settings via D-Bus.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.txt OWNERS README-settings-manager.md
%_bindir/phosphor-settings-manager

%changelog
* Thu Jul 23 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0-alt2.git4af51a7.1
- Merge with upstream 4af51a7.

* Tue Aug 12 2025 Anton Meleshnikov <alton@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.

