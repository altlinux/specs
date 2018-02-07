%define oname zest.releaser

%def_with python3

Name: python-module-%oname
Version: 6.12.2
Release: alt1.1

Summary: Software releasing made easy and repeatable
License: GPLv2+
Group: Development/Python

Url: https://pypi.python.org/pypi/zest.releaser

# https://github.com/zestsoftware/zest.releaser.git
Source: %name-%version.tar

BuildRequires: python-module-nose python-module-setuptools python-module-sphinx python-module-z3c.testsetup time
BuildRequires: python-module-colorama python-module-twine
BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-setuptools python3-module-sphinx python3-module-z3c.testsetup
BuildRequires: python3-module-colorama python3-module-twine
%endif

%setup_python_module %oname

Requires: python-module-zest = %EVR

%description
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

%package -n python3-module-%oname
Summary: Software releasing made easy and repeatable
Group: Development/Python3
Requires: python3-module-zest = %EVR

%description -n python3-module-%oname
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

%package -n python3-module-%oname-tests
Summary: Tests for zest.releaser
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

This package contains tests for zest.releaser.

%package tests
Summary: Tests for zest.releaser
Group: Development/Python
Requires: %name = %EVR

%description tests
zest.releaser is collection of command-line programs to help you
automate the task of releasing a Python project.

This package contains tests for zest.releaser.

%package -n python-module-zest
Summary: Core package of zest
Group: Development/Python

%description -n python-module-zest
This package contains core package of zest.

%package -n python3-module-zest
Summary: Core package of zest
Group: Development/Python3

%description -n python3-module-zest
This package contains core package of zest.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

touch %buildroot%python_sitelibdir/zest/__init__.py
%if_with python3
touch %buildroot%python3_sitelibdir/zest/__init__.py
%endif

%check
python setup.py test ||:
%if_with python3
pushd ../python3
python3 setup.py test ||:
popd
%endif

%files
%doc *.rst
%doc doc/source/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/zest/__init__.py*

%files tests
%python_sitelibdir/*/*/tests

%files -n python-module-zest
%dir %python_sitelibdir/zest
%python_sitelibdir/zest/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%doc doc/source/*
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/zest/__init__.py
%exclude %python3_sitelibdir/zest/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-zest
%dir %python3_sitelibdir/zest
%python3_sitelibdir/zest/__init__.py
%dir %python3_sitelibdir/zest/__pycache__
%python3_sitelibdir/zest/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.12.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.12.2-alt1
- Updated to upstream release 6.12.2.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.55-alt1.dev0.git20141229.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.55-alt1.dev0.git20141229.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.55-alt1.dev0.git20141229.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.55-alt1.dev0.git20141229
- Version 3.55.dev0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.54-alt1.dev0.git20141121
- New snapshot

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.54-alt1.dev0.git20141110
- Version 3.54.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53-alt1.dev0.git20140717
- Version 3.53.dev0

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.50-alt1
- Version 3.50
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.48-alt1
- Version 3.48

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.46-alt1
- Version 3.46

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.44-alt1
- Initial build for Sisyphus

