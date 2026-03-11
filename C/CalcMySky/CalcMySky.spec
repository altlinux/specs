%def_with check

Name:     CalcMySky
Version:  0.4.0
Release:  alt2

Summary:  Simulator of light scattering by planetary atmospheres

License:  GPL-2.0+
Group:    Sciences/Astronomy
URL:      https://10110111.github.io/CalcMySky
VCS:      https://github.com/10110111/CalcMySky

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libglm-devel
BuildRequires: qt6-base-devel
BuildRequires: eigen3-devel

%if_with check
BuildRequires: ctest
%endif

%description
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

%package -n lib%name-devel
Summary: Development files for CalcMySky
Group: Development/C
Requires: %name = %EVR

%description -n lib%name-devel
CalcMySky is a software package that simulates scattering of light by the
atmosphere to render daytime and twilight skies (without stars). Its primary
purpose is to enable realistic view of the sky in applications such as
planetaria. Secondary objective is to make it possible to explore
atmospheric effects such as glories, fogbows etc., as well as simulate
unusual environments such as on Mars or an exoplanet orbiting a star with
a non-solar spectrum of radiation.

These are the development files.

%prep
%setup

%build
%cmake -DQT_VERSION=6
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc COPYING README.mdown
%_bindir/calcmysky
%_bindir/showmysky
%_datadir/CalcMySky/
%_libdir/libShowMySky-Qt6.so.15*

%files -n lib%name-devel
%_libdir/cmake/ShowMySky-Qt6/
%_libdir/libShowMySky-Qt6.so
%_includedir/ShowMySky/

%changelog
* Wed Mar 11 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt2
- Fixed package license.

* Wed Jan 14 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Automatically updated to 0.4.0.

* Tue Jun 24 2025 Grigory Ustinov <grenka@altlinux.org> 0.3.5-alt1
- Automatically updated to 0.3.5.

* Mon Mar 17 2025 Grigory Ustinov <grenka@altlinux.org> 0.3.4-alt1
- Automatically updated to 0.3.4.

* Sun Oct 13 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
