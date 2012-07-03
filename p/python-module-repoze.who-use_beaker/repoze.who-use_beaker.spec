%define oname repoze.who-use_beaker
Name: python-module-%oname
Version: 0.3
Release: alt1.1
Summary: Identifier plugin for repoze.who with beaker.session cache implementation
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who-use_beaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who paste.script beaker

%description
repoze.who-use_beaker is a repoze.who identifier plugin. It is aimed at
replacing repoze.who.plugins.auth_tkt in order to store the user data in
beaker session.

The plugin stores a dictionary containing at least
{'repoze.who.userid': userid} under key repoze.who.tkt.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

