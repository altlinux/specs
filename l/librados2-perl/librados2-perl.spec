Name: librados2-perl
Summary: Perl bindings for librados
Version: 1.0.4
Release: alt2%ubt
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64

Source: librados2-perl-1.0-4.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: pve-common librados2-devel perl-devel perl(PVE/RPCEnvironment.pm) perl(JSON.pm)

%description
This package contains librados perl binding used by PVE

%prep
%setup -q

%install
%make DESTDIR=%buildroot install

%files
%perl_vendor_privlib/PVE
%perl_vendor_autolib/PVE

%changelog
* Wed Jan 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2%ubt
- rebuild

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt0.M80C.1
- backport to c8 branch

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt0.M80P.1
- backport to p8 branch

* Mon Jul 17 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0-4

* Tue Feb 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- rebuild with perl 5.24.1

* Wed Dec 09 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- initial release

