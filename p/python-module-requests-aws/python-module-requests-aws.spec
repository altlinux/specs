%define oname requests-aws

%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1.1
Summary: AWS authentication for Amazon S3 for the python requests module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-aws/

# https://github.com/tax/python-requests-aws.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
AWS authentication for Amazon S3 for the wonderful pyhon requests library.

%package -n python3-module-%oname
Summary: AWS authentication for Amazon S3 for the python requests module
Group: Development/Python3

%description -n python3-module-%oname
AWS authentication for Amazon S3 for the wonderful pyhon requests library.

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu May 21 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- Initial build for Sisyphus
