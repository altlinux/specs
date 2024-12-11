%define optflags_lto %nil
%define pypi_name cramjam

# target_pointer_width = "64" option seems a reason of tests errors
# on %%ix86 arches
%ifarch %ix86
%def_without check
%endif

Name: python3-module-%pypi_name
Version: 2.9.0
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
# XXX: Since v2.8.4 isal and blosc2 subprojects could not be linked with
# system provided libs.
# use-system-isal-shared and use-system-blosc2-shared config opts did not
# produced any result
BuildRequires: gcc gcc-c++ glibc-devel-static cmake nasm
BuildRequires: pkgconfig(blosc2)
BuildRequires: pkgconfig(libisal)
BuildRequires: /proc
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pytest
}}

%description
Your go-to for easy access to a plethora of compression algorithms,
all neatly bundled in one simple installation.

%prep
%setup -n %pypi_name-%version
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
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
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest --ignore benchmarks -v

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Dec 10 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.9.0-alt1
- 2.8.3 -> 2.9.0

* Thu May 16 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus
