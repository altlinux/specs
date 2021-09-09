Name: rpm-macros-features
Version: 0.1
Release: alt1

Summary: RPM macros to check if can build with a feature
License: GPLv2
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch

%description
RPM macros to check if can build with a feature (a library is possible).

Usage:
if_with feature_vulkan
BuildRequires: libvulkan-devel
endif

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/features

%files
%_rpmmacrosdir/features

%changelog
* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
