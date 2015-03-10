%define oname elastic-git

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20150220
Summary: JSON Object storage backed by Git & Elastic Search
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/elastic-git/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/elastic-git.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-confmodel python-module-elasticutils
BuildPreReq: python-module-GitPython python-module-jinja2
BuildPreReq: python-module-pytest python-module-pytest-cov
BuildPreReq: python-module-pytest-xdist python-module-sphinx-devel
BuildPreReq: python-module-GitDB python-module-unidecode
BuildPreReq: python-module-avro
BuildPreReq: python-module-sphinx-argparse
BuildPreReq: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-confmodel python3-module-elasticutils
BuildPreReq: python3-module-GitPython python3-module-jinja2
BuildPreReq: python3-module-pytest python3-module-pytest-cov
BuildPreReq: python3-module-pytest-xdist
BuildPreReq: python3-module-GitDB python3-module-unidecode
BuildPreReq: python3-module-avro
%endif

%py_provides elasticgit
%py_requires avro

%description
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: JSON Object storage backed by Git & Elastic Search
Group: Development/Python3
%py3_provides elasticgit
%py3_requires avro

%description -n python3-module-%oname
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/examples
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/examples
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150220
- Version 1.0.1
- Added module for Python 3

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1.git20150212
- Version 0.3.7

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20150206
- Version 0.3.4

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150116
- Version 0.3.3

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141127
- Version 0.3.1

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.12-alt1.git20141124
- Version 0.2.12

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1.git20141119
- Version 0.2.10

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141110
- Version 0.2.8

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20141104
- Version 0.2.6

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141024
- Initial build for Sisyphus

