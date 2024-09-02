Name: trousers
Version: 0.3.15
Release: alt3

Summary: Implementation of the TCG's Software Stack
License: BSD-3-Clause
Group: System/Base
Url: http://www.sf.net/projects/trousers

Source: %name-%version-%release.tar

BuildRequires: libssl-devel

Requires: lib%name = %version-%release

%description
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.

%package -n lib%name
Summary: TrouSerS shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: TrouSerS header files and documentation
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.
This package contains TrouSerS shared library.

%description -n lib%name-devel
Header files and man pages for use in creating Trusted Computing enabled
applications.

%prep
%setup

%build
%autoreconf
%configure --with-gui=openssl
%make_build

%install
%makeinstall_std
rm -v %buildroot%_libdir/*.a
install -pm0644 -D trousers.service %buildroot%_unitdir/trousers.service
install -pm0644 -D trousers.rules %buildroot%_udevrulesdir/60-trousers.rules

%pre
# common user for both trousers and tpm2-tss
%_sbindir/groupadd -r -f tss &>/dev/null ||:
%_sbindir/useradd -r -g tss -d /var/empty -s /dev/null -c 'TCG Core Services' -n tss &>/dev/null ||:

%files
%doc AUTHORS LICENSE NEWS README* ChangeLog
%config(noreplace) %attr(0640,root,tss) %_sysconfdir/tcsd.conf
%_unitdir/trousers.service
%_udevrulesdir/60-trousers.rules
%_sbindir/tcsd
%_man5dir/tcsd.conf.5*
%_man8dir/tcsd.8*
%_localstatedir/tpm

%files -n lib%name
%_libdir/libtspi.so.*

%files -n lib%name-devel
%_libdir/libtspi.so
%_includedir/tss
%_includedir/trousers
%_man3dir/Tspi_*.3*

%changelog
* Mon Sep 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.15-alt3
- fixed trousers conffile permissions (closes: 51271)

* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.15-alt2
- unpackaged static library dropped

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.15-alt1
- 0.3.15 released
- Corrected mutliple security issues in tcsd
  (Fixes: CVE-2020-24332, CVE-2020-24330, CVE-2020-24331)

* Wed Aug 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.14-alt1
- 0.3.14 released

* Mon Aug 03 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.13-alt1
- 0.3.13 released

* Sun Dec 22 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.11.2-alt1
- 0.3.11.2 released

* Thu Mar 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.10-alt1
- initial
