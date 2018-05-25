%define oname chameleon

Name: python-module-%oname.core
Version: 3.1
Release: alt1.2

Summary: Chameleon Template Compiler
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
# https://github.com/malthe/chameleon.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-alabaster python-module-docutils
BuildRequires: python-module-setuptools time
BuildRequires: python-module-html5lib python-module-objects.inv

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildPreReq: python3-module-setuptools


%description
Attribute language template compiler.

%package -n python3-module-%oname.core
Summary: Chameleon Template Compiler (Python 3)
Group: Development/Python3

%description -n python3-module-%oname.core
Attribute language template compiler.

%package -n python3-module-%oname.core-tests
Summary: Tests for Chameleon Template Compiler (Python 3)
Group: Development/Python3
Requires: python3-module-%oname.core = %version-%release

%description -n python3-module-%oname.core-tests
Attribute language template compiler.

This package contains tests for Chameleon Template Compiler.

%package tests
Summary: Tests for Chameleon Template Compiler
Group: Development/Python
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

rm -rf ../python3
cp -a . ../python3

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd

%make pickle
%make html

%install
%python_install

pushd ../python3
%python3_install
popd

cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

pushd ../python3
python3 setup.py test
popd

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc _build/html/*

%files -n python3-module-%oname.core
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname.core-tests
%python3_sitelibdir/%oname/tests


%changelog
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

