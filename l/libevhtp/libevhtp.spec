# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		0
%define libname		libevhtp%{major}
%define develname	libevhtp-devel

Name:		libevhtp
Version:	1.2.18
Release:	alt1_4
Summary:	A more flexible replacement for libevent's http API
License:	BSD
Group:		System/Libraries
Url:		https://criticalstack.com/
Source0:	https://github.com/criticalstack/libevhtp/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		libevhtp-1.2.18-fix-libraries-path.patch
BuildRequires:	cmake
BuildRequires:	glibc-devel
BuildRequires:	pkgconfig(jemalloc)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(oniguruma)
Source44: import.info

%description
Libevhtp was created as a replacement API for Libevent's current
HTTP API. The reality of libevent's http interface is that it
was created as a JIT server, meaning the developer never thought
of it being used for creating a full-fledged HTTP service.
Infact I am under the impression that the libevent http API was
designed almost as an example of what you can do with libevent.
It's not Apache in a box, but more and more developers are
attempting to use it as so.

#----------------------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n	%{libname}
Libevhtp was created as a replacement API for Libevent's current
HTTP API. The reality of libevent's http interface is that it
was created as a JIT server, meaning the developer never thought
of it being used for creating a full-fledged HTTP service.
Infact I am under the impression that the libevent http API was
designed almost as an example of what you can do with libevent.
It's not Apache in a box, but more and more developers are
attempting to use it as so.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	evhtp-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%prep
%setup -q
%patch0 -p1


%build
%{mageia_cmake} -DEVHTP_BUILD_SHARED:STRING=ON \
       -DEVHTP_USE_JEMALLOC:STRING=ON

%mageia_cmake_build

%install
%mageia_cmake_install

%files -n %{libname}
%{_libdir}/libevhtp.so.%{major}
%{_libdir}/libevhtp.so.%{version}

%files -n %{develname}
%doc ChangeLog README.markdown
%doc --no-dereference LICENSE
%{_includedir}/evhtp.h
%{_includedir}/evhtp/
%{_libdir}/libevhtp.so
%{_libdir}/pkgconfig/evhtp.pc
%{_libdir}/cmake/libevhtp/


%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_4
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.18-alt1_3
- fixed build

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.18-alt1_1
- new version

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.16-alt1.S1.1
- NMU: rebuilt with new openssl.

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.16-alt1.1
- NMU: rebuilt with new openssl.

* Fri Apr 06 2018 Anton Farygin <rider@altlinux.ru> 1.2.16-alt1%ubt
- 1.2.16
- build with liboniguruma 6.8.1
- soname changed to 0 by upstream
- added %%ubt tag for facilitate backporting to stable branches

* Thu Nov 16 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.13-alt1
- new version 1.2.13 (with rpmrb script)

* Wed May 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.11n-alt4
- change upstream Url
- build with jemalloc

* Tue Aug 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.11n-alt3
- build with external libOniGuruma-devel
- fix soname

* Sat Aug 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.11n-alt2
- fix dir packing

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.11n-alt1
- new version 1.2.11n via git merge

* Sun Aug 24 2014 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)
- add devel package

* Sat Mar 16 2013 Denis Baranov <baraka@altlinux.ru> 1.2.1-alt1
- Initial build for ALTLinux

