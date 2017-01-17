%def_disable static
%def_disable docs
%def_enable regexp

Name: liblognorm
Version: 2.0.2
Release: alt1

Summary: liblognorm is a tool to normalize log data.
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.liblognorm.com/

Source: %name-%version.tar
BuildRequires: pkgconfig(libestr)
BuildRequires: pkgconfig(libfastjson)
%{?_enable_regexp:BuildRequires: pkgconfig(libpcre)}
%{?_enable_docs:BuildRequires: /usr/bin/sphinx-build}

%description
Liblognorm shall help to make sense out of syslog data, or, actually, any event data that is present in text form.

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
	%{subst_enable docs} \
	%{subst_enable regexp}

%make_build

%install
%makeinstall

%files
%_bindir/lognormalizer
%_libdir/%name.so.*
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
* Tue Jan 17 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue Nov 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Jan 14 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- Initial build for ALT Linux
