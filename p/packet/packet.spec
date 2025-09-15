%define _unpackaged_files_terminate_build 1
%define app_id io.github.nozwock.Packet
%define nautilus_extdir %_datadir/nautilus-python/extensions

Name: packet
Version: 0.5.4
Release: alt1

# Fails to link under aarch64
ExcludeArch: aarch64

Summary: A Quick Share client for Linux
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/nozwock/packet
Vcs: https://github.com/nozwock/packet
Source: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

%add_python3_path %nautilus_extdir

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson rust-cargo protobuf-compiler
BuildRequires: blueprint-compiler
BuildRequires: libdbus-devel
BuildRequires: appstream
BuildRequires: pkgconfig(libadwaita-1)

%description
An implementation of the Google Quick Share protocol to send and receive files
to Android devices or another instance of Packet.

%package nautilus
Summary: Nautilus extension for Packet
Group: Other
Requires: %name = %EVR
Requires: nautilus-python
AutoProv: nopython3

%description nautilus
An extension for Nautilus that allows you to quickly share files using packet.

%prep
%setup -a1
install -vDm644 %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %buildroot%nautilus_extdir
mv %buildroot%_datadir/%name/plugins/%{name}_nautilus.py \
    %buildroot%nautilus_extdir/%{name}_nautilus.py
# drop unknown languages, find known
rm -r %buildroot%_datadir/locale/zh_Han*
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/metainfo/%app_id.releases.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/packet/resources.gresource
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%files nautilus
%nautilus_extdir/%{name}_nautilus.py
%nautilus_extdir/__pycache__/*

%changelog
* Tue Aug 26 2025 Alexander Davydzik <paladindev@altlinux.org> 0.5.4-alt1
- 0.5.4

* Mon Jun 23 2025 Alexander Davydzik <paladindev@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jun 16 2025 Alexander Davydzik <paladindev@altlinux.org> 0.5.2-alt1
- 0.5.2

* Fri May 30 2025 Alexander Davydzik <paladindev@altlinux.org> 0.3.0-alt1
- initial build
