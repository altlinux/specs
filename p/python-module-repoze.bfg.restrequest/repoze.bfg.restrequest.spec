%define oname repoze.bfg.restrequest
Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: A REST aware Request for implementing RESTful applications with repoze.bfg
License: Repoze license
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.restrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg

%description
repoze.bfg.restrequest implements 4 additional Request types for use
with RESTful applications.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

