%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
#%set_verify_elf_method strict
%define lname libopen62541

Name: open62541
Version: 1.3.4
Release: alt1

Summary: open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages.

License: MPL-2.0
Group: Development/C
Url: https://github.com/open62541/open62541

Packager: Pavel Vainerman <pv@altlinux.ru>

# Automatically added by buildreq on Mon Jan 02 2023
# optimized out: cmake-modules ghostscript-classic git-core glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 poppler python-modules python2-base python3 python3-base python3-dev python3-module-paste python3-module-pkg_resources sh4 texlive-collection-basic tzdata
BuildRequires: rpm-macros-cmake cmake gcc libssl-devel

BuildRequires: python3-dev python3-module-setuptools
BuildRequires(pre): rpm-build-python3

# run tests
BuildRequires: ctest

# Source-url: https://github.com/open62541/open62541/archive/v%{version}.tar.gz
Source: %name-%version.tar

%description
open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages. The library is usable with all major compilers and provides the necessary tools to implement dedicated OPC UA clients and servers, or to integrate OPC UA-based communication into existing applications. open62541 library is platform independent. All platform-specific functionality is implemented via exchangeable plugins. Plugin implementations are provided for the major operating systems.

%package -n %lname
Group: Development/C
Summary: open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages.

%description -n %lname
open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages. The library is usable with all major compilers and provides the necessary tools to implement dedicated OPC UA clients and servers, or to integrate OPC UA-based communication into existing applications. open62541 library is platform independent. All platform-specific functionality is implemented via exchangeable plugins. Plugin implementations are provided for the major operating systems.

%package -n %lname-devel
Group: Development/C
Summary: open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture

%description -n %lname-devel
open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture) written in the common subset of the C99 and C++98 languages. The library is usable with all major compilers and provides the necessary tools to implement dedicated OPC UA clients and servers, or to integrate OPC UA-based communication into existing applications. open62541 library is platform independent. All platform-specific functionality is implemented via exchangeable plugins. Plugin implementations are provided for the major operating systems.

%package -n %lname-tools
Summary: open62541 is an open source and free implementation of OPC UA (OPC Unified Architecture
Group: Development/C
Requires: python3
%add_findreq_skiplist %_datadir/%name/tools/nodeset_compiler/*.py %_datadir/%name/tools/*.py
AutoProv: yes,nopython

%description -n %lname-tools
open62541 tools

%prep
%setup
subst 's|#!/usr/bin/env python|#!/usr/bin/env python3|g' tools/nodeset_compiler/nodeset_testing.py

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%cmake -DBUILD_SHARED_LIBS=ON -DUA_BUILD_TOOLS=ON -DOPEN62541_VERSION="v%{version}" -DUA_ENABLE_JSON_ENCODING=ON
#-DUA_ENABLE_WEBSOCKET_SERVER=ON -DUA_ENABLE_AMALGAMATION=ON
%cmake_build

%install
%cmake_install

%check
cd %_cmake__builddir
ctest -V

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/%{name}/
%_includedir/*.h
%_libdir/*.so
%_libdir/cmake/%{name}/
%_libdir/pkgconfig/*.pc

%files -n %lname-tools
%_datadir/%{name}/


%changelog
* Sun Jan 01 2023 Pavel Vainerman <pv@altlinux.ru> 1.3.4-alt1
- new version (1.3.4) with rpmgs script

