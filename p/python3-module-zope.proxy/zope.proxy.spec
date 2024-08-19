%define _unpackaged_files_terminate_build 1
%define pypi_name zope.proxy
%define ns_name zope
%define mod_name proxy

%def_with check

Name: python3-module-%pypi_name
Version: 5.3
Release: alt1
Summary: Generic Transparent Proxies
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.proxy/
Vcs: http://github.com/zopefoundation/zope.proxy
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%py3_requires zope
# setuptools(pkg_resources) is used by namespace root that is packaged
# separately at python3-module-zope
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is responsible.

%package devel
Summary: Development files for %pypi_name
Group: Development/Python3
Requires: %name

%description devel
This package contains development files for %pypi_name.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src

%files
%doc README.*
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %_includedir/python3*/%pypi_name/
%exclude %python3_sitelibdir/%ns_name/%mod_name/*.h
%exclude %python3_sitelibdir/%ns_name/%mod_name/*.c

%files devel
%_includedir/python3*/%pypi_name/
%python3_sitelibdir/%ns_name/%mod_name/*.h
%python3_sitelibdir/%ns_name/%mod_name/*.c

%changelog
* Mon Aug 19 2024 Stanislav Levin <slev@altlinux.org> 5.3-alt1
- 5.2 -> 5.3.

* Fri Mar 15 2024 Stanislav Levin <slev@altlinux.org> 5.2-alt1
- 5.0.0 -> 5.2.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.3.5 -> 5.0.0.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 4.3.5-alt2
- Bootstrap for python3.9.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 4.3.5-alt1
- 4.3.3 -> 4.3.5.

* Tue Feb 25 2020 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt2
- Bootstrap for python3.8.

* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.3-alt1
- NMU: 4.2.0 -> 4.3.3
- Remove python2 module build
- Add unittests execution

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.6-alt1
- Version 4.1.6

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1
- Version 4.1.4
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

