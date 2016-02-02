%define oname invoke

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.10.1
Release: alt2.git20150730
Summary: Simple Python task execution
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/invoke/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyinvoke/invoke.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-alabaster python-module-docutils python-module-flake8 python-module-html5lib python-module-objects.inv python-module-pbr python-module-pytest python-module-spec python-module-unittest2

#BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
#BuildPreReq: python-module-invocations-tests python-module-releases
#BuildPreReq: python-module-alabaster python-module-nose
#BuildPreReq: python-module-spec python-module-mock
#BuildPreReq: python-module-flake8
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-invocations-tests python3-module-releases
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-spec python3-module-mock
#BuildPreReq: python3-module-flake8
BuildRequires: python3-module-flake8 python3-module-html5lib python3-module-pbr python3-module-spec python3-module-unittest2
%endif

%add_findreq_skiplist %python_sitelibdir/%oname/vendor/yaml3/__init__.py

%py_provides %oname

%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%package -n python3-module-%oname
Summary: Simple Python task execution
Group: Development/Python3
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/vendor/yaml2/*.py

%description -n python3-module-%oname
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx sites
ln -s ../objects.inv sites/docs/

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

pushd sites/docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR sites/docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
spec
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
spec.py3
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc sites/docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.1-alt2.git20150730
- cleanup buildreq

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150730
- Version 0.10.1

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20141113
- Initial build for Sisyphus

