%define _cups_serverbin %_libexecdir/cups
%global _localstatedir %_var

Name: cups-filters
Version: 2.0.1
Release: alt1

Summary: OpenPrinting CUPS filters and backends
License: GPLv2 and GPLv2+ and GPLv3 and MIT
Group: System/Servers

Url: http://www.linuxfoundation.org/collaborate/workgroups/openprinting/pdf_as_standard_print_job_format
Source0: http://www.openprinting.org/download/cups-filters/cups-filters-%version.tar
Source1: %name.watch
Patch0: %name-alt.patch
Conflicts: cups < 1.6.1-alt1
Conflicts: ghostscript-cups
Obsoletes: ghostscript-cups
Provides: ghostscript-cups
Obsoletes: foomatic-filters
Provides: foomatic-filters
Conflicts: foomatic-filters

Requires: poppler-utils
Requires: /usr/bin/gs

BuildRequires: libgtk+3-devel
BuildRequires: libppd-devel
Provides: cups-backend-serial = %EVR
Obsoletes: cups-backend-serial < %EVR

%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.


%prep
%setup
%patch0 -p2

%build
./autogen.sh

%configure --disable-static \
	   --disable-silent-rules \
	   --disable-rpath \
	   --disable-mutool \
	   --enable-driverless \
           --enable-universal-cups-filter \
	   #
%make

%check
make check

%install
%make install DESTDIR=%buildroot
ln -sf ../lib/cups/filter/universal %buildroot/%_bindir/foomatic-rip
rm -rf %buildroot%_docdir/%name
mkdir -p %buildroot/%_datadir/cups/data/


%files
%doc README.md AUTHORS NEWS
%attr(0755,root,root) %_cups_serverbin/filter/*
%attr(0755,root,root) %_cups_serverbin/driver/*
%attr(0755,root,root) %_cups_serverbin/backend/parallel
%attr(0755,root,root) %_cups_serverbin/backend/beh
%attr(0755,root,root) %_cups_serverbin/backend/driverless
%attr(0755,root,root) %_cups_serverbin/backend/driverless-fax
%attr(0700,root,root) %_cups_serverbin/backend/serial
%_datadir/cups/drv/cupsfilters.drv
%_datadir/cups/mime/cupsfilters.types
%_datadir/cups/mime/cupsfilters.convs
%_datadir/cups/mime/cupsfilters-universal-postscript.convs
%_datadir/cups/mime/cupsfilters-universal.convs
%_datadir/ppdc/escp.h
%_datadir/ppdc/pcl.h
%_datadir/ppd/cupsfilters
%_bindir/foomatic-rip
%_bindir/driverless
%_bindir/driverless-fax
%_datadir/man/man*/*

%changelog
* Thu Aug 22 2024 Anton Farygin <rider@altlinux.ru> 2.0.1-alt1
- 2.0.0 -> 2.0.1

* Fri Sep 29 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0
- default-testpage was moved to libcupsfilters package

* Fri Aug 11 2023 Anton Midyukov <antohami@altlinux.org> 2.0-alt0.rc2_1
- NMU: Fix obsoletes cups-backend-serial

* Mon Jul 24 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc2
- update to 2.0rc2

* Mon Jun 19 2023 Anton Farygin <rider@altlinux.ru> 2.0-alt0.rc1
- 2.0rc1
- fix remote code execution in beh backend (Fixes: CVE-2023-24805)
- include cups-backend-serial into main package
- removed devel and libs subpackages (split by upstream)

* Mon Feb 27 2023 Anton Farygin <rider@altlinux.ru> 1.28.17-alt1
- 1.28.17

* Tue Sep 06 2022 Anton Farygin <rider@altlinux.ru> 1.28.16-alt1
- 1.28.16

* Mon Apr 18 2022 Anton Farygin <rider@altlinux.ru> 1.28.15-alt1
- 1.28.15

