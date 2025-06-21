# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: kdump-tools
Summary: Scripts and configuration files to use kdump
Version: 1.10.7
Release: alt10
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
BuildRequires(pre): kernel-%kernel_latest
BuildRequires(pre): rpm-build-kernel
BuildRequires: pandoc
%{?!_without_check:%{?!_disable_check:
%ifarch %ix86 x86_64
# There is no shellcheck on other arches in p9.
BuildRequires: shellcheck
%endif
}}

%description
Scripts and tools for automating kdump (Linux crash dumps) kdump-tools
provides an init script and a configuration script for automating the
use of kdump. It uses the makedumpfile utility to reduce the size of
the /proc/vmcore file based on user preferences.

After installing, please see /usr/share/doc/%name/README
for information on enabling and configuring kdump.

%package -n kernel-ci-%name-debuginfo
Summary: CI test for %name
Group: Development/Other
Requires(post): crash
Requires(post): make-initrd
Requires(post): %name = %EVR
Requires(post): rpm-build-vm
Requires(post): %(rpm -qa 'kernel-image-*' --qf '%%{NAME}-debuginfo' | grep . || echo unknown)
Requires(post): systemd-sysvinit

%description -n kernel-ci-%name-debuginfo
%summary with a workaround for 'sisyphus_check: check-deps ERROR: package
dependencies violation' for a kernel-image.

%prep
%setup

%build
%make_build

%install
%makeinstall_std UDEVRULESDIR=%_udevrulesdir UNITDIR=%_unitdir
%define _customdocdir %_docdir/%name
%ifnarch %testable_arches
# Avoid 'Installed (but unpackaged) file(s) found'.
rm %buildroot%_libexecdir/kdump-tools-checkinstall.sh
%endif

%check
# Shall not appear accidentally.
! grep -r '/etc/default' --exclude='.*' %buildroot || exit 2
# NB: We intentionally don't install /var/lib/kdump selecting the internal logic
# based on its absence.
! test -e %buildroot/var/lib/kdump || exit 3
%ifarch %ix86 x86_64
make shellcheck
%endif
# NB: Releases should monotonically increment. While we can't verify they never
# decrement, we can ensure they don't unintentionally reset to alt1.
grep -vw alt1 <<<'%release'

%post -n kernel-ci-%name-debuginfo -p %_libexecdir/kdump-tools-checkinstall.sh

%ifarch %testable_arches
%files -n kernel-ci-%name-debuginfo
%_libexecdir/kdump-tools-checkinstall.sh
%endif

%files
%doc README debian/changelog debian/copyright
%config(noreplace) %_sysconfdir/sysconfig/kdump-tools
%_bindir/kdumpctl
%_sbindir/kdump-config
%_udevrulesdir/50-kdump-tools.rules
%_sysconfdir/rc.d/init.d/kdump-tools
%_datadir/%name
%_unitdir/kdump*.service
%_man5dir/kdump-tools.5*
%_man8dir/kdump-config.8*
%_man1dir/kdumpctl.1*
%dir /var/crash

%changelog
* Sat Jun 21 2025 Vitaly Chikunov <vt@altlinux.org> 1.10.7-alt10
- kdumpctl: Fix finding vmlinux when there is .build-id symlink.
- Sync with 1.10.7 (2025-05-01).

* Mon Jun 09 2025 Vitaly Chikunov <vt@altlinux.org> 1.8-alt9
- kdumpctl debug: Workaround absence of .build-id symlink for vmlinux.
- checkinstall: Add smoke test for 'kdumpctl debug'.
- spec: Remove optional dependencies to busybox, bzip2, crash, gzip, iproute2,
  lz4, ssh.

* Sat Nov 02 2024 Vitaly Chikunov <vt@altlinux.org> 1.8-alt8
- checkinstall: Fallback to grep for file4.

* Mon Aug 19 2024 Vitaly Chikunov <vt@altlinux.org> 1.8-alt7
- Fix build with old shellcheck (for p9).

* Wed Aug 14 2024 Vitaly Chikunov <vt@altlinux.org> 1.8-alt6
- Some compatibility with older branches (shellcheck, udevrulesdir).

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
