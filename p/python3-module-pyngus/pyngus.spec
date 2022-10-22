%define  oname pyngus

%def_with check

Name:    python3-module-%oname
Version: 2.3.1
Release: alt1

Summary: Callback API implemented over Proton

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pyngus

# https://github.com/kgiusti/pyngus
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-qpid-proton
%endif

BuildArch: noarch

%description
A connection oriented messaging framework using QPID Proton.
It provides a callback-based API for message passing.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus.
