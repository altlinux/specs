%define _unpackaged_files_terminate_build 1

Name:     aqbanking
Version:  6.9.2
Release:  alt1

Summary:  A library for online banking functions and financial data import/export
License:  GPL-2.0+
Group:    System/Libraries
URL:      https://github.com/aqbanking/aqbanking

Source:   %name-%version.tar
Patch0:   %name-tm2-includes.patch

BuildRequires: astyle
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ktoblzcheck-devel
BuildRequires: libchipcard-devel
BuildRequires: libgamin-devel
BuildRequires: libgmp-devel
BuildRequires: libgwenhywfar-devel >= 4.10.0.0
BuildRequires: libofx-devel
BuildRequires: rpm-build-compat
BuildRequires: libxmlsec1-gnutls-devel
BuildRequires: zlib-devel
#BuildRequires:	libOpenSP-devel
#BuildRequires:	libssl-devel
#BuildRequires:	libpcsclite-devel

Provides: libaqhbci = %EVR
Provides: libaqebics = %EVR
Provides: libaqpaypal = %EVR
Provides: %name-ofx = %EVR
Obsoletes: libaqhbci < %EVR
Obsoletes: libaqebics < %EVR
Obsoletes: libaqpaypal < %EVR
Obsoletes: %name-ofx < %EVR

%description
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package devel
Summary: Aqbanking development kit
Group: Development/Other
Requires: %name = %version-%release
Requires: libaqbanking  = %version
Requires: libaqhbci = %version
Requires: libchipcard-devel
Requires: libgwenhywfar-devel
Requires: ktoblzcheck-devel
Provides: libaqbanking-devel = %version-%release

%description devel
This package contains aqbanking-config and header files for writing
and compiling programs using Aqbanking.

# Backends

%package ofx
Summary:  Aqbanking tools for OFX 
Group:	  System/Libraries
Requires: %name = %version

%description ofx
Aqbanking tools for OFX

# Libraries

%package -n libaqbanking
Summary:  Aqbanking shared library
Group:	  System/Libraries

%description -n libaqbanking
This package contains the shared libraries for aqbanking.

%package doc
Summary: AqBanking4 Handbook
Group: Development/Documentation 
BuildArch: noarch

%description doc
AqBanking4 Handbook (PDF)

%prep
%setup -q
%autopatch -p1

%build
make -f Makefile.cvs
%undefine _configure_gettext
%autoreconf
%configure \
	--disable-static \
	--enable-gwenhywfar \
	--enable-release \
	--with-docpath=%_docdir \
	--enable-gui-tests=no
%make_build typefiles && %make_build

%install
%make_install install DESTDIR=%buildroot

rm -f %buildroot%_libdir/*/plugins/*/*.la
rm -f %buildroot%_libdir/*/plugins/*/*/*.la
rm -f %buildroot%_libdir/*/plugins/*/*/*/*/*.la
rm -f %buildroot%_docdir/aqhbci/aqhbci-tool/README
rm -f %buildroot%_docdir/aqebics/aqebics-tool/README

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/aqbanking-cli
%_bindir/aqhbci-tool4
%_bindir/aqebics-tool
%_bindir/aqpaypal-tool
%_bindir/aqofxconnect-tool             
%dir %_libdir/%name
%dir %_datadir/%name/bankinfo
%_datadir/%name/bankinfo/*
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/*
%dir %_libdir/%name/plugins/*/imexporters
%_libdir/%name/plugins/*/bankinfo
%_libdir/%name/plugins/*/imexporters/camt.*
%_libdir/%name/plugins/*/imexporters/csv.*
%_libdir/%name/plugins/*/imexporters/eri2.*
%_libdir/%name/plugins/*/imexporters/openhbci1.*
%_libdir/%name/plugins/*/imexporters/q43.*
%_libdir/%name/plugins/*/imexporters/sepa.*
%_libdir/%name/plugins/*/imexporters/swift.*
%_libdir/%name/plugins/*/imexporters/xml.*
%_libdir/%name/plugins/*/imexporters/xmldb.*
%_libdir/%name/plugins/*/imexporters/ctxfile.*
%_libdir/%name/plugins/*/imexporters/yellownet.*
%dir %_libdir/%name/plugins/*/dbio
%_libdir/%name/plugins/*/dbio/*
%dir %_datadir/%name/imexporters
%_datadir/%name/imexporters/camt
%_datadir/%name/imexporters/csv
%_datadir/%name/imexporters/eri
%_datadir/%name/imexporters/eri2
%_datadir/%name/imexporters/openhbci1
%_datadir/%name/imexporters/q43
%_datadir/%name/imexporters/sepa
%_datadir/%name/imexporters/swift
%_datadir/%name/imexporters/xml
%_datadir/%name/imexporters/xmldb
%_datadir/%name/imexporters/ctxfile
%_datadir/%name/imexporters/yellownet
%_datadir/%name/dialogs
### The aqofxconnect files
%_datadir/%name/backends/aqofxconnect
%dir %_libdir/%name/plugins/*/providers
### The aqnone files
%_libdir/%name/plugins/*/providers/aqnone.xml
### The aqhbci files
%_libdir/%name/plugins/*/providers/aqhbci.xml
%_datadir/%name/backends/aqhbci
### The aqebics files
%_libdir/%name/plugins/*/providers/aqebics.xml
%_datadir/%name/backends/aqebics/
### The aqpaypal files
%_libdir/%name/plugins/*/providers/aqpaypal.xml
%_datadir/%name/backends/aqpaypal/
### The aqgivve files
%_libdir/%name/plugins/*/providers/aqgivve.xml
%_datadir/%name/backends/aqgivve/dialogs/*.dlg
### The ofx files
%_libdir/%name/plugins/*/providers/aqofxconnect.xml
%_libdir/%name/plugins/*/imexporters/ofx.*
%_datadir/%name/imexporters/ofx
### Typemaker2
%_datadir/%name/%name/typemaker2
%_datadir/%name/typemaker2

%files devel
%_bindir/aqbanking-config
%_includedir/aqbanking6
%_libdir/libaqbanking.so
%_aclocaldir/aqbanking.m4
%_pkgconfigdir/aqbanking.pc
%_libdir/cmake/aqbanking-*/aqbanking-config*.cmake

