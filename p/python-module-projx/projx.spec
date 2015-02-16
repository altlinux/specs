%define oname projx

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20150215
Summary: Graph transformations in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/projx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davebshow/projx.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-networkx python-module-pyparsing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-networkx python3-module-pyparsing
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires networkx pyparsing

%description
projx provides a simple and extensible API for interacting with graphs
in Python. Its core functionality is built around making graph
transformations using the NetworkX module and a DSL based on Neo4j's
Cypher query language. It also provides an extensible ETL pipeline that
uses JSON configuration (roughly modeled after orientdb-etl) to
translate graph data between various persistent and in-memory
representations.

%package -n python3-module-%oname
Summary: Graph transformations in Python
Group: Development/Python3
%py3_provides %oname
%py3_requires networkx pyparsing

%description -n python3-module-%oname
projx provides a simple and extensible API for interacting with graphs
in Python. Its core functionality is built around making graph
transformations using the NetworkX module and a DSL based on Neo4j's
Cypher query language. It also provides an extensible ETL pipeline that
uses JSON configuration (roughly modeled after orientdb-etl) to
translate graph data between various persistent and in-memory
representations.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%check
python setup.py test
py.test -vv $(find projx -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv $(find projx -name '*.py')
popd
%endif

%files
%doc *.txt *.md *.ipynb docs/* site
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md *.ipynb docs/* site
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20150215
- Initial build for Sisyphus

