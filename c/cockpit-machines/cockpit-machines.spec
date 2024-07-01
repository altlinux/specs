Name: cockpit-machines
Version: 315
Release: alt1

Summary: Cockpit user interface for virtual machines
License: LGPL-2.1-or-later AND MIT
Group: System/Base

Url: https://github.com/cockpit-project/cockpit-machines
Source0: https://github.com/cockpit-project/%name/releases/download/%version/%name-%version.tar
Source1: node_modules.tar
Source2: pkg.tar

BuildArch: noarch

BuildRequires: libappstream-glib
BuildRequires: make git npm
BuildRequires: gettext
BuildRequires: libappstream-glib-devel

Requires: cockpit-bridge >= 215
Requires: libvirt-daemon-driver-qemu
Requires: libvirt-daemon-driver-network
Requires: libvirt-daemon-driver-nodedev
Requires: libvirt-daemon-driver-storage-core
Requires: qemu-kvm
Requires: qemu-audio-spice
Requires: qemu-char-spice
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0

%description
Cockpit component for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%prep
%setup -n %name-%version
%setup -T -D -a 1
%setup -T -D -a 2

%build
export PREFIX=%prefix
NODE_ENV=production npm run build

%install
export PREFIX=%prefix
%makeinstall_std
appstream-util validate-relax --nonet %buildroot/%_datadir/metainfo/*

%files
%doc README.md
%doc LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%_datadir/cockpit/*
%_datadir/metainfo/*

%changelog
* Mon Jul 01 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 315-alt1
- Initial build for Sisyphus (closes: 44671)

