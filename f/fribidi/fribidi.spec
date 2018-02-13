%def_disable static
# for tests only
%def_with glib

Name: fribidi
Version: 1.0.1
Release: alt1

Summary: Bi-directional scripts support
License: %lgpl21plus
Group: Development/C
Url: https://github.com/%name/%name/

Source: %url/releases/download/v%version/%name-%version.tar.bz2

Requires: lib%name = %version-%release

BuildPreReq: rpm-build-licenses
%{?_with_glib:BuildRequires: glib2-devel}
%{?_enabled_static:BuildRequires: glibc-devel-static}

%package -n lib%name
Summary: Library implementing the Unicode BiDi algorithm
Group: System/Libraries

%package -n lib%name-devel
Summary: Library implementing the Unicode BiDi algorithm
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%description
Bi-directional scripts support.

%package -n lib%name-devel-static
Summary: Library implementing the Unicode BiDi algorithm
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name
A library to handle bidirectional scripts (eg hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.
The library uses unicode internally.

%description -n lib%name-devel
The libfribidi-devel package includes  header files
for the fribidi package.

Install libfribidi-devel if you want to develop programs which will use
fribidi.

%description -n lib%name-devel-static
The libfribidi-devel-static package includes the static libraries
for the fribidi package.

Install libfribidi-devel-static if you want to develop statically linked
programs which will use fribidi.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%configure %{subst_enable static} \
	%{?_with_glib:--with-glib=yes}
%make_build

%install
%makeinstall

%make check

%files
%_bindir/*
%doc README AUTHORS ChangeLog TODO THANKS NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Feb 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon May 09 2011 Sergey Vlasov <vsu@altlinux.ru> 0.19.2-alt1
- Version 0.19.2.
- Really disable static libraries.
- Package fribidi_*(3) man pages into libfribidi-devel.
- Use rpm-build-licenses; specify %lgpl21plus license version.
- Run tests after build.

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.9-alt4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.9-alt3
- Rebuilt for soname set-versions

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.10.9-alt2
- post-scripts removed

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 0.10.9-alt1
- new version

* Mon Apr 26 2004 Vital Khilko <vk@altlinux.ru> 0.10.4-alt3
- rebuild without .la 

* Tue Jul 08 2003 AEN <aen@altlinux.ru> 0.10.4-alt2
- missing *.pc files restored

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 0.10.4-alt1
- new version, patches removed

* Sun Mar 31 2002 AEN <aen@logic.ru> 0.10.1-alt3
- rebuilt with glib2-1.0.1
* Wed Mar 27 2002 AEN <aen@logic.ru> 0.10.1-alt2
- rebuilt with glib2-1.0.0
* Wed Feb 13 2002 AEN <aen@logic.ru> 0.10.1-alt1
- new version

* Tue Feb 12 2002 AEN <aen@logic.ru> 0.9.1-alt2
- Group in libfribidi fixed

* Wed Jan 09 2002 AEN <aen@logic.ru> 0.9.1-alt1
- new version

* Wed Oct 17 2001 AEN <aen@logic.ru> 0.9.0-alt4
- rebuild with glib2-1.3.9

* Tue Sep 25 2001 AEN <aen@logic.ru> 0.9.0-alt3
- Rebuild with glib2-1.3.7

* Mon Sep 17 2001 AEN <aen@loigc.ru> 0.9.0-alt2
- group fixed (thnx to Sergey Epifanov!)

* Tue Jun 26 2001 AEN <aen@logic.ru> 0.9.0-alt1
- new version
- libification

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation
- back to 2 packages

* Sun Jan 07 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 0.1.15-2mdk
- fixed Requires

* Sun Jan 07 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 0.1.15-1mdk
- new lib policy
- updated to 0.1.15

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.1.12-1mdk
- new and shiny version.
- macros and _tmppath.

* Sun Apr 02 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.1.9-1mdk
- New Group: naming
- updated to 0.1.9
- splitted in a -devel rpm; to make it compatible with the rpms in
  the http://www.pango.org/ site

* Mon Mar 13 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.1.8-1mdk
- updated to 0.1.8

* Mon Jan 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.1.6-3mdk
- Use %configure.

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environmint

* Thu Aug 05 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- first rpm version
