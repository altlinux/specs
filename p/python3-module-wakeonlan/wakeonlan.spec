Name: python3-module-wakeonlan
Version: 2.0.1
Release: alt1

Summary: Python WOL implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wakeonlan/

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
%python3_sitelibdir/wakeonlan.py
%python3_sitelibdir/__pycache__/wakeonlan.*
%python3_sitelibdir/wakeonlan-%version-*-info

%changelog
* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial
