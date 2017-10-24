Name: kdc-test
Version: 0.0.1
Release: alt1

Summary: KDC High-Load Testing Suite
License: GPLv2+
Group: Networking/Other

Url: https://www.altlinux.org/ActiveDirectory/DC
Source: %name-%version.tar

Requires: libkrb5
BuildPreReq: libkrb5-devel

%description
This package provides KDC high-load testing suite.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_bindir/kdc-test

%changelog
* Tue Oct 24 2017 Leonid Krivoshein <klark@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus.

