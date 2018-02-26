Name: libmm
Version: 1.4.2
Release: alt3

%define srcname mm-%version

Summary: Shared Memory Abstraction Library
License: BSD-style
Group: System/Libraries

Url: http://www.ossp.org/pkg/lib/mm
Source: %url/%srcname.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

Provides: mm = %version
Obsoletes: mm < %version

# Automatically added by buildreq on Mon Mar 21 2011
BuildRequires: glibc-devel-static termutils

%package devel
Summary: Development files for Shared Memory Abstraction Library
Group: Development/C
Requires: %name = %version-%release
Provides: mm-devel = %version
Obsoletes: mm-devel < %version

%package devel-static
Summary: Static version of Shared Memory Abstraction Library
Group: Development/C
Requires: %name-devel = %version-%release

%description
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

%description devel
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

This package contains header files and tools needed for development with %name.

%description devel-static
The MM library is a 2-layer abstraction library which simplifies the usage of
shared memory between forked (and this way strongly related) processes under
Unix platforms. On the first layer it hides all platform dependent
implementation details (allocation and locking) when dealing with shared
memory segments and on the second layer it provides a high-level malloc(3)-
style API for a convenient and well known way to work with data-structures
inside those shared memory segments.

This package contains static library needed for development of statically
linked software with %name.

%prep
%setup -q -n %srcname
bzip2 -k ChangeLog

%build
%configure --enable-debug
%make_build
make test

%install
%makeinstall

%files
%_libdir/*.so.*
%doc README LICENSE ChangeLog.bz2 PORTING THANKS

%files devel
%_bindir/*
%_libdir/*.so
#_libdir/*.la
%_includedir/*
%_mandir/man?/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.4.2-alt3
- rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.4.2-alt2
- applied repocop patch

* Fri Apr 06 2007 Michael Shigorin <mike@altlinux.org> 1.4.2-alt1
- 1.4.2 (thanks ldv@ for notifying that apache builds against
  an ancient release)
- shortened description
- compressed ChangeLog (1/3 of package size)
- removed patch

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 1.3.0-alt2
- Do not package .la files.
- Do not package %name-devel-static by default.

* Thu May 08 2003 Rider <rider@altlinux.ru> 1.3.0-alt1
- new version

* Mon Jan 06 2003 Rider <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Nov 18 2002 Rider <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1
- removed old patches

* Mon Jul 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-ipl4mdk
- Fixed tmp races (by Sebastian Krahmer).

* Mon Sep 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.3-ipl3mdk
- Libification.

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.3-ipl2mdk
- FHSification.

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.3-ipl1mdk
- 1.1.3
- RE adaptions.

* Wed May 03 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.1.1

* Sun Mar  5 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
