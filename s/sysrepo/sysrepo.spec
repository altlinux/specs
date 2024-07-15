%define _unpackaged_files_terminate_build 1
%define abiversion 7

Name: sysrepo
Version: 2.2.60
Release: alt1
Summary: YANG-based configuration and operational data store
License: BSD-3-Clause  
Group: System/Libraries
Url: https://github.com/sysrepo/sysrepo

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: pkgconfig(libyang) >= 2.0.7

%description
YANG-based configuration and operational data store - runtime Applications can
use sysrepo to store their configuration modeled by provided YANG model
instead of using e.g. flat configuration files. Sysrepo will ensure data
consistency of the data stored in the data store and enforce data constraints
defined by YANG model.

%package -n lib%name%abiversion
Summary:  Shared library for %name
Group: Development/C

%description -n lib%name%abiversion
libs files for %name

%package -n %name-devel
Summary: Development package for %name
Group: Development/C

%description -n %name-devel
Files for development with %name.

%package -n %name-tools
Summary: tools for %name package
Group: Development/C

%description -n %name-tools
Executable tools for %name.

%prep
%setup

%build
export CFLAGS="%optflags"
%cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
    -DSYSREPO_UMASK=007 \
    -DSYSREPO_GROUP=sysrepo \
    -DNACM_SRMON_DATA_PERM=660
%cmake_build 

%install
%cmakeinstall_std

%files -n %name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*.h
%_includedir/%name/
%_datadir/yang/modules/%name/
%_man1dir/*.1.*

%files -n lib%name%abiversion
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%files -n %name-tools
%_bindir/*
%_man8dir/*.8.*

%changelog
* Sat Mar 02 2024 Pavel Shilov <zerospirit@altlinux.org> 2.2.60-alt1
- initial build for Sisyphus