* Mon Apr 11 2022 Anton Farygin <rider@altlinux.ru> 1.28.14-alt1
- 1.28.14

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 1.28.13-alt1
- 1.28.13

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 1.28.12-alt1
- 1.28.12

* Sat Jan 29 2022 Anton Farygin <rider@altlinux.ru> 1.28.11-alt1
- 1.28.11

* Wed Aug 18 2021 Anton Farygin <rider@altlinux.ru> 1.28.10-alt1
- 1.28.10

* Fri Jun 18 2021 Anton Farygin <rider@altlinux.ru> 1.28.9-alt1
- 1.28.9

* Thu Apr 01 2021 Anton Farygin <rider@altlinux.org> 1.28.8-alt1
- 1.28.8

* Thu Mar 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.28.7-alt3
- Applied fix for MFC support from upstream.

* Fri Jan 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.28.7-alt2
- Disabled fax support due to CUPS issue #5886.

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 1.28.7-alt1
- 1.28.7

* Mon Dec 28 2020 Anton Farygin <rider@altlinux.ru> 1.28.6-alt1
- 1.28.6

* Thu Nov 05 2020 Anton Farygin <rider@altlinux.ru> 1.28.5-alt1
- 1.28.5

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 1.28.4-alt1
- 1.28.4

* Mon Sep 28 2020 Anton Farygin <rider@altlinux.ru> 1.28.3-alt1
- 1.28.3

* Tue Sep 15 2020 Anton Farygin <rider@altlinux.ru> 1.28.2-alt1
- 1.28.2

* Fri Aug 28 2020 Anton Farygin <rider@altlinux.ru> 1.28.1-alt1
- 1.28.1

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 1.27.5-alt1
- 1.27.5

* Thu May 28 2020 Anton Farygin <rider@altlinux.ru> 1.27.4-alt2
- changed the default behavior: autosetup is only for driverless printers

* Mon Apr 13 2020 Anton Farygin <rider@altlinux.ru> 1.27.4-alt1
- new version 1.27.4

* Mon Mar 23 2020 Anton Farygin <rider@altlinux.ru> 1.27.3-alt1
- new version 1.27.3

* Fri Mar 13 2020 Anton Farygin <rider@altlinux.ru> 1.27.2-alt1
- new version 1.27.2

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 1.27.1-alt1
- new version 1.27.1

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 1.27.0-alt1
- new version 1.27.0

* Wed Jan 15 2020 Anton Farygin <rider@altlinux.ru> 1.26.2-alt1
- new version 1.26.2

* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 1.26.1-alt1
- new version 1.26.1

* Tue Dec 17 2019 Anton Farygin <rider@altlinux.ru> 1.26.0-alt1
- new version 1.26.0

* Mon Dec 02 2019 Anton Farygin <rider@altlinux.ru> 1.25.13-alt1
- new version 1.25.13

* Thu Nov 14 2019 Anton Farygin <rider@altlinux.ru> 1.25.12-alt1
- new version 1.25.12

* Mon Oct 28 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.25.11-alt2
- new default testpage

* Fri Oct 11 2019 Anton Farygin <rider@altlinux.ru> 1.25.11-alt1
- new version 1.25.11

* Wed Sep 25 2019 Anton Farygin <rider@altlinux.ru> 1.25.6-alt1
- new version 1.25.6

* Tue Sep 10 2019 Anton Farygin <rider@altlinux.ru> 1.25.5-alt1
- new version 1.25.5
- enabled tests
- built with pclm support

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 1.25.4-alt2
- fixed build with qpdf-9.0.0
- cleanup patches

* Sun Sep 01 2019 Anton Farygin <rider@altlinux.ru> 1.25.4-alt1
- new version 1.25.4

* Fri Aug 23 2019 Anton Farygin <rider@altlinux.ru> 1.25.3-alt1
- new version 1.25.3

