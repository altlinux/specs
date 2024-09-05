Name: python3-module-jsonpath
Version: 0.82.2
Release: alt1

Summary: JSONPath for Python
License: MIT
Group: Development/Python
Url: https://pypi.org/project/jsonpath/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
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
%python3_sitelibdir/jsonpath.*
%python3_sitelibdir/*/jsonpath.*
%python3_sitelibdir/jsonpath-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.82.2-alt1
- 0.82.2 released
