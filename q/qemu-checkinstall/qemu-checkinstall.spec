# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: qemu-checkinstall
Summary: QA tests for QEMU
Version: 3
Release: alt1
License: GPL-2.0-only
Group: Other

ExclusiveArch: aarch64 armh x86_64 %ix86 ppc64le
Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: qa-qemu-vmlinuz
BuildRequires: qemu
BuildRequires: rpm-build-vm
BuildRequires: toilet
Requires(post): /proc
Requires(post): qa-qemu-vmlinuz
Requires(post): qemu
Requires(post): rpm-build-vm
Requires(post): toilet

%description
Non-comprehensive smoke tests for QEMU.

%package -n qemu-common-checkinstall
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description -n qemu-common-checkinstall
%summary.

%prep
%setup

%install
install -Dp qemu-ci-tests.sh -t %buildroot%_libexecdir/%name

# Run once after QEMU and after package creation (under rooter).
%post -n qemu-common-checkinstall -p %_libexecdir/%name/qemu-ci-tests.sh

%check
# Run once after package creation and periodically in ALT beekeeper (under builder).
./qemu-ci-tests.sh

%files -n qemu-common-checkinstall
%_libexecdir/%name

%changelog
* Sun Dec 17 2023 Vitaly Chikunov <vt@altlinux.org> 3-alt1
- Move tests into qemu-common-checkinstall.

* Fri Jan 13 2023 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Test TCG for main architectures.

* Wed Dec 28 2022 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version doing basic testing.
