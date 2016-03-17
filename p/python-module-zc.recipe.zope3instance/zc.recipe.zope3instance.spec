%define oname zc.recipe.zope3instance

%def_with python3

Name: python-module-%oname
Version: 1.0.0a1
Release: alt2.git20110408.1
Summary: ZC Buildout recipe for defining a Zope 3 instance
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.zope3instance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.zope.org/repos/main/zc.recipe.zope3instance/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc.recipe zc.buildout zope.testing zc.recipe.egg

%description
This recipe creates a Zope instance that has been extended by a
collection of eggs.

%package -n python3-module-%oname
Summary: ZC Buildout recipe for defining a Zope 3 instance
Group: Development/Python3
%py3_requires zc.recipe zc.buildout zope.testing zc.recipe.egg

%description -n python3-module-%oname
This recipe creates a Zope instance that has been extended by a
collection of eggs.

%prep
%setup

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
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0a1-alt2.git20110408.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a1-alt2.git20110408
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a1-alt1.git20110408.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a1-alt1.git20110408.1
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a1-alt1.git20110408
- Initial build for Sisyphus

