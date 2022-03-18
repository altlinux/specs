Name: python3-module-zeep
Version: 4.1.0
Release: alt1

Summary: A fast and modern Python SOAP client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/python-zeep/

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
%python3_sitelibdir/zeep
%python3_sitelibdir/zeep-%version-*-info

%changelog
* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.0-alt1
- 4.1.0 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- initial
