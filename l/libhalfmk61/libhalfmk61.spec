%define soname 1

Name: libhalfmk61
Version: 0.3
Release: alt1

Summary: Library for USSR programmable calculator MK-61 notprogrammable subsystem only
License: GPLv3
Group: System/Libraries

URL: https://github.com/saahriktu/libhalfmk61
Source: %name-%version.tar

BuildRequires: gcc-c++

%description
USSR programmable calculator MK-61 notprogrammable subsystem only (stack and
registers + operations)

%package -n %name-%soname
Summary: Library for USSR programmable calculator MK-61 notprogrammable subsystem only
Group: System/Libraries

%description -n %name-%soname
USSR programmable calculator MK-61 notprogrammable subsystem only (stack and
registers + operations)

%package devel
Summary: Development files for USSR programmable calculator MK-61 notprogrammable subsystem only
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
USSR programmable calculator MK-61 notprogrammable subsystem only (stack and
registers + operations)

%prep
%setup

%build
%make

%install
libdir=%_libdir prefix=%_usr %makeinstall_std

%files -n %name-%soname
%_libdir/libhalfmk61.so.%soname

%files devel
%_libdir/libhalfmk61.so
%_includedir/halfmk61/halfmk61.hpp

%changelog
* Fri Jun 14 2024 Artem Kurashov <saahriktu@altlinux.org> 0.3-alt1
- Initial package.
