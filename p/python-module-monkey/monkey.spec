%define oname monkey

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: A package that provides tools for guerilla (monkey)-patching
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/monkey/
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
Provides tools for guerilla (monkey)-patching.

The package provides two methods, patch and wrap, that are used to
decorate the patch method.

Patching is only allowed if a signature on the original method is
provided. Multiple signatures can be provided corresponding to various
bona fide versions of the method.

%package -n python3-module-%oname
Summary: A package that provides tools for guerilla (monkey)-patching
Group: Development/Python3

%description -n python3-module-%oname
Provides tools for guerilla (monkey)-patching.

The package provides two methods, patch and wrap, that are used to
decorate the patch method.

Patching is only allowed if a signature on the original method is
provided. Multiple signatures can be provided corresponding to various
bona fide versions of the method.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

