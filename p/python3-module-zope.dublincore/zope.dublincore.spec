%define _unpackaged_files_terminate_build 1
%define pypi_name zope.dublincore
%define ns_name zope
%define mod_name dublincore

%def_with check

Name: python3-module-%pypi_name
Epoch: 1
Version: 6.0
Release: alt1.1
Summary: Zope Dublin Core implementation
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.dublincore
Vcs: https://github.com/zopefoundation/zope.dublincore
BuildArch: noarch
Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-btrees
BuildRequires: python3-module-persistent
BuildRequires: python3-module-pytz
BuildRequires: python3-module-zope-annotation
BuildRequires: python3-module-zope-component
BuildRequires: python3-module-zope-configuration
BuildRequires: python3-module-zope-datetime
BuildRequires: python3-module-zope-interface
BuildRequires: python3-module-zope-lifecycleevent
BuildRequires: python3-module-zope-location
BuildRequires: python3-module-zope-publisher
BuildRequires: python3-module-zope-schema
BuildRequires: python3-module-zope-security
BuildRequires: python3-module-zope-testing
BuildRequires: python3-module-zope-testrunner
# zope.component.testing is required but subpackaged
BuildRequires: python3-module-zope.component-tests
%endif

%description
zope.dublincore provides a Dublin Core support for Zope-based web
applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -v

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/browser/tests/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1:6.0-alt1.1
- Demodernized packaging.

* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 1:6.0-alt1
- 5.1 -> 6.0.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 1:5.1-alt1
- 5.0 -> 5.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1:5.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Jul 05 2023 Anton Vyatkin <toni@altlinux.org> 1:5.0-alt1
- New version 5.0.

* Tue Mar 07 2023 Anton Vyatkin <toni@altlinux.org> 1:4.3.0-alt1
- new version 4.3.0

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.1.1-alt2
- disable python2

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1:4.1.1-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.1-alt1
- Version 4.0.1

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.2-alt1
- Initial build for Sisyphus

