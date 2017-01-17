%def_disable static
%def_enable tls

Name: librelp
Version: 1.2.12
Release: alt1

Summary: The RELP (reliable event logging protocol) core protocol library
License: GPLv3
Group: System/Libraries
Url: http://www.librelp.com/

Source: %name-%version.tar

%{?_enable_tls:BuildRequires: pkgconfig(gnutls) >= 2.0.0}

%description
librelp is an easy to use library for the RELP protocol. RELP in turn
provides reliable event logging over the network (and consequently
RELP stands for Reliable Event Logging Protocol).

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable tls}

%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS ChangeLog doc/relp.html

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/%name.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
* Fri Jan 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Thu Apr 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Thu Nov 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Thu Jul 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Dec 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Rebuilt for soname set-versions

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for librelp
  * postun_ldconfig for librelp
  * postclean-05-filetriggers for spec file

* Sun Nov 02 2008 Ivan Fedorov <ns@altlinux.org> 0.1.1-alt1
- Initial build for ALT Linux
