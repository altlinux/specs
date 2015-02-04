%define oname jmespath

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150203
Summary: JSON Matching Expressions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jmespath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boto/jmespath.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-tox
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-guzzle_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-tox
%endif

%py_provides %oname

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%package -n python3-module-%oname
Summary: JSON Matching Expressions
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

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
export LC_ALL=en_US.UTF-8
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
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
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141105
- Initial build for Sisyphus

