Name: cpu-checker
Version: 0.7
Release: alt2

Summary: Tools to help evaluate certain CPU (or BIOS) features
License: GPLv3
Group: System/Kernel and hardware
Url: https://launchpad.net/cpu-checker

Source: %name-%version.tar
Patch0: %name-%version-launchpad-add-support-cortex-A15.patch
Patch1: %name-%version-launchpad-add-arm64-ppc64el-checks.patch
Patch2: %name-%version-launchpad-ppc64le-test-as-ppc64.patch
Patch3: %name-%version-launchpad-add-s390x-support.patch
Patch4: %name-%version-launchpad-add-riscv64-support.patch
Patch5: %name-%version-launchpad-add-loongarch64-support.patch

%description
Userspace tools for helping to evaluate the CPU (or BIOS) support for
various features.

%prep
%setup
%autopatch -p1

%build

%install
%makeinstall_std

%files
%_sbindir/check-bios-nx
%_sbindir/kvm-ok
%_man1dir/check-bios-nx.1.*
%_man1dir/kvm-ok.1.*

%changelog
* Mon Mar 03 2025 Anton Kurachenko <srebrov@altlinux.org> 0.7-alt2
- Added loongarch64 support.
- Totally replaced egrep by grep -E (#43193).

* Thu Feb 15 2024 Anton Kurachenko <srebrov@altlinux.org> 0.7-alt1
- New version 0.7.

* Fri Jul 07 2023 Anton Kurachenko <srebrov@altlinux.org> 0.6-alt2
- Cosmetic changes in the spec file.

* Sat Jun 10 2023 Anton Kurachenko <srebrov@altlinux.org> 0.6-alt1
- Initial build for ALT.
