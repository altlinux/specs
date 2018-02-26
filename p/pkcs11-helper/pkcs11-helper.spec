Name: pkcs11-helper
Version: 1.08
Release: alt1
Summary: A library for using PKCS#11 providers

Group: Development/Other
License: GPLv2 or BSD
Url: http://www.opensc-project.org/pkcs11-helper/
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: http://www.opensc-project.org/files/%name/%name-%version.tar.bz2

BuildRequires: doxygen graphviz
BuildRequires: openssl-devel
BuildRequires: pkg-config

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
Requires: openssl-devel
Requires: pkg-config
# for %_datadir/aclocal
Requires: automake

%description devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.

%prep
%setup

%build
%configure --disable-static --enable-doc
%make_build

%install
%makeinstall_std INSTALL="install -p"

# Use %%doc to install documentation in a standard location
mkdir apidocdir
mv %buildroot%_docdir/%name/api/ apidocdir/
rm -rf %buildroot%_docdir/%name/

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
