%define oname duktape

Name: libduktape
Version: 2.7.0
Release: alt3
%define sover 207
%define libduktape libduktape%sover
%define libduktaped libduktaped%sover

Summary: Embeddable Javascript engine library
License: MIT
Group: System/Libraries

Url: http://duktape.org/
Packager: Vitaly Lipatov <lav@altlinux.ru>
# Source-url: http://duktape.org/%oname-%version.tar.xz
Source: %name-%version.tar
Patch: duktape-2.7.0-makefile.patch

%description
Duktape is an embeddable Javascript engine, with a focus on portability
and compact footprint.

#----------------------------------------------------------------------------

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
Libraries and header files for developing programs based on %name.


#----------------------------------------------------------------------------

%package -n %libduktape
Summary: Embeddable Javascript engine commandline duk interpreter
Group: System/Libraries
Provides: libduktape = %EVR
Obsoletes: libduktape < %EVR

%description -n %libduktape
Duktape is an embeddable Javascript engine, with a focus on portability
and compact footprint.

%package -n %libduktaped
Summary: Embeddable Javascript engine commandline duk interpreter
Group: System/Libraries
Conflicts: libduktape <= 2.7.0-alt2

%description -n %libduktaped
Duktape is an embeddable Javascript engine, with a focus on portability
and compact footprint.

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
%add_optflags %optflags_shared
%make CFLAGS="%optflags" -f Makefile.sharedlibrary
%make CFLAGS="%optflags" -f Makefile.cmdline duk

%install
%makeinstall_std \
	INSTALL_PREFIX="%prefix" \
	LIBDIR="/%_lib" \
	-f Makefile.sharedlibrary

mkdir -p %buildroot%_bindir
install -m 755 duk %buildroot%_bindir/duk

%files -n %libduktape
%_libdir/libduktape.so.*
%_libdir/libduktape.so.%sover

%files -n %libduktaped
%_libdir/libduktaped.so.*
%_libdir/libduktaped.so.%sover

%files devel
%_includedir/duk_config.h
%_includedir/duktape.h
%_libdir/lib*.so
%_libdir/pkgconfig/duktape.pc

%files -n %oname
%doc AUTHORS.rst LICENSE.txt README.rst
%_bindir/duk

%changelog
* Sun Jul 07 2024 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt3
- build cmdline duk with useful extra modules (ALT bug #50835)

* Fri Feb 09 2024 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt2.1
- apply shared libs policy
- fix compile flags

* Wed Dec 06 2023 Michael Shigorin <mike@altlinux.org> 2.7.0-alt2
- package duktaped library too

* Wed Dec 06 2023 Michael Shigorin <mike@altlinux.org> 2.7.0-alt1
- new version 2.7.0 (with rpmgs script)
- link with -lm (see upstream issues 2464, 2484)

* Thu Jun 01 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.6.0-alt2
- Added pkg-config data (closes:  #46355)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Mon Aug 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

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


