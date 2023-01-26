Name: python3-module-micloud
Version: 0.6
Release: alt1

Summary: Python library for connecting to xiaomi cloud.
License: MIT
Group: Development/Python
Url: https://pypi.org/project/micloud/

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
%_bindir/micloud
%python3_sitelibdir/micloud
%python3_sitelibdir/micloud-%version.dist-info

%changelog
* Thu Jan 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- 0.6 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- 0.5 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- initial
