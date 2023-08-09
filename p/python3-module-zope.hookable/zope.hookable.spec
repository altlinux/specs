%define _unpackaged_files_terminate_build 1

%define pypi_name zope.hookable
%define ns_name zope
%define mod_name hookable

%def_with check

%define descr \
Support the efficient creation of hookable objects, which are callable \
objects that are meant to be replaced by other callables, at least \
optionally. \
\
The idea is you create a function that does some default thing and make \
it hookable. Later, someone can modify what it does by calling its \
sethook method and changing its implementation.  All users of the \
function, including those that imported it, will see the change.

Name: python3-module-%pypi_name
Version: 5.4
Release: alt1
Summary: Hookable object support
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.hookable/
Vcs: http://github.com/zopefoundation/zope.hookable
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
%descr

%package tests
Summary: Tests for zope.hookable
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
%descr

This package contains tests for zope.hookable.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# strip devel files
rm %buildroot%python3_sitelibdir/%ns_name/%mod_name/*.c

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests

%changelog
* Thu Aug 03 2023 Stanislav Levin <slev@altlinux.org> 5.4-alt1
- 5.0.1 -> 5.4.
- Modernized packaging.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0.1-alt2.1
- NMU: mapped PyPI name to distro's one.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt2
- Drop specsubst scheme.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 5.0.0 -> 5.0.1.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.
- Fix license.

* Mon Oct 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Build new version.

* Thu May 10 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.4-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.4-alt1.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

