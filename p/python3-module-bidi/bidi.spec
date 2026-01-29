%define  oname bidi

%def_with check

Name:    python3-module-%oname
Version: 0.6.7
Release: alt1

Summary: BIDI algorithm related functions

License: LGPL-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/python-bidi
VCS:     https://github.com/MeirKriheli/python-bidi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-rust

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-maturin
BuildRequires: /proc

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

Source:  %name-%version.tar
Source1: vendor.tar

%description
%summary.

%prep
%setup -a1
%rust_prep

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rv bidi
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.rst
%_bindir/py%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/python_bidi-%version.dist-info

%changelog
* Thu Jan 29 2026 Grigory Ustinov <grenka@altlinux.org> 0.6.7-alt1
- Automatically updated to 0.6.7.

* Tue Feb 25 2025 Grigory Ustinov <grenka@altlinux.org> 0.6.6-alt1
- Automatically updated to 0.6.6.

* Wed Oct 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Automatically updated to 0.6.3.

* Tue Oct 15 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.2-alt1
- Automatically updated to 0.6.2.

* Tue Oct 15 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Automatically updated to 0.6.1.

* Tue Oct 08 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0 (thx to k0tran@).

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.
