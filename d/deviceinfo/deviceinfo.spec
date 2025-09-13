%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: deviceinfo
Version: 0.2.4
Release: alt1

Summary: Detect and configure devices in Lomiri
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://gitlab.com/ubports/development/core/deviceinfo

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: pkgconfig(systemd)

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(gtest)
BuildRequires: ayatana-cmake-modules
%endif

%description
%summary

%package -n libdeviceinfo0
Summary: Library to detect and configure devices 
Group: System/Libraries

%description -n libdeviceinfo0
Library to detect and configure devices.

%package -n libdeviceinfo-devel
Summary: Development headers to detect and configure devices 
Group: Development/Other
Requires: libdeviceinfo0 = %version-%release

%description -n libdeviceinfo-devel
Development headers for libdeviceinfo, to detect and configure devices

%package -n deviceinfo-tools
Summary: Tools to detect and configure devices
Group: System/Configuration/Hardware
Requires: libdeviceinfo0 = %version-%release

%description -n deviceinfo-tools
Tools to detect and configure devices

%package -n deviceinfo-extras
Summary: Extra programs to detect and configure devices
Group: System/Configuration/Hardware
Requires: libdeviceinfo0 = %version-%release

%description -n deviceinfo-extras
Library to detect and configure devices

This package contains extra programs shipped with deviceinfo. At the
moment, this includes update-machine-info-from-deviceinfo tool.

%prep
%setup

%build
%cmake \
       -DWITH_EXTRAS=ON \
%if_with check
       -DDISABLE_TESTS=OFF
%else
       -DDISABLE_TESTS=ON
%endif
%cmake_build

%install
%cmake_install

install -Dm644 tools/device-info.1 %{buildroot}%{_man1dir}/device-info.1

%check
%ctest -V

%files -n libdeviceinfo0
%dir %_sysconfdir/deviceinfo
%_sysconfdir/deviceinfo/default.yaml
%dir %_sysconfdir/deviceinfo/devices
%_sysconfdir/deviceinfo/devices/halium.yaml
%_sysconfdir/deviceinfo/devices/pinebook.yaml
%_sysconfdir/deviceinfo/devices/pinephone-pro.yaml
%_sysconfdir/deviceinfo/devices/pinephone.yaml
%_sysconfdir/deviceinfo/devices/pinetab.yaml
%_sysconfdir/deviceinfo/devices/pinetab2.yaml
%dir %_sysconfdir/deviceinfo/sensorfw
%_sysconfdir/deviceinfo/sensorfw/pinephone-pro.conf
%_sysconfdir/deviceinfo/sensorfw/pinephone.conf
%_sysconfdir/deviceinfo/sensorfw/pinetab.conf
%_sysconfdir/deviceinfo/sensorfw/pinetab2.conf
%_libdir/libdeviceinfo.so.0*

%files -n libdeviceinfo-devel
%dir %_includedir/deviceinfo
%_includedir/deviceinfo/deviceinfo.h
%_includedir/deviceinfo/deviceinfo_c_api.h
%_libdir/libdeviceinfo.so
%_pkgconfigdir/deviceinfo.pc

%files -n deviceinfo-tools
%doc AUTHORS ChangeLog LICENSE README.md
%_bindir/device-info
%_man1dir/device-info.1.*

%files -n deviceinfo-extras
%_unitdir/update-machine-info-from-deviceinfo.service
%_libexecdir/update-machine-info-from-deviceinfo

%changelog
* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.4-alt1
- New version 0.2.4.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
