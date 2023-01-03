#%%define _unpackaged_files_terminate_build 1
#%%define _stripped_files_terminate_build 1
#%%set_verify_elf_method strict
%define lname libopen62541pp

Name: open62541pp
Version: 0.0.1
Release: alt1

Summary: open62541++ is a C++ wrapper built on top of the amazing open62541 OPC UA (OPC Unified Architecture) library.

License: MPL-2.0
Group: Development/C++
Url: https://github.com/open62541pp/open62541pp
Packager: Pavel Vainerman <pv@altlinux.ru>

BuildRequires: rpm-macros-cmake cmake gcc-c++ libopen62541-devel

# Source-url: https://github.com/open62541pp/open62541pp/archive/v%{version}.tar.gz
Source: %name-%version.tar
Source1: %{name}.pc.in
Patch0: CMakeLists.txt.patch

%description
open62541++ is a C++ wrapper built on top of the amazing open62541 OPC UA (OPC Unified Architecture) library.

%package -n %lname
Group: Development/C++
Summary: open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages.

%description -n %lname
open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages. The library is usable with all major compilers and provides the necessary tools to implement dedicated OPC UA clients and servers, or to integrate OPC UA-based communication into existing applications. open62541 library is platform independent. All platform-specific functionality is implemented via exchangeable plugins. Plugin implementations are provided for the major operating systems.

%package -n %lname-devel
Group: Development/C++
Summary: open62541++ is a C++ wrapper built on top of the amazing open62541 OPC UA (OPC Unified Architecture) library.

%description -n %lname-devel
open62541++ is a C++ wrapper built on top of the amazing open62541 OPC UA (OPC Unified Architecture) library.

%prep
%setup
%patch0 -p 1
cp -p %{SOURCE1} .

%build
%cmake -DBUILD_SHARED_LIBS=ON -DUAPP_INTERNAL_OPEN62541=OFF
%cmake_build

%install
%cmake_install

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%dir %_includedir/open62541pp
%_includedir/open62541pp/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc


%changelog
* Tue Jan 03 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- fixed pkgconfig patch

* Mon Jan 02 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt0.1
- initial build

