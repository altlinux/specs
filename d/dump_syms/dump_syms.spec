%define _unpackaged_files_terminate_build 1
%def_with check

Name: dump_syms
Version: 2.3.7
Release: alt1

Summary: Is a command-line utility for parsing the debugging information the compiler provides
License: Apache-2.0
Group: Development/Other
Vcs: https://github.com/mozilla/dump_syms.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: cargo-vendor-checksum
BuildRequires: gcc-c++

%description
dump_syms is a command-line utility for parsing the debugging information the compiler provides 
(whether as DWARF or STABS sections in an ELF file or as stand-alone PDB files) 
and writing that information back out in the Breakpad symbol file format.

%prep
%setup -a1
mkdir -pv .cargo
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
rustdocflags = ["-Arustdoc::private_intra_doc_links"]
rustflags = ["-Cforce-frame-pointers=yes"]

[alias]
build_testing = ["build", "--features", "testing"]
neon = ["run", "--bin", "neon_local"]

[profile.release]
strip = false
EOF

%build
%rust_build 

%install
%rust_install

%check
#tests requiring access to Microsoft Symbol Server were skipped
%rust_test -- --skip=test_ntdll \
--skip=test_oleaut32 \
#

%files
%_bindir/dump_syms

%changelog
* Fri Apr 03 2026 Ivan Khanas <xeno@altlinux.org> 2.3.7-alt1
- New version.

* Mon Jul 07 2025 Ivan Khanas <xeno@altlinux.org> 2.3.5-alt1
- New version.

* Fri Apr 18 2025 Ivan Khanas <xeno@altlinux.org> 2.3.4-alt1
- First build for ALT.
