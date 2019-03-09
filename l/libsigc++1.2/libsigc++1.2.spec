Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define apiver 1.2
%define dir_name sigc++-%apiver

Name: libsigc++%apiver
Version: 1.2.7
Release: alt3

%def_disable static

Summary: The Typesafe Signal Framework for C++
License: LGPL
Group: System/Libraries
Url: http://libsigc.sourceforge.net/

#Provides: libsigc++ = %version

Prefix: %prefix

Source: http://download.sourceforge.net/libsigc/libsigc++-%version.tar.bz2

BuildRequires: gcc-c++ libstdc++-devel xsltproc docbook-style-xsl

%description
This library implements a full callback system for use in widget libraries,
abstract interfaces, and general programming. Originally part of the Gtk--
widget set, libsigc++ is now a seperate library to provide for more general
use. It is the most complete library of its kind with the ablity to connect
an abstract callback to a class method, function, or function object. It
contains adaptor classes for connection of dissimilar callbacks and has an
ease of use unmatched by other C++ callback libraries.

Package gtkmm, which is a C++ binding to the gtk+ library, uses libsigc++.

%package devel
Summary: Development tools for the Typesafe Signal Framework for C++
Group: Development/C++
Requires: %name = %version-%release
#Provides: libsigc++-devel = %version

%description devel
This package contains files needed for development with libsigc++.

%if_enabled static
%package devel-static
Summary: Static library for the Typesafe Signal Framework for C++
Group: Development/C++
Requires: %name-devel = %version-%release
#Provides: libsigc++-devel-static = %version

%description devel-static
This package contains static library needed for development
of statically linked software with libsigc++.
%endif	# enabled static

%package examples
Summary: Examples and test suite for the Typesafe Signal Framework for C++
Group: Development/C++
Requires: %name-devel = %version-%release

%description examples
This package contains source code of example and test
programs for libsigc++.

%prep
%setup -q -n libsigc++-%version

%build
# the 1.2.5 tarball is so fresh it's ahead of my time
touch configure
%undefine __libtoolize
%configure %{subst_enable static}

%make_build
%make check

%make -C doc/manual DOCBOOK_STYLESHEET=%_datadir/xml/docbook/xsl-stylesheets/html/chunk.xsl

%install
%define docdir %_docdir/libsigc++-%version

mkdir -p -m 755 $RPM_BUILD_ROOT{%_includedir,%_libdir}/%dir_name
%makeinstall

mkdir -p -m 755 $RPM_BUILD_ROOT%docdir
cp -a examples tests $RPM_BUILD_ROOT%docdir
find $RPM_BUILD_ROOT%docdir -type d \( -name .libs -o -name .deps \) -print0 |
	xargs -r0 rm -rf
find $RPM_BUILD_ROOT%docdir -type f -print0 |xargs -r0 file |
	egrep '(relocatable|executable|shell script)' |cut -d: -f1 |xargs -r rm -f
find $RPM_BUILD_ROOT%docdir -type f -name 'Makefile.*' -print0 |
	xargs -r0 rm -f
cp -pf scripts/examples.Makefile \
	$RPM_BUILD_ROOT%docdir/examples/Makefile
cp -pf scripts/tests.Makefile \
	$RPM_BUILD_ROOT%docdir/tests/Makefile

echo "%%dir %docdir" >docs.list
for f in AUTHORS FEATURES README IDEAS ChangeLog NEWS TODO \
         doc/{API,FAQ,UML,conventions,diagrams,marshal,powerusers,requirements,signals}; do
    destname=`basename $f`
    install -m 644 $f $RPM_BUILD_ROOT%docdir/$destname
    echo "%docdir/$destname" >>docs.list
done
cp -a doc/manual/html $RPM_BUILD_ROOT%docdir
echo "%docdir/html" >>docs.list

