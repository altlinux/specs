%define  modulename catkin_pkg

Name:    python3-module-%modulename
Version: 1.0.0
Release: alt1

Summary: Standalone Python library for the catkin build system.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ros-infrastructure/catkin_pkg

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Standalone Python library for the Catkin package system.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/catkin_*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Sep 14 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.

* Sat May 28 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1
- New version.

* Fri May 27 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version.

* Wed May 11 2022 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.24-alt1
- Initial build for Sisyphus.
