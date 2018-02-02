%define oname jmespath

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt1.1
Summary: JSON Matching Expressions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jmespath/

# https://github.com/boto/jmespath.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-guzzle_sphinx_theme python-module-html5lib python-module-objects.inv
BuildRequires: python-module-nose python-module-setuptools python-module-tox
BuildRequires: python-module-hypothesis
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-setuptools python3-module-tox
BuildRequires: python3-module-hypothesis
%endif

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%package -n python3-module-%oname
Summary: JSON Matching Expressions
Group: Development/Python3

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
%patch1 -p1

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
PYTHONPATH=$(pwd) py.test ||:
%if_with python3
pushd ../python3
python3 setup.py test
PYTHONPATH=$(pwd) py.test3 ||:
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.3-alt1
- Updated to upstream version 0.9.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.1-alt1.git20150712.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.git20150712.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150712
- Version 0.7.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150420
- Version 0.7.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141105
- Initial build for Sisyphus

