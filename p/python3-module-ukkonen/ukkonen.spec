%define  oname ukkonen

%def_with check

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: Implementation of bounded Levenshtein distance (Ukkonen)

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/ukkonen

# https://github.com/asottile/ukkonen
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: python3-module-cffi

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-covdefaults
%endif

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%python3_sitelibdir/%oname.py
%python3_sitelibdir/_%oname.abi3.so
%python3_sitelibdir/__pycache__
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Nov 03 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
