%define  modulename rospkg

Name:    python3-module-%modulename
Version: 1.4.0
Release: alt1

Summary: rospkg Python library for ROS
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ros-infrastructure/rospkg

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Standalone Python library for the ROS package system.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/rosversion
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
