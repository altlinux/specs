Name: phosphor-user-manager
Version: 0.1
Release: alt1.git34e6ccd

Summary: Tools for working with LDAP and CA certificates
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-user-manager
Vcs: https://github.com/openbmc/phosphor-user-manager.git

Source: %name-%version.tar

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

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/phosphor-ldap-conf
%_bindir/phosphor-user-manager
%_unitdir/multi-user.target.wants/phosphor-certificate-manager@nslcd.service
%_datadir/dbus-1/system.d/phosphor-nslcd-cert-config.conf
%_datadir/phosphor-certificate-manager/nslcd

%changelog
* Thu Dec 04 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git34e6ccd
- Initial build for Sisyphus.
