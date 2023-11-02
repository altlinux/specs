%define _unpackaged_files_terminate_build 1
%define pypi_name wcwidth
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.9
Release: alt1
Summary: Measures number of Terminal column cells of wide-character codes
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/wcwidth/
Vcs: https://github.com/jquast/wcwidth
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter docformatter restructuredtext-lint
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This API is mainly for Terminal Emulator implementors - any python
program that attempts to determine the printable width of a string on a
Terminal. It is implemented in python (no C library calls) and has no
3rd-party dependencies.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-tests39.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# get rid of tox.ini as pytest's config:
# [pytest] section and its cov cli options
rm tox.ini
%pyproject_run_pytest -ra tests

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 0.2.9-alt1
- 0.2.8 -> 0.2.9.

* Mon Oct 02 2023 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1
- 0.2.6 -> 0.2.8.

* Thu Apr 27 2023 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1
- 0.2.5 -> 0.2.6.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1
- 0.1.9 -> 0.2.5.

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 0.1.9-alt1
- 0.1.7 -> 0.1.9.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt2
- Fixed tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150413.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150413
- New snapshot

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150125
- Initial build for Sisyphus

