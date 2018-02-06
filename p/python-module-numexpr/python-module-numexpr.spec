%define oname numexpr

%def_with python3

Name:           python-module-%oname
Version:        2.6.2
Release:        alt2
Epoch: 1
Summary:        Fast numerical array expression evaluator for Python and NumPy
Group:          Development/Python
License:        MIT
URL:            https://github.com/pydata/numexpr
# https://github.com/pydata/numexpr.git
Source:         %oname-%version.tar.gz
Source1: site.cfg
Patch1: %oname-%version-alt-config.patch

BuildRequires: gcc-c++ time libnumpy-devel liblapack-devel python-module-html5lib python-module-numpy-testing python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing python3-module-setuptools
%endif

Requires: %name-tests = %epoch:%version-%release /proc
%py_requires numpy


%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

Also, numexpr has support for the Intel VML (Vector Math Library) --
integrated in Intel MKL (Math Kernel Library) --, allowing nice
speed-ups when computing transcendental functions (like trigonometrical,
exponentials...) on top of Intel-compatible platforms. This support also
allows to use multiple cores in your computations.

%package -n python3-module-%oname
Summary: Fast numerical array expression evaluator for Python and NumPy
Group: Development/Python3
Requires: python3-module-%oname-tests = %epoch:%version-%release /proc
%py3_requires numpy

%description -n python3-module-%oname
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

Also, numexpr has support for the Intel VML (Vector Math Library) --
integrated in Intel MKL (Math Kernel Library) --, allowing nice
speed-ups when computing transcendental functions (like trigonometrical,
exponentials...) on top of Intel-compatible platforms. This support also
allows to use multiple cores in your computations.

%package -n python3-module-%oname-tests
Summary: Tests for numexpr
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release

%description -n python3-module-%oname-tests
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

Also, numexpr has support for the Intel VML (Vector Math Library) --
integrated in Intel MKL (Math Kernel Library) --, allowing nice
speed-ups when computing transcendental functions (like trigonometrical,
exponentials...) on top of Intel-compatible platforms. This support also
allows to use multiple cores in your computations.

This package contains tests for numexpr.

%package tests
Summary: Tests for numexpr
Group: Development/Python
Requires: %name = %epoch:%version-%release

%description tests
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

Also, numexpr has support for the Intel VML (Vector Math Library) --
integrated in Intel MKL (Math Kernel Library) --, allowing nice
speed-ups when computing transcendental functions (like trigonometrical,
exponentials...) on top of Intel-compatible platforms. This support also
allows to use multiple cores in your computations.

This package contains tests for numexpr.

%prep
%setup
%patch1 -p1
install -p -m644 %SOURCE1 ./
sed -i 's|@LIBDIR@|%_libdir|' site.cfg
%ifnarch %ix86 x86_64
sed -i 's@ openblas,@ blas,@' site.cfg
%endif
%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|@PYVER@|%_python3_version%_python3_abiflags|' \
	../python3/site.cfg
%endif

sed -i 's|@PYVER@|%_python_version|' site.cfg

%build
%add_optflags -fno-strict-aliasing
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
pushd build/lib.linux*
python -c 'import numexpr; numexpr.test()'
popd
%if_with python3
pushd ../python3
pushd build/lib.linux*
PYTHONPATH=%buildroot%python3_sitelibdir python3 -c 'import numexpr; numexpr.test()'
popd
popd
%endif

%files
%doc *.txt *.rst LICENSES
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst LICENSES
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Tue Feb 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.2-alt2
- fix build on arm

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.6.2-alt1
- Updated to upstream release 2.6.2

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.4.4-alt1.dev0.git20150815.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.4.4-alt1.dev0.git20150815.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.4-alt1.dev0.git20150815
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.4-alt1.dev0.git20150427
- Version 2.4.4.dev0

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.1-alt1.git20141130
- Version 2.4.1

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt2.hg20140104
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt1.hg20140104
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt1.hg20130908
- Version 2.3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.hg20121113
- New snapshot

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.hg20120301
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1-alt1.hg20111127.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.hg20111127
- Version 2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1.svn20110225.1
- Rebuild with Python-2.7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20110225
- New snapshot

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20101116.1
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20101116
- Version 1.5

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100615.1
- Fixed underlinking

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100615
- Initial build for Sisyphus

