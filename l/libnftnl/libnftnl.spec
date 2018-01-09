Name:           libnftnl
Version:        1.0.9
Release:        alt1
Summary:        Netfilter nf_tables infrastructure library
Group:          System/Libraries
License:        LGPLv2.1+
URL:            http://netfilter.org/projects/libnftnl/
Source:        %name-%version.tar
BuildRequires: libmnl-devel libmxml-devel libjansson-devel

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%package        devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package        devel-static
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel-static
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package        examples
Summary:        Examples for %name
Group:          System/Libraries

%description    examples
The %name-examples package contains examples files for %name.


%prep
%setup

%build
%autoreconf
%configure --with-xml-parsing --with-json-parsing --enable-static
%make_build

%check
%make check
pushd tests
    ./test-script.sh
popd
mkdir -p %buildroot%_sbindir
cp examples/.libs/* %buildroot%_sbindir/

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

%files examples
%doc examples/*.c
%_sbindir/*

%changelog
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