* Sun Aug 18 2019 Anton Farygin <rider@altlinux.ru> 1.25.2-alt1
- new version 1.25.2

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.25.1-alt1
- new version 1.25.1

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.25.0-alt1
- new version 1.25.0

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 1.24.0-alt1
- new version 1.24.0

* Tue Apr 09 2019 Anton Farygin <rider@altlinux.ru> 1.22.5-alt1
- new version 1.22.5

* Sun Apr 07 2019 Anton Farygin <rider@altlinux.ru> 1.22.4-alt1
- new version 1.22.4

* Thu Mar 28 2019 Anton Farygin <rider@altlinux.ru> 1.22.3-alt1
- new version 1.22.3

* Sun Mar 17 2019 Anton Farygin <rider@altlinux.ru> 1.22.2-alt1
- new version 1.22.2

* Fri Mar 08 2019 Anton Farygin <rider@altlinux.ru> 1.22.1-alt2
- clenup spec (removed php5 support)

* Thu Feb 28 2019 Anton Farygin <rider@altlinux.ru> 1.22.1-alt1
- new version 1.22.1

* Wed Feb 13 2019 Anton Farygin <rider@altlinux.ru> 1.22.0-alt2
- fixed build with poppler 0.74

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.22.0-alt1
- 1.22.0
- enabled opvp filter
- disabled mutool (changed to qpdf)
- pdftops renderer changed to hybrid (for better support printers from Brother,
  Minolta, and Konica Minolta)
- added generic UBRL braille ppd
- added backend for Virtual Braille BRF Printer

* Fri Dec 21 2018 Anton Farygin <rider@altlinux.ru> 1.21.6-alt1
- new version 1.21.6

* Fri Dec 07 2018 Anton Farygin <rider@altlinux.ru> 1.21.5-alt1
- new version 1.21.5

* Mon Nov 26 2018 Anton Farygin <rider@altlinux.ru> 1.21.4-alt1
- new version 1.21.4

* Wed Oct 24 2018 Anton Farygin <rider@altlinux.ru> 1.21.3-alt2
- disabled build of the php extension, due to end of life for php-5 at december 2018

* Sat Oct 06 2018 Anton Farygin <rider@altlinux.ru> 1.21.3-alt1
- new version 1.21.3

* Sat Sep 22 2018 Anton Farygin <rider@altlinux.ru> 1.21.2-alt2
- rebuilt with php5-5.6.38

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.21.2-alt1
- new version 1.21.2

* Sun Sep 02 2018 Anton Farygin <rider@altlinux.ru> 1.21.1-alt1
- new version 1.21.1

* Mon Aug 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.20.4-alt3
- handling Postscript with PJH heading fixed

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 1.20.4-alt2
- rebuilt for php5-5.6.37

* Tue Jul 17 2018 Anton Farygin <rider@altlinux.ru> 1.20.4-alt1
- new version 1.20.4

* Fri May 11 2018 Anton Farygin <rider@altlinux.ru> 1.20.3-alt2
- rebuilt for php5-5.6.36

* Sat Apr 21 2018 Anton Farygin <rider@altlinux.ru> 1.20.3-alt1
- new version 1.20.3

* Tue Apr 03 2018 Anton Farygin <rider@altlinux.ru> 1.20.2-alt1
- new version 1.20.2

* Fri Mar 02 2018 Anton Farygin <rider@altlinux.ru> 1.20.1-alt1
- new version 1.20.1

* Mon Feb 12 2018 Anton Farygin <rider@altlinux.ru> 1.20.0-alt1
- new version 1.20.0

* Mon Jan 29 2018 Anton Farygin <rider@altlinux.ru> 1.19.0-alt1
- new version 1.19.0

* Fri Nov 03 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt3
- rebuilt for php5-5.6.32

* Thu Oct 26 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt2
- use /var for localstatedir

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 1.17.9-alt1
- new version 1.17.9

