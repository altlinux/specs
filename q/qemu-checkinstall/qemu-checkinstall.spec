# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: qemu-checkinstall
Summary: QA tests for QEMU
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Other

ExclusiveArch: aarch64 armh x86_64 %ix86 ppc64le
BuildArch: noarch
Source: %name-%version.tar

Requires(post): rpm-build-vm
Requires(post): toilet
BuildRequires: rpm-build-vm
BuildRequires: toilet

%description
Non-comprehensive smoke tests for QEMU.

%prep
%setup

%install
install -Dp qemu-ci-tests.sh -t %buildroot%_libexecdir/%name

# Run once after QEMU and after package creation (under rooter).
%post -p %_libexecdir/%name/qemu-ci-tests.sh

%check
# Run once after package creation and periodically in ALT beekeeper (under builder).
./qemu-ci-tests.sh

%files
%_libexecdir/%name

%changelog
* Wed Dec 28 2022 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version doing basic testing.
