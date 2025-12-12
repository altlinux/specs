%def_with check

%global soversion 0

%global descr gpioplus is a c++ wrapper around the linux gpio ioctl interface.\
It aims to provide c++ ergonomics to the usage.

Name: gpioplus
Version: 0.1
Release: alt1.gitf8dfbb8

Summary: C++ wrapper around the linux gpio ioctl interface
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/openbmc/gpioplus
Vcs: https://github.com/openbmc/gpioplus.git

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-meson

BuildRequires: gcc-c++
BuildRequires: meson
%if_with check
BuildRequires: libgtest-devel
%endif

%description
%descr

%package -n lib%name%soversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%soversion
%descr

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name%soversion

%description -n lib%name-devel
%summary.
%descr

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n lib%name%soversion
%_libdir/lib%name.so.%{soversion}*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Dec 10 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.gitf8dfbb8
- Initial build for Sisyphus.