* Sat Oct 07 2017 Michael Shigorin <mike@altlinux.org> 1.17.8-alt2
- introduced php knob (on by default)

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 1.17.8-alt1
- new version 1.17.8

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 1.17.7-alt1
- new version 1.17.7
- build with ldap
- enabled auto-setup for driverless printers

* Tue Aug 22 2017 Anton Farygin <rider@altlinux.ru> 1.16.3-alt1
- new version 1.16.3

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 1.16.2-alt1
- new version 1.16.2

* Mon Aug 14 2017 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- new version 1.16.1

* Fri Aug 04 2017 Anton Farygin <rider@altlinux.ru> 1.16.0-alt1
- new version 1.16.0

* Fri Jul 07 2017 Anton Farygin <rider@altlinux.ru> 1.14.1-alt2
- rebuild with new php

* Mon Jul 03 2017 Anton Farygin <rider@altlinux.ru> 1.14.1-alt1
- new version 1.14.1

* Wed May 24 2017 Anton Farygin <rider@altlinux.ru> 1.14.0-alt1
- new version 1.14.0

* Tue May 02 2017 Anton Farygin <rider@altlinux.ru> 1.13.5-alt1
- new version

* Tue Mar 07 2017 Anton Farygin <rider@altlinux.ru> 1.13.4-alt1
- new version 1.13.4

* Mon Jan 30 2017 Anton Farygin <rider@altlinux.ru> 1.13.3-alt1
- new version 1.13.3

* Fri Dec 30 2016 Anton Farygin <rider@altlinux.ru> 1.13.2-alt1
- new version 1.13.2

* Mon Dec 19 2016 Anton Farygin <rider@altlinux.ru> 1.13.1-alt1
- new version 1.13.1

* Wed Dec 14 2016 Anton Farygin <rider@altlinux.ru> 1.13.0-alt1
- new version 1.13.0

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 1.12.0-alt1
- new version 1.12.0

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 1.11.6-alt1
- new version 1.11.6

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt3
- rebuild with new PHP

* Mon Oct 17 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt2
- rebuild with new PHP

* Mon Sep 26 2016 Anton Farygin <rider@altlinux.ru> 1.11.4-alt1
- new version 1.11.4

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 1.11.1-alt1
- new version 1.11.1

* Mon Jul 25 2016 Anton Farygin <rider@altlinux.ru> 1.10.0-alt2
- rebuild with php5-5.6.24

* Thu Jul 21 2016 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- new version 1.10.0

* Mon Jun 27 2016 Anton Farygin <rider@altlinux.ru> 1.9.0-alt2
- rebuild with php5-5.6.23

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- new version 1.9.0
- build with avahi

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt6
- rebuild with php5-5.6.22

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt5
- rebuild with php5-5.6.21

* Tue Apr 05 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt4
- rebuild with php5-5.6.20

* Mon Mar 28 2016 Anton Farygin <rider@altlinux.ru> 1.0.76-alt3
- rebuild with php5-5.6.19

* Mon Dec 21 2015 Anton Farygin <rider@altlinux.ru> 1.0.76-alt2
- rebuild with php5-5.6.16

* Mon Oct 19 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.76-alt1
- new version 1.0.76

* Tue Jul 14 2015 Anton Farygin <rider@altlinux.ru> 1.0.71-alt1
- new version 1.0.71

* Thu May 28 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt4
- rebuild in new environment

* Mon May 18 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt3
- rebuild with php5-5.5.25

* Fri Apr 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt2
- rebuild for new php-5.5.24

* Wed Apr 15 2015 Anton Farygin <rider@altlinux.ru> 1.0.68-alt1
- new version 1.0.68

* Fri Mar 13 2015 Anton Farygin <rider@altlinux.ru> 1.0.67-alt1
- new version 1.0.67

* Mon Mar 02 2015 Anton Farygin <rider@altlinux.ru> 1.0.66-alt1
- new version 1.0.66

