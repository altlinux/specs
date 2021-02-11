Name: python3-module-httptools
Version: 0.1.1
Release: alt1

Summary: Python binding for the nodejs HTTP parser
License: MIT
Group: Development/Python
Url: https://pypi.org/project/httptools/

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: python3-module-Cython

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%python3_sitelibdir/httptools
%python3_sitelibdir/httptools-%version-*-info

%changelog
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.1-alt1
- initial
