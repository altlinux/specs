%define _unpackaged_files_terminate_build 1

Name: cargo-make
Version: 0.37.24
Release: alt2

Summary: Rust task runner and build tool
License: Apache-2.0
Group: Development/Tools
Url: https://crates.io/crates/cargo-make
Vcs: https://github.com/sagiegurari/cargo-make

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

Requires: rust-cargo

BuildRequires: /proc
BuildRequires: rust-cargo

%description
The cargo-make task runner enables to define and configure sets of tasks
and run them as a flow.
A task is a command, script, rust code, or other sub tasks to execute.
Tasks can have dependencies which are also tasks that will be executed
before the task itself.
With a simple toml based configuration file, you can define a multi platform
build script that can run build, test, generate documentation, run bench
tests, run security validations and more, executed by running a single command.

%prep
%setup -a1
%autopatch -p1
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

%install
install -Dp target/release/cargo-make -t %buildroot%_bindir
install -Dp target/release/makers -t %buildroot%_bindir
install -pDm644 extra/shell/makers-completion.bash \
	%buildroot%_datadir/bash-completion/completions/makers

%files
%doc README.md docs
%_bindir/cargo-make
%_bindir/makers
%_datadir/bash-completion/completions/makers

%changelog
* Wed Jan 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.37.24-alt2
- Added dependency on rust-cargo.

* Sun Jan 26 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.37.24-alt1
- Built again after deleting as FTBFS package by reminder.

* Tue Feb 21 2023 Alexander Burmatov <thatman@altlinux.org> 0.36.5-alt1
- Initial build for Sisyphus

