%define _unpackaged_files_terminate_build 1
%define oname green

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.5.3
Release: alt1
Summary: Clean, colorful test runner for Python unit tests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/green/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/CleanCut/green.git
Source0: https://pypi.python.org/packages/d2/a7/f4525dac4cf86c3e445bf4579da82f0e0a78ffab669d477e0144800681f5/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-termstyle python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-termstyle
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pbr python-module-pytest python-module-unittest2 python3-module-pytest rpm-build-python3

%description
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Clean, colorful test runner for Python unit tests
Group: Development/Python3

%description -n python3-module-%oname
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *.md PKG-INFO
%_bindir/%oname
%_bindir/%{oname}2*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md PKG-INFO
%_bindir/%{oname}3*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.1-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1.git20141125
- Version 1.7.1

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.git20140826
- Initial build for Sisyphus

