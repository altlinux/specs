%define oname networkx

%def_enable docs

Name:           python-module-%oname
Version:        1.7
Release:        alt1.hg20111126
Summary:        Creates and Manipulates Graphs and Networks
Group:          Development/Python
License:        LGPLv2+
URL:            https://networkx.lanl.gov/trac
# hg clone http://networkx.lanl.gov/hg/networkx
Source:         %oname-%version.tar.gz
BuildArch:      noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel
BuildPreReq: python-module-pygraphviz ipython libnumpy-devel
BuildPreReq: python-module-pydot python-module-matplotlib
BuildPreReq: python-module-yaml python-module-scipy python-module-pyparsing
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: graphviz

Requires: python-module-pygraphviz ipython python-module-numpy
Requires: python-module-pydot python-module-matplotlib
Requires: python-module-yaml python-module-scipy
Requires: %name-tests = %version-%release
%add_python_req_skip tests

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%if_enabled docs

%package docs
Summary: Documentation for NetworkX
Group: Development/Documentation
BuildArch: noarch

%description docs
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains development documentation for NetworkX.

%package pickles
Summary: Pickles for NetworkX
Group: Development/Python

%description pickles
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains pickles for NetworkX.

%endif

%package tests
Summary: Tests for NetworkX
Group: Development/Python
Requires: %name = %version-%release

%description tests
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains tests for NetworkX.

%prep
%setup
chmod -x examples/*/*.py
chmod -x examples/*/*.bz2
sed -i '1,1d' networkx/tests/test.py
%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

%build
%python_build_debug
#pushd nose_plugin
#python_build
#popd

%install
%python_install -O1
#pushd nose_plugin
#python_install -O1
#popd

%if_enabled docs
export PYTHONPATH=$PYTHONPATH:%buildroot%python_sitelibdir
#make -C doc latex ||:
#cp doc/build/doctrees/reference/credits.doctree \
#	doc/build/doctrees/
%make -C doc html

mv %buildroot%_docdir/%oname-%{version}* ./installed-docs

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*.egg-info
#exclude %python_sitelibdir/networkxdoctest.py*
%if_enabled docs
%exclude %python_sitelibdir/%oname/pickle
%endif
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
#python_sitelibdir/networkxdoctest.py*
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_enabled docs

%files docs
%doc installed-docs/*
%doc doc/build/html

%files pickles
%python_sitelibdir/%oname/pickle

%endif

%changelog
* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.hg20111126
- Version 1.7

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.svn20100829
- Enabled docs (except pdf)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.svn20100829.2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.2
- Fixed build

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829.1
- Rebuilt with python-module-sphinx-devel

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100829
- Version 1.4

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20100505
- Version 1.2

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306.1
- Added docs and pickles packages

* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20100306
- Version 1.1
- Exatracted tests into separate package

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004.1
- Rebuilt with python 2.6

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20091004
- Initial build for Sisyphus

* Tue Mar 24 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-3
- Replace __python macros with direct python invocations.
- Disable checks for now.
- Replace a define with global.

* Thu Mar 12 2009 Conrad Meyer <konrad@tylerc.org> - 0.99-2
- License is really LGPLv2+.
- Include license as documentation.
- Add a check section to run tests.

* Sat Dec 13 2008 Conrad Meyer <konrad@tylerc.org> - 0.99-1
- Initial package.
