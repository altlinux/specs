%define oname sunburnt

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 0.7
Release: alt2.git20140217.1
Summary: Python interface to Solr
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sunburnt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tow/sunburnt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml python-module-pytz
BuildPreReq: python-module-requests python-module-nose
BuildPreReq: python-module-egenix-mx-base python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml python3-module-pytz
BuildPreReq: python3-module-requests python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-egenix-mx-base

%description
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python interface to Solr
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

This package contains pickles for %oname.

%package docs
Summary: Pickles for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Sunburnt is a Python-based interface for working with the Apache Solr
search engine.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
nosetests
%if_with python3
pushd ../python3
nosetests3
popd
%endif

%files
%doc Changelog *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt2.git20140217.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2.git20140217
- Fixed build

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20140217
- Initial build for Sisyphus

