%define _unpackaged_files_terminate_build 1
%define pypi_name zExceptions
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: zExceptions contains common exceptions used in Zope
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zExceptions
Vcs: https://github.com/zopefoundation/zExceptions
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope.

%prep
%setup
%autopatch -p1
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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%changelog
* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.0 -> 6.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Jun 28 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Mon Mar 06 2023 Anton Vyatkin <toni@altlinux.org> 4.3-alt1
- new version 4.3

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.dev0.git20150331.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.dev0.git20150331.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev0.git20150331
- Version 3.0.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev
- Enabled testing

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt1.1
- Rebuild with Python-2.7

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

