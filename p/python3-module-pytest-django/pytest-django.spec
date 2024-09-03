%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-django

%def_with check

Name: python3-module-%pypi_name
Version: 4.9.0
Release: alt1
Summary: A Django plugin for py.test
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pytest-django/
Vcs: https://github.com/pytest-dev/pytest-django
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter django-configurations
%pyproject_builddeps_metadata_extra testing
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python3(django\(\..*\)\?)/d

%description
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

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
# pytest_django_test package must be importable by Pytest's subprocesses
export PYTHONPATH=$(pwd)
%pyproject_run_pytest -ra -Wignore tests

%files
%doc README.*
%python3_sitelibdir/pytest_django/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 03 2024 Stanislav Levin <slev@altlinux.org> 4.9.0-alt1
- 4.8.0 -> 4.9.0.

* Fri Mar 29 2024 Stanislav Levin <slev@altlinux.org> 4.8.0-alt1
- 4.5.2 -> 4.8.0.

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 4.5.2-alt3
- Modernized packaging.
- Fixed FTBFS (pytest-xdist 3).

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 4.5.2-alt2
- Fixed FTBFS (setuptools 64).

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 4.5.2-alt1
- 4.0.0 -> 4.5.2.

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt2
- fix BR

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 3.9.0 -> 4.0.0.

* Thu Jun 04 2020 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.5.1 -> 3.9.0.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 2.8.0 -> 3.5.1.
- Enabled testing for Python3.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3.1
- rebuild with all requires

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt2.git20150303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 2.8.0-alt2.git20150303
- cleanup buildreq
- disable tests

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.git20150303
- Version 2.8.0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20141012
- Initial build for Sisyphus

