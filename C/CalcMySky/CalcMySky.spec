%def_with check

Name: CalcMySky
Version: 0.3.3
Release: alt1

Summary: Simulator of light scattering by planetary atmospheres

License: GPL-3.0-only
Group: Sciences/Astronomy
URL: https://10110111.github.io/CalcMySky
VCS: https://github.com/10110111/CalcMySky

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libglm-devel
BuildRequires: qt6-base-devel
BuildRequires: eigen3

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

%package -n libCalcMySky-devel
Summary: Development files for CalcMySky
Group: Development/C
Requires: %name = %EVR

%description -n libCalcMySky-devel
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
%doc README.mdown doc/ COPYING
%_bindir/calcmysky
%_bindir/showmysky
%_datadir/CalcMySky/
%_libdir/libShowMySky-Qt6.so.15*

%files -n libCalcMySky-devel
%_libdir/cmake/ShowMySky-Qt6/
%_libdir/libShowMySky-Qt6.so
%_includedir/ShowMySky/

%changelog
* Sun Oct 13 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
