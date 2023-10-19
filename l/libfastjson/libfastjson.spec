%def_disable static

Name: libfastjson
Version: 1.2304.0
Release: alt1

Summary: A JSON implementation in C
License: MIT
Group: System/Libraries

Url: https://github.com/rsyslog/libfastjson
Source: %name-%version.tar

%description
libfastjson implements a reference counting object
model that allows you to easily construct JSON
objects in C, output them as JSON formatted strings
and parse JSON formatted strings back into the
C representation of JSON objects.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

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
	%{subst_enable static}

%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc README.md ChangeLog

%files devel
%_pkgconfigdir/*.pc
%_libdir/%name.so
%_includedir/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
* Thu Oct 19 2023 Alexey Shabalin <shaba@altlinux.org> 1.2304.0-alt1
- New version 1.2304.0 (Fixed: CVE-2020-12762).

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 0.99.9-alt1
- new version 0.99.9

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.99.8-alt3
- NMU: remove rpm-build-ubt from BR:

* Mon Apr 08 2019 Michael Shigorin <mike@altlinux.org> 0.99.8-alt2
- drop %%ubt macro
- minor spec cleanup

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 0.99.8-alt1%ubt
- 0.99.8

* Wed Nov 08 2017 Alexey Shabalin <shaba@altlinux.ru> 0.99.7-alt1%ubt
- 0.99.7

* Tue Jan 17 2017 Alexey Shabalin <shaba@altlinux.ru> 0.99.4-alt1
- Initial build for ALT Linux
