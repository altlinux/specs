Name: rpm-macros-features
Version: 0.3
Release: alt1

Summary: RPM macros to check if can build with a feature
License: GPLv2
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch

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
install -D -m644 macros %buildroot/%_rpmmacrosdir/features

%files
%_rpmmacrosdir/features

%changelog
* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- implement if_feature FEATURE [VERSION]

* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
