%define oname repoze.what.plugins.ip
Name: python-module-%oname
Version: 0.2
Release: alt1.1
Summary: ip based restrictions for repoze.what
License: Apache 2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.ip/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins repoze.what

%description
Basic IP based restriction predicate, using googles ipaddr library.

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
%doc tests
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

