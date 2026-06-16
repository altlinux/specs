%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-qemu-server
Summary: PVE Qemu Server Tools
Version: 9.1.16
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/qemu-server.git
Source: %name-%version.tar
Source71: basealt_bootsplash.jpg

ExclusiveArch: x86_64 aarch64

# from debian/control
Provides: qemu-server = %EVR
Obsoletes: qemu-server < %EVR

Requires: socat genisoimage pve-qemu-system >= 10.1 swtpm swtpm-tools proxmox-websocket-tunnel dbus
Requires: conntrack-tools python3-module-virt-firmware proxmox-termproxy >= 2.1.0
Conflicts: pve-ha-manager < 4.0.1 pve-manager < 6.0.13
BuildRequires: glib2-devel libjson-c-devel
BuildRequires: pve-common >= 9.1.6 pve-guest-common >= 5.2.2 pve-firewall pve-ha-manager libpve-rs-perl >= 0.14.0
BuildRequires: pve-doc-generator >= 6.2.5 pve-storage >= 9.1.6 pve-qemu-system >= 10.1 pve-network
BuildRequires: perl(Term/ReadLine.pm) perl(IO/Multiplex.pm) perl(JSON.pm) perl(Time/HiRes.pm) perl(UUID.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(XML/LibXML.pm) perl(Digest/SHA.pm) perl(URI/Escape.pm)
BuildRequires: perl(Class/MethodMaker.pm)
BuildRequires: pkgconf libpcre2-devel

%description
%summary.
This package contains the Qemu Server tools used by Proxmox VE.

%prep
%setup
sed -i 's!SERVICEDIR=.*systemd/system!SERVICEDIR=%_unitdir!' src/qmeventd/Makefile
sed -i 's!SERVICEDIR=.*systemd/system!SERVICEDIR=%_unitdir!' src/query-machine-capabilities/Makefile

%build
%make_build qmeventd -C src/qmeventd
%make_build query-machine-capabilities -C src/query-machine-capabilities

%install
%makeinstall_std -C src
install -Dm0644 debian/tmpfiles %buildroot%_tmpfilesdir/qemu-server.conf
install -m0644 %SOURCE71 %buildroot%_datadir/qemu-server/bootsplash.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-cirrus.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-std.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-vmware.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-qxl.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial0.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial1.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial2.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-serial3.jpg
ln -s bootsplash.jpg %buildroot%_datadir/qemu-server/bootsplash-virtio.jpg

%triggerun -- pve-qemu-server < 9.1.13
touch /run/qemu-server/force-legacy-cleanup \
    || echo "warning: force-legacy-cleanup marker write failed - in-flight VMs may skip cleanup on stop" >&2

%post
%tmpfiles_create %_tmpfilesdir/qemu-server.conf

%files
%_tmpfilesdir/qemu-server.conf
%_modules_loaddir/qemu-server.conf
%_unitdir/qmeventd.service
%_unitdir/qmeventd.socket
%_unitdir/pve-query-machine-capabilities.service
%_unitdir/pve-dbus-vmstate@.service
%_prefix/libexec/qemu-server
%_prefix/lib/qemu-server
%_sbindir/*
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_datadir/qemu-server
%_datadir/dbus-1/system.d/org.qemu.VMState1.conf
%_man1dir/*
%_man5dir/*
%_man8dir/*

%perl_vendor_privlib/PVE/API2/*
%perl_vendor_privlib/PVE/CLI/*
%perl_vendor_privlib/PVE/QemuServer
%perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/*.pm
%perl_vendor_privlib/PVE/QemuConfig/NoWrite.pm
%perl_vendor_privlib/PVE/QemuMigrate/Helpers.pm

%changelog
* Wed Jun 10 2026 Sergey Konev <darisishe@altlinux.org> 9.1.16-alt1
- 9.1.16

* Tue Feb 10 2026 Sergey Konev <darisishe@altlinux.org> 9.1.4-alt2
- Add dependency to perl-Class-MethodMaker

* Wed Jan 21 2026 Sergey Konev <darisishe@altlinux.org> 9.1.4-alt1
- 9.1.4

* Fri Aug 29 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 9.0.18-alt1
- 9.0.18 

* Tue May 06 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 8.3.12-alt2
- fix merge conflicts with get_command_for_arch()
- fix merge conflicts with kvm_user_version()

* Tue Apr 22 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 8.3.12-alt1
- 8.3.12 

* Mon Dec 16 2024 Sergey Konev <darisishe@altlinux.org> 8.3.3-alt1
- 8.3.3

* Thu Nov 28 2024 Alexey Shabalin <shaba@altlinux.org> 8.2.8-alt1
- 8.2.8

* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.2.4-alt1
- 8.2.4

* Mon Jun 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.1-alt2.1
- FTBFS: fix systemd path

* Fri Apr 12 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.1-alt2
- fix merge error with is_native_arch() (ALT #50005)

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.1-alt1
- 8.1.1

* Wed Mar 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.1.0-alt1
- 8.1.0

* Fri Mar 01 2024 Andrew A. Vasilyev <andy@altlinux.org> 8.0.10-alt1
- 8.0.10

* Mon Feb 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 7.4.4-alt1
- 7.4-4

* Tue Oct 31 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.3-alt3
- add new (block) VM state

* Mon May 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.3-alt2
- qmeventd: fix daemon fall with "epoll_wait: Interrupted system call" (ALT #46195)

* Mon Mar 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.4.3-alt1
- 7.4-3

* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.3.4-alt1
- 7.3-4

* Wed Nov 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.12-alt1
- 7.2-12

* Fri Nov 18 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.7-alt2
- fix "Operation not supported" for ISO on OCFS2

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.7-alt1
- 7.2-7

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.4-alt1
- 7.2-4
- update basealt logo

* Sat May 07 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.2-alt1
- 7.2-2

* Wed Mar 09 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.4-alt1
- 7.1-4
- build as separate package

