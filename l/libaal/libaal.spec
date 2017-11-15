%def_enable shared
%def_enable static
%def_disable Werror
%def_disable debug
%def_enable libminimal
%def_disable memory_manager
%def_enable largefile

%define bname aal
Name: lib%bname
Version: 1.0.6
Release: alt1
Summary: Abstraction library for ReiserFS utilities
License: GPLv2
Group: System/Libraries
URL: http://reiser4.sourceforge.net/

Source: %name-%version.tar

%description
This is a library that provides application abstraction mechanism.
It include device abstraction, libc independence code, etc.

%package devel
Summary: Headers and libraries for developing with %name
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
This package includes headers and libraries for developing with the
%name library.

%package devel-static
Summary: Static libraries for developing with %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package includes static libraries for developing with the %name
library.

%if_enabled libminimal
%if_enabled shared
%package minimal
Summary: Minimal abstraction library for ReiserFS utilities
Group: System/Libraries

%description minimal
This is a minimal library that provides application abstraction
mechanism. It include device abstraction, libc independence code, etc.
%endif

%package minimal-devel
Summary: Headers and libraries for developing with %name-minimal
Group: Development/C
Requires: %name-minimal = %version-%release
Requires: %name-devel = %version-%release
Provides: %name-minimal-devel-static = %version-%release

%description minimal-devel
This package includes the headers and libraries for developing with the
%name-minimal library.
%endif

%prep
%setup
sed -i -r '/^[[:blank:]]+\.\/run-ldconfig/d' Makefile.am

%build
%autoreconf
%configure \
	--libdir=/%_lib \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable debug} \
	%{subst_enable Werror} \
	%{subst_enable largefile} \
	%{subst_enable libminimal} \
	%{subst_enable_to memory_manager memory-manager}

%make_build

%install
%makeinstall_std

# Static libraries and library symlinks not needed to be in %_lib/, relocate them to %_libdir/
install -d  -m 0755 %buildroot{%_libdir,%_docdir/%name-%version}
for f in %buildroot/%_lib/*.so; do
	ln -sf /%_lib/$(readlink -n "$f") "$f"
done
mv %buildroot/%_lib/*.{a,so} %buildroot%_libdir/

install -m 0644 AUTHORS COPYING CREDITS ChangeLog THANKS %buildroot%_docdir/%name-%version/

%if_enabled shared
%files
%doc %_docdir/%name-%version
/%_lib/%name-1.0.so.*
%endif

%files devel
%{?_disable_shared:%doc %_docdir/%name-%version}
%{?_enable_shared:%_libdir/%name.so}
%_includedir/%bname
%_datadir/aclocal/*

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%if_enabled libminimal
%if_enabled shared
%files minimal
/%_lib/%name-minimal.so.*
%endif

%files minimal-devel
%_libdir/%name-minimal.*
%endif

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1
- Updated to upstream version 1.0.6.

* Sat Aug 31 2013 Led <led@altlinux.ru> 1.0.5-alt4
- cleaned up code
- cleaned up spec
- cleaned up BuildRequires
- fixed Group
- fixed URL
- added docs

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.5-alt3.1.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt3.1
- rebuild (with the help of girar-nmu utility)

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 1.0.5-alt3
- Spec cleaning, updated URL etc.
- Remove explicit debug build enabling (this triggered disabling optimization
  flags in rpm macro substitution).

* Thu Aug 17 2006 Sergey Ivanov <seriv@altlinux.org> 1.0.5-alt2
- fix bug #9885

* Fri Aug 12 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.5-alt1
- updated to new version from namesys.com

* Mon Feb 21 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.4-alt1
- new version from namesys.com

* Sat Dec 11 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.3-alt1
- new version from namesys.com, includes:
- a lot of bug fixes,
- correct handling of super block backups,
- recovery according to the super block backups,
- demos/busy is a reiser4progs-busy-box program that is able
  to create/remove/copy/read/ls/etc on reiser4 working through
  libreiser4, without kernel reiser4 support.

  It happened that the previous super block backups were created 
  with a mistake and to resync them now you need to run
	fsck.reiser4 --build-sb <device>

* Wed Nov 17 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt2
- [#5222] (*.so should be installed into /lib/, not /usr/lib/),
  *-minimal libs moved to separate package, removed false g77 dependency.

* Tue Oct 26 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt1
- version 1.0.2; descriptions, files and options taken from libaal.spec from sourcces package

* Wed Aug 25 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.0-alt1
- initial build
