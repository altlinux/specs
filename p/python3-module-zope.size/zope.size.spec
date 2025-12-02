%define _unpackaged_files_terminate_build 1
%define pypi_name zope.size
%define ns_name zope
%define mod_name size

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: Interfaces and simple adapter that give the size of an object
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.size
VCS: https://github.com/zopefoundation/zope.size
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
This package provides a definition of simple interface that allows to
retrieve the size of the object for displaying and for sorting.

The default adapter is also provided. It expects objects to have the
getSize method that returns size in bytes, however, it won't crash if an
object doesn't have one and will show size as not available instead.

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
%doc README.*
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.*

%changelog
* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Fri Jun 30 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

