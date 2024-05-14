%define soname 1

Name: libnvme
Version: 1.9
Release: alt1
Summary: Linux-native nvme device management library
Group: System/Libraries

License: LGPL-2.1+
# https://github.com/linux-nvme/libnvme/archive/refs/tags/v%{version}.tar.gz
Source: %{name}-%{version}.tar

Url: http://github.com/linux-nvme/libnvme

BuildRequires(pre): meson
BuildRequires: libjson-c-devel libdbus-devel openssl-devel
BuildRequires: python3-dev rpm-macros-python3 rpm-build-python3 
BuildRequires: swig libkeyutils-devel

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

%package -n python3-module-libnvme
Summary: Python files for Linux-native nvme
Requires: %{name}%{soname}
Group: Development/Python
 
%description -n python3-module-libnvme
This package provides Python files for Linux-native nvme device maangement.

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

%files -n python3-module-libnvme
%python3_sitelibdir/libnvme/

%changelog
* Tue May 14 2024 L.A. Kostis <lakostis@altlinux.ru> 1.9-alt1
- 1.9.

* Fri Mar 15 2024 L.A. Kostis <lakostis@altlinux.ru> 1.8-alt1
- 1.8.

* Tue Feb 13 2024 L.A. Kostis <lakostis@altlinux.ru> 1.7.1-alt1
- 1.7.1.

* Tue Dec 05 2023 Artem Kurashov <saahriktu@altlinux.org> 1.6-alt2
- Add python3-module-libnvme package.

* Sat Nov 04 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6-alt1
- 1.6.

* Mon Jul 03 2023 L.A. Kostis <lakostis@altlinux.ru> 1.5-alt1
- 1.5.

* Fri Apr 28 2023 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1
- 1.4.

* Thu Mar 02 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3-alt1
- Initial build for ALTLinux.

