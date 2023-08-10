Name: distro_check
Version: 0.0.3
Release: alt1

Summary: distribution checker for Sisyphus
License: GPLv2+
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: getopt, cdrkit-utils
Requires: distro-licenses >= 1.1

%description
This package contains distro_check utility.

%prep
%setup

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 distro-check-functions \
	%buildroot%_bindir/distro-check-functions

mkdir -p -- %buildroot%_sysconfdir/%name
cp -a -- distro_check.d %buildroot%_sysconfdir/%name/check.d

%files
%config %_sysconfdir/%name
%_bindir/*

%changelog
* Fri Jul 07 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Fix check of mime type for images.

* Sat May 13 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.0.2-alt1
- Add support of distro-license-check name validation tool.

* Wed Apr 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt1
- Inital release for Sisyphus
