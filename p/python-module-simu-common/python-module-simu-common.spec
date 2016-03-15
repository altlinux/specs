%define module_name simu-common

%def_with python3

Name: python-module-%module_name
Version: 0.1
Release: alt1.git20120629.1

Summary: common library that are reused by Star2Billing

License: GPLv3
Group: Development/Python
Url: https://github.com/Star2Billing/simu-common.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

%description
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%package -n python3-module-%module_name
Summary: common library that are reused by Star2Billing
Group: Development/Python3

%description -n python3-module-%module_name
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%prep
%setup

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
%doc README* LICENSE
%python_sitelibdir/common*
%python_sitelibdir/simu_common*

%if_with python3
%files -n python3-module-%module_name
%doc README* LICENSE
%python3_sitelibdir/common*
%python3_sitelibdir/simu_common*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20120629.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120629
- New snapshot
- Added module for Python 3

* Fri Apr 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- Initial build for ALT Linux
