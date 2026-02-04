%define _unpackaged_files_terminate_build 1

Name: gpsdrivers
Version: 2026.01.13
Release: alt1.caf5158

Summary: User-space gps drivers
License: BSD-3-Clause
Group: Development/Tools
URL: https://px4.io/
Vcs: https://github.com/PX4/PX4-GPSDrivers
BuildArch: noarch

Source0: %name-%version.tar

%description
User-space gps drivers used as submodule in QGroundControl and PX4 Autopilot.

%prep
%setup

%install
mkdir -pv %buildroot%_usrsrc/PX4-GPSDrivers
cp -r %_builddir/gpsdrivers-%version/* %buildroot%_usrsrc/PX4-GPSDrivers/

%files
%doc README.md LICENSE.md
%_usrsrc/PX4-GPSDrivers

%changelog
* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2026.01.13-alt1.caf5158
- Initial build.
