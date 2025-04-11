Name:    catkin
Version: 0.8.11
Release: alt1

Summary: A CMake-based build system that is used to build all packages in ROS.
License: BSD-3-Clause
Group:   Other
URL:     https://github.com/ros/catkin

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3-module-wheel
BuildRequires: python3-module-catkin_pkg
BuildRequires: python3-module-empy
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
Catkin is a collection of cmake macros and associated python code used to build
some parts of ROS.

%prep
%setup -n %name-%version

%build
%cmake -DCATKIN_ENABLE_TESTING=False \
       -DCATKIN_GLOBAL_LIB_DESTINATION=%_libdir
#       -DCATKIN_DEVEL_PREFIX=%_libexecdir/%name
%cmake_build

%install
%cmake_install

%files
%doc *.rst
%_bindir/catkin_*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}-*.egg-info
%_datadir/%name

%changelog
* Fri Apr 11 2025 Andrey Cherepanov <cas@altlinux.org> 0.8.11-alt1
- New version.

* Wed Mar 22 2023 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt2
- Packaged cmake rules.
- Used cmake for build.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