* Tue Feb 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.65-alt1
- new version 1.0.65

* Fri Jan 23 2015 Anton Farygin <rider@altlinux.ru> 1.0.62-alt2
- rebuild with php-5.5.21

* Fri Jan 16 2015 Anton Farygin <rider@altlinux.ru> 1.0.62-alt1
- new version 1.0.62

* Thu Jan 15 2015 Anton Farygin <rider@altlinux.ru> 1.0.61-alt3
- rebuild with php-5.5.20

* Thu Nov 20 2014 Anton Farygin <rider@altlinux.ru> 1.0.61-alt2
- rebuild with new php

* Tue Oct 14 2014 Anton Farygin <rider@altlinux.ru> 1.0.61-alt1
- new version 1.0.61

* Mon Oct 06 2014 Anton Farygin <rider@altlinux.ru> 1.0.59-alt1
- new version 1.0.59

* Wed Sep 10 2014 Anton Farygin <rider@altlinux.ru> 1.0.58-alt2
- rebuild with php-5.5.16

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 1.0.58-alt1
- new version 1.0.58

* Thu Jun 19 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt3
- exclude snapshot in watch file

* Wed Jun 18 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt2
- rebuld with php-5.5.13

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 1.0.54-alt1
- new version 1.0.54

* Fri May 16 2014 Anton Farygin <rider@altlinux.ru> 1.0.53-alt1
- new version

* Tue Apr 08 2014 Anton Farygin <rider@altlinux.ru> 1.0.52-alt1
- new version

* Fri Mar 28 2014 Anton Farygin <rider@altlinux.ru> 1.0.50-alt1
- new version
- watch file added
- initscript added (closes: #29524)

* Fri Mar 21 2014 Anton Farygin <rider@altlinux.ru> 1.0.48-alt2
- rebuild with php-5.5.10

* Thu Mar 13 2014 Anton Farygin <rider@altlinux.ru> 1.0.48-alt1
- new version

* Wed Mar 12 2014 Anton Farygin <rider@altlinux.ru> 1.0.47-alt1
- new version with security fixes: CVE-2013-6474, CVE-2013-6475,
  CVE-2013-6476 and CVE-2013-6473
- fixed ghostscript path (closes: #29884)

* Wed Feb 26 2014 Anton Farygin <rider@altlinux.ru> 1.0.46-alt1
- new version

* Tue Nov 05 2013 Andriy Stepanov <stanv@altlinux.ru> 1.0.41-alt2
- ghostsctip filters, add bannertopdf as PDF form

* Thu Oct 31 2013 Anton Farygin <rider@altlinux.ru> 1.0.41-alt1
- new version

* Tue Oct 29 2013 Fr. Br. George <george@altlinux.ru> 1.0.40-alt1.1
- Make serial backend root-only (Closes: #24172)

* Tue Oct 15 2013 Anton Farygin <rider@altlinux.ru> 1.0.40-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.0.39-alt1
- new version

* Tue Sep 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt2
- conflict with ghostscript-cups resolved

* Mon Sep 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.38-alt1
- update to 1.0.38
- cups-browsed packaged

* Fri Jul 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4.2
- Rebuild with php5-5.4.17.20130704

* Sat May 18 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.31-alt4.1
- Rebuild with php5-5.3.24.20130412-alt1

* Mon May 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt4
- rebuild with php5-5.3.25.20130512-alt1

* Tue Apr 23 2013 Anton Farygin <rider@altlinux.ru> 1.0.31-alt3
- rebuild with new poppler35

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt2
- rebuild with php5-5.3.24.20130412-alt1

* Wed Apr 03 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.31-alt1
- updated from upstream (closes: #28783)
- rebuild with php5-5.3.23.20130314-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt3
- rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt2
- rebuild with php5-5.3.17.20120913-alt1

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 1.0.24-alt1
- first build for Sisyphus, based on RH spec
