Name: python-module-aiodns
Version: 1.1.1
Release: alt1
License: BSD
Group: Development/Python
Summary: Asynchronous DNS resolutions
Source0: https://pypi.python.org/packages/3b/45/dcee156eabca900af3a1bab8acb9531636b13db4b677d44ba468a43969e0/aiodns-%{version}.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python3-devel python3-module-setuptools
%py_requires trollius

%description
Aiodns provides a simple way for doing asynchronous DNS resolutions with
a synchronous looking interface by using pycares.

%package -n python3-module-aiodns
BuildArch: noarch
Group: Development/Python3
Summary: Asynchronous DNS resolutions

%description -n python3-module-aiodns
Aiodns provides a simple way for doing asynchronous DNS resolutions with
a synchronous looking interface by using pycares.

%prep
%setup -q -n aiodns-%{version}

%build
%python_build -b build2
%python3_build -b build3

%install
rm -f build && ln -s build2 build && %python_install
rm -f build && ln -s build3 build && %python3_install

%files
%python_sitelibdir_noarch/*

%files -n python3-module-aiodns
%python3_sitelibdir_noarch/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1
- Drop tests (did not run actually)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20141207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20141207.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141207
- Initial build for Sisyphus


