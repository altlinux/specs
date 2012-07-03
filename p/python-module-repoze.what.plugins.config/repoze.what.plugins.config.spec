%define oname repoze.what.plugins.config
Name: python-module-%oname
Version: 0.2.1
Release: alt2.1
Summary: pastedeploy help methods for repoze.what
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.config/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins repoze.what

%description
repoze.what.plugins.config allows you to configure repoze.who and
repoze.what using pastedeploy. repoze.who and repoze.what are WSGI
middleware frameworks for authentication and authorization,
respectively. paster and pastedeploy allows you to configure your WSGI
application via INI files.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

