# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define jsoncpp_major 1
%define libname       libjsonrpccpp%{jsoncpp_major}
%define develname     libjsonrpccpp-devel

Name:           libjson-rpc-cpp
Version:        1.4.1
Release:        alt1_1
Summary:        C++ JSON Library
License:        Public Domain
Group:          System/Libraries
#Url:           http://jsoncpp.sourceforge.net/
URL:            https://github.com/cinemast/libjson-rpc-cpp
Source0:        https://github.com/cinemast/libjson-rpc-cpp/archive/v%{version}/%{name}-%{version}.tar.gz
#To generate docs
BuildRequires:  ccmake cmake ctest
BuildRequires:  doxygen
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  libhiredis-devel
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(argtable2)
Source44: import.info

%description
JsonCpp is a simple API to manipulate JSON value, handle serialization
and unserialization to string.

%package -n %libname
Summary:        JsonCpp library
Group:          System/Libraries

%description -n %libname
This framework provides cross platform JSON-RPC (remote procedure call)
support for C++. It is fully JSON-RPC 2.0 & 1.0 compatible.

%package -n     %{develname}
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       json-rpc-cpp-devel = %{version}-%{release}
Provides:       libjson-rpc-cpp-devel = %{version}-%{release}

%description -n    %{develname}
It can also preserve existing comment in unserialization/serialization steps,
making it a convenient format to store user input files.

Files for building applications with %{name} support.

%prep
%setup -q


%build
%{mageia_cmake} \
	-DCOMPILE_TESTS=NO \
	-DCOMPILE_STUBGEN=NO \
	-DFULL_PATH_LIBDIR=%{_libdir} \
	-DFULL_PATH_INCLUDEDIR=%{_includedir}
%mageia_cmake_build

%install
%mageia_cmake_install

%files -n %libname
%{_libdir}/libjsonrpccpp-*.so.%{jsoncpp_major}
%{_libdir}/libjsonrpccpp-*.so.%{jsoncpp_major}.*

%files -n %develname
%doc AUTHORS.md CHANGELOG.md README.md
%doc --no-dereference LICENSE.txt
%{_includedir}/jsonrpccpp/
%{_libdir}/libjsonrpccpp-*.so
%dir %{_libdir}/libjson-rpc-cpp/
%{_libdir}/libjson-rpc-cpp/cmake/
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_1
- update by mgaimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_5
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- fixed build

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- update by mgaimport

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- update by mgaimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5
- update by mgaimport

* Mon Sep 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1_3.1
- rebuild with libmicrohttpd-0.9.59

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- new version

