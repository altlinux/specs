# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: kdump-tools
Summary: Scripts and configuration files to use kdump
Version: 1.8
Release: alt5
Group: System/Kernel and hardware
License: GPL-2.0-or-later
Vcs: https://salsa.debian.org/debian/kdump-tools.git

%define testable_arches x86_64 aarch64 ppc64le

Requires: /sbin/kexec
Requires: file
Requires: lsb-init
Requires: procps
%filter_from_requires /busybox\|ssh\|scp\|reboot\|systemctl\|lib\/lsb\/init-functions/d

Source: %name-%version.tar
BuildRequires: pandoc
%{?!_without_check:%{?!_disable_check:
BuildRequires: shellcheck
}}

%description
Scripts and tools for automating kdump (Linux crash dumps) kdump-tools
provides an init script and a configuration script for automating the
use of kdump. It uses the makedumpfile utility to reduce the size of
the /proc/vmcore file based on user preferences.

After installing, please see /usr/share/doc/%name/README
for information on enabling and configuring kdump.

%package checkinstall
Summary: QA test for %name
Group: Development/Other
Requires: %name = %EVR
Requires: make-initrd
Requires: rpm-build-vm
Requires: systemd-sysvinit

%description checkinstall
%summary.

%prep
%setup

%build
%make_build

%install
%makeinstall_std UDEVRULESDIR=%_udev_rulesdir UNITDIR=%_unitdir
%define _customdocdir %_docdir/%name
%ifnarch %testable_arches
# Avoid 'Installed (but unpackaged) file(s) found'.
rm %buildroot%_libexecdir/kdump-tools/kdump-checkinstall.sh
%endif

%check
# Shall not appear accidentally.
! grep -r '/etc/default' --exclude='.*' %buildroot || exit 2
make shellcheck
# NB: Releases should monotonically increment. While we can't verify they never
# decrement, we can ensure they don't unintentionally reset to alt1.
grep -vw alt1 <<<'%release'

%post checkinstall -p %_libexecdir/kdump-tools/kdump-checkinstall.sh

%ifarch %testable_arches
%files checkinstall
%_libexecdir/kdump-tools/kdump-checkinstall.sh
%endif

%files
%doc README debian/changelog debian/copyright
%config(noreplace) %_sysconfdir/sysconfig/kdump-tools
%_bindir/kdumpctl
%_sbindir/kdump-config
%_udevrulesdir/50-kdump-tools.rules
%_sysconfdir/init.d/kdump-tools
%_unitdir/kdump*.service
%_man5dir/kdump-tools.5*
%_man8dir/kdump-config.8*
%_man1dir/kdumpctl.1*
%dir /var/crash
# NB: We don't install /var/lib/kdump

%changelog
* Sun Jun 23 2024 Vitaly Chikunov <vt@altlinux.org> 1.8-alt5
- Fix FTBFS after usrmerge related changes to systemd.
- Add kdumpctl(1) man page.

* Sat Apr 15 2023 Vitaly Chikunov <vt@altlinux.org> 1.8-alt4
- Fix (ALT beekeeper) rebuild after shellcheck update.

* Sun Dec 04 2022 Vitaly Chikunov <vt@altlinux.org> 1.8-alt3
- Secure permissions for dumps.
- Remove timestamp out of dump/dmesg file extensions, and rename 'dump'
  to 'kdump' and 'dmesg' to 'dmesg.txt'.
- Local Kdumps are not flattened anymore.
- spec: Refactor checkinstall.

* Fri Nov 25 2022 Vitaly Chikunov <vt@altlinux.org> 1.8-alt2
- Add kdumpctl tool to view or debug kdumps.

* Tue Nov 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- First import and adaptation for ALT.
