%define oname pyaxon

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.11
Release: alt1.git20150217
Summary: Python library for AXON
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaxon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intellimath/pyaxon.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-yaml
BuildPreReq: python-modules-json
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-yaml
%endif

%py_provides %oname axon
%py_requires json

%description
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires yaml
%add_python_req_skip test_construct test_anonymous

%description tests
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python library for AXON
Group: Development/Python3
%py3_provides %oname axon
%py3_requires json

%description -n python3-module-%oname
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires yaml
%add_python3_req_skip test_construct test_anonymous

%description -n python3-module-%oname-tests
pyaxon is an MIT Licensed python library for AXON. AXON is eXtended
Object Notation. It's a simple text based format for interchanging
objects, documents and data. It tries to combine the best of JSON, XML
and YAML.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python test_benchmark.py
python test_all.py
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test_benchmark.py
python3 test_all.py
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt1.git20150217
- Initial build for Sisyphus

