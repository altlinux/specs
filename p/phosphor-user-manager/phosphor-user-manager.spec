Name: phosphor-user-manager
Version: 0.1
Release: alt2.git34e6ccd.1

Summary: Tools for working with LDAP and CA certificates
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-user-manager
Vcs: https://github.com/openbmc/phosphor-user-manager.git

Source: %name-%version.tar

Patch: add_dbus_config_and_systemd_unit_file.patch

BuildRequires(Pre): rpm-macros-meson

BuildRequires: boost-filesystem-devel
BuildRequires: cereal-devel
BuildRequires: gcc-c++
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libldap-devel
BuildRequires: libsdbusplus-devel
BuildRequires: nlohmann-json-devel
BuildRequires: meson

Requires: phosphor-certificate-manager

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/phosphor-ldap-conf
%_bindir/phosphor-user-manager
%_unitdir/multi-user.target.wants/phosphor-certificate-manager@nslcd.service
%_unitdir/xyz.openbmc_project.User.Manager.service
%_datadir/dbus-1/system.d/phosphor-nslcd-cert-config.conf
%_datadir/dbus-1/system.d/xyz.openbmc_project.User.Manager.conf
%_datadir/phosphor-certificate-manager/nslcd

%changelog
* Thu Mar 10 2026 Anatoly Mukosey <mukav@altlinux.org> 0.1-alt2.git34e6ccd.1
- Added dbus config and systemd unit file.

* Thu Dec 04 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git34e6ccd
- Initial build for Sisyphus.
