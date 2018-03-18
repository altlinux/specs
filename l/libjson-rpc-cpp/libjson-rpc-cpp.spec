# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/git gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define jsoncpp_major 1
%define libname libjsonrpccpp%{jsoncpp_major}
%define develname libjsonrpccpp-devel

Name:       libjson-rpc-cpp
Version:    1.0.0
Release:    alt1_3
Summary:    C++ JSON Library
License:    Public Domain
Group:      System/Libraries
#Url:        http://jsoncpp.sourceforge.net/
URL:            https://github.com/cinemast/libjson-rpc-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#To generate docs
BuildRequires: 	ccmake cmake ctest
BuildRequires: 	pkgconfig(libcurl)
BuildRequires: 	pkgconfig(libmicrohttpd)
BuildRequires:  libhiredis-devel
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(argtable2)
Source44: import.info

%description
JsonCpp is a simple API to manipulate JSON value, handle serialization
and unserialization to string.

%package -n %libname
Summary:        JsonCpp library
Group:          System/Libraries
Obsoletes:      %{_lib}libjson-rpc-cpp1 < 1.0.0-2

%description -n %libname
This framework provides cross platform JSON-RPC (remote procedure call)
support for C++. It is fully JSON-RPC 2.0 & 1.0 compatible.

%package -n     %{develname}
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Provides:       json-rpc-cpp-devel = %{version}-%{release}
Provides:       libjson-rpc-cpp-devel = %{version}-%{release}
Obsoletes:      %{_lib}libjson-rpc-cpp-devel >= 1.0.0
Conflicts:      libjsonrpccpp0.6-devel < 1.0.0

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
	-DCATCH_INCLUDE_DIR=%{_includedir}/catch \
	-DFULL_PATH_LIBDIR=%{_libdir} \
	-DFULL_PATH_INCLUDEDIR=%{_includedir}
%make_build

%install
%makeinstall_std -C build

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
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- new version

