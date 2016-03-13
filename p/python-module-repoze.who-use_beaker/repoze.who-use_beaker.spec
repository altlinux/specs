%define oname repoze.who-use_beaker

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Identifier plugin for repoze.who with beaker.session cache implementation
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who-use_beaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.who paste.script beaker

%description
repoze.who-use_beaker is a repoze.who identifier plugin. It is aimed at
replacing repoze.who.plugins.auth_tkt in order to store the user data in
beaker session.

The plugin stores a dictionary containing at least
{'repoze.who.userid': userid} under key repoze.who.tkt.

%package -n python3-module-%oname
Summary: Identifier plugin for repoze.who with beaker.session cache implementation
Group: Development/Python3
%py3_requires repoze.who paste.script beaker

%description -n python3-module-%oname
repoze.who-use_beaker is a repoze.who identifier plugin. It is aimed at
replacing repoze.who.plugins.auth_tkt in order to store the user data in
beaker session.

The plugin stores a dictionary containing at least
{'repoze.who.userid': userid} under key repoze.who.tkt.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

