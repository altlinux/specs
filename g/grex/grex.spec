%define _unpackaged_files_terminate_build 1
%def_with check

Name: grex
Version: 1.4.5
Release: alt1

Summary: A command-line tool and Rust library with Python bindings for generating regular expressions from user-provided test cases
License: Apache-2.0
Group: Development/Other
Url: https://pemistahl.github.io/grex-js
Vcs: https://github.com/pemistahl/grex

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: rust-cargo
BuildRequires: python3-module-maturin
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary

%package -n python3-module-%name
Version: 1.0.1
Summary: A command-line tool and Rust library with Python bindings for generating regular expressions from user-provided test cases
Group: Development/Python3

%description -n python3-module-%name
A command-line tool and Rust library with Python bindings.

%prep
%setup -a1
mkdir .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release
%pyproject_build

%install
install -Dp target/release/%name -t %buildroot%_bindir
%pyproject_install

%check
%pyproject_run_pytest
cargo test

%files
%_bindir/%name
%doc LICENSE README.md

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-*.dist-info/
%doc LICENSE README.md

%changelog
* Thu Mar 25 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.4.5-alt1
- Initial build for ALT Sisyphus.
