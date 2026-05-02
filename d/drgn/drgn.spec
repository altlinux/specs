# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    drgn
Version: 0.2.0
Release: alt1
Summary: Programmable debugger
License: LGPL-2.1-or-later
Group:   Development/Debuggers
URL:     https://drgn.readthedocs.io
Vcs:     https://github.com/osandov/drgn
# Docs:  https://drgn.readthedocs.io/en/latest/
# Refs:  https://www.kernel.org/doc/html/latest/bpf/drgn.html
# LWN:   https://lwn.net/Articles/789641/ (LSFMM 2019)
# Conf:  https://linuxplumbersconf.org/event/4/contributions/440/ (LPC 2019)
# Intro: https://youtu.be/ukxH_55BiQE (KR 2022)
# LWN:   https://lwn.net/Articles/952942/ (LPC 2023)
Provides: python3-module-drgn

Source: %name-%version.tar

BuildRequires(pre): kernel-%kernel_latest
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): rpm-build-python3
BuildRequires: bzip2-devel
BuildRequires: flex
BuildRequires: libdebuginfod-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libgomp-devel
BuildRequires: libjson-c-devel
BuildRequires: libkdumpfile-devel
BuildRequires: liblzma-devel
BuildRequires: libpcre2-devel
BuildRequires: libstdc++-devel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-wheel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: libcheck-devel
BuildRequires: /proc
}}
# Note: Bundled with own version of elfutils.

%description
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python. For example, you can debug the Linux kernel (as an
alternative to the crash utility).

Note: Requires debuginfo package installed to work.

%package -n kernel-ci-drgn-debuginfo
Summary: CI test for %name
Group: Development/Other
Requires(post): drgn = %EVR
Requires(post): rpm-build-vm
Requires(post): %(rpm -qa 'kernel-image-*' --qf '%%{NAME}-debuginfo' | grep . || echo unknown)

%description -n kernel-ci-drgn-debuginfo
%summary with a workaround for 'sisyphus_check: check-deps ERROR: package
dependencies violation' for a kernel-image.

%prep
%setup
sed -i '/local_version/s/+unknown/+%release/' setup.py
# Tries network access.
sed -i '/sphinx.ext.intersphinx/d' docs/conf.py
# Man page does not need this since package is already installed.
sed -Ei /^[[:space:]]+installation/d docs/index.rst

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build
%__python3 -m sphinx -bman docs/ build/man

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
mkdir -p %buildroot%_datadir/drgn
cp -r contrib tools -t %buildroot%_datadir/drgn
install -Dpm644 build/man/drgn.1 -t %buildroot%_man1dir
# Python code of doc generator.
rm -r docs/exts docs/conf.py

%check
test -d /proc/self
# Build-in tests (require /proc)
%__python3 setup.py test

# Simple test
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/drgn --version

# Naive live-testing in %%check with vm-run does not work becasuf of no debuginfo:
#    warning: could not get debugging information for:
#    kernel (could not find vmlinux for 6.4.14-un-def-alt1)
#    kernel modules (could not find loaded kernel modules: could not find 'struct module')
%ifnarch armh
# armh: [Errno 2] No such file or directory: '/proc/kcore'
#   config PROC_KCORE
#           bool "/proc/kcore support" if !ARM
%post -n kernel-ci-drgn-debuginfo
set -ex
# ppc64le: Exception: virtual address translation is only supported for Radix MMU
vm-run --heredoc <<-EOF
	%_datadir/drgn/contrib/lsmod.py
%ifnarch ppc64le
	drgn %_datadir/drgn/contrib/platform_drivers.py
%endif
EOF
rm -f /tmp/initramfs-*.img /tmp/vm.*
%endif

%files
%define _customdocdir %_docdir/%name
%doc COPYING LICENSES README.rst docs
%_bindir/drgn
%_bindir/drgn-crash
%_datadir/drgn
%_man1dir/drgn.1*
%python3_sitelibdir/*drgn*

# warning: package with no files has %post-script
%files -n kernel-ci-drgn-debuginfo

%changelog
* Sat May 02 2026 Vitaly Chikunov <vt@altlinux.org> 0.2.0-alt1
- Update to v0.2.0 (2026-04-29).

* Fri Feb 20 2026 Vitaly Chikunov <vt@altlinux.org> 0.1.0-alt1
- Update to v0.1.0 (2026-02-19).
- Linux 6.19 and tentative 7.0 support.

* Thu Oct 30 2025 Vitaly Chikunov <vt@altlinux.org> 0.0.33-alt1
- Update to v0.0.33 (2025-10-29).
- Linux 6.17 and 6.18 support.
- No More Python 3.6 & 3.7 support.

* Thu Jun 19 2025 Vitaly Chikunov <vt@altlinux.org> 0.0.32-alt1
- Update to v0.0.32 (2025-06-18).
- Linux 6.16 support.
- Last release with Python 3.6 & 3.7 support.

* Sat Apr 19 2025 Vitaly Chikunov <vt@altlinux.org> 0.0.31-alt1
- Update to v0.0.31-1-g3977bdc7 (2025-04-19).
- Linux 6.14 and 6.15 support.

* Tue Feb 25 2025 Vitaly Chikunov <vt@altlinux.org> 0.0.30-alt2
- spec: Remove dependence on kernel-image-6.6.
- Linux 6.13 support.

* Thu Dec 19 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.30-alt1
- Update to v0.0.30 (2024-12-18).

* Thu Oct 31 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.29-alt3
- Remove dependency on kernel-image-un-def.

* Thu Oct 17 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.29-alt2
- spec: Change kernel for checkinstall preparing for removal of un-def.

* Wed Oct 09 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.29-alt1
- Update to v0.0.29 (2024-10-08).
- Linux 6.11 and 6.12 support (since 0.0.28).

* Fri Jul 05 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.27-alt1
- Update to v0.0.27 (2024-07-01).
- Linux 6.9 and 6.10 support.

* Wed Mar 13 2024 Vitaly Chikunov <vt@altlinux.org> 0.0.26-alt1
- Update to v0.0.26 (2024-03-11).
- Linux 6.8 support, Python 3.13 support.

* Sun Dec 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.0.25-alt1
- Update to v0.0.25 (2023-12-01).
- spec: Update License tag (upstream relicense).
- spec: Add CI package with live-debugging smoke tests.
- spec: Generate and install man page drgn(1).

* Tue Sep 26 2023 Vitaly Chikunov <vt@altlinux.org> 0.0.24-alt1
- Update to v0.0.24 (2023-09-08).
- Linux 6.3 & 6.4 support, Python 3.12 support.

* Wed Sep 06 2023 Vitaly Chikunov <vt@altlinux.org> 0.0.23-alt1
- Update to v0.0.23 (2023-06-28).

* Wed Nov 23 2022 Vitaly Chikunov <vt@altlinux.org> 0.0.21-alt1
- Update to v0.0.21 (2022-10-12).

* Sun Dec 26 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.16-alt1
- Updated to v0.0.16 (2021-12-09).
- Built on all architectures.

* Sun Jun 20 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.13-alt1
- Update to v0.0.13 (2021-06-07) -4-gc4b174a (2021-06-09).

* Thu Feb 18 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.9-alt1
- Update to v0.0.9 (2021-02-17).

* Thu Dec 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.8-alt1
- Update to v0.0.8 (2020-11-11) -3-g5975d19 (2020-10-28).

* Tue Jul 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.7-alt1
- Update to v0.0.7 (2020-07-27).

* Wed Jun 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.5-alt1
- First import of v0.0.5 (2020-05-26).
