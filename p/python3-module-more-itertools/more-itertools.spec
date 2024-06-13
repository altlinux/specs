%define _unpackaged_files_terminate_build 1
%define pypi_name more-itertools

Name: python3-module-%pypi_name
Version: 10.3.0
Release: alt1
Summary: More routines for operating on iterables, beyond itertools
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/more-itertools/
VCS: https://github.com/more-itertools/more-itertools
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# wellknown PyPI name
%py3_provides %pypi_name
Provides: python3-module-more_itertools = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Python's itertools library is a gem - you can compose elegant solutions
for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/more_itertools/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 11 2024 Stanislav Levin <slev@altlinux.org> 10.3.0-alt1
- 10.2.0 -> 10.3.0.

* Tue Jan 09 2024 Stanislav Levin <slev@altlinux.org> 10.2.0-alt1
- 10.1.0 -> 10.2.0.

* Fri Aug 04 2023 Stanislav Levin <slev@altlinux.org> 10.1.0-alt1
- 10.0.0 -> 10.1.0.

* Wed Jul 26 2023 Stanislav Levin <slev@altlinux.org> 10.0.0-alt1
- 9.1.0 -> 10.0.0.

* Tue Feb 28 2023 Stanislav Levin <slev@altlinux.org> 9.1.0-alt1
- 9.0.0 -> 9.1.0.

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
