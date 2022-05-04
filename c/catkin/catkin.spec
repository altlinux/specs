Name:    catkin
Version: 0.8.10
Release: alt1

Summary: A CMake-based build system that is used to build all packages in ROS.
License: BSD-3-Clause
Group:   Other
URL:     https://github.com/ros/catkin

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-catkin_pkg

BuildArch: noarch

Source:  %name-%version.tar

%description
Catkin is a collection of cmake macros and associated python code used to build
some parts of ROS.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/catkin_*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
