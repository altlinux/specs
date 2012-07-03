Name: OpenSP
Version: 1.5.2
Release: alt3

%def_disable static
%def_enable http

%define sgmlbase %_datadir/sgml
%define sgmlconfdir %_sysconfdir/sgml

Summary: SGML and XML parsing tools from the OpenJade Group
Group: Publishing
License: BSD
Url: http://openjade.sourceforge.net/

Requires: lib%name = %version-%release
Conflicts: openjade < 1.3.2-alt1

Source: http://download.sourceforge.net/openjade/OpenSP-%version.tar.bz2
Patch0: %name-1.5.1-disable-http.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=245104
Patch1: opensp-sigsegv.patch

# Automatically added by buildreq on Sat Jun 03 2006
BuildRequires: cvs gcc-c++ xmlto

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.

%package -n lib%name
Summary: Runtime library for the OpenJade group's SP suite
Group: System/Libraries

%description -n lib%name
This is the SP suite's shared library runtime support.  This C++
library contains entity management functions, parsing functions, and
other functions useful for SGML/XML/DSSSL development.
'

%package -n lib%name-devel
Summary: Libraries and include files for developing OpenSP applications
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This contains include files and libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for developing OpenSP applications
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This contains static libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.
%endif	# enabled static

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .sigsegv

%build
%autoreconf
%configure %{subst_enable static} \
    --enable-default-catalog=%sgmlconfdir/catalog \
    --enable-default-search-path=%sgmlbase \
    %{subst_enable http}
%make_build

%install
%make_install DESTDIR=%buildroot \
    pkgdatadir=%sgmlbase/%name \
    pkgdocdir=%_docdir/%name-%version \
    install

# oMy, othis ois osilly.
for file in nsgmls sgmlnorm spam spent; do
    ln -s o$file %buildroot%_bindir/$file
    echo ".so man1/o${file}.1" > %buildroot%_man1dir/${file}.1
done
# Provide the sgml2xml alias as RedHat does
ln -s osx %buildroot%_bindir/sgml2xml
echo ".so man1/osx.1" > %buildroot%_man1dir/sgml2xml.1

rm -f %buildroot%_docdir/%name-%version/ABOUT-NLS

%find_lang %name

%files -f %name.lang
%_bindir/*
%sgmlbase/%name
%_man1dir/*
%_docdir/%name-%version

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif	# enabled static

%changelog
* Thu Oct 28 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt3
- rebuild

* Tue Dec 16 2008 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt2
- removed obsolete %%post{,un}_ldconfig
- added patch from Fedora to fix openjade segfault
  see https://bugzilla.redhat.com/show_bug.cgi?id=245104

* Sat Jun 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.2-alt1
- Release 1.5.2
- Patch1 is obsolete
- Buildreq

* Mon Jan 17 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.1-alt2
- Fix for GCC 3.4

* Fri Dec 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.1-alt1
- New upstream release
- Patch0 obsoleted
- Removed libtool files from the filelist

* Tue Apr 01 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5-alt2
- Removed sx alias as it conflicts with lrzsz

* Sat Mar 29 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5-alt1
- Adopted to ALT Linux
- Added libOpenSP-devel-static package
- HTTP Host: header patch from RH's openjade package

* Mon Feb  3 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1.5-1mdk
- Initial Mandrake package
