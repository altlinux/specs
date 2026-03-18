%define _unpackaged_files_terminate_build 1
%define pypi_name zope.cachedescriptors
%define ns_name zope
%define mod_name cachedescriptors

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1

Summary: Method and property caching decorators
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.cachedescriptors/
Vcs: https://github.com/zopefoundation/zope.cachedescriptors
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
BuildArch: noarch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

%prep
%setup
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
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt2
- Build for python2 disabled.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3.1-alt1
- new version 4.3.1 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150204.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150204.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150204
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

