%define oname repoze.bfg.restrequest

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt3
Summary: A REST aware Request for implementing RESTful applications with repoze.bfg
License: Repoze license
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.restrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.bfg

%description
repoze.bfg.restrequest implements 4 additional Request types for use
with RESTful applications.

%package -n python3-module-%oname
Summary: A REST aware Request for implementing RESTful applications with repoze.bfg
Group: Development/Python3
%py3_requires repoze.bfg

%description -n python3-module-%oname
repoze.bfg.restrequest implements 4 additional Request types for use
with RESTful applications.

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
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

