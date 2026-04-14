Name: cockpit-machines
Version: 342
Release: alt2

Summary: Cockpit user interface for virtual machines
License: LGPL-2.1-or-later AND MIT
Group: System/Base

Url: https://github.com/cockpit-project/cockpit-machines
Source0: https://github.com/cockpit-project/%name/releases/download/%version/%name-%version.tar
Source1: node_modules.tar
Source2: pkg.tar
Source3: ru.po

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
Requires: virt-install

%description
Cockpit component for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%prep
%setup -n %name-%version
%setup -T -D -a 1
%setup -T -D -a 2
install -Dm0644 %SOURCE3 po/

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
* Tue Apr 14 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 342-alt2
- add old russian translations

* Thu Oct 16 2025 Daniil-Viktor Ratkin <krf10@altlinux.org> 342-alt1
- update version

* Thu Oct 31 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 322-alt1
- update version

* Mon Jul 01 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 315-alt1
- Initial build for Sisyphus (closes: 44671)

