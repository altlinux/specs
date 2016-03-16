%define oname repoze.what.plugins.mongodb

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: MongoDB adapter plugins for repoze.what
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.mongodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.what.plugins repoze.what

%description
MongoDB adapter plugins for repoze.what.

%package -n python3-module-%oname
Summary: MongoDB adapter plugins for repoze.what
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what

%description -n python3-module-%oname
MongoDB adapter plugins for repoze.what.

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
%python_sitelibdir/repoze/what/plugins/mongodb
%python_sitelibdir/*egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/repoze/what/plugins/mongodb
%python3_sitelibdir/*egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

