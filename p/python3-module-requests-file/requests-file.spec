Name: python3-module-requests-file
Version: 1.5.1
Release: alt1

Summary: Local filesystem access for Requests module
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/requests-file/

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
%python3_sitelibdir/requests_file.py
%python3_sitelibdir/*/requests_file.*.py?
%python3_sitelibdir/requests_file-%version-*-info

%changelog
* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- initial
