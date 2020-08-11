%define _unpackaged_files_terminate_build 1

%define oname sympy

%def_with doc

Name: python-module-%oname
Epoch: 1
Version: 1.1.1
Release: alt2

Summary: A Python library for symbolic mathematics
License: BSD-3-Clause
Group: Development/Python

Url: http://sympy.org/
# https://github.com/sympy/sympy.git

Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-py python-module-setuptools
BuildRequires: python-module-numpy python-module-mpmath
BuildRequires: dvipng ImageMagick-tools graphviz librsvg-utils
%if_with doc
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-docutils
BuildRequires: python-module-Pygments
%endif

Requires: %name-tests = %EVR
%add_python_req_skip primetest pytest runtests
%setup_python_module %oname

%description
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains python module of SymPy.

%package examples
Summary: Examples for SymPy
Group: Development/Documentation
Requires: %name = %EVR

%description examples
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains examples for SymPy.

%package tests
Summary: Tests for SymPy
Group: Development/Python
Requires: %name = %EVR

%description tests
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains tests for SymPy.

%package pickles
Summary: Pickles for SymPy
Group: Development/Python

%description pickles
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains pickles for SymPy.

%package doc
Summary: Documentation for SymPy
Group: Development/Documentation
BuildArch: noarch

%description doc
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains development documentation for SymPy.

%prep
%setup
%patch1 -p1

for i in $(find ./ -name tests); do
	touch $i/__init__.py
done

sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%if_with doc
%prepare_sphinx .
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build

%if_with doc
pushd doc
%make html
popd

rm -fR doctrees
cp -fR doc/_build/doctrees doc/src/
export PYTHONPATH=$PYTHONPATH:$PWD
cp -fR doc/_build/doctrees ./

%generate_pickles $PWD $PWD/doc/_build/html %oname
%endif

%install
%python_install

rm -f %buildroot%python_sitelibdir/%oname/mpmath/libmp/exec_py3.py

%if_with doc
cp -fR pickle %buildroot%python_sitelibdir/%oname/
%endif

rm -rf %buildroot%_bindir
rm -rf %buildroot%_man1dir

%check
#python setup.py test -v
#python bin/test -v
%if_with doc
python bin/doctest -v ||:
%endif

%files
%doc AUTHORS LICENSE README*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*test*
%if_with doc
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/*/*test*
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/*test*

%files examples
%doc examples/*

%if_with doc
%files doc
%doc doc/_build/html/*
%endif

%changelog
* Tue Aug 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt2
- Built only python-2 module.

* Sat Apr 27 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1.1.1
- introduce doc knob (on by default)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.7-alt1.dev.git20150830.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.7-alt1.dev.git20150830
- New snapshot

* Fri May 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.7-alt1.dev.git20150430
- Version 0.7.7.dev

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.6-alt1.git20141120
- Version 0.7.6

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140814
- New snapshot
- Added module for Python 3

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140710
- New snapshot

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140609
- Version 0.7.5

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.3-alt1.git20131118
- New snapshot

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.3-alt1.git20130725
- Version 0.7.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:0.7.2-alt1.git20130210.1
- Rebuild with Python-3.3

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.2-alt1.git20130210
- Version 0.7.2

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120623
- New snapshot
- Applied repocop patch

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120511
- New snapshot
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120124
- Version 0.7.1

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt2.git20110405
- Enabled docs

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.6.7-alt1.git20110405.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20110405
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102.2
- Rebuilt with python-module-sphinx-devel

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102.1
- Fixed bad imports from tests

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102
- New snapshot
- Corrected version number

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.svn20100302
- Version 0.7.0
- Extracted examples and tests into separate packages
- Added pickles packages

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt2
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus

