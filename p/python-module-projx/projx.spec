%define oname projx

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.git20150215.1
Summary: Graph transformations in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/projx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davebshow/projx.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-networkx python-module-pyparsing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-networkx python3-module-pyparsing
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires networkx pyparsing

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-decorator python-module-future python-module-matplotlib python-module-mpmath python-module-networkx-core python-module-numpy python-module-pluggy python-module-py python-module-pydot python-module-pygraphviz python-module-pyparsing python-module-pytest python-module-scipy python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-decorator python3-module-matplotlib python3-module-networkx-core python3-module-numpy python3-module-pluggy python3-module-py python3-module-pydot python3-module-pygraphviz python3-module-pyparsing python3-module-pytest python3-module-scipy python3-module-setuptools python3-module-yaml xz
BuildRequires: python-module-networkx-drawing python-module-numpy-testing python-module-setuptools-tests python3-module-networkx-drawing python3-module-numpy-testing python3-module-setuptools-tests rpm-build-python3 time

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1.git20150215.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1.git20150215
- Initial build for Sisyphus

