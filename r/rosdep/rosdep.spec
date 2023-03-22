Name:    rosdep
Version: 0.22.2
Release: alt1

Summary: rosdep multi-package manager system dependency tool
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ros-infrastructure/rosdep

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %name-%version.tar

%description
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that you
are building from source. For developers, rosdep simplifies the problem of
installing system dependencies on different platforms. Instead of having to
figure out which debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/%name
%python3_sitelibdir/rosdep2
%python3_sitelibdir/*.egg-info

%changelog
* Tue Mar 21 2023 Andrey Cherepanov <cas@altlinux.org> 0.22.2-alt1
- New version.

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 0.22.1-alt1
- New version.

* Wed May 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.21.0-alt1
- Initial build for Sisyphus.
