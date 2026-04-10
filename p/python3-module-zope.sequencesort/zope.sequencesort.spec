%define _unpackaged_files_terminate_build 1
%define pypi_name zope.sequencesort

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1

Summary: Sequence Sorting
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.sequencesort/
Vcs: https://github.com/zopefoundation/zope.sequencesort
BuildArch: noarch
Source: %name-%version.tar
Source1111: %pyproject_deps_config_name
AutoReq: yes, nopython3
Requires: python3-module-zope >= 3.3.0-alt10
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
This package provides support for sorting sequences based on multiple keys,
including locale-based comparisons and per-key directions.

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
%python3_sitelibdir/zope/sequencesort/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/*/*/tests

%changelog
* Fri Mar 27 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Jan 22 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version  5.0.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt3
- Fixed BuildRequires.

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev.git20141106.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev.git20141106.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev.git20141106.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev.git20141106
- Version 4.0.2dev
- Enabled check

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

