%define soname 1

Name: libnvme
Version: 1.3
Release: alt1
Summary: Linux-native nvme device management library
Group: System/Libraries

License: LGPL-2.1+
# https://github.com/linux-nvme/libnvme/archive/refs/tags/v1.3.tar.gz
Source: %{name}-%{version}.tar

Url: http://github.com/linux-nvme/libnvme

BuildRequires(pre): meson
BuildRequires: libjson-c-devel libdbus-devel openssl-devel

%description
Provides library functions for accessing and managing nvme devices on a Linux
system.

%package -n %{name}%{soname}
Summary: Linux-native nvme device management library
Group: System/Libraries

%description -n %{name}%{soname}
Provides library functions for accessing and managing nvme devices on a Linux
system.

%package devel
Summary: Development files for Linux-native nvme
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
for Linux-native nvme device maangement.

%prep
%setup

%build
%meson \
    -Ddocs=man \
    -Ddocs-build=true \
    -Ddefault_library=both
%meson_build

%install
%meson_install
# to make LTO checks happy
rm -f %buildroot%_libdir/*.a

%files -n %{name}%{soname}
%_libdir/%{name}*.so.%{soname}*
%doc COPYING

%files devel
%dir %_includedir/nvme
%_includedir/nvme/*
%_includedir/%{name}*
%_libdir/%{name}*.so
%_pkgconfigdir/*
%_man2dir/*

%changelog
* Thu Mar 02 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt1
- Initial build for ALTLinux.

