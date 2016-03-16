%define oname repoze.what.plugins.config

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt3.1
Summary: pastedeploy help methods for repoze.what
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.config/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.what.plugins repoze.what

%description
repoze.what.plugins.config allows you to configure repoze.who and
repoze.what using pastedeploy. repoze.who and repoze.what are WSGI
middleware frameworks for authentication and authorization,
respectively. paster and pastedeploy allows you to configure your WSGI
application via INI files.

%package -n python3-module-%oname
Summary: pastedeploy help methods for repoze.what
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what

%description -n python3-module-%oname
repoze.what.plugins.config allows you to configure repoze.who and
repoze.what using pastedeploy. repoze.who and repoze.what are WSGI
middleware frameworks for authentication and authorization,
respectively. paster and pastedeploy allows you to configure your WSGI
application via INI files.

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
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

