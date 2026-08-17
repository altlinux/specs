# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: phosphor-certificate-manager
Version: 0.0.1
Release: alt2.gitefe7c29.1

Summary: Certificate management allows the user to install a certificates
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-certificate-manager
Vcs: https://github.com/openbmc/phosphor-certificate-manager.git

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-meson

BuildRequires: cli11-devel
BuildRequires: gcc-c++
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsdeventplus-devel
BuildRequires: libssl-devel
BuildRequires: meson

%description
Certificate management allows to replace the existing certificate and
private key file with another (possibly CA signed) Certificate key file.
Certificate management allows the user to install both the server and
client certificates.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/bmc-vmi-ca
%_bindir/phosphor-certificate-manager
%_unitdir/bmc-vmi-ca-manager.service
%_unitdir/multi-user.target.wants/phosphor-certificate-manager@authority.service
%_unitdir/multi-user.target.wants/phosphor-certificate-manager@bmcweb.service
%_unitdir/phosphor-certificate-manager@.service
%_datadir/dbus-1/system.d/bmc-vmi-ca.conf
%_datadir/dbus-1/system.d/phosphor-authority-cert-config.conf
%_datadir/dbus-1/system.d/phosphor-bmcweb-cert-config.conf
%_datadir/phosphor-certificate-manager

%changelog
* Thu Jul 23 2026 Anatoly Mukosey <mukav@altlinux.org> 0.0.1-alt2.gitefe7c29.1
- Merge with upstream efe7c29.
- Update build for Sisyphus.

* Thu Dec 04 2025 Ulysses Apokin <ulysses@altlinux.org> 0.0.1-alt1.gitaf701a6
- Initial build for Sisyphus.
