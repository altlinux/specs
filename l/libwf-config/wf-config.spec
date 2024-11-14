# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with test

Name: libwf-config
Version: 0.9.0
Release: alt1
Summary: Library for managing configuration files, written for wayfire
License: MIT
Url: https://github.com/WayfireWM/wf-config
Group: Graphical desktop/Other

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: meson >= 0.47

BuildRequires: libglm-devel
%if_with test
BuildRequires: doctest-devel
%endif

BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libxml-2.0)

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for %name.

%prep
%setup

%build
%if_with test
%meson \
    -Dtests=enabled
%else
%meson \
    -Dtests=disabled
%endif

%meson_build

%install
%meson_install

%if_with test
%check
%meson_test
%endif

%files
%doc LICENSE
%_libdir/%name.so.0*
%_libdir/%name.so.1*

%files devel
%_includedir/wayfire/
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- initial build
