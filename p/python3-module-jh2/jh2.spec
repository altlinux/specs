%define pypi_name jh2

Name: python3-module-%pypi_name
Version: 5.0.13
Release: alt1

Summary: HTTP/2 state-machine based protocol implementation
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/jh2
Vcs: https://github.com/jawah/h2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel
BuildRequires: python3-module-maturin rust-cargo

Source: %name-%version.tar
Source1: vendor.tar

%description
HTTP/2 state-machine based protocol implementation with optional
Rust hpack speedup.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md CHANGELOG.rst README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.0.13-alt1
- Initial build for ALT Linux.

