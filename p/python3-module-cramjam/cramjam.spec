%define optflags_lto %nil
%define pypi_name cramjam

%def_with check

Name: python3-module-%pypi_name
Version: 2.8.3
Release: alt1

Summary: A collection of compression algorithms
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/cramjam
VCS: https://github.com/milesgranger/cramjam
Source0: %pypi_name-%version.tar
Source1: crates.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-maturin
BuildRequires: /proc
BuildRequires: rust-cargo
%if_with check
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pytest
%endif

%description
Your go-to for easy access to a plethora of compression algorithms,
all neatly bundled in one simple installation.

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
pushd %pypi_name-python
%pyproject_build
popd

%install
pushd %pypi_name-python
%pyproject_install
popd

%check
pushd %pypi_name-python
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 --ignore benchmarks -v
popd

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Thu May 16 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus
