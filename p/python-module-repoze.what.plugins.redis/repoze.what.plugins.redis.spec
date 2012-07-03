%define oname repoze.what.plugins.redis
Name: python-module-%oname
Version: 1.0rc1
Release: alt1.1
Summary: The repoze.what Redis plugin
License: Apache 2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.redis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins repoze.what

%description
The Redis plugin makes repoze.what support sources defined in Redis
key-value databases by providing one group adapter and one permission
adapter.

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
%doc README doc/* test
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0rc1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0rc1-alt1
- Initial build for Sisyphus

