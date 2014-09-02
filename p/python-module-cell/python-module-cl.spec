%define oname cell

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20140709
Group: Development/Python
License: BSD
Summary: cell - Actor framework
URL: https://github.com/celery/cell
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-kombu
BuildPreReq: python-module-sphinxcontrib-issuetracker
BuildPreReq: python-module-eventlet python-module-greenlet
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
cell is an actor framework for Kombu and celery.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
cell is an actor framework for Kombu and celery.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
cell is an actor framework for Kombu and celery.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: cell - Actor framework
Group: Development/Python3

%description -n python3-module-%oname
cell is an actor framework for Kombu and celery.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%make -C docs pickle
%make -C docs html

cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS Changelog README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS Changelog README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20140709
- Initial build for Sisyphus

