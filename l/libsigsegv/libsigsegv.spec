Name: libsigsegv
Version: 2.10
Release: alt1

Summary: Library for handling page faults in user mode
License: GPLv2+
Group: System/Libraries
Url: http://www.gnu.org/software/libsigsegv/
# git://git.altlinux.org/gears/l/libsigsegv
Source: %name-%version-%release.tar
%define libname %{name}2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description
This is a library for handling page faults in user mode.  A page fault
occurs when a program tries to access to a region of memory that is
currently not available.  Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package -n %libname
Summary: Library for handling page faults in user mode
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: %name < %version-%release

%description -n %libname
This is a library for handling page faults in user mode.  A page fault
occurs when a program tries to access to a region of memory that is
currently not available.  Catching and handling a page fault is a useful
technique for implementing:
  - pageable virtual memory
  - memory-mapped access to persistent databases
  - generational garbage collectors
  - stack overflow handlers
  - distributed shared memory

%package devel
Summary: GNU libsigsegv development library and header files
Group: Development/C
Requires: %libname = %version-%release

%description devel
The development library and header files for building applications
with GNU libsigsegv.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files -n %libname
%_libdir/*.so.*
%doc AUTHORS README NEWS

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt4
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt3
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt2
- Renamed shared library subpackage to libsigsegv2.

* Sun Jun 06 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt1
- Updated to 2.8.
- Moved "make check" to %%check section.

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt3
- fixes based in wrar's spec:
   - package the shared library into its own package, not in -devel (Closes: #19895)
   - fix other specfile problems
   - enable tests

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt2
- move *.so to main package

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.6-alt1
- 2.6

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.4-alt2
- Remove Russian summary and description.

* Sun Oct 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.4-alt1
- Stable version 2.4.

* Sat Feb 19 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt3
- Reduild with gcc 3.4.

* Fri May 14 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt2
- BuildPreReq on autoconf 1.7.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1.20030818-alt1
- Rebuild.

* Tue Aug 19 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1-alt1csv20030818
- CVS 18.08.2003.

* Sun Jul 06 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.1-alt1csv20030706
- CVS 06.07.2003.

* Sat Oct 19 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 2.0.1-alt1csv20021019
- First ALT Linux release.

