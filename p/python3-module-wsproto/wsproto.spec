Name: python3-module-wsproto
Version: 1.2.0
Release: alt1

Summary: Python WebSocket implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wsproto/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(h11)

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
%python3_sitelibdir/wsproto
%python3_sitelibdir/wsproto-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
