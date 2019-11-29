%define oname zope.structuredtext

Name: python3-module-%oname
Version: 4.1.1
Release: alt2

Summary: StructuredText parser
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.structuredtext/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nosexcover python3-module-coverage

%py3_requires zope


%description
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation

%package tests
Summary: Tests for StructuredText parser
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation

This package contains tests for StructuredText parser.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%check
%__python3 setup.py test -v
nosetests3 -vv --with-xunit --with-xcoverage

%files
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/examples*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/examples*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150203.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150203.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150203
- Version 4.1.1.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

