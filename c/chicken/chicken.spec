Name: chicken
Version: 4.1.0
Release: alt2.1
License: BSD style (see LICENSE)
Group: Development/Scheme
Url: http://www.call-with-current-continuation.org/
Source: %name-%version.tar
Requires: libchicken-devel = %version-%release
Summary: CHICKEN is a simple Scheme-to-C compiler
Packager: Alexey Voinov <voins@altlinux.ru>

BuildPreReq: chrpath

# Automatically added by buildreq on Sat Nov 01 2003

%description
CHICKEN is a simple Scheme-to-C compiler supporting the language features as
defined in the 'Revised^5 Report on Scheme'. CHICKEN generates quite
portable C code, linkage to C modules and C library functions is
straightforward, compiled programs can easily be embedded into existing C
code, loads of extra libraries.

%package -n libchicken
Summary: Runtime libraries for programs produced with chicken compiler
Group: System/Libraries

%description -n libchicken
Runtime libraries for programs produced with chicken compiler

%package -n libchicken-unsafe
Summary: Faster runtime libraries for programs produced with chicken compiler
Group: System/Libraries

%description -n libchicken-unsafe
Faster runtime libraries for programs produced with chicken compiler

%package -n libchicken-devel
Summary: Development libraries for using with chicken scheme-to-c compiler
Group: Development/Scheme
Requires: libchicken = %version-%release
Requires: libchicken-unsafe = %version-%release

%description -n libchicken-devel
Development libraries for using with chicken scheme-to-c compiler

%package -n libchicken-devel-static
Summary: Static libraries for using with chicken scheme-to-c compiler
Group: Development/Scheme
Requires: libchicken-devel = %version-%release

%description -n libchicken-devel-static
Static libraries for using with chicken scheme-to-c compiler

%package docs
Summary: Manual for Chicken scheme-to-c compiler
Group: Development/Documentation
Requires: chicken = %version-%release
BuildArch: noarch

%description docs
Manual for Chicken scheme-to-c compiler

%prep
%setup -q

%build
%remove_optflags -Wall
make PLATFORM=linux PREFIX=%_prefix LIBDIR=%_libdir \
    C_COMPILER_OPTIMIZATION_OPTIONS="$RPM_OPT_FLAGS"


%install
make PLATFORM=linux PREFIX=%_prefix LIBDIR=%_libdir \
    DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%_datadir/%name/doc

for i in %buildroot%_bindir/* %buildroot%_libdir/%name/4/*.so
do
	chrpath -d $i ||:
done

%files
%_bindir/*
%_datadir/%name
%_man1dir/*

%files docs
%doc LICENSE README html

%files -n libchicken
%_libdir/libchicken.so
%_libdir/%name

%files -n libchicken-unsafe
%_libdir/libuchicken.so

%files -n libchicken-devel
%_includedir/*

%files -n libchicken-devel-static
%_libdir/lib*.a

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2.1
- Removed bad RPATH

* Tue Sep 29 2009 Alexey Voinov <voins@altlinux.ru> 4.1.0-alt2
- fixed build for x86_64

* Wed Sep 23 2009 Alexey Voinov <voins@altlinux.ru> 4.1.0-alt1
- new version (4.1.0)
- docs subpackage created
- chicken doesn't use autotools any more.

* Wed Jan 10 2007 Alexey Voinov <voins@altlinux.ru> 2.5-alt1
- new version (2.5)
- alt-makefile patch removed (obsolete)


* Sun Oct 02 2005 Alexey Voinov <voins@altlinux.ru> 2.2-alt1
- new version (2.2)

* Sun Jul 24 2005 Alexey Voinov <voins@altlinux.ru> 2.0-alt1
- new version (2.0)

* Mon Feb 21 2005 Alexey Voinov <voins@altlinux.ru> 1.89-alt1
- new version (1.89)

* Fri Oct 29 2004 Alexey Voinov <voins@altlinux.ru> 1.66-alt1
- new version (1.66)
- warnings suppressed (temporarily I hope)
- url fixed
- split into multiple subpackages

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 1.33-alt1
- New release

* Sat Nov 01 2003 Ott Alex <ott@altlinux.ru> 1.22-alt1
- New main release

* Sun Sep 21 2003 Ott Alex <ott@altlinux.ru> 1.17-alt2
- removing make_build

* Tue Sep 02 2003 Ott Alex <ott@altlinux.ru> 1.17-alt1
- New main release

* Mon Jun 23 2003 Ott Alex <ott@altlinux.ru> 1.12-alt2
- Fixing build deps

* Sun Jun 22 2003 Ott Alex <ott@altlinux.ru> 1.12-alt1
- Initial build for ALTLinux
