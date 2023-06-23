%define _unpackaged_files_terminate_build 1
%define pypi_name PyHamcrest
%define mod_name hamcrest

%def_with check

Name: python3-module-%mod_name
Version: 2.0.4
Release: alt1
Summary: Hamcrest framework for matcher objects
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/PyHamcrest/
Vcs: https://github.com/hamcrest/PyHamcrest
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter 'pytest-mypy-plugins$'
%pyproject_builddeps_metadata_extra tests
%pyproject_builddeps_metadata_extra tests-numpy
%endif

%description
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 23 2023 Stanislav Levin <slev@altlinux.org> 2.0.4-alt1
- 2.0.2 -> 2.0.4.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.0.2-alt2
- Fixed FTBFS(Pytest 6).

* Tue Oct 06 2020 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 2.0.0 -> 2.0.2.
- Stopped Python2 package build.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 2.0.0-alt4.a1.git20150729
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 2.0.0-alt3.a1.git20150729
- Fixed Pytest4.x compatibility errors.
- Enabled testing for Python3 package.

* Tue Apr 23 2019 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1.1.1
- introduce doc knob (on by default)
- minor spec cleanup

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2.a1.git20150729
- cleanup buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20150729
- New snapshot

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20141030
- Initial build for Sisyphus

