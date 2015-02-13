%define oname Wextracto

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20150116
Summary: Web Data Extraction Library Written in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Wextracto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eBay/wextracto.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-requests
BuildPreReq: python-module-lxml python-module-cssselect
BuildPreReq: python-module-publicsuffix python-module-singledispatch
BuildPreReq: python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildPreReq: graphviz python-modules-multiprocessing
BuildPreReq: python-modules-logging python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-requests
BuildPreReq: python3-module-lxml python3-module-cssselect
BuildPreReq: python3-module-publicsuffix python3-module-singledispatch
BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname wex
%py_requires six requests lxml cssselect publicsuffix singledispatch
%py_requires multiprocessing logging json
%add_python_req_skip pytest

%description
Wextracto is a toolkit for command-line web data extraction.

%package -n python3-module-%oname
Summary: Web Data Extraction Library Written in Python
Group: Development/Python3
%py3_provides %oname wex
%py3_requires six requests lxml cssselect publicsuffix singledispatch
%add_python3_req_skip pytest

%description -n python3-module-%oname
Wextracto is a toolkit for command-line web data extraction.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Wextracto is a toolkit for command-line web data extraction.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Wextracto is a toolkit for command-line web data extraction.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc NOTICES.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html docs/samples

%if_with python3
%files -n python3-module-%oname
%doc NOTICES.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20150116
- Initial build for Sisyphus

