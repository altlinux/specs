Name:    openpace
Version: 1.1.2
Release: alt1

Summary: Cryptographic library for EAC version 2
License: GPL-3.0
Group:   Security/Networking
Url:     https://github.com/frankmorgner/openpace

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: help2man
BuildRequires: gengetopt
# For tests
BuildRequires: openssl

%description
OpenPACE implements Extended Access Control (EAC) version 2 as specified in BSI
TR-03110. OpenPACE comprises support for the following protocols:

* Password Authenticated Connection Establishment (PACE) Establish a secure
channel with a strong key between two parties that only share a weak secret.
Terminal Authentication (TA) Verify/prove the terminal's certificate (or rather
certificate chain) and secret key.

* Chip Authentication (CA) Establish a secure channel based on the chip's
static key pair proving its authenticy.

* Furthermore, OpenPACE also supports Card Verifiable Certificates (CV
Certificates) as well as easy to use wrappers for using the established secure
channels.

The handlers for looking up trust anchors during TA and CA (i.e. the CVCA and
the CSCA certificates) can be customized. By default, the appropriate
certificates will be looked up in the file system.

OpenPACE supports all variants of PACE (DH/ECDH, GM/IM), TA
(RSASSA-PKCS1-v1_5/RSASSA-PSS/ECDSA), CA (DH/ECDH) and all standardized domain
parameters (GFP/ECP).

%package -n libeac
Summary: Library for %name
Group: System/Libraries

%description -n libeac
%summary

%package -n libeac-devel
Summary: Development files for %name
Group: Development/C

%description -n libeac-devel
%summary

%package docs
Summary: Library for %name
Group: Development/Documentation

%description docs
%summary

%prep
%setup

%build
%autoreconf
%configure --disable-static
export NPROCS=1
%make_build

%install
%makeinstall_std
mv %buildroot%_bindir/{,%name-}example

%check
%make_build check

%files
%doc *.md
%_sysconfdir/eac
%_bindir/cvc-create
%_bindir/cvc-print
%_bindir/eactest
%_bindir/%name-example
%_man1dir/*.1*

%files -n libeac
%_libdir/libeac.so.*

%files -n libeac-devel
%_libdir/libeac.so
%_includedir/eac
%_libdir/pkgconfig/*.pc

%files docs
%_defaultdocdir/%name

%changelog
* Wed Nov 30 2022 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
