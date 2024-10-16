Name: rpm-macros-features
Version: 20240408
Release: alt1

Summary: RPM macros to check if can build with a feature
License: GPLv2
Group: Development/Other

Source: %name-%version.tar

Obsoletes: rpm-build-features
Provides: rpm-build-features

%description
RPM macros to check if can build with a feature (a library is possible).

Usage:
if_feature vulkan
BuildRequires: libvulkan-devel
endif

if_feature icu 6.5
...
endif

if_notfeature python3 3.10
...
endif

%prep
%setup

%install
dfile=''

dfile=macros.%_arch

%ifarch %e2k
dfile=macros.e2k
%endif

%ifarch %ix86
dfile=macros.i586
%endif

%ifarch %mips32
dfile=macros.mips32
%endif

%ifarch %arm
dfile=macros.arm
%endif

%ifarch loongarch64
dfile=macros.loongarch64
%endif

install -D -m644 macros %buildroot/%_rpmmacrosdir/features
[ -n "$dfile" ] && [ -s "$dfile" ] && cat $dfile >> %buildroot/%_rpmmacrosdir/features

%files
%_rpmmacrosdir/features

%changelog
* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 20240408-alt1
- add qt6_webengine feature
- macros: add osmesa, webkit2gtk
- macros: update versions

* Tue Feb 27 2024 Vitaly Lipatov <lav@altlinux.ru> 20240227-alt1
- add glusterfs feature
- add numactl feature

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 20240217-alt1
- add if_notfeature
- add python3, wine features

* Tue Feb 06 2024 Vitaly Lipatov <lav@altlinux.ru> 20240206-alt1
- update features' versions

* Sun Jan 14 2024 Anton Farygin <rider@altlinux.ru> 20240114-alt1
- removed php 8.0
- added php 8.3

* Tue Oct 24 2023 Ivan A. Melnikov <iv@altlinux.org> 20231024-alt1
- no php8.0 on loongarch64

* Mon Aug 21 2023 Ivan A. Melnikov <iv@altlinux.org> 20230821-alt1
- loongarch64 support
- enable OpenCV on riscv64
- update glibc feature version

* Fri Aug 04 2023 Vitaly Lipatov <lav@altlinux.ru> 20230804-alt1
- switch to date stamp release
- update features' versions, add gcc, glibc, glib2, glibmm

* Thu Jul 27 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add ctest, cmake, wayland, clickhouse, kernel
- add opencv 4.7.0

* Thu Mar 16 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- sisyphus: step dotnet version to 7.0
- add mono and gtk_sharp features
- add arm, mips32 and i586 support
- sisyphus: update versions for all features

* Sun Jan 29 2023 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- add php8.2 feature

* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add php presence flags

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- add arch dependend part for feature macros

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- add unwind 1.5.0

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- add pcad and llvm versions

* Fri Oct 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- set versions for qt5 and vkd3d
- add provides/obsoletes for rpm-build-features

* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- implement if_feature FEATURE [VERSION]

* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
