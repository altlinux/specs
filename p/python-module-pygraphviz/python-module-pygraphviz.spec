%define module_name pygraphviz

%def_with python3

Name: python-module-%module_name
Version: 1.3
Release: alt2.git20140720

Summary: Python wrapper for the Graphviz Agraph data structure

License: BSD
Group: Development/Python
Url: http://networkx.lanl.gov/pygraphviz
Packager: Denis Klimov <zver@altlinux.org>

Source: %module_name-%version.tar

BuildRequires: libgraphviz-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3 swig
%endif

%setup_python_module %module_name
%add_python_req_skip tests

%description
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

%package tests
Summary: Tests for %module_name
Group: Development/Python
Requires: %name = %version-%release
%add_python3_req_skip tests

%description tests
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

This package contains tests for %module_name.

%if_with python3
%package -n python3-module-%module_name
Summary: Python 3 wrapper for the Graphviz Agraph data structure
Group: Development/Python3

%description -n python3-module-%module_name
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

%package -n python3-module-%module_name-tests
Summary: Tests for %module_name (Python 3)
Group: Development/Python3
Requires: python3-module-%module_name = %version-%release

%description -n python3-module-%module_name-tests
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

This package contains tests for %module_name.
%endif

%prep
%setup -n %module_name-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -I%_includedir/graphviz

sed -i 's|@PY2@||' pygraphviz/graphviz.i
sed -i 's|@PY3@.*||' pygraphviz/graphviz.i
%python_build_debug

%if_with python3
pushd ../python3
rm -f %module_name/graphviz_wrap.c %module_name/graphviz.py
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|UserDict\.DictMixin|collections.MutableMapping|' \
	%module_name/agraph.py
sed -i 's|import UserDict|import collections|' \
	%module_name/agraph.py
sed -i 's|@PY2@.*||' pygraphviz/graphviz.i
sed -i 's|@PY3@||' pygraphviz/graphviz.i
swig -python -py3 %module_name/graphviz.i
%python3_build_debug
popd
%endif

%install
%python_build_install
%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%_datadir/doc/%module_name-%version.dev

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%module_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.3-alt2.git20140720
- Fix graphviz.i

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140720
- Version 1.3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn20120328
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt1.svn20120328.1
- Rebuild with Python-3.3

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20120328
- Version 1.2
- Extracted tests into separate package
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.99.1-alt1.3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.99.1-alt1.3.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.99.1-alt1.3
- NMU: rebuilt with current graphviz

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1-alt1.2
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.1-alt1.1
- Rebuilt with python 2.6

* Thu Jan 22 2009 Denis Klimov <zver@altlinux.org> 0.99.1-alt1
- Initial build for ALT Linux

