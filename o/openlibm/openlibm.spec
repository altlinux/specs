# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major     4
%define libname   libopenlibm%{major}
%define develname libopenlibm-devel

Summary:        High quality system independent, open source libm
Name:           openlibm
Version:        0.8.1
Release:        alt1_1
License:        BSD and MIT and ISC and Public Domain
Group:          System/Libraries
URL:            https://github.com/JuliaLang/openlibm/
Source0:        https://github.com/JuliaLang/openlibm/archive/v%{version}/%{name}-%{version}.tar.gz
Source44: import.info

%description
OpenLIBM is an effort to have a high quality standalone LIBM library.
It is meant to be used standalone in applications and programming language
implementations. The OpenLIBM code derives from the FreeBSD msun implementation,
which in turn derives from FDLIBM 5.3. As a result, it has a number of fixes
and updates that have accumulated over the years in msun, and also optimized
assembly versions of many functions.

%package -n %{libname}
Summary:        High quality system independent, open source libm
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{_lib}openlibm5 < 0.5.3-2

%description -n %{libname}
OpenLIBM is an effort to have a high quality standalone LIBM library.
It is meant to be used standalone in applications and programming language
implementations. The OpenLIBM code derives from the FreeBSD msun implementation,
which in turn derives from FDLIBM 5.3. As a result, it has a number of fixes
and updates that have accumulated over the years in msun, and also optimized
assembly versions of many functions.

%package -n %{develname}
Summary:        High quality system independent, open source libm
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
Contains header files for developing applications that use the %{name}
library.

%prep
%setup -q

# File under the Apple Public Source License Version 1.1
rm -f test/ieeetestnew.c
# File under the Apple Public Source License Version 2.0
rm -f i387/osx_asm.h

%build

%make_build

%check
# Tests still fail on ARM because of floating-point exceptions
# which are not set correctly (but other tests are fine)
%ifnarch %{arm}
make test
%endif

%install
%makeinstall_std prefix=%{_prefix} \
              libdir=%{_libdir} \
              includedir=%{_includedir}

rm %{buildroot}%{_libdir}/libopenlibm.a

%files -n %{libname}
%doc LICENSE.md README.md
%{_libdir}/libopenlibm.so.%{major}*

%files -n %{develname}
%{_libdir}/libopenlibm.so
%{_libdir}/pkgconfig/openlibm.pc
%{_includedir}/openlibm/


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt1_1
- update by mgaimport

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- update by mgaimport

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_2
- new version

