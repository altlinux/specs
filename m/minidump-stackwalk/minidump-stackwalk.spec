%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name: minidump-stackwalk
Version: 0.26.1
Release: alt1

Summary: Analyzes minidumps and produces a report (human-readable or JSON)

License: MIT
Group: Development/Tools
Url: https://github.com/rust-minidump/rust-minidump

# Source-url: https://github.com/rust-minidump/rust-minidump/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Cargo modules for build rust code
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
minidump-stackwalk is a CLI frontend for minidump-processor, providing
both machine-readable and human-readable digests of a minidump with
backtraces and symbolication.

The tool analyzes crash dumps and outputs operating system and CPU
information, crash reason and address, thread backtraces, symbolicated
output (function names, source files, line numbers) when symbol files
are provided, and register states for crashed threads.

%prep
%setup -a1
%cargo_prep
mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
%cargo_install

%files
%doc README.md
%doc LICENSE
%_bindir/minidump-stackwalk

%changelog
* Mon May 18 2026 Vitaly Lipatov <lav@altlinux.ru> 0.26.1-alt1
- initial build for ALT Sisyphus

