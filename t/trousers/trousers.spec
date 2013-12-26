Name: trousers
Version: 0.3.11.2
Release: alt1

Summary: Implementation of the TCG's Software Stack v1.1 Specification
License: CPL
Group: System/Base
Url: http://www.sf.net/projects/trousers

Source: %name-%version-%release.tar

BuildRequires: libgtk+2-devel libssl-devel

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
%configure
%make_build

%install
%makeinstall_std

%files
%doc README AUTHORS
%config(noreplace) %_sysconfdir/tcsd.conf
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
* Sun Dec 22 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.11.2-alt1
- 0.3.11.2 released

* Thu Mar 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.10-alt1
- initial
