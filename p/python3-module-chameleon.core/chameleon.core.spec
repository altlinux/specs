%define oname chameleon
%def_with check

Name: python3-module-%oname.core
Version: 3.10.2
Release: alt1

Summary: Chameleon Template Compiler
License: BSD
Group: Development/Python3
Url: http://chameleon.repoze.org/
# https://github.com/malthe/chameleon.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: time

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-sphinx_rtd_theme

%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%description
Attribute language template compiler.

%package tests
Summary: Tests for Chameleon Template Compiler
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Attribute language template compiler.

This package contains tests for Chameleon Template Compiler.

%package pickles
Summary: Pickles for Chameleon Template Compiler
Group: Development/Python

%description pickles
Attribute language template compiler.

This package contains pickles for Chameleon Template Compiler.

%package docs
Summary: Documentation for Chameleon Template Compiler
Group: Development/Documentation

%description docs
Attribute language template compiler.

This package contains documentation for Chameleon Template Compiler.

%prep
%setup

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" pickle
%make SPHINXBUILD="sphinx-build-3" html
cp -fR _build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%tox_check

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/pickle

%files tests
%python3_sitelibdir/%oname/tests

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc _build/html/*

%changelog
* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.2-alt1
- Automatically updated to 3.10.2.
- Build with check.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.1-alt1
- Build new version.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 3.8.1-alt1
- Build new version.
- Drop python2 support.

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt1.2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1
- Updated to upstream version 3.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.19-alt1.dev.git20141103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.19-alt1.dev.git20141103.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.19-alt1.dev.git20141103
- Version 2.19-dev
- Enabled testing

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.16-alt1.git20140506
- Version 2.16

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14-alt1.git20131128
- Version 2.14

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt2.git20130817
- Fixed build

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12-alt1.git20130817
- Version 2.12

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11-alt2.git20130114
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.11-alt1.git20130114.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11-alt1.git20130114
- Version 2.11

* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt1.git20120501
- Version 2.8.4

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1.git20120416
- Version 2.8.3
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.git20111208
- Version 2.6.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.rc8-alt1.git20110411.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.rc8-alt1.git20110411
- Initial build for Sisyphus

