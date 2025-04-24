%define _unpackaged_files_terminate_build 1
%def_with check

Name: AFL_Runner
Version: 0.6.0
Release: alt1

Summary: AFL_Runner is a modern CLI tool designed to streamline running efficient multi-core AFLPlusPlus campaigns
License: Apache-2.0
Group: Development/Other
Url: https://crates.io/crates/afl_runner
Vcs: https://github.com/0xricksanchez/AFL_Runner
# 32 bit systems aren't supported due explicit use of x64 float and integer types
ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
# Tests dependencies.
BuildRequires: AFLplusplus llvm lcov

%description
AFL_Runner is a modern CLI tool designed to streamline running
efficient multi-core AFLPlusPlus campaigns.

%prep
%setup -a1
mkdir -pv .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install aflr

%check
%rust_test

%files
%doc LICENSE
%_bindir/aflr

%changelog
* Tue Apr 23 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.6.0-alt1
- Initial build.
