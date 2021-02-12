Name: python3-module-marshmallow
Version: 3.10.0
Release: alt1

Summary: Simplified object serialization
License: MIT
Group: Development/Python
Url: https://pypi.org/project/marshmallow/

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
%python3_sitelibdir/marshmallow
%python3_sitelibdir/marshmallow-%version-*-info

%changelog
* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- initial
