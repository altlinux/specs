%define oname crayons

Name: python3-module-%oname
Version: 0.1.2
Release: alt2

Summary: This module is really simple, it gives you colored strings for terminal usage.
License: MIT
Group: Development/Python3
Url: https://github.com/kennethreitz/crayons
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Crayons is nice because it automatically wraps a given string in both the 
foreground color, as well as returning to the original state after the 
string is complete. Most terminal color libraries make you manage this 
yourself.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.2-alt2
- Drop python2 support.

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
