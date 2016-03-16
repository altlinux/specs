%define oname twill

%def_with python3

Name: python-module-%oname
Version: 1.8.0
Release: alt2.1
Summary: twill Web browsing language
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/twill/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

%package tests
Summary: Tests for twill
Group: Development/Python
Requires: %name = %EVR

%description tests
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

This package contains tests for twill.

%package -n python3-module-%oname
Summary: twill Web browsing language
Group: Development/Python3

%description -n python3-module-%oname
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

%package -n python3-module-%oname-tests
Summary: Tests for twill
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

This package contains tests for twill.

%package docs
Summary: Documentation for twill
Group: Development/Documentation

%description docs
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

This package contains documentation and examples for twill.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n twill-fork
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc README*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

#files docs
#doc doc/* examples

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

