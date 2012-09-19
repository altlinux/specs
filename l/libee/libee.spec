%def_disable static

Name: libee
Version: 0.4.1
Release: alt1

Summary: An Event Expression Library inspired by CEE
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.libee.org/

Source: %name-%version.tar
BuildRequires: libestr-devel

%description
CEE is an upcoming standard used to describe network events in a number of normalized formats.
It's goal is to unify they currently many different representations that exist in the industry.

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
%make

%install
%makeinstall

%files
%_libdir/%name.so.*
%_sbindir/%name-convert
%doc AUTHORS ChangeLog

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- Initial build for ALT Linux
