%define _unpackaged_files_terminate_build 1
%define pypi_name djangorestframework

%def_with check

Name: python3-module-%pypi_name
Version: 3.15.1
Release: alt2
Summary: Web APIs for Django, made easy
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/djangorestframework
Vcs: https://github.com/encode/django-rest-framework
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python3(django\(\..*\)\?)/d
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/requirements-testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python runtests.py

%files
%doc README.md
%python3_sitelibdir/rest_framework/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 06 2024 Stanislav Levin <slev@altlinux.org> 3.15.1-alt2
- Fixed FTBFS (Pytest 8.2.0).

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 3.15.1-alt1
- 3.15.0 -> 3.15.1.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.14.0 -> 3.15.0.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.1 -> 3.14.0.

* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 3.13.1-alt1
- 3.12.4 -> 3.13.1.

* Thu Sep 09 2021 Alexey Shabalin <shaba@altlinux.org> 3.12.4-alt3
- Fix BR.
- Backport upstream patches for fix tests with Django-3.2.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 3.12.4-alt2
- Applied upstream fix for new Pygments.

* Wed Apr 14 2021 Stanislav Levin <slev@altlinux.org> 3.12.4-alt1
- 3.12.1 -> 3.12.4.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.11.0 -> 3.12.1.

* Thu Jun 04 2020 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.2 -> 3.11.0.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 3.10.2-alt3
- Fixed FTBS.

* Mon Aug 19 2019 Stanislav Levin <slev@altlinux.org> 3.10.2-alt2
- Allowed testing against Pytest5.1+.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 3.10.2-alt1
- 3.5.3 -> 3.10.2.
- Enabled testing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 3.5.3-alt1
- Version 3.6.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.4-alt2.git20150128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 3.0.4-alt2.git20150128
- Rebuild with "def_disable check"
- Cleanup buildreqs

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.git20150128
- Version 3.0.4

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.git20141108
- Initial build for Sisyphus

