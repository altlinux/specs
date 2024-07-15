%define _unpackaged_files_terminate_build 1
%define abiversion 4

Name: libnetconf2
Version: 3.0.8
Release: alt1
Summary: C NETCONF library 
License: BSD-3-Clause  
Group: System/Libraries
Url: https://github.com/CESNET/libnetconf2

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: libssh-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: libpam0-devel
BuildRequires: pkgconfig(libyang) >= 2

%description
libnetconf is a NETCONF library in C intended for building NETCONF
clients and servers. NETCONF is the NETwork CONFiguration protocol
introduced by IETF.

%package -n %{name}_%{abiversion}
Summary:  Shared library for %name
Group: Development/C

%description -n %{name}_%{abiversion}
libs files for %name

%package -n %name-devel
Summary: Development package for %name
Group: Development/C
Requires:   pkgconfig

%description -n %name-devel
Files for development with %name.

%prep
%setup

%build
export CFLAGS="%optflags"
%cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%prefix 
%cmake_build 

%install
%cmakeinstall_std

%files -n %name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*.h
%_includedir/%name/
%_datadir/yang/modules/%name/

%files -n %{name}_%{abiversion}
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%changelog
* Sat Mar 02 2024 Pavel Shilov <zerospirit@altlinux.org> 3.0.8-alt1
- initial build for Sisyphus
