%define _unpackaged_files_terminate_build 1
%define pypi_name zope.event
%define ns_name zope
%define mod_name event

%def_with check

Name: python3-module-%pypi_name
Version: 6.2
Release: alt1
Summary: Very basic event publishing system
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.event/
Vcs: https://github.com/zopefoundation/zope.event
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
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests*

%changelog
* Wed Apr 29 2026 Stanislav Levin <slev@altlinux.org> 6.2-alt1
- 6.1 -> 6.2.

* Wed Dec 17 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt1
- 5.1.1 -> 6.1.

* Tue Jul 22 2025 Stanislav Levin <slev@altlinux.org> 5.1.1-alt1
- 5.1 -> 5.1.1.

* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 5.0 -> 5.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: mapped PyPI name to distro's one.

* Sat Jun 24 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 4.6-alt1
- New version 4.6.

* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 4.4-alt2
- Drop python2 support.

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.4-alt1
- Version updated to 4.4
- Cleanup spec

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.3-alt1.1
- NMU: Use buildreq for BR.

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.2-alt1
- Version 4.0.2

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Version 3.5.2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0.1-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt4
- Added necessary requirement

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt3
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt1
- Initial build for Sisyphus

