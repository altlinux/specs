# examples depend on this
%def_with check
%def_enable check

Name: libnftnl
Version: 1.2.8
Release: alt1

Summary: Netfilter nf_tables infrastructure library
License: GPL-2.0-only
Group: System/Libraries

Url: http://netfilter.org/projects/libnftnl/
Source: %name-%version.tar
BuildRequires: libmnl-devel libmxml-devel libjansson-devel

%description
libnftnl is a userspace library providing a low-level netlink
programming interface (API) to the in-kernel nf_tables subsystem.
The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: pkgconfig, %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Development files for %name
Group: System/Libraries
Requires: pkgconfig, %name = %version-%release

%description devel-static
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package examples
Summary: Examples for %name
Group: System/Libraries

%description examples
The %name-examples package contains examples files for %name.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure --with-xml-parsing --with-json-parsing --enable-static
%make_build

# FIXME: --without check will cause packaging breakage
%check
%make check
mkdir -p %buildroot%_sbindir
cp -a examples/.libs/* %buildroot%_sbindir/

%install
%makeinstall_std

%files
%doc COPYING
%_libdir/%name.so.*

%files devel
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

%files devel-static
%_libdir/*.a

%if_with check
%if_enabled check
%files examples
%doc examples/*.c
%_sbindir/*
%endif
%endif

%changelog
* Fri Oct 04 2024 Alexei Takaseev <taf@altlinux.org> 1.2.8-alt1
- 1.2.8

* Tue Jul 23 2024 Alexei Takaseev <taf@altlinux.org> 1.2.7-alt1
- 1.2.7

* Fri Jul 14 2023 Alexei Takaseev <taf@altlinux.org> 1.2.6-alt1
- 1.2.6

* Fri Mar 10 2023 Alexei Takaseev <taf@altlinux.org> 1.2.5-alt1
- 1.2.5

* Fri Nov 11 2022 Alexei Takaseev <taf@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Aug 10 2022 Alexei Takaseev <taf@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Jun 09 2022 Alexei Takaseev <taf@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Nov 22 2021 Alexei Takaseev <taf@altlinux.org> 1.2.1-alt1
- 1.2.1

* Wed Aug 25 2021 Alexei Takaseev <taf@altlinux.org> 1.2.0-alt2
- Added -ffat-lto-objects to %optflags_lto.

* Thu May 27 2021 Alexei Takaseev <taf@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Mar 25 2021 Alexei Takaseev <taf@altlinux.org> 1.1.9-alt1
- 1.1.9

* Mon Nov 16 2020 Alexei Takaseev <taf@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Jun 17 2020 Alexei Takaseev <taf@altlinux.org> 1.1.7-alt1
- Version 1.1.7

* Fri Apr 03 2020 Alexei Takaseev <taf@altlinux.org> 1.1.6-alt1
- Version 1.1.6

* Tue Dec 03 2019 Alexei Takaseev <taf@altlinux.org> 1.1.5-alt1
- Version 1.1.5

* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 1.1.4-alt2
- Fix build --without check (still weird though)
- Minor spec cleanup

* Tue Aug 20 2019 Alexei Takaseev <taf@altlinux.org> 1.1.4-alt1
- Version 1.1.4

* Mon May 27 2019 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3 (required by iptables-nft >= 1.8.3).

* Thu Jan 10 2019 Alexei Takaseev <taf@altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Sat Jun 09 2018 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Wed May 02 2018 Alexei Takaseev <taf@altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Tue Jan 09 2018 Alexei Takaseev <taf@altlinux.org> 1.0.9-alt1
- Version 1.0.9

* Fri Oct 13 2017 Alexei Takaseev <taf@altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Tue Dec 20 2016 Alexei Takaseev <taf@altlinux.org> 1.0.7-alt1
- Version 1.0.7

* Fri Jun 03 2016 Alexei Takaseev <taf@altlinux.org> 1.0.6-alt1
- Version 1.0.6

* Mon Dec 21 2015 Alexei Takaseev <taf@altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140908
- Version 1.0.2

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt2
- move examples to own package

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- first build for ALT Linux
