%define _unpackaged_files_terminate_build 1
%define pypi_name blessed
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.45.0
Release: alt1
Summary: Easy, practical library for making terminal apps
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/blessed/
Vcs: https://github.com/jquast/blessed.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
Requires: python3-modules-curses
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-modules-curses
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Easy, practical library for making terminal apps, by providing an elegant,
well-documented interface to Colors, Keyboard input, and screen Positioning
capabilities.

%prep
%setup
%autopatch -p1
%python3_fix_shebang .
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# skip timing-sensitive tests
export TEST_QUICK=1
%pyproject_run_pytest -vra -o=addopts=-Wignore tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 30 2026 Stanislav Levin <slev@altlinux.org> 1.45.0-alt1
- 1.44.0 -> 1.45.0

* Fri Jun 05 2026 Stanislav Levin <slev@altlinux.org> 1.44.0-alt1
- 1.42.0 -> 1.44.0

* Thu May 21 2026 Stanislav Levin <slev@altlinux.org> 1.42.0-alt1
- 1.41.0 -> 1.42.0.

* Wed May 20 2026 Stanislav Levin <slev@altlinux.org> 1.41.0-alt1
- 1.39.0 -> 1.41.0.

* Mon May 18 2026 Stanislav Levin <slev@altlinux.org> 1.39.0-alt1
- 1.38.0 -> 1.39.0.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 1.38.0-alt1
- 1.33.0 -> 1.38.0.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 1.33.0-alt1
- 1.30.0 -> 1.33.0.

* Mon Feb 09 2026 Stanislav Levin <slev@altlinux.org> 1.30.0-alt1
- 1.25.0 -> 1.30.0.

* Fri Nov 21 2025 Stanislav Levin <slev@altlinux.org> 1.25.0-alt1
- 1.24.0 -> 1.25.0.

* Mon Nov 17 2025 Stanislav Levin <slev@altlinux.org> 1.24.0-alt1
- 1.20.0 -> 1.24.0.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 1.20.0-alt1
- 1.17.10 -> 1.20.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 1.17.10-alt1
- 1.17.5 -> 1.17.10.

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 1.17.5-alt1
- 1.14.2 -> 1.17.5.
- Enabled testing.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt2
- disable python2

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt1
- Version 1.14.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.5-alt1.git20150112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.5-alt1.git20150112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.5-alt1.git20150112
- Initial build for Sisyphus
