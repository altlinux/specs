%define _unpackaged_files_terminate_build 1

%define pypi_name zope.contenttype

%def_with check

Name: python3-module-%pypi_name
Version: 5.0
Release: alt2

Summary: Zope contenttype
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.contenttype/
Vcs: https://github.com/zopefoundation/zope.contenttype.git

Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%py3_requires zope

%description
A utility module for content-type handling.

%package tests
Summary: Tests for zope.contenttype
Group: Development/Python3
Requires: %name = %EVR

%description tests
A utility module for content-type handling.

This package contains tests for zope.contenttype.

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
%doc *.txt *.rst
%python3_sitelibdir/zope/contenttype/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt2
- Mapped PyPI name to distro's one.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Wed Aug 17 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt3
- Make package arch dependent back (Closes: #43521).

* Mon Jun 06 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt2
- Drop 2to3 dependency.

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.5.0-alt1
- Version updated to 4.5.0.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150223.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150223.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150223
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.5.5-alt2.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.5-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.5-alt1
- Version 3.5.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

