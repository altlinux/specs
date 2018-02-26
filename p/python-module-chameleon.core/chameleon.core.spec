%define oname chameleon

%def_with python3

Name: python-module-%oname.core
Version: 2.8.4
Release: alt1.git20120501
Summary: Chameleon Template Compiler
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/malthe/chameleon.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
Attribute language template compiler.

%if_with python3
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
%endif

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
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif

%make pickle
%make html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/

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

%if_with python3
%files -n python3-module-%oname.core
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname.core-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
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

