#%%define _unpackaged_files_terminate_build 1
#%%define _stripped_files_terminate_build 1
#%%set_verify_elf_method strict
%define lname libopen62541pp

Name: open62541pp
Version: 0.14.0
Release: alt1

Summary: open62541++ is a C++ wrapper built on top of the amazing open62541 OPC UA (OPC Unified Architecture) library.

License: MPL-2.0
Group: Development/C++
Url: https://github.com/open62541pp/open62541pp
Packager: Pavel Vainerman <pv@altlinux.ru>

BuildRequires: rpm-macros-cmake cmake gcc-c++ python2-base
BuildRequires: libopen62541-devel >= 1.3.6

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
%cmake -DBUILD_SHARED_LIBS=ON -DUAPP_INTERNAL_OPEN62541=OFF -DUAPP_BUILD_DOCUMENTATION=OFF
%cmake_build

%install
%cmake_install

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%dir %_includedir/open62541pp
%_includedir/open62541pp/
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/%{name}/



%changelog
* Fri Jul 19 2024 Pavel Vainerman <pv@altlinux.ru> 0.14.0-alt1
- new version (0.14.0) with rpmgs script

* Sat Apr 27 2024 Pavel Vainerman <pv@altlinux.ru> 0.13.0-alt1
- new version (0.13.0) with rpmgs script

* Sun Feb 18 2024 Pavel Vainerman <pv@altlinux.ru> 0.12.0-alt1
- new version (0.12.0) with rpmgs script

* Sat Jul 29 2023 Pavel Vainerman <pv@altlinux.ru> 0.6.0-alt1
- new version (0.6.0) with rpmgs script

* Sun Jul 16 2023 Pavel Vainerman <pv@altlinux.ru> 0.5.0-alt1
- new version (0.5.0) with rpmgs script

* Sat May 20 2023 Pavel Vainerman <pv@altlinux.ru> 0.4.0-alt1
- new version (0.4.0) with rpmgs script
- packaged docs

* Mon May 01 2023 Pavel Vainerman <pv@altlinux.ru> 0.3.0-alt1
- new version (0.3.0) with rpmgs script

* Mon May 01 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt4
- rebuild with new libopen62541

* Sun Jan 08 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt3
- new version (commit aeccfa8)

* Thu Jan 05 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt2
- new version (commit 7d9f5df)

* Tue Jan 03 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt1
- fixed pkgconfig patch

* Mon Jan 02 2023 Pavel Vainerman <pv@altlinux.ru> 0.0.1-alt0.1
- initial build

