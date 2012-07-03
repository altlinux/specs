Name: orc
Version: 0.4.16
Release: alt2
Summary: The Oil Runtime Compiler
Group: Development/Other
License: BSD
URL: http://code.entropywave.com/projects/orc/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc valgrind-devel
BuildRequires: glib2-devel >= 2.10.0

%description
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

%package -n lib%name
Summary: The Oil Runtime Compiler library
Group: System/Libraries

%description -n lib%name
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

This package contains the Orc library.

%package -n lib%name-devel
Summary: Development files for liborc
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

This package contains development files for the Orc library.

%package -n lib%name-test
Summary: The Oil Runtime Compiler library
Group: System/Libraries

%description -n lib%name-test
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

This package contains the Orc test library.

%package -n lib%name-test-devel
Summary: Development test files for liborc
Group: Development/C
Requires: lib%name-test = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-test-devel
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

This package contains development files for the Orc test library.

%package doc
Summary: Dcumentation for Orc
Group: Development/Documentation
BuildArch: noarch

%description doc
Orc is a library and set of tools for compiling and executing very
simple programs that operate on arrays of data.
The languag is a generic assembly language that represents many of
the features available in SIMD architectures, including saturated
addition and subtraction, and many arithmetic operations.

This package contains documentation for Orc.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/orc-bugreport
%_bindir/orcc

%files -n lib%name
%_libdir/liborc-0.4.so.*

%files -n lib%name-test
%_libdir/liborc-test-0.4.so.*

%files -n lib%name-devel
%dir %_includedir/orc-0.4
%_includedir/orc-0.4/orc
%_libdir/liborc-0.4.so
%_pkgconfigdir/orc-0.4.pc
%_datadir/aclocal/orc.m4

%files -n lib%name-test-devel
%_includedir/orc-0.4/orc-test
%_libdir/liborc-test-0.4.so

%files doc
%_datadir/gtk-doc/html/orc

%changelog
* Wed Oct 26 2011 Paul Wolneykien <manowar@altlinux.ru> 0.4.16-alt2
- Add glib-2.0 to the set of build requisites.

* Tue Oct 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.16-alt1
- 0.4.16

* Sat May 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.14-alt1
- 0.4.14

* Thu Dec 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Sun Sep 26 2010 Paul Wolneykien <manowar@altlinux.ru> 0.4.9-alt2
- Fix some of the repocop warnings:
  * liborc-0.4.9-alt1 altlinux-policy-shared-lib-contains-devel-so;
  * liborc-test-0.4.9-alt1 altlinux-policy-shared-lib-contains-devel-so;
  * liborc-devel-0.4.9-alt1 library-pkgnames-static;
  * liborc-test-devel-0.4.9-alt1 library-pkgnames-static;
  * orc-doc-0.4.9-alt1 arch-dep-package-consists-of-usr-share.

* Thu Sep 23 2010 Paul Wolneykien <manowar@altlinux.ru> 0.4.9-alt1
- Initial build for ALT Linux.
- Version 0.4.9.
