
Name:     aqbanking
Version:  5.0.22
Release:  alt1

Summary:  A library for online banking functions and financial data import/export
License:  GPLv2+
Group:    System/Libraries

URL:      http://www.aquamaniac.de/aqbanking/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar.bz2
Source1:  aqbanking4-handbook-20091231.pdf
Source2:  %name.watch
Patch0:   %name-link.patch

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ktoblzcheck-devel
BuildRequires: libchipcard-devel
BuildRequires: libgamin-devel
BuildRequires: libgmp-devel
BuildRequires: libgwenhywfar-devel
BuildRequires: libofx-devel
BuildRequires: rpm-build-compat
#BuildRequires:	libOpenSP-devel
#BuildRequires:	libssl-devel
#BuildRequires:	libpcsclite-devel

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
Requires: %name-ofx-devel = %version-%release
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

%package -n libaqofxconnect
Summary:  Library for OFX access for Aqbanding
Group:    System/Libraries

%description -n libaqofxconnect
Library for OFX access for Aqbanding.

%package ofx-devel
Summary:  Aqbanking development tools for OFX direct connect
Group:	  Development/Other
Requires: %name-ofx = %version
Requires: libaqofxconnect = %version
Requires: libofx-devel
Provides: libaqbanking-ofx-devel = %version-%release

%description ofx-devel
Aqbanking development tools. Necessary for OFX direct connect access.

# Libraries

%package -n libaqbanking
Summary:  Aqbanking shared library
Group:	  System/Libraries

%description -n libaqbanking
This package contains the shared libraries for aqbanking.

%package -n libaqhbci
Summary:  The HBCI backend for the Aqbanking library
Group:	  System/Libraries

%description -n libaqhbci
This is the backend for the Aqbanking library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol.

%package doc
Summary: AqBanking4 Handbook
Group: Development/Documentation 
BuildArch: noarch

%description doc
AqBanking4 Handbook (PDF)

%prep
%setup -q
cp %SOURCE1 .

%build
%autoreconf
%configure \
	--disable-static \
	--enable-gwenhywfar \
	--enable-release \
	--with-docpath=%_docdir \
	--enable-full-doc \
	--enable-tutorials

# hack for semi SMP build
%make_build || make

%install
%make_install install DESTDIR=%buildroot

rm -f %buildroot%_libdir/*/plugins/*/*/*.la,a
rm -f %buildroot%_libdir/*/plugins/*/*/*/*/*.la,a
rm -f %buildroot%_docdir/aqhbci/aqhbci-tool/README

install -m 644 %SOURCE1 %buildroot%_docdir/%name/

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/aqbanking-cli
%_bindir/aqhbci-tool4
%_bindir/hbcixml3
%dir %_libdir/gwenhywfar
%_libdir/gwenhywfar/*
%dir %_libdir/%name
%dir %_datadir/%name/bankinfo
%_datadir/%name/bankinfo/*
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/*
%dir %_libdir/%name/plugins/*/imexporters
%_libdir/%name/plugins/*/bankinfo
%_libdir/%name/plugins/*/imexporters/csv.*
%_libdir/%name/plugins/*/imexporters/dtaus.*
%_libdir/%name/plugins/*/imexporters/eri2.*
%_libdir/%name/plugins/*/imexporters/openhbci1.*
%_libdir/%name/plugins/*/imexporters/q43.*
%_libdir/%name/plugins/*/imexporters/sepa.*
%_libdir/%name/plugins/*/imexporters/swift.*
%_libdir/%name/plugins/*/imexporters/xmldb.*
%_libdir/%name/plugins/*/imexporters/ctxfile.*
%_libdir/%name/plugins/*/imexporters/yellownet.*
%dir %_datadir/%name/imexporters
%_datadir/%name/imexporters/csv
%_datadir/%name/imexporters/dtaus
%_datadir/%name/imexporters/eri
%_datadir/%name/imexporters/eri2
%_datadir/%name/imexporters/openhbci1
%_datadir/%name/imexporters/q43
%_datadir/%name/imexporters/sepa
%_datadir/%name/imexporters/swift
%_datadir/%name/imexporters/xmldb
%_datadir/%name/imexporters/ctxfile
%_datadir/%name/imexporters/yellownet
%_libdir/%name/plugins/*/providers
%exclude %_libdir/%name/plugins/*/providers/aqofxconnect.*
%_datadir/%name/dialogs
### The aqofxconnect files
%_datadir/%name/backends/aqofxconnect
### The aqhbci files
%_libdir/%name/plugins/*/providers/aqhbci.*
%_datadir/%name/backends/aqhbci
### The aqnone files
%_libdir/%name/plugins/*/providers/aqnone.*
### Typemaker2
%_datadir/%name/%name/typemaker2
%_datadir/%name/typemaker2


%files devel
%_bindir/aqbanking-config
%_libdir/libaqbanking.so
%_libdir/libaqnone.so
%_includedir/aqbanking5/aqbanking/
%_includedir/aqbanking5/aqbankingpp/
%_includedir/aqbanking5/aqhbci/
%_aclocaldir/aqbanking.m4
%_pkgconfigdir/aqbanking.pc
%_libdir/libaqbankingpp.so
%_libdir/libaqhbci.so

%files ofx
%_libdir/%name/plugins/*/providers/aqofxconnect.*
%_libdir/%name/plugins/*/imexporters/ofx.*
%_datadir/%name/imexporters/ofx

%files ofx-devel
%_includedir/aqbanking5/aqofxconnect/
%_libdir/libaqofxconnect.so

%files -n libaqofxconnect
%_libdir/libaqofxconnect.so.*

%files -n libaqbanking
%_libdir/libaqbanking.so.*
%_libdir/libaqbankingpp.so.*
%_libdir/libaqnone.so.*

%files -n libaqhbci
%_libdir/libaqhbci.so.*

%files doc
%_docdir/%name/*.pdf
%_docdir/%name/

%changelog
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

