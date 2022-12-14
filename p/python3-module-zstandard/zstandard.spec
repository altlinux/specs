Name: python3-module-zstandard
Version: 0.19.0
Release: alt1

Summary: Python bindings for zstandard compression library
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/zstandard/

Source0: %name-%version-%release.tar

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
%python3_sitelibdir/zstandard
%python3_sitelibdir/zstandard-%version.dist-info

%changelog
* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- initial
