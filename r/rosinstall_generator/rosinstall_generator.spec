Name:    rosinstall_generator
Version: 0.1.23
Release: alt1

Summary: A tool for generating rosinstall files
License: BSD-3-Clause
Group:   Other
URL:     https://github.com/ros-infrastructure/rosinstall_generator

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Feb 28 2023 Andrey Cherepanov <cas@altlinux.org> 0.1.23-alt1
- New version.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.1.22-alt1
- Initial build for Sisyphus.
