%define oname plumbum

%def_with python3

Name: python-module-%oname
Version: 1.4.3
Release: alt1.git20141103.1.1
Summary: Plumbum: shell combinators library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/plumbum/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tomerfiliba/plumbum.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

Apart from shell-like syntax and handy shortcuts, the library provides
local and remote command execution (over SSH), local and remote
file-system paths, easy working-directory and environment manipulation,
and a programmatic Command-Line Interface (CLI) application toolkit. Now
let's see some code!

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Plumbum: shell combinators library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

Apart from shell-like syntax and handy shortcuts, the library provides
local and remote command execution (over SSH), local and remote
file-system paths, easy working-directory and environment manipulation,
and a programmatic Command-Line Interface (CLI) application toolkit. Now
let's see some code!

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
touch experiments/__init__.py
cp -fR experiments %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
touch experiments/__init__.py
cp -fR experiments %buildroot%python3_sitelibdir/%oname/
find %buildroot%python3_sitelibdir/%oname/experiments \
	-type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc examples *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc examples *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.3-alt1.git20141103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1.git20141103.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20141103
- Initial build for Sisyphus

