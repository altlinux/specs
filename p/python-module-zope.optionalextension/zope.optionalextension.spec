%define oname zope.optionalextension

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt4.1
Summary: Optional compilation of C extensions
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.optionalextension/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope

%description
This package provides a distutils extension for building optional C
extensions. It is intended for use in projects which have a Python
reference implementation of one or more features, and which can function
without needing any C extensions to be successfully compiled.

%package -n python3-module-%oname
Summary: Optional compilation of C extensions
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
This package provides a distutils extension for building optional C
extensions. It is intended for use in projects which have a Python
reference implementation of one or more features, and which can function
without needing any C extensions to be successfully compiled.

%prep
%setup

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
rm -f %buildroot%python3_sitelibdir/zope/__init__*
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/zope/__init__*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added necessary requirements

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Avoid conflict with python-module-zope

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

