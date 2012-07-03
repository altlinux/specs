Summary: POSIX regexp functions
Name: librx
Version: 1.5

Packager: Alexey Voinov <voins@altlinux.ru>

Release: alt8
License: GPL
Group: Development/C
Url: http://www.gnu.org/software/rx/rx.html

Source0: %name-%version.tar

%description
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

%package devel
Summary: POSIX regexp functions, developers library
Group: Development/C
Requires: %name = %version-%release

%description devel
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

This package contains files needed for development with librx.

%package devel-static
Summary: POSIX regexp functions, developers static library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

This package contains files needed for development static
binaries with librx.

%prep
%setup -q

%build
%configure
make libdir=%_libdir
make doc/rx.info

%install
mkdir -p $RPM_BUILD_ROOT%prefix
mkdir -p $RPM_BUILD_ROOT%_infodir
mkdir -p $RPM_BUILD_ROOT%_libdir
mkdir -p $RPM_BUILD_ROOT%_includedir
make install DESTDIR=$RPM_BUILD_ROOT libdir=%_libdir
install -m 644 doc/rx.info $RPM_BUILD_ROOT%_infodir

%files
%_libdir/*.so.*

%files devel
%doc ANNOUNCE BUILDING COOKOFF rx/ChangeLog
%_includedir/*
%_infodir/*
%_libdir/*.so

%files devel-static
%_libdir/*.a

%changelog
* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt8
- Rebuilt for debuginfo

* Thu Nov 04 2010 Alexey Voinov <voins@altlinux.org> 1.5-alt7
- bumped up release to update deps with symbols

* Sat Jun 06 2009 Alexey Voinov <voins@altlinux.org> 1.5-alt6
- info-file fixed
- libtool invocation fixed
- obsolete macros removed

* Mon Jul 11 2005 Anton D. Kachalov <mouse@altlinux.org> 1.5-alt5.1
- multilib support

* Wed Dec 03 2003 Alexey Voinov <voins@altlinux.ru> 1.5-alt5
- rebuild wihtout .la

* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.5-alt4
- rebuild

* Tue Apr 30 2002 Alexey Voinov <voins@voins.program.ru> 1.5-alt3
- spec cleanup
- .texinfo patch

* Wed Apr 24 2002 Alexey Voinov <voins@voins.program.ru> 1.5-alt2
- rebuild as shared library
- subpackages -devel, -devel-static

* Mon Nov 05 2001 Alexey Voinov <voins@voins.program.ru> 1.5-alt1
- initial build. i need this lib for building aegis.

