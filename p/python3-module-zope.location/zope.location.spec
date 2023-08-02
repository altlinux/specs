%define _unpackaged_files_terminate_build 1
%define oname zope.location

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1.1

Summary: Zope Location
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.location/
Vcs: https://github.com/zopefoundation/zope.location.git

Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.copy
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.configuration
%endif

%py3_requires zope.configuration
%py3_requires zope.interface
%py3_requires zope.proxy
%py3_requires zope.schema

%description
In Zope3, location are special objects that has a structural location.

%package tests
Summary: Tests for Zope Location
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

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
%doc LICENSE.txt *.rst
%python3_sitelibdir/zope/location/
%python3_sitelibdir/%oname-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/zope/location/tests

%files tests
%python3_sitelibdir/zope/location/tests

%changelog
* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: mapped PyPI name to distro's one.

* Thu May 25 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 4.3-alt1
- New version 4.3.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 4.2-alt6
- Bootstrap for python3.9.

* Wed Apr 01 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.2-alt5
- Enable tests
- Add zope.component back to requires

* Fri Mar 06 2020 Anton Farygin <rider@altlinux.ru> 4.2-alt4
- removed zope.component requires to avoid cyclic deps for python 3.8 build

* Wed Mar 04 2020 Nikolai Kostrigin <nickel@altlinux.org> 4.2-alt3
- Temporary disable tests to break cyclic deps for python 3.8 build
- Fix license

* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.2-alt2
- NMU: remove python2 module build

* Mon Apr 29 2019 Grigory Ustinov <grenka@altlinux.org> 4.2-alt1
- Build new version.

* Tue Mar 06 2018 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1.S1
- 4.0.4 -> 4.1.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.dev0.git20150128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.dev0.git20150128.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2.dev0.git20150128
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20141027
- New snapshot

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20140319
- Version 4.0.4dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Version 3.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

