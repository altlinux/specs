Name: libtommath
Version: 1.0.1
Release: alt1
Summary: A portable number theoretic multiple-precision integer library
Group: System/Libraries
License: WTFPL
Url: http://www.libtom.net/

# https://github.com/libtom/libtommath.git
Source: ltm-%version.tar

BuildRequires: texlive-latex-recommended
BuildRequires: ghostscript-utils libtiff-utils

%description
A free open source portable number theoretic multiple-precision integer
library written entirely in C. (phew!). The library is designed to
provide a simple to work with API that provides fairly efficient
routines that build out of the box without configuration.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
The %name-devel-static package contains static libraries for
developing applications that use %name.

%package doc
Summary: Documentation files for %name
Group: Documentation
Requires: %name = %EVR

%description doc
The %name-doc package contains PDF documentation for
using %name.

%prep
%setup
# Fix permissions on installed library
sed -i -e 's/644 $(LIBNAME)/755 $(LIBNAME)/g' makefile.shared

# Fix pkgconfig path
sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=%{_libdir}|g' \
    -e 's|^includedir=.*|includedir=%{_includedir}|g' \
    %{name}.pc.in

%build
%make_build V=1 LIBPATH=%_libdir CFLAGS="%{optflags} -I./" -f makefile.shared
%make_build V=1 -f makefile poster manual docs

%install
# There is no configure script that ships with libtommath but it does
# understand DESTDIR and it installs via that and the
# INSTALL_USER and INSTALL_GROUP environment variables.

export INSTALL_USER=$(id -un)
export INSTALL_GROUP=$(id -gn)
make install INCPATH=%_includedir/tommath DESTDIR=%buildroot LIBPATH=%_libdir -f makefile.shared
find %buildroot -name '*.la' -exec rm -f {} ';'
find %buildroot -name '*.h' -exec chmod 644 {} ';'

%files
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc LICENSE
%_includedir/tommath
%_libdir/*.so
%_pkgconfigdir/*.pc

%files devel-static
%_libdir/*.a

%files doc
%doc LICENSE
%doc doc/bn.pdf doc/poster.pdf doc/tommath.pdf

%changelog
* Fri Jan 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Updated to upstream version 1.0.1.

* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 0.42.0-alt1
- Autobuild version bump to 0.42.0

* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 0.41-alt1
- Initial build from FC

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.41-8
- Autorebuild for GCC 4.3

* Sun Nov 25 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 0.41-7
- Resolve multilib conflicts from Bug #342441 by splitting out
  documentation to libtommath-docs subpackage
- fix rpmlint Summary: warning

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.41-6
- Rebuild for selinux ppc32 issue.

* Fri Jun 29 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 0.41-5
- removed package name from summary

* Wed Jun 27 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 0.41-4
- changed patch to honor RPM_OPT_FLAGS
- changed patch to allow INCPATH to be set externally
- changed installation of headers to _includedir/tommath

* Sun Jun 24 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 0.41-3
- changed patch to bring it into line with the style of libtomcrypt

* Sat Jun 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 0.41-2
- add patch to makefile.shared to allow for /usr/lib64 installs
- update spec to pass libdir build and install process

* Fri Jun 22 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 0.41-1
- Initial spec file creation
