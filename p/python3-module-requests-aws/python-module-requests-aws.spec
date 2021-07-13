%define oname requests-aws

Name: python3-module-%oname
Version: 0.1.6
Release: alt2
Summary: AWS authentication for Amazon S3 for the python requests module
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-aws/

# https://github.com/tax/python-requests-aws.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
AWS authentication for Amazon S3 for the wonderful pyhon requests library.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.6-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu May 21 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- Initial build for Sisyphus
