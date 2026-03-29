%define _unpackaged_files_terminate_build 1
%define pypi_name zope.datetime
%define ns_name zope
%define mod_name datetime

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1.1
Summary: Zope datetime
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.datetime/
Vcs: https://github.com/zopefoundation/zope.datetime
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope-testrunner
%endif

%description
Commonly used date and time related utility functions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.0-alt1.1
- Demodernized packaging.

* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 4.3.0 -> 5.1.

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt2
- Moved on modern pyproject macros.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- new version (4.3.0) with rpmgs script
- cleanup build

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.2.0-alt1
- NMU: 4.1.0 -> 4.2.0
- Remove python2 module build
- Add unittests execution

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Version 3.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

