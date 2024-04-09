%define oname sarif_om

Name: python3-module-%oname
Version: 1.0.4
Release: alt1

Summary: Python classes for the SARIF 2.1.0 object model

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/sarif-om
VCS: https://github.com/microsoft/sarif-python-om

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-attrs

%py3_provides %oname

%description
The Static Analysis Results Interchange Format (SARIF) has been approved as an
OASIS standard.
A collection of tools offering facilities for producing, consuming, and
validating files in the SARIF format.

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Apr 09 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
