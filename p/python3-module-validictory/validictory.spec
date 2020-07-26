Name: python3-module-validictory
Version: 1.1.2
Release: alt1

Summary: A general purpose Python data validator
License: MIT
Group: Development/Python
Url: https://pypi.org/project/validictory/

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
%python3_sitelibdir/validictory
%python3_sitelibdir/validictory-%version-*-info

%changelog
* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- initial
