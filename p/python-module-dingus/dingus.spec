%define oname dingus

%def_with python3

Name: python-module-%oname
Version: 0.3.4
Release: alt1.1
Summary: A record-then-assert mocking library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dingus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A dingus is sort of like a mock object. The main difference is that you
don't set up expectations ahead of time. You just run your code, using a
dingus in place of another object or class, and it will record what
happens to it. Then, once your code has been exercised, you can make
assertions about what it did to the dingus.

%package -n python3-module-%oname
Summary: A record-then-assert mocking library
Group: Development/Python3

%description -n python3-module-%oname
A dingus is sort of like a mock object. The main difference is that you
don't set up expectations ahead of time. You just run your code, using a
dingus in place of another object or class, and it will record what
happens to it. Then, once your code has been exercised, you can make
assertions about what it did to the dingus.

%prep
%setup

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

