Name: usbids
Version: 20120612
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Repository of USB vendor IDs
License: GPLv2+ or BSD 3-clause
Group: System/Libraries

Url: http://www.linux-usb.org
Source: %url/usb.ids

BuildArch: noarch

%description
This package contains a public list of all known IDs used in USB devices.

%prep
%setup -c -T

%build

%install
install -pD -m644 %SOURCE0 %buildroot%_datadir/misc/usb.ids

%files
%_datadir/misc/usb.ids

%changelog
* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 20120612-alt1
- repocop cronbuild 20120612. At your service.

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120417-alt1
- repocop cronbuild 20120417. At your service.

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 20120214-alt1
- repocop cronbuild 20120214. At your service.

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 20120207-alt1
- repocop cronbuild 20120207. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120124-alt1
- repocop cronbuild 20120124. At your service.

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120117-alt1
- repocop cronbuild 20120117. At your service.

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20111116-alt1
- repocop cronbuild 20111116. At your service.

* Fri Sep 30 2011 Cronbuild Service <cronbuild@altlinux.org> 20110930-alt1
- repocop cronbuild 20110930. At your service.

* Fri Sep 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110909-alt1
- repocop cronbuild 20110909. At your service.

* Fri Aug 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110812-alt1
- repocop cronbuild 20110812. At your service.

* Fri Jun 24 2011 Cronbuild Service <cronbuild@altlinux.org> 20110624-alt1
- repocop cronbuild 20110624. At your service.

* Sat Apr 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20110416-alt1
- repocop cronbuild 20110416. At your service.

* Sat Mar 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110312-alt1
- repocop cronbuild 20110312. At your service.

* Sat Mar 05 2011 Cronbuild Service <cronbuild@altlinux.org> 20110305-alt1
- repocop cronbuild 20110305. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110128-alt1
- repocop cronbuild 20110128. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 20110114-alt1
- repocop cronbuild 20110114. At your service.

* Tue Nov 16 2010 Cronbuild Service <cronbuild@altlinux.org> 20101116-alt1
- repocop cronbuild 20101116. At your service.

* Tue Nov 02 2010 Cronbuild Service <cronbuild@altlinux.org> 20101102-alt1
- repocop cronbuild 20101102. At your service.

* Tue Oct 26 2010 Cronbuild Service <cronbuild@altlinux.org> 20101026-alt1
- repocop cronbuild 20101026. At your service.

* Tue Oct 12 2010 Cronbuild Service <cronbuild@altlinux.org> 20101012-alt1
- repocop cronbuild 20101012. At your service.

* Mon Sep 20 2010 Cronbuild Service <cronbuild@altlinux.org> 20100920-alt1
- repocop cronbuild 20100920. At your service.

* Mon Sep 13 2010 Cronbuild Service <cronbuild@altlinux.org> 20100913-alt1
- repocop cronbuild 20100913. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 20100906-alt1
- repocop cronbuild 20100906. At your service.

* Tue Sep 15 2009 Victor Forsyuk <force@altlinux.org> 20090912-alt1
- 2009-09-12 snapshot.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 20090705-alt1
- 2009-07-05 snapshot.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 20080921-alt1
- 2008-09-21 snapshot.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 20080327-alt1
- 2008-03-27 snapshot.

* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 20080210-alt1
- 2008-02-10 snapshot.

* Tue Aug 07 2007 Victor Forsyuk <force@altlinux.org> 20070728-alt1
- Initial build.
