Name: apt-printchanges
Version: 0.02
Release: alt1

Summary: Print last changelog for each installed/upgraded package
License: GPLv3+
Group: System/Configuration/Packaging

BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar

Requires: python3-module-rpm

%description
Print last changelog for each installed/upgraded package
%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -p -m755 %name %buildroot%_bindir/
install -pD -m644 apt.conf %buildroot/etc/apt/apt.conf.d/20-%name.conf

%files
%_bindir/*
%config(noreplace) /etc/apt/apt.conf.d/*

%changelog
* Sun Nov 24 2019 Terechkov Evgenii <evg@altlinux.org> 0.02-alt1
- Port to python3

* Wed Dec 14 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.01.1-alt1
- Fix for new rpm python module.

* Fri Feb 10 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt3
- Format changelog record exactly as rpm do (date added)

* Wed Feb  8 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt2
- Concat changelog for same packager/description pairs

* Sun Jan 29 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt1
- Initial build for ALT Linux Sisyphus
