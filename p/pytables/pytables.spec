%define descr PyTables is a package for managing hierarchical datasets and designed \
to efficiently and easily cope with extremely large amounts of data. \
\
PyTables is built on top of the HDF5 library, using the Python language \
and the NumPy package (it also supports numarray and Numeric right \
out-of-the-box). It features an object-oriented interface that, combined \
with C extensions for the performance-critical parts of the code \
(generated using Pyrex), makes it a fast, yet extremely easy to use tool \
for interactively dealing with, processing and searching very large \
amounts of data. One important feature of PyTables is that it optimizes \
memory and disk resources so that data takes much less space (specially \
if on-flight compression is used) than other solutions such as \
relational or object oriented databases.

%define oname tables

# Tests fail on armh
%ifarch armh
%def_disable check
%endif

#TODO: fix docs and bench

Name: py%oname
Version: 3.8.0
Release: alt1
Epoch: 1

Summary: Managing hierarchical datasets

License: MIT
Group: Development/Python3
Url: http://www.pytables.org/

VCS: https://github.com/PyTables/PyTables.git
Source: %name-%version.tar

# Patch from Debian
Patch1: 0004-remove-gtags.patch

Patch2: pytables-3.8.0-alt-fix-blosc2-get-directories.patch

Requires: python3-module-%oname = %EVR

BuildRequires: libhdf5-devel liblzo2-devel bzlib-devel
BuildRequires: xsltproc inkscape fop
BuildRequires: java-devel-default docbook-tldp-xsl docbook-dtds
BuildRequires: libblosc-devel
BuildRequires: libblosc2-devel

%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/nctoh5.py
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/make_hdf.py

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: python3-module-distribute python3-module-Cython
BuildRequires: python3-module-numexpr
BuildRequires: python3-module-mock
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-cpuinfo
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%descr

%package -n python3-module-%oname
Summary: Managing hierarchical datasets (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
%descr

This package contains python module of PyTables.

%package -n python3-module-%oname-tests
Summary: Tests and examples for PyTables (Python 3)
Group: Development/Python3
Requires: python3-module-pkg_resources
Requires: python3-module-numpy-testing
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
%descr

This package contains tests and examples for PyTables.

%package -n python3-module-%oname-bench
Summary: Benchmarks for PyTables (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-bench
%descr

This package contains benchmarks for PyTables.

%package doc
Summary: Documentation for PyTables
Group: Development/Documentation
BuildArch: noarch

%description doc
%descr

This package contains documentation for PyTables.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%add_optflags -fno-strict-aliasing
export NPY_NUM_BUILD_JOBS=%__nprocs
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make_build SPHINXBUILD="sphinx-build-3" -C doc pickle
%make_build SPHINXBUILD="sphinx-build-3" -C doc html

cp -fR doc/build/html %buildroot%_docdir/%name/
cp -fR examples %buildroot%_docdir/%name/
cp -fR bench contrib %buildroot%_docdir/%name/

%endif

install -d %buildroot%_docdir/%name/pdf
install -p -m644 LICENSE.txt README.rst RELEASE_NOTES.rst THANKS \
    %buildroot%_docdir/%name
cp -fR LICENSES %buildroot%_docdir/%name

%check
cd build/lib.* && env PYTHONPATH=. python3 tables/tests/test_all.py

%files
%_bindir/*

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests/

%files doc
%_docdir/%name

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests/

%changelog
* Mon Jan 16 2023 Anton Vyatkin <toni@altlinux.org> 1:3.8.0-alt1
- new version 3.8.0

* Tue Jan 11 2022 Grigory Ustinov <grenka@altlinux.org> 1:3.6.1-alt7
- Disable check for python3.10.

* Mon Apr 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.6.1-alt6
- Rebuilt with new libhdf5.

* Mon Apr 19 2021 Grigory Ustinov <grenka@altlinux.org> 1:3.6.1-alt5
- Fixed FTBFS.

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.6.1-alt4
- NMU: update buildreqs, build tests subpackage

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.6.1-alt3
- NMU: s/numexpr-tests/numexpr/
- NMU: don't package tests
- NMU: pack examples, bench and contrib if doc build

* Mon Aug 31 2020 Grigory Ustinov <grenka@altlinux.org> 1:3.6.1-alt2
- Remove mistaken obsoletes tag.

* Tue Feb 25 2020 Grigory Ustinov <grenka@altlinux.org> 1:3.6.1-alt1
- Build new version for python3.8.
- Build without python2 support.
- Build without docs.

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1:3.5.2-alt2
- disable build python2 submodules
- stop using obsoleted sqlite module

* Fri Jul 19 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.5.2-alt1
- Build new version.

* Tue Apr 09 2019 Grigory Ustinov <grenka@altlinux.org> 1:3.5.1-alt1
- Build new version for python3.7.

* Fri Mar 22 2019 Anton Farygin <rider@altlinux.ru> 1:3.4.2-alt2
- removed w3c-markup-validator-libs build dependency

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.4.2-alt1
- Updated to upstream release version 3.4.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:3.2.2-alt1.dev0.git20150828.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1.dev0.git20150828
- New snapshot

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2.2-alt1.dev0.git20150817
- Version 3.2.2.dev0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.2-alt1.dev.git20150418
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.2-alt1.dev.git20141012
- Version 3.1.2dev

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.1-alt3.git20140325
- Added module for Python 3

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.1-alt2.git20140325
- NMU: corrected java deps

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.1-alt1.git20140325
- Version 3.1.1

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt3.git20130601
- Rebuilt with updated NumPy

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt2.git20130601
- Rebuilt with new libhdf5

* Sun Jun 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt1.git20130601
- Version 3.0.0

* Tue Oct 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.0-alt2.git20120720
- Rebuilt with updated NumPy

* Thu Sep 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.0-alt1.git20120720
- Version 2.4.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20120613
- New snapshot
- Applied repocop patch

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20120318
- New snapshot

* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3.1-alt1.git20111114
- Version 2.3.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3b1-alt1.svn20110408.1.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20110408.1
- Rebuilt with libhdf5-7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20110408
- New snapshot

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20101118.1
- Rebuilt for debuginfo

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20101118
- New snapshot

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.3
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.2
- Fixed underlinking

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707.1
- Avoid requirement on RandomArray

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3b1-alt1.svn20100707
- Version 2.3b1
- Rebuilt with docbook-style-xsl 1.75.2

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b3-alt1.svn20100203
- Version 2.2b3

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.4
- Fixed creating some extensions
- Added docs, benchmarks and tests/examples

* Wed Feb 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.3
- Rebuilt with reformed NumPy

* Sat Jan 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.2
- Rebuilt without python-module-Numeric

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911.1
- Rebuilt with python 2.6

* Fri Sep 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2b2-alt1.svn20090911
- Initial build for Sisyphus
