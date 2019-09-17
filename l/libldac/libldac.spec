%define soname 2

Name: libldac
Version: 2.0.2.3
Release: alt0.1
Summary: LDAC Bluetooth library
License: ASL 2.0
Group: System/Libraries
Url: https://github.com/EHfive/ldacBT
Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: ldacBT-%version.tar

BuildRequires: cmake

%description
LDAC is an audio coding technology developed by Sony, which allows streaming
audio over Bluetooth connections up to 990 kbit/s at 24 bit/96 kHz (also called
high-resolution audio).

%package -n %{name}%{soname}
Summary: LDAC Bluetooth library
Group: System/Libraries

%description -n %{name}%{soname}
LDAC is an audio coding technology developed by Sony, which allows streaming
audio over Bluetooth connections up to 990 kbit/s at 24 bit/96 kHz (also called
high-resolution audio).

%package devel
Summary: LDAC Bluetooth library headers
Group: Development/C
Requires: %{name}%{soname} = %EVR

%description devel
%name-devel contains header files needed to
develop programs which make use of %name

%prep
%setup -q -n ldacBT-%version
 
%build
%cmake \
  -DINSTALL_LIBDIR=%_libdir

%install
%cmakeinstall_std

%files -n %{name}%{soname}
%_libdir/*.so.*

%files devel
%dir %_includedir/ldac
%_includedir/ldac/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 2.0.2.3-alt0.1
- libldac: use 82b6a1abee84787b8fa167efe20290073f60db2d GIT
- Initial build for ALTLinux.
