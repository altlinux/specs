%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec
%define proxy_user backup

Name: proxmox-backup
Version: 2.2.6
Release: alt2
Epoch: 1
Summary: Proxmox Backup Server daemon with tools and GUI
License: AGPL-3.0+
Group: Archiving/Backup
URL: https://www.proxmox.com/en/proxmox-backup-server
Vcs: git://git.proxmox.com/git/proxmox-backup.git
Source: %name-%version.tar

Source6: basealt_logo.png
Source8: basealt_favicon.ico
Source9: basealt_logo-128.png

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd rpm-macros-javascript
BuildRequires: rpm-build-rust clang-devel

BuildRequires: libudev-devel libssl-devel libacl-devel libsystemd-devel libpam-devel libfuse3-devel libuuid-devel
BuildRequires: libsgutils-devel python3-module-sphinx python3-module-docutils python3-module-sphinx-sphinx-build-symlink
BuildRequires: proxmox-widget-toolkit-dev
BuildRequires: rsync
BuildRequires: /proc

%description
PVE Backup Server daemon with tools and GUI
This package contains the Proxmox Backup Server daemons and related
tools. This includes a web-based graphical user interface.

%package server
Summary: Proxmox Backup Server daemon with tools and GUI
Group: Archiving/Backup
Requires(pre): shadow-utils
Requires: %name-client = %EVR pve-xtermjs >= 4.12.0  pbs-i18n %name-docs
Requires: javascript-common javascript-extjs javascript-qrcodejs proxmox-widget-toolkit proxmox-mini-journalreader
Requires: lvm2 zfs-utils sg3_utils smartmontools gdisk
Requires: openssh-server
Provides: pve-backup-server = %EVR
Obsoletes: pve-backup-server < %EVR

%description server
This package contains the Proxmox Backup Server daemons and related
tools. This includes a web-based graphical user interface.

%package client
Summary: Proxmox Backup Client tools
Group: Archiving/Backup
Requires: qrencode
Provides: pve-backup-client = %EVR
Obsoletes: pve-backup-client < %EVR

%description client
This package contains the Proxmox Backup client, which provides a
simple command line tool to create and restore backups.

%package file-restore
Summary: Proxmox Backup single file restore tools for pxar and block device backups
Group: Archiving/Backup
Provides: pve-backup-file-restore = %EVR
Obsoletes: pve-backup-file-restore < %EVR

%description file-restore
This package contains the Proxmox Backup single file restore client for
restoring individual files and folders from both host/container and VM/block
device backups. It includes a block device restore driver using QEMU.

%package docs
Summary: Proxmox Backup Documentation
Group: Documentation
Requires: javascript-common javascript-extjs mathjax fonts-font-awesome
Buildarch: noarch

%description docs
This package contains the Proxmox Backup Documentation files.

%prep
%setup
rm -f docs/installation.rst

%build
export REPOID=alt
#%make_build PROXY_USER=%proxy_user
%make PROXY_USER=%proxy_user

%install
%makeinstall_std PROXY_USER=%proxy_user
%makeinstall_std -C docs install_html

install -m0644 %SOURCE6 %buildroot%_datadir/javascript/%name/images/basealt_logo.png
install -m0644 %SOURCE8 %buildroot%_datadir/javascript/%name/images/favicon.ico
install -m0644 %SOURCE9 %buildroot%_datadir/javascript/%name/images/logo-128.png

for d in api-viewer prune-simulator lto-barcode ; do
    ln -r -s %buildroot%_jsdir/extjs %buildroot%_datadir/doc/%name/html/$d/extjs
done
ln -r -s %buildroot%_datadir/fonts-font-awesome %buildroot%_datadir/doc/%name/html/lto-barcode/font-awesome
ln -r -s %buildroot%_jsdir/mathjax %buildroot%_datadir/doc/%name/html/_static/mathjax

install -dm755 %buildroot%_unitdir
for u in proxmox-backup.service proxmox-backup-proxy.service proxmox-backup-daily-update.service proxmox-backup-daily-update.timer ; do
    install -m644 etc/$u %buildroot%_unitdir/
done

install -dm755 %buildroot%_datadir/bash-completion/completions
pushd debian
for b in *.bc ; do
    install -m644 $b %buildroot%_datadir/bash-completion/completions/${b%%.*}
done
popd

mkdir -p %buildroot%_sysconfdir/%name
touch %buildroot%_sysconfdir/%name/{authkey.key,authkey.pub,csrf.key,proxy.key,proxy.pem,user.cfg}
mkdir -p %buildroot{%_logdir,%_localstatedir,%_cachedir}/%name
mkdir -p %buildroot%_localstatedir/backups

# Cleanup
rm -f %buildroot%_libexecdir/%name/%name-banner

