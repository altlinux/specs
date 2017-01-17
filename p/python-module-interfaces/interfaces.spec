%define _unpackaged_files_terminate_build 1
%define oname interfaces

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1
Summary: Simple decorator implementation of an interface
License: Apache v2
Group: Development/Python
Url: https://pypi.python.org/pypi/interfaces/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/eb/36/2976c3c99aa36ea5a50b60e4f8014a91c20c7561150564abdfd445cb2430/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
This library is a trivial implementation of an interface in Python,
with the following aspects / features:

* It fails at import time, not at construction, so you know
  immediately when you have a problem.
* It's quite simple (very few LOC) and lenient where it counts
* It exclusively uses decorators, so...
* It does not require inheritance (reducing 'forced' subclassing)
* It does not enforce any typing checks
* It is intended to 'enhance' duck typing by avoiding common
  pitfalls (forgot to implement something on your fake duck class,
  overwrote something fundamental, etc.)

%package -n python3-module-%oname
Summary: Simple decorator implementation of an interface
Group: Development/Python3

%description -n python3-module-%oname
This library is a trivial implementation of an interface in Python,
with the following aspects / features:

* It fails at import time, not at construction, so you know
  immediately when you have a problem.
* It's quite simple (very few LOC) and lenient where it counts
* It exclusively uses decorators, so...
* It does not require inheritance (reducing 'forced' subclassing)
* It does not enforce any typing checks
* It is intended to 'enhance' duck typing by avoiding common
  pitfalls (forgot to implement something on your fake duck class,
  overwrote something fundamental, etc.)

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

