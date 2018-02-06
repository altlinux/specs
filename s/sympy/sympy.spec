%def_with python3

Name: sympy
Version: 1.1.1
Epoch: 1
Release: alt1.1
Summary: A Python library for symbolic mathematics
License: New BSD License
Group: Sciences/Mathematics
BuildArch: noarch
Url: http://sympy.org/

# https://github.com/sympy/sympy.git
Source: %name-%version.tar

Patch1: %name-%version-alt-build.patch

Requires: python-module-%name = %EVR

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-py python-module-setuptools
BuildRequires: dvipng python-module-sphinx-devel python-module-Pygments
BuildRequires: python-module-docutils python-module-numpy librsvg-utils
BuildRequires: python-module-mpmath
BuildRequires: ImageMagick-tools graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-py python-tools-2to3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-mpmath
%endif

%add_python3_req_skip py.__.test.item py.__.test.terminal.terminal

%description
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

%if_with python3
%package py3
Summary: A Python 3 library for symbolic mathematics
Group: Development/Python3
Requires: python3-module-%name = %EVR

%description py3
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

%package -n python3-module-%name
Summary: A Python 3 module for symbolic mathematics
Group: Development/Python3
Requires: python3-module-%name-tests = %EVR
%add_python3_req_skip primetest pytest runtests

%description -n python3-module-%name
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains python module of SymPy.

%package -n python3-module-%name-tests
Summary: Tests for SymPy (Python 3)
Group: Development/Python3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-tests
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains tests for SymPy.
%endif

%package -n python-module-%name
Summary: A Python module for symbolic mathematics
Group: Development/Python
Requires: python-module-%name-tests = %EVR
%add_python_req_skip primetest pytest runtests
%setup_python_module %name

%description -n python-module-%name
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains python module of SymPy.

%package -n python-module-%name-examples
Summary: Examples for SymPy
Group: Development/Documentation
Requires: python-module-%name = %EVR

%description -n python-module-%name-examples
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains examples for SymPy.

%package -n python-module-%name-tests
Summary: Tests for SymPy
Group: Development/Python
Requires: python-module-%name = %EVR

%description -n python-module-%name-tests
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains tests for SymPy.

%package -n python-module-%name-pickles
Summary: Pickles for SymPy
Group: Development/Python

%description -n python-module-%name-pickles
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains pickles for SymPy.

%package -n python-module-%name-doc
Summary: Documentation for SymPy
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-%name-doc
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
%prepare_sphinx .

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

pushd doc
%make html
popd

rm -fR doctrees
cp -fR doc/_build/doctrees doc/src/
export PYTHONPATH=$PYTHONPATH:$PWD
cp -fR doc/_build/doctrees ./

%generate_pickles $PWD $PWD/doc/_build/html %name

%install
%if_with python3
pushd ../python3
%python3_install
popd

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd

pushd %buildroot%_man1dir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

rm -f %buildroot%python_sitelibdir/%name/mpmath/libmp/exec_py3.py
rm -f %buildroot%python3_sitelibdir/%name/mpmath/libmp/exec_py2.py

cp -fR pickle %buildroot%python_sitelibdir/%name/

%check
#python setup.py test -v
#python bin/test -v
python bin/doctest -v ||:

%if_with python3
pushd ../python3
#python3 setup.py test -v
#python3 bin/test -v
python3 bin/doctest -v ||:
popd
%endif

%files
%doc AUTHORS LICENSE README*
%_bindir/*
%_man1dir/*
%if_with python3
%exclude %_bindir/py3_*
%exclude %_man1dir/py3_*
%endif

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/%name/pickle
%exclude %python_sitelibdir/*/*test*
%exclude %python_sitelibdir/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*test*

%files -n python-module-%name-pickles
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/pickle

%files -n python-module-%name-tests
%python_sitelibdir/*/*test*
%python_sitelibdir/*/*/*test*
%python_sitelibdir/*/*/*/*test*

%files -n python-module-%name-examples
%doc examples/*

%files -n python-module-%name-doc
%doc doc/_build/html/*

%if_with python3
%files py3
%doc AUTHORS LICENSE README*
%_bindir/py3_*
%_man1dir/py3_*

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test*
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*/*test*

%files -n python3-module-%name-tests
%python3_sitelibdir/*/*test*
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%python3_sitelibdir/*/*/*/*/*test*
%endif

%changelog
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

