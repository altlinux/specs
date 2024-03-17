%define _unpackaged_files_terminate_build 1
%define pypi_name zope.configuration
%define ns_name zope
%define mod_name configuration

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.1
Release: alt1

Summary: Zope Configuration Markup Language (ZCML)
License: ZPL-2.1
Group: Development/Python3

Url: https://pypi.org/project/zope.configuration
Vcs: https://github.com/zopefoundation/zope.configuration.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
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
The zope configuration system provides an extensible system for
supporting various kinds of configurations.

It is based on the idea of configuration directives. Users of the
configuration system provide configuration directives in some language
that express configuration choices. The intent is that the language be
pluggable. An XML language is provided by default.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version-nspkg.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Fri Mar 15 2024 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 5.0 -> 5.0.1.

* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: mapped PyPI name to distro's one.

* Mon May 22 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt3
- Fixed BuildRequires.
- Build with check again.

* Fri Jan 29 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt2
- Bootstrap for python3.9.

* Tue Nov 17 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.4.0-alt1
- 4.3.1 -> 4.4.0

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt2
- NMU: Remove python2 module build
- Rearrange unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt1
- Version updated to 4.3.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.dev0.git20150225.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.dev0.git20150225.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev0.git20150225
- Version 4.0.4.dev0
- Added documentation
- Enabled check

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.8.0-alt2.1
- Rebuild with Python-3.3

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt5.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt5
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt3
- Enabled tests

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Set archdep for package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

