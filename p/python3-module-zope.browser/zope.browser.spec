%define _unpackaged_files_terminate_build 1
%define pypi_name zope.browser
%define ns_name zope
%define mod_name browser

%def_with check

Name: python3-module-%pypi_name
Version: 4.0
Release: alt1.1
Summary: Shared Zope Toolkit browser components
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.browser/
Vcs: https://github.com/zopefoundation/zope.browser.git
BuildArch: noarch
Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope-interface
BuildRequires: python3-module-zope-testrunner
%endif

%description
This package provides shared browser components for the Zope Toolkit.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vv

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/*/tests.*

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.0-alt1.1
- Demodernized packaging.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- 3.1 -> 4.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri Feb 14 2025 Stanislav Levin <slev@altlinux.org> 3.1-alt1
- 3.0 -> 3.1.

* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 3.0-alt2
- Mapped PyPI name to distro's one.

* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Thu Dec 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 2.3-alt1
- NMU: 2.2.0 -> 2.3
- Remove python2 module build
- Remove ubt tags from changelog

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2
- NMU: remove ubt from release

* Wed Mar 07 2018 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Dec 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt3.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt3
- Added module for Python 3

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

