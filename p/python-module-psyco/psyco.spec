# -*- coding: utf-8 -*-
Summary: specializing compiler for Python code
Summary(ru_RU.UTF-8): "JIT-компилятор" для программ на Python
%define modulename psyco
Name: python-module-%modulename
Version: 1.6
Release: alt2.svn20100222

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://codespeak.net/svn/psyco/branch/py27/
Source: %modulename-%version-src.tar.bz2
Source1: Makefile
License: MIT
Group: Development/Python
Url: http://psyco.sf.net
ExclusiveArch: %ix86

BuildPreReq: python-devel rpm-build-python latex2html
#BuildPreReq: texlive-latex-extra texlive-fonts-recommended
BuildPreReq: python-doc-tools
BuildPreReq: ghostscript-utils
# Automatically added by buildreq on Sun Oct 02 2005 (-bi)
BuildRequires: python-base python-modules-compiler python-modules-email
BuildPreReq: python-modules-encodings python-modules-logging

%description
Psyco is a kind of just-in-time (JIT) compiler,
a little bit like Java's, that emits machine code on the fly
instead of interpreting your Python program step by step.
The result is that your unmodified Python programs run faster.

This module is built for python %_python_version.

%description -l ru_RU.UTF-8
Psyco - это "JIT-компилятор" для программ на языке Python,
который генерирует на лету машинный код, вместо того чтобы
шаг за шагом интерпретировать программу. В результате
программы на Python выполняются быстрее без изменений 
в исходном коде.

Этот модуль собран для Python версии %_python_version.

%package tests
Summary: Tests for Psyco
Group: Development/Python
Requires: %name = %version-%release

%description tests
Psyco is a kind of just-in-time (JIT) compiler,
a little bit like Java's, that emits machine code on the fly
instead of interpreting your Python program step by step.
The result is that your unmodified Python programs run faster.

This package contains tests for Psyco.

%package doc
Summary: Documentation for Psyco
Group: Development/Documentation

%description doc
Psyco is a kind of just-in-time (JIT) compiler,
a little bit like Java's, that emits machine code on the fly
instead of interpreting your Python program step by step.
The result is that your unmodified Python programs run faster.

This package contains documentation for Psyco.

%prep
%setup
cp -f %SOURCE1 doc/

%build
%add_optflags -fno-strict-aliasing
export TEXINPUT=/usr/share/python-doc-tools/tools/texinputs
%python_build_debug

%install
%python_install --optimize 2

# doc

#export PYTHONPATH=%buildroot%python_sitelibdir
#make -C doc default
make -C doc html

#install -d %buildroot%_docdir/%name/pdf
install -d %buildroot%_docdir/%name/html
install -d %buildroot%_docdir/%name/test

#install -p -m644 doc/*.pdf %buildroot%_docdir/%name/pdf
install -p -m644 doc/psycoguide/* %buildroot%_docdir/%name/html
install -p -m644 COPYING.txt README.txt %buildroot%_docdir/%name/

# tests

cp -fR test %buildroot%python_sitelibdir/%modulename/
touch %buildroot%python_sitelibdir/%modulename/test/__init__.py
rm -f %buildroot%python_sitelibdir/%modulename/test/pystone-jit.py \
	%buildroot%python_sitelibdir/%modulename/test/btrun.py \
	%buildroot%python_sitelibdir/%modulename/test/test_base.py \
	%buildroot%python_sitelibdir/%modulename/test/test_base.py \

%files
%doc %dir %_docdir/%name
%doc %_docdir/%name/README.txt
%doc %_docdir/%name/COPYING.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files doc
%doc %dir %_docdir/%name
#doc %_docdir/%name/pdf
%doc %_docdir/%name/html

%files tests
%python_sitelibdir/*/test

%changelog
* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20100222
- Rebuilt with updated NumPy
- Disabled pdf

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20100215.1
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20100215
- New snapshot
- Fixed underlinking

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20091218.1
- Rebuilt without texmf-latex-python

* Fri Feb 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.svn20091218
- Rebuilt from git-svn
- Added documentation and tests without very long (test_doctest,
  test_zipimport_support) and broken (test_pyexpat)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Fr. Br. George <george@altlinux.ru> 1.6-alt1.1
- Psyco doesn't support non-i586 platforms

* Tue Feb 26 2008 Grigory Batalov <bga@altlinux.ru> 1.6-alt1
- New upstream release.
- Rebuild with python-2.5.

* Mon Jun 12 2006 Alex V. Myltsev <avm@altlinux.ru> 1.5.1-alt1
- Version 1.5.1: bug fixes, faster new-style class instantiation.

* Tue Nov 01 2005 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt1
- Version 1.5, latest and probably last.

* Mon Oct 03 2005 Alex V. Myltsev <avm@altlinux.ru> 1.4-alt2.svn18103
- Latest revision from Subversion.

* Sun Mar 20 2005 Alex V. Myltsev <avm@altlinux.ru> 1.4-alt1
- Initial build for Sisyphus.

