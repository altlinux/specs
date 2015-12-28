%define _name pkcs11-helper
%def_enable openssl
%def_disable gnutls
%def_disable nss
%def_disable polarssl

Name: lib%_name
Version: 1.12.0
Release: alt2.git20140427
Summary: A library for using PKCS#11 providers

Group: Development/Other
License: GPLv2 or BSD
Url: http://www.opensc-project.org/pkcs11-helper/
Packager: Mykola Grechukh <gns@altlinux.ru>

# https://github.com/OpenSC/pkcs11-helper.git
Source: %name-%version.tar

Provides: %_name = %version-%release
Obsoletes: %_name < %version-%release

BuildRequires: doxygen graphviz
%{?_enable_openssl:BuildRequires: pkgconfig(libcrypto) >= 0.9.7 pkgconfig(openssl) >= 0.9.7}
%{?_enable_gnutls:BuildRequires: pkgconfig(gnutls) >= 1.4}
%{?_enable_nss:BuildRequires: pkgconfig(nss) >= 3.11}
%{?_enable_polarssl:BuildRequires: libpolarssl-devel}

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications using a simple API and optional OpenSSL
engine. The library allows using multiple PKCS#11 providers at the same time,
enumerating available token certificates, or selecting a certificate directly
by serialized id, handling card removal and card insert events, handling card
re-insert to a different slot, supporting session expiration and much more all
using a simple API.

%package devel
Summary: Development files for pkcs11-helper
Group: Development/Other
Requires: %name = %version-%release
Provides: %_name-devel = %version-%release
Obsoletes: %_name-devel < %version-%release

%description devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.

%prep
%setup

%build
%autoreconf
%configure \
		--disable-static \
		--enable-doc \
		--with-apidocdir \
		%{?_disable_openssl:--disable-openssl --disable-crypto-engine-openssl} \
		%{?_disable_gnutls:--disable-crypto-engine-gnutls} \
		%{?_disable_nss:--disable-crypto-engine-nss} \
		%{?_disable_polarssl:--disable-crypto-engine-polarssl} \
		--enable-tests
%make_build

%install
%makeinstall_std INSTALL="install -p"

# Use %%doc to install documentation in a standard location
mkdir apidocdir
mv doc/api/api.out/html/* apidocdir/
rm -rf %buildroot%_docdir/%_name/

# Remove libtool .la files
rm -f %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog COPYING* README THANKS
%_libdir/libpkcs11-helper.so.*

%files devel
%doc apidocdir/*
%_includedir/pkcs11-helper-1.0/
%_libdir/libpkcs11-helper.so
%_pkgconfigdir/libpkcs11-helper-1.pc
%_datadir/aclocal/pkcs11-helper-1.m4
%_man8dir/pkcs11-helper-1.8*

%changelog
* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt2.git20140427
- fix build (drop BR: libpolarssl-devel)
- rename to libpkcs11-helper
- build with openssl support only

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1.git20140427
- Version 1.12.0

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 1.08-alt1
- new version

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 1.07-alt1
- initial build for ALT Linux Sisyphus

* Mon Jul 13 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2.1
- Fix EPEL-5 build by adding pkgconfig to BuildRequires.

* Sat Jul 11 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2
- Make devel package depend on automake for %_datadir/aclocal

* Tue Jun 23 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-1
- Initial RPM release.
