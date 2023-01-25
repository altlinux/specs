Name: python3-module-zeep
Version: 4.2.1
Release: alt1

Summary: A fast and modern Python SOAP client
License: MIT
Group: Development/Python
Url: https://pypi.org/project/python-zeep/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/zeep
%python3_sitelibdir/zeep-%version.dist-info

%changelog
* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.1-alt1
- 4.2.1 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.0-alt1
- 4.1.0 released

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- initial
