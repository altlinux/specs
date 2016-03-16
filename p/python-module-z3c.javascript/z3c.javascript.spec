%define oname z3c.javascript

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.svn20100323.1
Summary: Javascript libraries Zope 3
License: BSD-like
Group: Development/Python
Url: http://svn.zope.org/z3c.javascript/?rev=80712#dirlist
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://z3c-javascript.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c

%description
Javascript libraries Zope 3.

%package -n python3-module-%oname
Summary: Javascript libraries Zope 3
Group: Development/Python3
%py3_requires z3c

%description -n python3-module-%oname
Javascript libraries Zope 3.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.svn20100323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20100323
- New snapshot
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.svn20080428.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20080428
- Initial build for Sisyphus

