%define oname hy

%def_with python3

Name: python-module-%oname
Version: 0.10.1
Release: alt1.git20150217
Summary: Lisp and Python love each other
License: MIT/Expat
Group: Development/Python
Url: https://pypi.python.org/pypi/hy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hylang/hy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-rply python-module-astor
BuildPreReq: python-module-clint python-module-requests
BuildPreReq: python-module-flake8 python-module-coverage
BuildPreReq: python-module-nose python-module-tox
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-rply python3-module-astor
BuildPreReq: python3-module-clint python3-module-requests
BuildPreReq: python3-module-flake8 python3-module-coverage
BuildPreReq: python3-module-nose python3-module-tox
%endif

%py_provides %oname
%py_requires rply astor clint requests

%description
Hy is a Python <-> Lisp layer. It helps make things work nicer, and lets
Python and the Hy lisp variant play nice together.

%package -n python3-module-%oname
Summary: Lisp and Python love each other
Group: Development/Python3
%py3_provides %oname
%py3_requires rply astor clint requests

%description -n python3-module-%oname
Hy is a Python <-> Lisp layer. It helps make things work nicer, and lets
Python and the Hy lisp variant play nice together.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Hy is a Python <-> Lisp layer. It helps make things work nicer, and lets
Python and the Hy lisp variant play nice together.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Hy is a Python <-> Lisp layer. It helps make things work nicer, and lets
Python and the Hy lisp variant play nice together.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PATH=$PATH:%buildroot%_bindir
python setup.py test
export PYTHONPATH=$PWD
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
#export PYTHONPATH=$PWD
#nosetests3 -v
popd
%endif

%files
%doc AUTHORS NEWS *.md *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html eg

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS *.md *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150217
- Initial build for Sisyphus

