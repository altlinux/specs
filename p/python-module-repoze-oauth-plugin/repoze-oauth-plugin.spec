%define oname repoze-oauth-plugin

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3.1
Summary: OAuth plugin for repoze.who and repoze.what
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze-oauth-plugin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who repoze.what oauth2 SQLAlchemy

%description
repoze-oauth-plugin is a repoze.who and repoze.what plugin implementing
the server side of the OAuth 1.0 protocol. It supports both:

* 2-legged flow where the client is at the same time a resource owner and
* 3-legged flow where the client acts on behalf of a resource owner.

%package -n python3-module-%oname
Summary: OAuth plugin for repoze.who and repoze.what
Group: Development/Python3
%py3_requires repoze.who repoze.what oauth2 SQLAlchemy

%description -n python3-module-%oname
repoze-oauth-plugin is a repoze.who and repoze.what plugin implementing
the server side of the OAuth 1.0 protocol. It supports both:

* 2-legged flow where the client is at the same time a resource owner and
* 3-legged flow where the client acts on behalf of a resource owner.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export PYTHONIOENCODING=UTF-8

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

