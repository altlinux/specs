%define _unpackaged_files_terminate_build 1
%define pypi_name zope.authentication
%define ns_name zope
%define mod_name authentication

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: Definition of authentication basics for the Zope Framework
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.authentication/
Vcs: https://github.com/zopefoundation/zope.authentication.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
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
This package provides a definition of authentication concepts for use in
Zope Framework.

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
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri Feb 14 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 5.0-alt2
- Fixed FBTFS.

* Wed Aug 23 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1.1
- Map PyPI name to distro's one.

* Thu May 18 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Thu Sep 23 2021 Nikolai Kostrigin <nickel@altlinux.org> 4.5.0-alt1
- 4.4.0 -> 4.5.0

* Thu Apr 02 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt2
- Fix tests by adding zope.security to BR:
- Fix license

* Thu Dec 19 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt1
- NMU: 4.2.1 -> 4.4.0
- Remove python2 module build
- Add unittests execution

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Dec 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1
- Version 4.2.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

