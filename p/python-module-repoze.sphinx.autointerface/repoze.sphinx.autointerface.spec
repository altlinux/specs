%define oname repoze.sphinx.autointerface

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt1.git20120215
Summary: Auto-generate Sphinx API docs from Zope interfaces
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.sphinx.autointerface
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.sphinx.autointerface.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.sphinx zope.interface sphinx

%description
This package defines an extension for the `Sphinx` documentation system.
The extension allows generation of API documentation by introspection of
`zope.interface` instances in code.

%if_with python3
%package -n python3-module-%oname
Summary: Auto-generate Sphinx API docs from Zope interfaces (Python 3)
Group: Development/Python3
%py3_requires repoze.sphinx zope.interface sphinx jinja2.tests

%description -n python3-module-%oname
This package defines an extension for the `Sphinx` documentation system.
The extension allows generation of API documentation by introspection of
`zope.interface` instances in code.

%package -n python3-module-repoze.sphinx
Summary: Core package for repoze.sphinx (Python 3)
Group: Development/Python3
%py3_provides repoze.sphinx
%py3_requires repoze

%description -n python3-module-repoze.sphinx
Core package for repoze.sphinx.
%endif

%package -n python-module-repoze.sphinx
Summary: Core package for repoze.sphinx
Group: Development/Python
%py_provides repoze.sphinx
%py_requires repoze

%description -n python-module-repoze.sphinx
Core package for repoze.sphinx.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
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

touch %buildroot%python_sitelibdir/repoze/sphinx/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd

%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

touch %buildroot%python3_sitelibdir/repoze/sphinx/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/repoze/sphinx/__init__.*

%files -n python-module-repoze.sphinx
%python_sitelibdir/repoze/sphinx/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/repoze/sphinx/__init__.*

%files -n python3-module-repoze.sphinx
%python3_sitelibdir/repoze/sphinx/__init__.*
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20120215
- New snapshot
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20110322
- Initial build for Sisyphus

