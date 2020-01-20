Name: python3-module-pyotp
Version: 2.3.0
Release: alt1

Summary: Python library for generating and verifying one-time passwords.
License: BSD
Group: Development/Python
Url: https://pypi.org/project/pyotp/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE* README.*
%python3_sitelibdir/pyotp
%python3_sitelibdir/pyotp-%version-*-info

%changelog
* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- initial
