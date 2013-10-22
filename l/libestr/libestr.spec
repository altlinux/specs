%def_disable static

Name: libestr
Version: 0.1.8
Release: alt1

Summary: Some Essentials for string processing
License: LGPLv2.1+
Group: System/Libraries
Url: http://libestr.adiscon.com

Source: %name-%version.tar

%description
Some essentials for string handling (and a bit more)

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
%doc AUTHORS ChangeLog

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/%name.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
* Tue Oct 22 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Fri Apr 26 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- Initial build for ALT Linux
