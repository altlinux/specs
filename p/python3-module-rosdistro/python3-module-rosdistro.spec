%define  modulename rosdistro

Name:    python3-module-%modulename
Version: 0.8.3
Release: alt1

Summary: Tools to work with catkinized rosdistro files
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ros-infrastructure/rosdistro

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/rosdistro_*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus.
