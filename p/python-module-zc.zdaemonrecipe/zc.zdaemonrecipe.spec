%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.zdaemonrecipe

%def_with python3

Name: python-module-%oname
Version: 1.0.0
#Release: alt2.1
Summary: ZC Buildout recipe for zdaemon scripts
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zdaemonrecipe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/14/0e/05ded59f327fe93e71b6fcd9263fe82016cfeec2c3a13b055bbd9119a414/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zc.buildout zc.recipe.egg ZConfig

%description
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

%package -n python3-module-%oname
Summary: ZC Buildout recipe for zdaemon scripts
Group: Development/Python3
%py3_requires zc zc.buildout zc.recipe.egg ZConfig

%description -n python3-module-%oname
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

%package -n python3-module-%oname-tests
Summary: Tests for zc.zdaemonrecipe
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zdaemon

%description -n python3-module-%oname-tests
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

This package contains tests for zc.zdaemonrecipe.

%package tests
Summary: Tests for zc.zdaemonrecipe
Group: Development/Python
Requires: %name = %version-%release
%py_requires zdaemon

%description tests
The zdaemon recipe provides support for generating zdaemon-based run
scripts.

This package contains tests for zc.zdaemonrecipe.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

