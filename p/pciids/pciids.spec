Name: pciids
Version: 20120626
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Repository of PCI IDs (pci.ids database)
License: GPLv2+ or BSD
Group: System/Libraries

Url: http://pciids.sourceforge.net
Source: %url/pci.ids
Patch: hwdatabase.ti24.patch

BuildArch: noarch

%description
This package contains a public list of all known IDs used in PCI devices: ID's
of vendors, devices, subsystems and device classes. It is used in various
programs to display full human-readable names instead of cryptic numeric codes.

%prep
%setup -c -T
cp %SOURCE0 .
%patch -p1

%build


%install
install -pD -m644 pci.ids %buildroot%_datadir/misc/pci.ids

%files
%_datadir/misc/pci.ids

%changelog
* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 20120626-alt1
- repocop cronbuild 20120626. At your service.

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 20120508-alt1
- repocop cronbuild 20120508. At your service.

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20120410-alt1
- repocop cronbuild 20120410. At your service.

* Tue Feb 28 2012 Cronbuild Service <cronbuild@altlinux.org> 20120228-alt1
- repocop cronbuild 20120228. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120124-alt1
- repocop cronbuild 20120124. At your service.

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120117-alt1
- repocop cronbuild 20120117. At your service.

* Tue Jan 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20120110-alt1
- repocop cronbuild 20120110. At your service.

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 20111227-alt1
- repocop cronbuild 20111227. At your service.

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 20111220-alt1
- repocop cronbuild 20111220. At your service.

* Wed Nov 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20111109-alt1
- repocop cronbuild 20111109. At your service.

* Sat Sep 10 2011 Cronbuild Service <cronbuild@altlinux.org> 20110910-alt1
- repocop cronbuild 20110910. At your service.

* Sat Jul 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20110716-alt1
- repocop cronbuild 20110716. At your service.

* Sat Jul 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110709-alt1
- repocop cronbuild 20110709. At your service.

* Sat Jun 25 2011 Cronbuild Service <cronbuild@altlinux.org> 20110625-alt1
- repocop cronbuild 20110625. At your service.

* Sat Jun 18 2011 Cronbuild Service <cronbuild@altlinux.org> 20110618-alt1
- repocop cronbuild 20110618. At your service.

* Sat May 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110528-alt1
- repocop cronbuild 20110528. At your service.

* Sat May 21 2011 Cronbuild Service <cronbuild@altlinux.org> 20110521-alt1
- repocop cronbuild 20110521. At your service.

* Sat Apr 30 2011 Cronbuild Service <cronbuild@altlinux.org> 20110430-alt1
- repocop cronbuild 20110430. At your service.

* Sat Apr 23 2011 Cronbuild Service <cronbuild@altlinux.org> 20110423-alt1
- repocop cronbuild 20110423. At your service.

* Sat Apr 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110409-alt1
- repocop cronbuild 20110409. At your service.

* Sat Mar 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110312-alt1
- repocop cronbuild 20110312. At your service.

* Fri Feb 11 2011 Cronbuild Service <cronbuild@altlinux.org> 20110211-alt1
- repocop cronbuild 20110211. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110128-alt1
- repocop cronbuild 20110128. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 20110114-alt1
- repocop cronbuild 20110114. At your service.

* Tue Nov 23 2010 Cronbuild Service <cronbuild@altlinux.org> 20101123-alt1
- repocop cronbuild 20101123. At your service.

* Tue Nov 09 2010 Cronbuild Service <cronbuild@altlinux.org> 20101109-alt1
- repocop cronbuild 20101109. At your service.

* Mon Oct 25 2010 Cronbuild Service <cronbuild@altlinux.org> 20101025-alt1
- repocop cronbuild 20101025. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 20101005-alt1
- repocop cronbuild 20101005. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 20100906-alt1
- repocop cronbuild 20100906. At your service.

* Tue Sep 15 2009 Victor Forsyuk <force@altlinux.org> 20090915-alt1
- 2009-09-15 snapshot.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 20090704-alt1
- 2009-07-04 snapshot.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 20081105-alt1
- 2008-11-05 snapshot.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 20080331-alt1
- 2008-03-31 snapshot.

* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 20080218-alt1
- 2008-02-18 snapshot.

* Mon Oct 15 2007 Victor Forsyuk <force@altlinux.org> 20071015-alt1
- 2007-10-15 snapshot.

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 20070904-alt1
- 2007-09-04 snapshot.

* Tue Aug 14 2007 Victor Forsyuk <force@altlinux.org> 20070814-alt1
- 2007-08-14 snapshot.

* Tue Aug 07 2007 Victor Forsyuk <force@altlinux.org> 20070807-alt1
- Initial build.
