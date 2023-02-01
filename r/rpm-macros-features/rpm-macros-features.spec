Name: rpm-macros-features
Version: 0.9
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

install -D -m644 macros %buildroot/%_rpmmacrosdir/features
[ -n "$dfile" ] && [ -s "$dfile" ] && cat $dfile >> %buildroot/%_rpmmacrosdir/features

%files
%_rpmmacrosdir/features

%changelog
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
