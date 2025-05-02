%define soversion 0
%define nameL libsteam_api

Name: freesteamapi
Version: 20190316
Release: alt1

Summary: reimplementation of libsteam_api.so
License: LGPL-3.0-only
Group: System/Libraries

Url: https://github.com/clayne/freesteamapi
Vcs: https://github.com/clayne/freesteamapi

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson cmake pkgconfig(openssl)

%description
%summary


%package -n %nameL%soversion
Group: System/Libraries
Summary: %name library

%description -n %nameL%soversion
reimplementation of libsteam_api.so

%package devel
Group:Development/C++
Summary: Development files for %name

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%meson
%meson_build

%install
install -D %_arch-alt-linux/%nameL.so %buildroot%_libdir/%nameL.so.%soversion
mkdir -p %buildroot%_includedir/%name
cp -r src/* %buildroot%_includedir/%name/
cd %buildroot%_libdir/
ln -s %nameL.so.%soversion %nameL.so

%files -n %nameL%soversion
%_libdir/%nameL.so.*

%files -n %name-devel
%_includedir/%name
%_libdir/%nameL.so

%changelog
* Fri May 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 20190316-alt1
- Initial build for ALT Linux (git.1546fb2e).
