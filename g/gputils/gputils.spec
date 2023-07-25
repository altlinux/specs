Name: gputils
Version: 1.5.2
Release: alt1

Summary: Development utilities for Microchip (TM) PIC (TM) microcontrollers

License: GPLv2
Group: Development/Other
Url: http://gputils.sourceforge.net

Source: http://prdownloads.sf.net/gputils/%name-%version.tar

BuildRequires: flex

%description
This is a collection of development tools for Microchip (TM) PIC (TM)
microcontrollers.

This is ALPHA software: there may be serious bugs in it, and it's
nowhere near complete.  gputils currently only implements a subset of
the features available with Microchip's tools.  See the documentation for
an up-to-date list of what gputils can do.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_datadir/%name/
%doc AUTHORS ChangeLog NEWS README doc/gputils.pdf doc/gputils.ps

%changelog
* Mon Jul 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.2-alt1
- 1.5.2 released

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.13.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun May 03 2009 Vitaly Lipatov <lav@altlinux.ru> 0.13.7-alt1
- new version 0.13.7 (with rpmrb script) (fix bug #19884)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.13.6-alt1
- new version 0.13.6 (with rpmrb script)
- cleanup spec, enable SMP build

* Thu Sep 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13.4-alt0.1
- new version 0.13.4 (with rpmrb script)

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13.3-alt1
- new version

* Mon Jan 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- first build for ALT Linux Sisyphus

