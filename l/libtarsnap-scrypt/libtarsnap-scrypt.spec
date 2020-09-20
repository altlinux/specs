# TODO: build library like used in fuse-cryfs
%define oname scrypt

Name: libtarsnap-scrypt
Version: 1.3.1
Release: alt1

Summary: The scrypt key derivation function

Group: System/Libraries
License: BSD like
Url: https://www.tarsnap.com/scrypt.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Tarsnap/scrypt/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: libssl-devel

%description
The scrypt key derivation function was originally developed for use
in the Tarsnap online backup system and is designed
to be far more secure against hardware brute-force attacks
than alternative functions such as PBKDF2 or bcrypt.

TODO: build library like used in fuse-cryfs.

%package devel
Summary: Files needed for developing with %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the files that are needed when building
software that uses %name.

%package -n scrypt
Summary: The scrypt key derivation function CLI utility
Group: File tools
#Requires: %name = %version-%release

%description -n scrypt
The scrypt key derivation function CLI utility.

The scrypt key derivation function was originally developed for use
in the Tarsnap online backup system and is designed
to be far more secure against hardware brute-force attacks
than alternative functions such as PBKDF2 or bcrypt.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

#%files
#%doc README.md
#%_libdir/%oname.so.1
#%_libdir/%oname.so.1.*

#%files devel
#%_libdir/%oname.so
#%dir %_includedir/%oname/
#%_includedir/%oname/%oname.h
#%_pkgconfigdir/%oname.pc

%files -n scrypt
%_bindir/scrypt
%_man1dir/scrypt.*

%changelog
* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
