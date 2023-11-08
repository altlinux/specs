Name: python3-module-pyradios
Version: 2.0.0
Release: alt1

Summary: Python client for the Radio Browser API
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pyradios/

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
%python3_sitelibdir/pyradios
%python3_sitelibdir/pyradios-%version.dist-info

%changelog
* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Feb 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- 1.0.2 released
