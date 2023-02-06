Name: python3-module-marshmallow
Version: 3.19.0
Release: alt1

Summary: Simplified object serialization
License: MIT
Group: Development/Python
Url: https://pypi.org/project/marshmallow/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(simplejson)
BuildRequires: python3(pytz)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/marshmallow
%python3_sitelibdir/marshmallow-%version.dist-info

%changelog
* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.0-alt1
- 3.19.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.0-alt1
- 3.17.0 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- initial
