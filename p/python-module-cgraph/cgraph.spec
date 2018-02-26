%define oname cgraph
Name: python-module-%oname
Version: 20110131
Release: alt1.1
Summary: High performance Directed Acyclic Graph implemented in Cython
License: Free
Group: Development/Python
Url: https://github.com/enthought/graph
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/graph.git
Source: %name-%version.tar

BuildPreReq: python-module-Cython

%description
The cgraph module is a high performance Directed Acyclic Graph
implemented in Cython. Expect graph traversals to be several hundred to
thousands of times faster than Networkx for large graphs. Graph's with
several hundred thousand nodes are handled with aplomb. That said, the
cgraph module doesn't have near the features of Networkx. The module is
designed solely for efficiently building, traversing, reversing, and
introspecting large graphs. A graph theory library it is not. Most of
the graph methods return iterators so that large graphs may be
efficiently managed by user code.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 20110131-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110131-alt1
- Initial build for Sisyphus

