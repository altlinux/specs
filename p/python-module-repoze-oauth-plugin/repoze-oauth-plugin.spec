%define oname repoze-oauth-plugin
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: OAuth plugin for repoze.who and repoze.what
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze-oauth-plugin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

#Requires: python-module-repoze.who python-module-repoze.what

%py_requires repoze.who repoze.what oauth2 SQLAlchemy

%description
repoze-oauth-plugin is a repoze.who and repoze.what plugin implementing
the server side of the OAuth 1.0 protocol. It supports both:

* 2-legged flow where the client is at the same time a resource owner and
* 3-legged flow where the client acts on behalf of a resource owner.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

