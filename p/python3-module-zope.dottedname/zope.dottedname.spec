%define _unpackaged_files_terminate_build 1
%define pypi_name zope.dottedname
%define ns_name zope
%define mod_name dottedname

%def_with check

Name: python3-module-%pypi_name
Version: 7.1
Release: alt1.1
Summary: Resolver for Python dotted names
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.dottedname
Vcs: https://github.com/zopefoundation/zope.dottedname
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
BuildRequires: python3-module-zope-testrunner
%endif

%description
Resolve strings containing dotted names into the appropriate python object.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/example.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/example.*

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 7.1-alt1.1
- Demodernized packaging.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 7.1-alt1
- 6.1 -> 7.1.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt1
- 6.0 -> 6.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.0-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 6.0-alt2
- Fixed FTBFS.

* Mon Mar 27 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150226.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150226.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150226
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.6-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt1
- Initial build for Sisyphus

