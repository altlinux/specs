%def_disable static

Name: 	libmpcdec
Version: 1.2.2
Release: alt2.1
Summary: Portable Musepack decoder library
License: BSD
Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Group: System/Libraries
URL: http://www.musepack.net

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Sun Jun 19 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
Portable Musepack decoder library.
Compatibility package.

%prep
%setup -q

%build
%configure %{subst_enable static}
%make_build CFLAGS="%optflags" CXXFLAGS="$CFLAGS"

%install
%makeinstall

%files
%_libdir/*.so.*

%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmpcdec
  * postun_ldconfig for libmpcdec

* Mon Apr 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.2-alt2
- Compatibility package without -devel.

* Thu Jun 15 2006 LAKostis <lakostis at altlinux.ru> 1.2.2-alt1
- 1.2.2.
- disable static build by default.

* Sun Jun 19 2005 LAKostis <lakostis@altlinux.ru> 1.2-alt1
- first build for Sisyphus.

