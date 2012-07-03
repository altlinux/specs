Name: printer-drivers
Version: 3.0
Release: alt5

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: printing subsystem
License: GPL
Group: Publishing
Url: http://www.linuxprinting.org
BuildArch: noarch


%package base
Summary: basic printing subsystem
Group: Publishing
#base
Requires: cups ghostscript-classic foomatic-db foomatic-db-engine foomatic-filters 
#big projects
Requires: foo2zjs hplip-hpijs hplip gutenprint-foomatic
#ijs drivers
Requires: epsoneplijs
#cups drivers
Requires: printer-driver-splix printer-driver-ptouch
#filters
Requires: c2070 c2050 pbm2l7k pbm2l2030 pbm2lwxl m2300w lz11-V2 cjet pnm2ppa ppmtomd min12xxw

Provides: %name-utils = %version
Obsoletes: %name-utils

Provides: ghostscript-drivers = 2008
Obsoletes: ghostscript-drivers


%package X11
Summary: printing subsystem with X Window support
Group: Publishing
Requires: %name-base = %version-%release
Requires: ghostscript-module-X hplip-gui

%description
This is a virtual package to get all printing subsystem

%description base
This is a virtual package to get all basic printing subsystem

%description X11
This is a virtual package to get printing subsystem with X11 printing utils

%files base

%files X11


%changelog
* Thu Sep 17 2009 Stanislav Ievlev <inger@altlinux.org> 3.0-alt5
- update hplip requires
- rename require: splix -> printer-driver-splix

* Wed Dec 03 2008 Stanislav Ievlev <inger@altlinux.org> 3.0-alt4
- remove requires: pup

* Tue Dec 02 2008 Stanislav Ievlev <inger@altlinux.org> 3.0-alt3
- remove requires: pentaxpj
- update requires: printer-driver-ptouch

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 3.0-alt2
- move from ghostscript-drivers: lz11-V2, pentaxpj, 
                                 epsoneplijs, pnm2ppa, ppmtomd
                                 (pbm2ppa is obsoleted by pnm2ppa)
- base: add requires: cjet, ptouch-driver, min12xxw

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 3.0-alt1
- remove utils subpackage
- base: add requires: c2070, c2050, pbm2l7k,
                      pbm2l2030, foo2zjs, splix, m2300w

* Tue Oct 02 2007 Stanislav Ievlev <inger@altlinux.org> 2.1-alt7
- update deps, remove obsolete utils 
  (save update-printers-db for backward compatibility with old packages)

* Thu Nov 16 2006 Stanislav Ievlev <inger@altlinux.org> 2.1-alt6
- require cups-drivers now

* Mon Apr 04 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt5
- backend now in separate package

* Tue Mar 29 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt4
- removed unused quotas for spaces

* Mon Mar 21 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt3
- removed deps on cups

* Fri Mar 11 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- added detection of usb printers, little improvements

* Thu Mar 10 2005 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- added device detection on parallel ports

* Sat Mar 05 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- backend improvements

* Mon Feb 07 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- fixed requires

* Fri Jan 28 2005 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- added utilities to generate precompiled drivers database
- added subpackage for alterator backend

* Fri Mar 26 2004 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- Added xojpanel

* Wed Mar 24 2004 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- Initial
