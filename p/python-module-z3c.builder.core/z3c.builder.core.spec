%define ocore z3c.builder
%define oname %ocore.core

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt6.1
Summary: A utility to help jump start Zope 3 projects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.builder.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
AutoReq: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%ocore = %EVR
%py_requires rwproperty zc.buildout zope.component
%py_requires zope.configuration zope.container zope.interface
%py_requires zope.schema lxml

%description
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

%package -n python3-module-%oname
Summary: A utility to help jump start Zope 3 projects
Group: Development/Python3
Requires: python3-module-%ocore = %EVR
%py3_requires rwproperty zc.buildout zope.component
%py3_requires zope.configuration zope.container zope.interface
%py3_requires zope.schema lxml
%add_findreq_skiplist %python3_sitelibdir/z3c/builder/core/file-templates/*

%description -n python3-module-%oname
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.builder.core
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.coverage

%description -n python3-module-%oname-tests
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

This package contains tests for z3c.builder.core

%package -n python3-module-%ocore
Summary: Core package of %ocore
Group: Development/Python3

%description -n python3-module-%ocore
Core package of %ocore.

%package tests
Summary: Tests for z3c.builder.core
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
z3c.builder is a tool that helps you jump start development of a Zope 3
application by generating all the boiler plate code and configuration
for you.

This package contains tests for z3c.builder.core

%package -n python-module-%ocore
Summary: Core package of %ocore
Group: Development/Python
Conflicts: %name < %EVR

%description -n python-module-%ocore
Core package of %ocore.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
for i in $(find -type f -name '*.py' |grep -v 'file-templates'); do
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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%else
install -d %buildroot%python3_sitelibdir/z3c/builder
cp %buildroot%python_sitelibdir/z3c/builder/__init__.py \
	%buildroot%python3_sitelibdir/z3c/builder/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/z3c/builder/__init__.py*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%files -n python-module-%ocore
%python_sitelibdir/z3c/builder/__init__.py*

%files -n python3-module-%ocore
%python3_sitelibdir/z3c/builder/__init__.py
#python3_sitelibdir/z3c/builder/__pycache__/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/z3c/builder/__init__.py
#exclude %python3_sitelibdir/z3c/builder/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt6.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt6
- Added module for Python 3

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt5
- Extracted %ocore into separate package

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt4.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt4
- Fixed build

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt3
- Removed setuptools from requirements

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

