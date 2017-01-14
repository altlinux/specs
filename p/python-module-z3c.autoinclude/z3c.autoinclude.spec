%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname z3c.autoinclude

%def_with python3

Name: python-module-%oname
Version: 0.3.7
#Release: alt2.1
Summary: Automatically include ZCML
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.autoinclude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/90/12/364342fbaa9f606c3de7baa92a29d6619d794d46716125bc91118c5bb82c/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.dottedname zope.interface zope.configuration
%py_requires zope.schema zc.buildout

%description
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

%package -n python3-module-%oname
Summary: Automatically include ZCML
Group: Development/Python3
%py3_requires zope.dottedname zope.interface zope.configuration
%py3_requires zope.schema zc.buildout

%description -n python3-module-%oname
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.autoinclude
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

This package contains tests for z3c.autoinclude.

%package tests
Summary: Tests for z3c.autoinclude
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package adds two new ZCML directives to automatically detect ZCML
files to include: "includeDependencies" and "includePlugins".

When you want to include a Zope-based package in your application, you
have to repeat yourself in two places: you have to add the package
itself (in a setup.py, buildout, etc) and you also have to include its
ZCML with an <include> directive or a package-includes slug. Because you
have to repeat yourself, you can easily make an error where you add a
new package but forget to include its ZCML.

z3c.autoinclude lets you circumvent this error-prone process with
automatic detection and inclusion of ZCML files.

This package contains tests for z3c.autoinclude.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%_bindir/*.py3
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

