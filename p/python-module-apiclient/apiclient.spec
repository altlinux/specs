%define oname apiclient

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1

Summary: Framework for making good API client libraries using urllib3
License: MIT
Group: Development/Python

Url: https://pypi.python.org/pypi/apiclient/

Source0: https://pypi.python.org/packages/b6/5e/08d11020ba6087be7352c8a1856d3a6601f9f1aa7ea434ef1c584b489325/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
%endif

%setup_python_module %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

%description
Framework for making good API client libraries using urllib3.

%package -n python3-module-%oname
Summary: Framework for making good API client libraries using urllib3
Group: Development/Python3

%description -n python3-module-%oname
Framework for making good API client libraries using urllib3.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.1
- NMU: Use buildreq for BR.

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

