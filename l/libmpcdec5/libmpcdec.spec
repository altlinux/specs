%def_disable static

%define libname libmpcdec
%define soversion 5

Name: 	%libname%soversion
Version: 1.2.6
Release: alt4
Summary: Portable Musepack decoder library
License: BSD

Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Group: System/Libraries
URL: http://www.musepack.net

Source: %libname-%version.tar.bz2

Provides: %libname = %version-%release

# Automatically added by buildreq on Sun Jun 19 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
Portable Musepack decoder library.

%package -n %libname-devel
Summary: Development part of %name
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
Contents header files and development libraries for %name

%package -n %libname-devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %libname-devel = %version-%release

%description -n %libname-devel-static
Contents static libraries for %name

%prep
%setup -q -n %libname-%version

%build
%configure %{subst_enable static}
%make_build CFLAGS="%optflags" CXXFLAGS="$CFLAGS"

%install
%makeinstall

%files
%_libdir/*.so.*

%files -n %libname-devel
%_libdir/*.so
%dir %_includedir/mpcdec
%_includedir/mpcdec/*

%if_enabled static
%files -n %libname-devel-static
%_libdir/*.a
%endif #static

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt3
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmpcdec5
  * postun_ldconfig for libmpcdec5

* Wed Apr 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt2
- Removed version from devel packages.

* Mon Apr 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt1
- 1.2.6 release.
- Renamed library to libmpcdec5.

* Thu Jun 15 2006 LAKostis <lakostis at altlinux.ru> 1.2.2-alt1
- 1.2.2.
- disable static build by default.

* Sun Jun 19 2005 LAKostis <lakostis@altlinux.ru> 1.2-alt1
- first build for Sisyphus.

