%define _unpackaged_files_terminate_build 1
%define pypi_name zope.filerepresentation
%define ns_name zope
%define mod_name filerepresentation

%def_with check

Name: python3-module-%pypi_name
Version: 7.0
Release: alt1

Summary: File-system Representation Interfaces
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.filerepresentation/
VCS: https://github.com/zopefoundation/zope.filerepresentation
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
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
File-system representation interfaces.

The interfaces defined here are used for file-system and
file-system-like representations of objects, such as file-system
synchronization, FTP, PUT, and WebDAV.

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
* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 7.0-alt1
- 6.1 -> 7.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 6.1-alt1
- New version 6.1.

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 6.0-alt2
- Fixed FTBFS.

* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.2.0 -> 5.0.0.

* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt1
- version updated to 4.2.0
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150228.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150228.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150228.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150228
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

