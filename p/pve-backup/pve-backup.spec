%define _libexecdir /usr/libexec
%define proxy_user backup

Name: pve-backup
Version: 2.0.1
Release: alt4
Epoch: 1
Summary: PVE Backup Server
License: GPL-1 and LGPLv2 and BSD
Group: Archiving/Backup
URL: https://www.proxmox.com/en/proxmox-backup-server

Source0: proxmox-0.11.5.tar.xz
Source1: proxmox-backup-2.0.1.tar.xz
Source2: proxmox-acme-rs-0.2.1.tar.xz
Source3: proxmox-openid-rs-0.6.0.tar.xz
Source4: proxmox-fuse.tar.xz
Source5: pxar.tar.xz
Source6: proxmox-backup-qemu-1.2.0.tar.xz
Source10: cargo.tar.xz
Source11: basealt_logo-128.png
Source12: basealt_logo.png

Source100: pve-i18n.tar.xz
Source101: proxmox-backup-js.tar

Patch0: proxmox-backup-alt.patch
Patch1: proxmox-openid-rs-alt.patch
Patch2: proxmox-backup-qemu-alt.patch
Patch3: proxmox-backup-alt-libexec.patch
Patch4: proxmox-backup-widgettoolkit.patch
Patch5: proxmox-backup-auth.patch
Patch6: proxmox-backup-sshkeypath.patch
Patch7: proxmox-backup-rm-subscription.patch
Patch8: pve-i18n-pbs.patch
Patch9: proxmox-backup-docs-rm-pdf.patch

ExclusiveArch: x86_64 aarch64

BuildRequires: /proc clang-devel git-core rust-cargo libudev-devel libssl-devel libacl-devel libsystemd-devel libpam-devel libfuse3-devel libuuid-devel
BuildRequires: libsgutils-devel python3-module-sphinx python3-module-docutils python3-module-sphinx-sphinx-build-symlink
BuildRequires: perl(JSON.pm) perl(Locale/PO.pm)

%description
PVE Backup Server daemon with tools and GUI
This package contains the Proxmox Backup Server daemons and related
tools. This includes a web-based graphical user interface.

%package server
Summary: PVE backup server
Group: Archiving/Backup
Requires(pre): shadow-utils
Requires: javascript-common %name-client = %EVR pve-xtermjs >= 4.12.0 pve-widget-toolkit pve-mini-journalreader lvm2 zfs-utils
Provides: proxmox-backup-server = %EVR

%description server
This package provides PVE Backup Server.

%package client
Summary: PVE backup client
Group: Archiving/Backup
Provides: proxmox-backup-client = %EVR

%description client
This package provides PVE Backup client.

%package file-restore
Summary: PVE backup single file restore tools
Group: Archiving/Backup
Provides: proxmox-backup-file-restore = %EVR

%description file-restore
This package contains the PVE Backup single file restore client for
restoring individual files and folders from both host/container and VM/block
device backups. It includes a block device restore driver using QEMU.

%package -n libpve-backup-qemu
Summary: PVE Backup Server client library for QEMU
Group: System/Libraries
Version: 1.2.0
Provides: libproxmox-backup-qemu0 = %EVR

%description -n libpve-backup-qemu
PVE Backup Server client library for QEMU
This library contains the library to access the Proxmox Backup server from
within QEMU.

%package -n libpve-backup-qemu-devel
Summary: PVE Backup Server development environment
Group: Development/Other
Version: 1.2.0

%description -n libpve-backup-qemu-devel
PVE Backup Server development environment.

%prep
%setup -q -c -n %name -a1 -a2 -a3 -a4 -a5 -a6 -a10 -a100 -a101
%patch0 -p0 -b .alt
%patch1 -p0
%patch2 -p0
%patch3 -p0 -b .libexec
%patch4 -p0 -b .wt
%patch5 -p0 -b .auth
%patch6 -p0 -b .sshkey
%patch7 -p0 -b .subscr
%patch8 -p0
%patch9 -p0 -b .rmpdf

rm -f */.cargo/config
rm -f proxmox-backup/docs/installation.rst

%build
export CARGO_HOME=%_builddir/%name/cargo
cd proxmox-backup-qemu
cargo build --release --offline
make -C %_builddir/%name/proxmox-backup PROXY_USER=%proxy_user
make -C %_builddir/%name/pve-i18n

%install
make -C proxmox-backup DESTDIR=%buildroot install
make -C proxmox-backup/docs DESTDIR=%buildroot install_html

