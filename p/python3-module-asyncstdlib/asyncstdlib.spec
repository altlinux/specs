Name: python3-module-asyncstdlib
Version: 3.10.5
Release: alt1

Summary: Async-compatible stdlib reimplementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/asyncstdlib

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)
BuildRequires: python3(flit_core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/asyncstdlib
%python3_sitelibdir/asyncstdlib-%version.dist-info

%changelog
* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.5-alt1
- 3.10.5 released
