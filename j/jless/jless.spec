%define _unpackaged_files_terminate_build 1

Name: jless
Version: 0.9.0
Release: alt1

Summary: Command-line JSON viewer
License: MIT
Group: Development/Tools
Url: https://jless.io
Vcs: https://github.com/PaulJuliusMartinez/jless.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-macros-rust  
BuildRequires: rpm-build-rust
BuildRequires: libxcb-devel
BuildRequires: python3

%description
jless is a command-line JSON viewer. Use it as a replacement for whatever
combination of less, jq, cat and your editor you currently use for viewing
JSON files. It is written in Rust and can be installed as a single
standalone binary.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc README.md LICENSE
%_bindir/jless

%changelog
* Thu Jan 26 2026 Grant Makyan <karonus@altlinux.org> 0.9.0-alt1
- First build for ALT.
