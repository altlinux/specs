Name:           libmnl
Version:        1.0.4
Release:        alt1
Summary:        Minimalistic Netlink library
Group:          System/Libraries
License:         LGPLv2.1+
URL:            http://netfilter.org/projects/libmnl
Source:        %name-%version.tar

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use
code and to avoid re-inventing the wheel.

%package	devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       pkgconfig, %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README COPYING
%_libdir/%name.so.*

%files devel
%doc examples
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

%changelog
* Thu Dec 01 2016 Alexei Takaseev <taf@altlinux.org> 1.0.4-alt1
- 1.0.4

* Mon Dec 21 2015 Alexei Takaseev <taf@altlinux.org> 1.0.3-alt1.git20151003
- New snapshot

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20140613
- New snapshot

* Thu Feb 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt1
- New version

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- New version

* Mon Mar 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt2
- Rebuild for debug

* Sun Jan 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- first build for ALT Linux
