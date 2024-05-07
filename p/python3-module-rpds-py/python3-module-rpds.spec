%define pypi_name rpds

%def_with check

Name: python3-module-%pypi_name-py
Version: 0.18.1
Release: alt1

Summary: Python bindings to the Rust rpds crate for persistent data structures
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/rpds-py
VCS: https://github.com/crate-py/rpds
Source0: %pypi_name-%version.tar
Source1: crates.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-maturin
BuildRequires: /proc
BuildRequires: rust-cargo
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
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

tar xf %SOURCE1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/rpds_py-%version.dist-info

%changelog
* Tue May 07 2024 Anton Vyatkin <toni@altlinux.org> 0.18.1-alt1
- New version 0.18.1.

* Tue Feb 27 2024 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt1
- New version 0.18.0.

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 0.17.1-alt1
- New version 0.17.1.

* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 0.12.0-alt1
- New version 0.12.0.

* Thu Oct 12 2023 Anton Vyatkin <toni@altlinux.org> 0.10.6-alt1
- New version 0.10.6.

* Thu Oct 05 2023 Anton Vyatkin <toni@altlinux.org> 0.10.4-alt1
- New version 0.10.4.

* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 0.10.3-alt1
- New version 0.10.3.

* Wed Sep 06 2023 Anton Vyatkin <toni@altlinux.org> 0.10.2-alt1
- New version 0.10.2.

* Tue Aug 29 2023 Anton Vyatkin <toni@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Thu Jul 20 2023 Anton Vyatkin <toni@altlinux.org> 0.9.2-alt1
- New version 0.9.2.

* Tue Jul 18 2023 Anton Vyatkin <toni@altlinux.org> 0.8.11-alt1
- New version 0.8.11.

* Thu Jul 13 2023 Anton Vyatkin <toni@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus
