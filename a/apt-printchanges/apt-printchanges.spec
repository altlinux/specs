Name: apt-printchanges
Version: 0.01
Release: alt3

Summary: Print last changelog for each installed/upgraded package
License: GPLv3+
Group: System/Configuration/Packaging

BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar

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
* Fri Feb 10 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt3
- Format changelog record exactly as rpm do (date added)

* Wed Feb  8 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt2
- Concat changelog for same packager/description pairs

* Sun Jan 29 2012 Terechkov Evgenii <evg@altlinux.org> 0.01-alt1
- Initial build for ALT Linux Sisyphus
