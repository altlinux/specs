%define _unpackaged_files_terminate_build 1

%define pypi_name zope.i18n
%define ns_name zope
%define mod_name i18n

%def_without check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt2
Summary: Zope Internationalization Support
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.i18n/
Vcs: https://github.com/zopefoundation/zope.i18n.git
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
This package implements several APIs related to internationalization and
localization.

* Locale objects for all locales maintained by the ICU project.
* Gettext-based message catalogs for message strings.
* Locale discovery for Web-based requests.

%package tests
Summary: Tests for zope.i18n (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-zope.component-tests
%py3_requires zope.publisher
%py3_requires zope.testrunner

%description tests
This package contains tests for %pypi_name.

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
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%ns_name/%mod_name/testing.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/*/testing.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests
%exclude %python3_sitelibdir/%ns_name/%mod_name/locales/tests

%files tests
%python3_sitelibdir/%ns_name/%mod_name/testing.*
%python3_sitelibdir/%ns_name/%mod_name/*/testing.*
%python3_sitelibdir/%ns_name/%mod_name/tests
%python3_sitelibdir/%ns_name/%mod_name/locales/tests

%changelog
* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt2
- Mapped PyPI name to distro's one.
- Modernized packaging.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri Sep 24 2021 Nikolai Kostrigin <nickel@altlinux.org> 4.8.0-alt1
- 4.7.0 -> 4.8.0

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.7.0-alt1
- NMU: 4.6.2 -> 4.7.0
- Remove python2 module build
- Remove ubt tag from changelog
- Enable check

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.6.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Mon Apr 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt3
- requires for tests fixed

* Fri Mar 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt2
- py3 requires fixed

* Thu Mar 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.6.2-alt1
- Version updated to 4.6.2

* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 4.3.1-alt1
- 4.1.0 -> 4.3.1

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.8.0-alt1.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

