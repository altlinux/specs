%global pypi_name betamax
%def_disable check

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt2
Summary: VCR imitation for python-requests

Group: Development/Python3
License: Apache-2.0 or BSD
Url: https://github.com/sigmavirus24/betamax
Source: %pypi_name-%version.tar.gz
Patch: betamax-system-urllib3.patch

BuildArch: noarch

BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-module-requests

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests\
much easier.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test -v

%files
%doc README.rst LICENSE
%python3_sitelibdir/*

%changelog
* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Drop python2 support.

* Mon Apr 22 2019 Ivan A. Melnikov <iv@altlinux.org> 0.8.1-alt1
- 0.8.1

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
