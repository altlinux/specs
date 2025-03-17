%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: wild
Version: 0.4.0
Release: alt1

Summary: Wild is a very fast linker for Linux for iterative development

License: MIT OR Apache-2.0
Group: Development/Tools
Url: https://github.com/davidlattimore/wild
VCS: https://github.com/davidlattimore/wild

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml

BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: /proc

%description
Wild is a command-line tool for running Python packages in isolated
environment without using virtualenv or venv. It allows to quickly
install, test, and execute Python packages in temporary environments,
making it useful for dependency testing and isolated code execution.
Wild main features are: automatically creating temporary isolated
environments, installation and running Python packages without
affecting your system, simple to use with minimal dependencies,
useful for testing and one-off executions of third-party code.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
cargo build --release %{?_smp_mflags} --offline

%install
install -pvD -m0755 target/release/wild %buildroot%_bindir/wild

%files
%doc README.md
%_bindir/wild

%changelog
* Tue Mar 04 2025 Anastasia Doronina <swaggyglice@altlinux.org> 0.4.0-alt1
- Initial Build for Sisyphus.
