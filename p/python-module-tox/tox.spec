%define oname tox

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.1.1
Release: alt1.1
Summary: virtualenv-based automation of test activities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-virtualenv python-module-py
#BuildPreReq: python-module-pytest python-module-py
#BuildPreReq: python-module-sphinx-devel python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-virtualenv python3-module-py
#BuildPreReq: python3-module-pytest python3-module-py
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools-tests python-module-virtualenv python3-module-setuptools-tests python3-module-virtualenv rpm-build-python3 time

%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%package -n python3-module-%oname
Summary: virtualenv-based automation of test activities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGELOG CONTRIBUTORS *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG CONTRIBUTORS *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

