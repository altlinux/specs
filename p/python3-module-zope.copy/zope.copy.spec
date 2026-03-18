%define _unpackaged_files_terminate_build 1
%define pypi_name zope.copy
%define ns_name zope
%define mod_name copy

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: Pluggable object copying mechanism
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.copy/
Vcs: https://github.com/zopefoundation/zope.copy.git
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
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

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
%pyproject_run -- zope-testrunner --test-path=src -vv

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.0 -> 6.0.

* Fri Jan 31 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt2
- Mapped PyPI name to the distro's one.

* Fri Oct 25 2024 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Thu May 18 2023 Anton Vyatkin <toni@altlinux.org> 4.3-alt1
- New version 4.3.

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.2-alt3
- NMU: remove python2 module build

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.2-alt1
- new version 4.2

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.3 -> 4.1.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

