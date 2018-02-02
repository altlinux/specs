%define oname natsort

%def_with python3

Name: python-module-%oname
Version: 3.5.1
Release: alt1.git20140925.1.1
Summary: Sort lists naturally
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/natsort/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SethMMorton/natsort.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest python-module-pytest-pep8
BuildPreReq: python-module-pytest-flakes python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest python3-module-pytest-pep8
BuildPreReq: python3-module-pytest-flakes python3-module-pytest-cov
%endif

%py_provides %oname

%description
Natural sorting for python.

%package -n python3-module-%oname
Summary: Sort lists naturally
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Natural sorting for python.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Natural sorting for python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Natural sorting for python.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees source build/pickle
sphinx-build -b html -d build/doctrees source build/html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1.git20140925.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt1.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.git20140925
- Initial build for Sisyphus

