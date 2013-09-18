%define oname networkx

%def_disable docs
%def_with python3

Name:           python-module-%oname
Version:        1.9
Release:        alt1.git20130915
Summary:        Creates and Manipulates Graphs and Networks
Group:          Development/Python
License:        LGPLv2+
URL:            https://networkx.lanl.gov/trac
# https://github.com/networkx/networkx.git
Source:         %oname-%version.tar.gz
BuildArch:      noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel
BuildPreReq: python-module-pygraphviz ipython libnumpy-devel
BuildPreReq: python-module-pydot python-module-matplotlib
BuildPreReq: python-module-yaml python-module-scipy python-module-pyparsing
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif

Requires: python-module-pygraphviz ipython python-module-numpy
Requires: python-module-pydot python-module-matplotlib
Requires: python-module-yaml python-module-scipy
Requires: %name-tests = %version-%release
%add_python_req_skip tests

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%if_with python3
%package -n python3-module-%oname
Summary: Creates and Manipulates Graphs and Networks (Python 3)
Group: Development/Python3
Requires: python3-module-%oname-tests = %version-%release
%add_python3_req_skip tests

%description -n python3-module-%oname
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-module-%oname-tests
Summary: Tests for NetworkX (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

This package contains tests for NetworkX.
%endif

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

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_enabled docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx .
%endif

%build
%python_build_debug
#pushd nose_plugin
#python_build
#popd

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%python_install -O1
#pushd nose_plugin
#python_install -O1
#popd

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_enabled docs
export PYTHONPATH=$PYTHONPATH:%buildroot%python_sitelibdir
#make -C doc latex ||:
#cp doc/build/doctrees/reference/credits.doctree \
#	doc/build/doctrees/
%make -C doc html

mkdir installed-docs
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
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
#python_sitelibdir/networkxdoctest.py*
%python_sitelibdir/*/tests
%python_sitelibdir/*/testing
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_enabled docs

%files docs
%doc installed-docs/*
%doc doc/build/html

%files pickles
%python_sitelibdir/%oname/pickle

%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/testing
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/testing
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1.git20130915
- Version 1.9

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt3.git20130303
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2.git20130303
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8-alt1.hg20120708.1
- Rebuild with Python-3.3

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.hg20120708
- Version 1.8
- Added module for Python 3
- Disabled docs

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
