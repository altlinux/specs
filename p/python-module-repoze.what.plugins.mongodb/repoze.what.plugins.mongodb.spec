%define oname repoze.what.plugins.mongodb
Name: python-module-%oname
Version: 0.1.1
Release: alt1.1
Summary: MongoDB adapter plugins for repoze.what
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.mongodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins

%description
MongoDB adapter plugins for repoze.what.

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
%python_sitelibdir/repoze/what/plugins/mongodb
%python_sitelibdir/*egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