%pre file-restore
groupadd -r -g 37 -f %proxy_user > /dev/null 2>&1 ||:
useradd -r -u 37 -g %proxy_user -M -d %_localstatedir/backups -s /dev/null -c "backup" %proxy_user > /dev/null 2>&1 ||:

%pre server
groupadd -r -g 37 -f %proxy_user > /dev/null 2>&1 ||:
useradd -r -u 37 -g %proxy_user -M -d %_localstatedir/backups -s /dev/null -c "backup" %proxy_user > /dev/null 2>&1 ||:
usermod -a -G tape %proxy_user ||:

%post server
%post_systemd_postponed %name.service %name-proxy.service

%preun server
%preun_systemd %name.service %name-proxy.service %name-daily-update.timer

%files server
%dir %attr(0700,%proxy_user,%proxy_user) %_sysconfdir/%name
%ghost %_sysconfdir/%name/*
%_bindir/pmt*
%_bindir/proxmox-tape
%_sbindir/proxmox-backup-manager
%_sbindir/proxmox-backup-debug
%dir %_libexecdir/%name
%_libexecdir/proxmox-backup/proxmox-backup-api
%_libexecdir/proxmox-backup/proxmox-backup-proxy
%_libexecdir/proxmox-backup/proxmox-daily-update
%attr(2511,root,%proxy_user) %_libexecdir/%name/sg-tape-cmd
%_jsdir/%name
%_datadir/zsh/vendor-completions/_pmt*
%_datadir/zsh/vendor-completions/_proxmox-tape
%_datadir/zsh/vendor-completions/_proxmox-backup-manager
%_datadir/zsh/vendor-completions/_proxmox-backup-debug
%_datadir/bash-completion/completions/pmt*
%_datadir/bash-completion/completions/proxmox-tape
%_datadir/bash-completion/completions/proxmox-backup-manager
%_datadir/bash-completion/completions/proxmox-backup-debug

%_unitdir/%name.service
%_unitdir/%name-proxy.service
%_unitdir/%name-daily-update.service
%_unitdir/%name-daily-update.timer
%dir %attr(0755,%proxy_user,%proxy_user) %_logdir/%name
%dir %attr(0755,%proxy_user,%proxy_user) %_localstatedir/%name
%dir %attr(0755,%proxy_user,%proxy_user) %_cachedir/%name
%dir %attr(2775,root,%proxy_user) %_localstatedir/backups
%_man1dir/pmt*.1*
%_man1dir/proxmox-tape.1*
%_man1dir/proxmox-backup-manager.1*
%_man1dir/proxmox-backup-proxy.1*
%_man1dir/proxmox-backup-debug.1*
%_man5dir/*.5*

%files client
%_bindir/pxar
%_bindir/proxmox-backup-client
%_datadir/zsh/vendor-completions/_pxar
%_datadir/zsh/vendor-completions/_proxmox-backup-client
%_datadir/bash-completion/completions/pxar
%_datadir/bash-completion/completions/proxmox-backup-client
%_man1dir/pxar.1*
%_man1dir/proxmox-backup-client.1*

%files file-restore
%_bindir/proxmox-file-restore
%_libexecdir/proxmox-backup/file-restore
%_datadir/zsh/vendor-completions/_proxmox-file-restore
%_datadir/bash-completion/completions/proxmox-backup-file-restore
%dir %attr(2775,root,%proxy_user) %_localstatedir/backups

%_man1dir/proxmox-file-restore.1*

%files docs
%_datadir/doc/%name

%changelog
* Thu Nov 17 2022 Andrew A. Vasilyev <andy@altlinux.org> 1:2.2.6-alt2
- disable repository/subscription status

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.2.6-alt1
- 2.2.6-1

* Wed Sep 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 1:2.2.1-alt2
- add BaseALT logo

* Thu May 19 2022 Andrew A. Vasilyev <andy@altlinux.org> 1:2.2.1-alt1
- 2.2.1-1

* Fri May 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 1:2.1.10-alt1
- 2.1.10-1

* Sat Apr 16 2022 Andrew A. Vasilyev <andy@altlinux.org> 1:2.1.5-alt3
- spec: fix build with rst2man

* Thu Mar 31 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.5-alt2
- add backup system user with UID=37 for server and file-restore
- fix execute post/preun scripts for server

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.5-alt1
- 2.1.5-1

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.4-alt1
- 2.1.4
- rename pve-backup to proxmox-backup
- build proxmox-backup-qemu from separate package
- build pbs-i18n from separate package
- add docs package as noarch
- build for all support arch
- package proxmox-backup-debug to server
- package proxmox-daily-update to server
- package bash-completions files
- add post and preun rpm scripts
- add requires on gdisk to server (ALT #41597)
- build from gear

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