for d in api-viewer prune-simulator lto-barcode ; do
	ln -s ../../../../javascript/extjs %buildroot%_datadir/doc/proxmox-backup/html/$d/extjs
done
ln -s ../../../../fonts-font-awesome %buildroot%_datadir/doc/proxmox-backup/html/lto-barcode/font-awesome

make -C pve-i18n DESTDIR=%buildroot install

install -pD -m644 proxmox-backup-qemu/proxmox-backup-qemu.h %buildroot%_includedir/proxmox-backup-qemu.h
install -pD -m644 proxmox-backup-qemu/target/release/libproxmox_backup_qemu.so %buildroot%_libdir/libproxmox_backup_qemu.so.0
ln -s libproxmox_backup_qemu.so.0 %buildroot%_libdir/libproxmox_backup_qemu.so

install -dm755 %buildroot%_unitdir
for u in proxmox-backup.service proxmox-backup-proxy.service ; do
    install -m644 proxmox-backup/etc/$u %buildroot%_unitdir/
done

install -m644 %SOURCE11 %buildroot%_datadir/javascript/proxmox-backup/images/logo-128.png
install -m644 %SOURCE12 %buildroot%_datadir/javascript/proxmox-backup/images/basealt_logo.png

mkdir -p %buildroot/%_sysconfdir/proxmox-backup
touch %buildroot/%_sysconfdir/proxmox-backup/{authkey.key,authkey.pub,csrf.key,proxy.key,proxy.pem,user.cfg}
mkdir -p %buildroot/{%_logdir,%_cachedir}/proxmox-backup

%pre server
grep -q "^%proxy_user:" %_sysconfdir/group || %_sbindir/groupadd -r -f %proxy_user ||:
grep -q "^%proxy_user:" %_sysconfdir/passwd || %_sbindir/useradd -g %proxy_user -c 'PBS proxy user' -d /tmp -s /sbin/nologin -r %proxy_user ||:

%files server
%dir %attr(0700,%proxy_user,%proxy_user) %_sysconfdir/proxmox-backup
%ghost %_sysconfdir/proxmox-backup/*
%_bindir/pmt*
%_bindir/proxmox-tape
%_sbindir/proxmox-backup-manager
%dir %_libexecdir/proxmox-backup
%_libexecdir/proxmox-backup/proxmox-backup-api
%_libexecdir/proxmox-backup/proxmox-backup-proxy
%attr(2511,root,%proxy_user) %_libexecdir/proxmox-backup/sg-tape-cmd
%_datadir/javascript/proxmox-backup
%_datadir/pbs-i18n
%_datadir/zsh/vendor-completions/_pmt*
%_datadir/zsh/vendor-completions/_proxmox-tape
%_datadir/zsh/vendor-completions/_proxmox-backup-manager
%_datadir/doc/proxmox-backup
%_unitdir/proxmox-backup.service
%_unitdir/proxmox-backup-proxy.service
%dir %attr(0755,%proxy_user,%proxy_user) %_logdir/proxmox-backup
%dir %_cachedir/proxmox-backup
%_man1dir/pmt*.1*
%_man1dir/proxmox-tape.1*
%_man1dir/proxmox-backup-manager.1*
%_man1dir/proxmox-backup-proxy.1*
%_man5dir/*.5*

%files client
%_bindir/pxar
%_bindir/proxmox-backup-client
%_datadir/zsh/vendor-completions/_pxar
%_datadir/zsh/vendor-completions/_proxmox-backup-client
%_man1dir/pxar.1*
%_man1dir/proxmox-backup-client.1*

%files file-restore
%_bindir/proxmox-file-restore
%_libexecdir/proxmox-backup/file-restore
%_datadir/zsh/vendor-completions/_proxmox-file-restore
%_man1dir/proxmox-file-restore.1*

%files -n libpve-backup-qemu
%_libdir/libproxmox_backup_qemu.so.0

%files -n libpve-backup-qemu-devel
%_includedir/*
%_libdir/libproxmox_backup_qemu.so

%changelog
* Tue Nov 09 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.1-alt4
- fixed html docs

* Mon Nov 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 1:2.0.1-alt3
- build with html docs

* Sun Nov 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.1-alt2
- updated required packages 

* Wed Sep 29 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.1-alt1
- 2.0.1

* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.5-alt2
- FTBFS: new rust (ALT #40521)

* Tue Feb 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.5-alt1
- initial build for ALT

