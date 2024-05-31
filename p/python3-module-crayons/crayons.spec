%define oname crayons

%def_with check

Name: python3-module-%oname
Version: 0.4.0
Release: alt1

Summary: This module is really simple, it gives you colored strings for terminal usage.

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/crayons
VCS: https://github.com/kennethreitz/crayons
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-colorama
%endif

%description
Crayons is nice because it automatically wraps a given string in both the
foreground color, as well as returning to the original state after the
string is complete. Most terminal color libraries make you manage this
yourself.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
python3 test_crayons.py

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Build new version.

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.2-alt2
- Drop python2 support.

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
