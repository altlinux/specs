%define oname numexpr
Name:           python-module-%oname
Version:        2.0.2
Release:        alt1.hg20120301
Epoch: 1
Summary:        Fast numerical array expression evaluator for Python and NumPy
Group:          Development/Python
License:        MIT
URL:            http://code.google.com/p/numexpr/
# hg clone https://code.google.com/p/numexpr/
Source:         %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel gcc-c++
BuildPreReq: libnumpy-devel python-module-setuptools

Requires: %name-tests = %epoch:%version-%release

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

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc *.txt LICENSES
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%changelog
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

