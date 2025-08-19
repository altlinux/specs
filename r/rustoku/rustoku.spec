%define _unpackaged_files_terminate_build 1

Name: rustoku
Version: 0.12.2
Release: alt1
Summary: Lightning-fast Sudoku.
License: MIT
Group: Games/Other
Url:  https://github.com/huangsam/rustoku

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
Rustoku is a highly optimized Sudoku puzzle solver and
generator built with a focus on speed and clarity.
It leverages bitmasking for constraint tracking and a
backtracking algorithm with MRV for puzzle navigation.
Available as a Rust library and CLI.

%prep
%setup -a 1
%autopatch -p1

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
%rust_install %name-cli
#mkdir -p %buildroot%_bindir
#install -Dm 755 target/release/librustoku_lib.so %buildroot%_libdir/
#install -Dm 755 target/release/%name-cli %buildroot%_bindir/

%files
%doc *.md LICENSE
%_bindir/%name-cli


%changelog
* Mon Aug 18 2025 Pavel Shilov <zerospirit@altlinux.org> 0.12.2-alt1
- initial build for Sisyphus
