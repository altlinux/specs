%define module_name simu-common

Name: python-module-%module_name
Version: 0.1
Release: alt1

Summary: common library that are reused by Star2Billing

License: GPLv3
Group: Development/Python
Url: https://github.com/Star2Billing/simu-common.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-distribute

%setup_python_module %module_name

%description
Dilla is a multi-purpose general testing tool for automated
database spamming, intented to use with projects built on top of Django,
populating data within any number of internal applications.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README* LICENSE
%python_sitelibdir/common*
%python_sitelibdir/simu_common*

%changelog
* Fri Apr 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- Initial build for ALT Linux
