%define pypi_name hwdata

Name:    python3-module-%pypi_name
Version: 2.4.3
Release: alt1

Summary: Python bindings to hwdata
License: GPL-2.0
Group:   Development/Python3
Url:     https://github.com/xsuchy/python-hwdata

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
Requires: hwdata

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/__pycache__/*.pyc
%python3_sitelibdir/hwdata-%version.dist-info/
%python3_sitelibdir/hwdata.py


%changelog
* Wed Dec 03 2025 Sergey Palcheh <minergenon@altlinux.org> 2.4.3-alt1
- new version (2.4.3) with rpmgs script

* Wed Feb 26 2025 Sergey Palcheh <minergenon@altlinux.org> 2.4.2-alt1
- initial build for ALT Sisyphus

