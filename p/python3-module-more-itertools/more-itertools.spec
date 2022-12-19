%define _unpackaged_files_terminate_build 1
%define pypi_name more-itertools

Name: python3-module-%pypi_name
Version: 9.0.0
Release: alt1

Summary: More routines for operating on iterables, beyond itertools
License: MIT
Group:   Development/Python3
URL: https://pypi.org/project/more-itertools/
VCS: https://github.com/more-itertools/more-itertools

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

# wellknown PyPI name
%py3_provides %pypi_name
Provides: python3-module-more_itertools = %EVR

%description
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/more_itertools/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 9.0.0-alt1
- 7.0.0 -> 9.0.0.

* Wed Apr 03 2019 Dmitry V. Levin <ldv@altlinux.org> 7.0.0-alt3
- Removed python-module-more-itertools subpackage.

* Tue Apr 02 2019 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt2
- Completely fix run from Python 2.

* Sat Mar 30 2019 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Mon Aug 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version.

* Tue Jul 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus
