Name: bluez-hcidump
Version: 2.0
Release: alt1

Summary: HCI packet analyzer
License: GPLv2+
Group: Networking/Other

Url: http://www.bluez.org/
Source: %name-%version.tar.gz
Patch: bluez-hcidump-fix-compile.patch
Packager: Mobile Development Team <mobile@packages.altlinux.org>

BuildRequires: libbluez-devel

%description
HCI packet analyzer for BlueZ

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog README
%_sbindir/*
%_man8dir/*

%changelog
* Thu May 05 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Sun Dec 19 2010 Michael Shigorin <mike@altlinux.org> 1.42-alt3
- BR: libbluez-devel

* Sat May 23 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.42-alt2
- rebuild with libbluez4

* Sat Jun 21 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.42-alt1
- 1.42

* Sat Feb 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.41-alt1
- 1.41

* Fri Aug 10 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.40-alt1
- 1.40

* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.39-alt1
- 1.39

* Thu Jul 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.37-alt1
- 1.37

* Sun Jun 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.36-alt1
- 1.36

* Thu May 10 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.35-alt1
- 1.35

* Tue Feb 27 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.34-alt1
- 1.34
- enable PIE

* Tue Nov 07 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.33-alt2
- Sisyphus build
- fix buildreqs

* Fri Oct 27 2006 Igor Zubkov <icesik@altlinux.org> 1.33-alt1
- 1.32 -> 1.33
- add packager tag
- change license to GPL
- remove COPYING from docs
- move libbluez-devel from BuildRequres to BuildPreReq
- bump libbluez-devel version to 3.3
- buildreq

* Wed Aug 23 2006 Grigory Milev <week@altlinux.ru> 1.32-alt1
- new version released

* Tue Feb 21 2006 Grigory Milev <week@altlinux.ru> 1.30-alt1
- new verion relesed

* Mon Aug 22 2005 Grigory Milev <week@altlinux.ru> 1.24-alt1
- new version released

* Tue Mar 15 2005 Grigory Milev <week@altlinux.ru> 1.18-alt2
- fix build requires

* Mon Mar 14 2005 Grigory Milev <week@altlinux.ru> 1.18-alt1
- new version released

* Wed Jan 12 2005 Grigory Milev <week@altlinux.ru> 1.16-alt2
- fixed build requires

* Tue Jan 11 2005 Grigory Milev <week@altlinux.ru> 1.16-alt1
- new version released

* Thu Sep 23 2004 Grigory Milev <week@altlinux.ru> 1.12-alt1
- new version released

* Mon Jun 21 2004 Grigory Milev <week@altlinux.ru> 1.9-alt1
- new version released

* Wed Mar  5 2003 Grigory Milev <week@altlinux.ru> 1.5-alt1
- Initial build for ALT Linux

