%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-qemu-server
Summary: PVE Qemu Server Tools
Version: 7.3.4
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

Requires: socat genisoimage pve-qemu-system >= 4.1.1-alt1 swtpm swtpm-tools
BuildRequires: glib2-devel libjson-c-devel pve-common pve-guest-common >= 4.2.3 pve-firewall pve-ha-manager pve-doc-generator
BuildRequires: perl(Term/ReadLine.pm) perl(IO/Multiplex.pm) perl(JSON.pm) perl(Time/HiRes.pm) perl(UUID.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(XML/LibXML.pm) perl(Digest/SHA.pm) perl(URI/Escape.pm)

%description
%summary.
This package contains the Qemu Server tools used by Proxmox VE.

%prep
%setup

%build
%make_build qmeventd -C qmeventd

%install
%makeinstall_std
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

%files
%config(noreplace) %_sysconfdir/modules-load.d/qemu-server.conf
%_unitdir/qmeventd.service
%_unitdir/qmeventd.socket
%_prefix/lib/qemu-server
%_sbindir/*
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_datadir/qemu-server
%_localstatedir/qemu-server
%_man1dir/*
%_man5dir/*
%_man8dir/*

%perl_vendor_privlib/PVE/API2/*
%perl_vendor_privlib/PVE/CLI/*
%perl_vendor_privlib/PVE/QemuServer
%perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/*.pm

%changelog
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

