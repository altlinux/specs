%define module_name pygraphviz

Name: python-module-%module_name
Version: 0.99.1
Release: alt1.3.1.1

Summary: Python wrapper for the Graphviz Agraph data structure

License: BSD
Group: Development/Python
Url: http://networkx.lanl.gov/pygraphviz
Packager: Denis Klimov <zver@altlinux.org>

Source: %module_name-%version.tar

BuildRequires: libgraphviz-devel

%setup_python_module %module_name


%description
Python wrapper for the Graphviz Agraph data structure.
It can be used to create and draw networks and graphs with Graphviz.

%prep
%setup -n %module_name-%version

%build
%python_build_debug

%install
%python_build_install

%files
%python_sitelibdir/*
%_datadir/doc/%module_name-%version

%changelog
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

