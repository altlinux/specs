%define _unpackaged_files_terminate_build 1

Name: parameterrepository
Version: 2026.01.13
Release: alt1.ad8589

Summary: ArduPilot parameter repository
License: GPL-3.0
Group: Development/Documentation
URL: https://ardupilot.org/
Vcs: https://github.com/ArduPilot/ParameterRepository
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-python3

%description
All parameters for drones, copters and so on in one place.

%prep
%setup

%install
mkdir -pv %buildroot%_datadir/ParameterRepository
cp -r %_builddir/parameterrepository-%version/* %buildroot%_datadir/ParameterRepository/

%files
%doc README.md
%_datadir/ParameterRepository

%changelog
* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 2026.01.13-alt1.ad8589
- Initial build.
