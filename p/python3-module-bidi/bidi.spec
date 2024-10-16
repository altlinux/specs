%define  oname bidi

%def_with check

Name:    python3-module-%oname
Version: 0.6.3
Release: alt1

Summary: BIDI algorithm related functions

License: LGPL-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/python-bidi
VCS:     https://github.com/MeirKriheli/python-bidi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-maturin
BuildRequires: rust-cargo
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
%setup

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

tar -xvf %SOURCE1

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
