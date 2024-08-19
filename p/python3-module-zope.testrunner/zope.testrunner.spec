%define _unpackaged_files_terminate_build 1
%define pypi_name zope.testrunner
%define ns_name zope
%define mod_name testrunner

%def_with check

Name: python3-module-%pypi_name
Version: 6.5
Release: alt1
Summary: Zope testrunner script
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.testrunner/
Vcs: https://github.com/zopefoundation/zope.testrunner.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%py3_requires zope
# setuptools(pkg_resources) is used by namespace root that is packaged
# separately at python3-module-zope
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
Conflicts: python-module-%pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This package provides a flexible test runner with layer support.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot{%python3_sitelibdir_noarch/*,%python3_sitelibdir}
%endif

cp -al %buildroot%_bindir/zope-testrunner{,3}

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc README.*
%_bindir/zope-testrunner
%_bindir/zope-testrunner3
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Mon Aug 19 2024 Stanislav Levin <slev@altlinux.org> 6.5-alt1
- 6.4 -> 6.5.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 6.4-alt1
- 6.2.1 -> 6.4.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 6.2.1-alt1
- Automatically updated to 6.2.1.
- Fixed cringe obninsk-style packaging.

* Thu Aug 03 2023 Stanislav Levin <slev@altlinux.org> 6.0-alt3
- Modernized packaging.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 6.0-alt2
- Mapped PyPI name to distro's one.

* Thu May 18 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.0 -> 5.4.0.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt2
- pack zope-testrunner3 for compatibility

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt1
- new version 5.3.0 (with rpmrb script)
- don't pack tests

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt3
- build python3 module separately

* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 5.2-alt2
- Disabled testing against Python2.

* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 5.2-alt1
- Automatically updated to 5.2.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- Build new version 5.1.
- Fix license.

* Fri Apr 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.0-alt1
- Build new version.

* Sat Jun 09 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt3.S1
- Fix namespace package import ( python3 subpackage )

* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt2.S1
- Fix a wrong logic of packaging for non x86_64 arch

* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.8.1-alt1.S1
- v4.4.9 -> v4.8.1

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.4.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.9-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.9-alt1
- Version 4.4.9

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1
- Version 4.4.6

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.5-alt1
- Version 4.4.5

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Version 4.4.4

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1
- Version 4.4.3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1
- Version 4.3.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.4-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.3-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

