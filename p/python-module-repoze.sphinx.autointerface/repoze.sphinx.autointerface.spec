%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname repoze.sphinx.autointerface

%def_with python3

Name: python-module-%oname
Version: 0.8
#Release: alt2.1.1
Summary: Auto-generate Sphinx API docs from Zope interfaces
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.sphinx.autointerface
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.sphinx.autointerface.git
Source0: https://pypi.python.org/packages/8f/65/ea18d09c6847b3a381e16c89f26de0ddcdf0bdb8d05f4581e4df9b7033fd/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%py_requires zope.interface sphinx
Requires: python-module-repoze.sphinx = %EVR

%description
This package defines an extension for the `Sphinx` documentation system.
The extension allows generation of API documentation by introspection of
`zope.interface` instances in code.

%if_with python3
%package -n python3-module-%oname
Summary: Auto-generate Sphinx API docs from Zope interfaces (Python 3)
Group: Development/Python3
%py3_requires zope.interface sphinx jinja2.tests
Requires: python3-module-repoze.sphinx = %EVR

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
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

touch %buildroot%python_sitelibdir/repoze/sphinx/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.1-alt1
- Version 0.7.1

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
