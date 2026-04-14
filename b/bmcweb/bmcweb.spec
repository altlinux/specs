# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global pseudouser _bmcweb

Name: bmcweb
Version: 1.0
Release: alt1.git5fe4ef3.1

Summary: A do everything Redfish, KVM, GUI, and DBus webserver for OpenBMC
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/bmcweb
Vcs: https://github.com/openbmc/bmcweb.git

Source: %name-%version.tar

Patch: 0001-boost-version-1.86-support.patch
Patch1: fix-bmcweb-git5fe4ef3-ALT-installation-path.patch
Patch2: Fix_pam_rules_for_alt_OS.patch

BuildRequires(Pre): rpm-macros-meson
BuildRequires(Pre): rpm-macros-webserver-common
BuildRequires(Pre): webserver-common

BuildRequires: boost-asio-devel
BuildRequires: boost-beast-devel
BuildRequires: boost-devel-headers
BuildRequires: boost-filesystem-devel
BuildRequires: cli11-devel
BuildRequires: gcc-c++
BuildRequires: libnghttp2-devel
BuildRequires: libpam0-devel
BuildRequires: libssl-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsystemd-devel
BuildRequires: libtinyxml2-devel
BuildRequires: meson
BuildRequires: nlohmann-json-devel
BuildRequires: zlib-devel

%filter_from_requires /bmcwebd/d
%filter_from_requires /common-account/d
%filter_from_requires /common-auth/d
%filter_from_requires /common-password/d

# Failed to build
ExcludeArch: %ix86

%description
The webserver implements a few distinct interfaces:

- DBus event websocket. Allows registering on changes to specific dbus
  paths, properties, and will send an event from the websocket if those
  filters match.
- OpenBMC DBus REST api. Allows direct, low interference, high fidelity
  access to dbus and the objects it represents.
- Serial: A serial websocket for interacting with the host serial console
  through websockets.
- Redfish: A protocol compliant, DBus to Redfish translator.
- KVM: A websocket based implementation of the RFB (VNC) frame buffer
  protocol intended to mate to webui-vue to provide a complete KVM
  implementation.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %buildroot%_localstatedir/%name

%pre
# Additional groups for bmcweb auth mechanism
groupadd -r -f redfish >/dev/null 2>&1 ||:
groupadd -r -f priv-admin >/dev/null 2>&1 ||:
groupadd -r -f priv-operator >/dev/null 2>&1 ||:
groupadd -r -f priv-user >/dev/null 2>&1 ||:

groupadd -r -f %pseudouser >/dev/null 2>&1 ||:
groupadd -r -f _webserver >/dev/null 2>&1 ||:
useradd -M -r -g %pseudouser -G _webserver -c 'OpenBMC bmcweb' \
	-s /bin/false -d %_localstatedir/%name %pseudouser >/dev/null 2>&1 ||:

%files
%_sysconfdir/pam.d/%name
%_bindir/%name
%_datadir/%name
%attr(2711,root,%pseudouser) %_libexecdir/%{name}d
%attr(2775,root,%pseudouser) %_localstatedir/%{name}
%_unitdir/%name.service
%_unitdir/%name.socket

%changelog
* Tue Mar 31 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0-alt1.git5fe4ef3.1
- Initial build for Sisyphus.
