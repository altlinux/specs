%def_disable static

Name: librelp
Version: 1.0.0
Release: alt1

Summary: The RELP (reliable event logging protocol) core protocol library
License: GPLv3
Group: System/Libraries
Url: http://www.librelp.com/

Source: %name-%version.tar

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

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall

%files
%_libdir/%name.so.*
%doc AUTHORS ChangeLog doc/relp.html

%files devel
%_pkgconfigdir/relp.pc
%_libdir/%name.so
%_includedir/%name.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
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