%files -n libaqbanking
%_libdir/libaqbanking.so.*

%files doc
%_docdir/%name/

%changelog
* Tue Sep 08 2026 Andrey Cherepanov <cas@altlinux.org> 6.9.2-alt1
- New version.
- Packaged all plugins to main package aqbanking.

* Mon Mar 10 2025 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- New version.

* Fri Jun 16 2023 Andrey Cherepanov <cas@altlinux.org> 6.5.4-alt1
- New version.

* Mon Jan 03 2022 Andrey Cherepanov <cas@altlinux.org> 6.4.1-alt1
- New version.

* Thu Sep 23 2021 Andrey Cherepanov <cas@altlinux.org> 6.3.2-alt1
- New version.

* Fri Jun 25 2021 Andrey Cherepanov <cas@altlinux.org> 6.3.0-alt1
- New version.

* Wed Dec 23 2020 Andrey Cherepanov <cas@altlinux.org> 6.2.5-alt1
- New version.

* Tue Feb 04 2020 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 5.99.40-alt0.beta
- New version (beta for kmymoney).

* Thu Oct 10 2019 Andrey Cherepanov <cas@altlinux.org> 5.8.2-alt1
- New version.

* Sat Aug 24 2019 Andrey Cherepanov <cas@altlinux.org> 5.8.1-alt1
- New version.

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 5.7.8-alt2
- Rebuild with libgwenhywfar-4.20.0.

* Thu Feb 15 2018 Andrey Cherepanov <cas@altlinux.org> 5.7.8-alt1
- new version 5.7.8

* Thu Jul 21 2016 Andrey Cherepanov <cas@altlinux.org> 5.6.12-alt1
- new version 5.6.12

* Sat Jul 16 2016 Andrey Cherepanov <cas@altlinux.org> 5.6.11-alt1
- new version 5.6.11

* Fri Apr 29 2016 Andrey Cherepanov <cas@altlinux.org> 5.6.10-alt1
- new version 5.6.10

* Sun Dec 27 2015 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt2
- Update watch file after upstream site reconstruction

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- new version 5.5.1

* Wed Nov 28 2012 Andrey Cherepanov <cas@altlinux.org> 5.0.25-alt1
- new version 5.0.25

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.22-alt1.1
- Rebuilt with gmp 5.0.5

* Mon Jan 16 2012 Andrey Cherepanov <cas@altlinux.org> 5.0.22-alt1
- New version 5.0.22
- Remove standard library path from RPATH
- Add watch file

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 5.0.14-alt1
- New version 5.0.14

* Thu Mar 24 2011 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- New version 5.0.4

* Thu Nov 11 2010 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt2
- Fix unmets
- Set noarch for documentation
- Rebuild for new requires detection

* Tue Apr 06 2010 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- New version 4.2.4
- Make package separation like SUSE
- Qt3 and Qt4 support
- Add AqBanking4 Handbook

* Thu Feb 14 2008 Grigory Batalov <bga@altlinux.ru> 2.2.4-alt1.1
- Rebuilt with python-2.5.

* Wed Apr 11 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version 2.2.4
- update buildreq, fix build on x86_64

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt0.1
- new version 2.2.3 (with rpmrb script)

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

