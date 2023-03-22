%define oname zope.structuredtext

%def_with check

Name: python3-module-%oname
Version: 4.4
Release: alt1

Summary: StructuredText parser
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.structuredtext
Vcs: https://github.com/zopefoundation/zope.structuredtext

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-sphinx
%endif

%description
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation.

%package tests
Summary: Tests for StructuredText parser
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation.

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
%tox_check

%files
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/zope
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/examples*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/examples*


%changelog
* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt3
- Fixed BuildRequires.

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

