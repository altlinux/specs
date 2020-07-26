Name: python3-module-gpsoauth
Version: 0.4.1
Release: alt1

Summary: Python API for google play services oauth
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gpsoauth/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: python3(requests) python3(Crypto) python3(pytest)

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 gpsoauth/tests.py

%files
%python3_sitelibdir/gpsoauth
%python3_sitelibdir/gpsoauth-%version-*-info

%changelog
* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- initial
