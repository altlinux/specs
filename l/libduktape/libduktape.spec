%define oname duktape
Name: libduktape
Version: 2.4.0
Release: alt1

Summary: Embeddable Javascript engine library

License: MIT
Group: System/Libraries
Url: http://duktape.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://duktape.org/%oname-%version.tar.xz
Source: %name-%version.tar
Patch: duktape-2.3.0-makefile.patch

%description
Duktape is an embeddable Javascript engine, with a focus on portability
and compact footprint.

#----------------------------------------------------------------------------

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Libraries and header files for developing programs based on %name.


#----------------------------------------------------------------------------

%package -n %oname
Summary: Embeddable Javascript engine commandline duk interpreter
Group: File tools

%description -n %oname
Duktape is an embeddable Javascript engine, with a focus on portability
and compact footprint.

This package contains a commandline duk interpreter.

#----------------------------------------------------------------------------

%prep
%setup
%patch -p2

%build
%make -f Makefile.sharedlibrary
%make -f Makefile.sharedlibrary duk
#make -f Makefile.cmdline

%install
%makeinstall_std \
	INSTALL_PREFIX="%prefix" \
	LIBDIR="%_libdir" \
	-f Makefile.sharedlibrary

mkdir -p %buildroot%_bindir
install -m 755 duk %buildroot%_bindir/duk

%files
%_libdir/libduktape.so.*

%files devel
%_includedir/duk_config.h
%_includedir/duktape.h
%_libdir/libduktape.so

%files -n %oname
%doc AUTHORS.rst LICENSE.txt README.rst
%_bindir/duk

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Sisyphus

* Tue May 30 2017 Rosa <rosa@abf.rosalinux.ru> 2.1.0-1
- (8c69ea0) Automatic import for version 2.1.0-1


