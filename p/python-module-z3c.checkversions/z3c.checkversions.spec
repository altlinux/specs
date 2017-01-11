%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname z3c.checkversions

%def_with python3

Name: python-module-%oname
Version: 0.5
#Release: alt2.1
Summary: Find newer package versions on PyPI
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.checkversions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/7c/bd/405e9684d54fef8c7af709252e3bc1349509974161c6631e653b1eadd109/%{oname}-%{version}.zip

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package provides a console script named checkversions.

%package -n python3-module-%oname
Summary: Find newer package versions on PyPI
Group: Development/Python3

%description -n python3-module-%oname
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package provides a console script named checkversions.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.checkversions
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.buildout

%description -n python3-module-%oname-tests
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package contains tests for z3c.checkversions.

%package tests
Summary: Tests for z3c.checkversions
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout

%description tests
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package contains tests for z3c.checkversions.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

