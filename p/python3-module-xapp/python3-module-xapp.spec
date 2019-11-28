%define oname xapp

Name: python3-module-%oname
Version: 1.8.0
Release: alt1

Summary: Python Xapp Library

License: LGPLv2
Group: Development/Python
Url: https://github.com/linuxmint/python-xapp

Source: python-%oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Python Xapp Library

%prep
%setup -n python-%oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Tue Nov 19 2019 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version
- Remove Python 2 subpackage

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt1
- New version

* Thu Nov 1 2018 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- New version

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