%files
%_libdir/*.so.*

%files devel -f docs.list
%_libdir/pkgconfig/*
%_libdir/*.so
%dir %_libdir/%dir_name
%_libdir/%dir_name/include
%_includedir/%dir_name

%if_enabled static
%files devel-static
%_libdir/*.a
%endif	# enabled static

%files examples
%dir %docdir
%docdir/examples
%docdir/tests

%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt3
- Rebuilt for debuginfo

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt2
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsigc++1.2
  * postun_ldconfig for libsigc++1.2

* Fri May 11 2007 Igor Zubkov <icesik@altlinux.org> 1.2.7-alt1
- 1.2.5 -> 1.2.7

* Fri May 11 2007 Igor Zubkov <icesik@altlinux.org> 1.2.5-alt3
- rebuilt

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.5-alt2.1
- Rebuilt with libstdc++.so.6.

* Wed Dec 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.5-alt2
- Removed libtool files from the filelist

* Fri May 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.5-alt1
- New version

* Tue Mar 25 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed Jan 08 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Mon Dec 02 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Nov 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.1-alt1
- introduced the libsigc++1.2 branch
- make manual
- disabled static by default
- docs are moved to devel package, docdir is nicely named
- examples are moved to docdir

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.4-alt2
- Bumped soname for g++ >= 3.2
- Updated %%post/%%postun scripts.

* Wed Oct 24 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.4-alt1
- 1.0.4

* Wed Aug 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.3-ipl2
- Moved static library to devel-static subpackage.

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.3-ipl1
- 1.0.3

* Sun Nov 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.2-ipl1
- 1.0.2

* Sat Sep 30 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.1-ipl1
- Rebuilt with glibc-2.1.94 and gcc-2.96.

* Wed Jun 28 2000 Dmitry V. Levin <ldv@fandra.org>
- RE and Fandra adaptions.
- FHSification.

* Mon May 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.0.1 released:
  + Fixed: slot_class from Peter R <petur_r@usa.net>,
  + Marshaller improvements to handle non POD data from Peter R.

* Sun Apr 16 2000 Dmitry V. Levin <ldv@fandra.org>
- retbind.h.m4 was lost in recent release

* Sat Apr 15 2000 Dmitry V. Levin <ldv@fandra.org>
- Updated Url and Source fileds
- 1.0.0 stable release

* Sat Jan 22 2000 Dmitry V. Levin <ldv@fandra.org>
- Filtering out -fno-rtti and -fno-exceptions options from $RPM_OPT_FLAGS
- Minor install section cleanup

* Wed Jan 19 2000 Allan Rae <rae@lyx.org>
- Autogen just creates configure, not runs it, so cleaned that up too.

* Wed Jan 19 2000 Dmitry V. Levin <ldv@fandra.org>
- Minor attr fix
- Removed unnecessary curly braces
- Fixed Herbert's adjustement

* Sat Jan 15 2000 Dmitry V. Levin <ldv@fandra.org>
- Minor package dependence fix

* Sat Dec 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- Fixed typo of mine
- Added traditional CUSTOM_RELEASE stuff
- Added SMP support

* Thu Dec 23 1999 Herbert Valerio Riedel <hvr@gnu.org>
- Adjusted spec file to get tests.Makefile and examples.Makefile from scripts/

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- Split into three packages: %name, %name-devel and %name-examples

* Thu Aug 12 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Updated source field and merged conflicts between revisions.

* Tue Aug 10 1999 Dmitry V. Levin <ldv@fandra.org>
- Updated Prefix and BuildRoot fields

* Thu Aug  5 1999 Herbert Valerio Riedel <hvr@hvrlab.dhs.org>
- Made sure configure works on all alphas

* Wed Jul  7 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Added autoconf macro for sigc.

* Fri Jun 11 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Made into a .in to keep version field up to date
- Still need to do release by hand

* Mon Jun  7 1999 Dmitry V. Levin <ldv@fandra.org>
- Added Vendor and Packager fields

* Sat Jun  5 1999 Dmitry V. Levin <ldv@fandra.org>
- Updated to 0.8.0

* Tue Jun  1 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision
