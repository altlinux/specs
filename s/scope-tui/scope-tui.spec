%define _unpackaged_files_terminate_build 1

Name: scope-tui
Version: 0.3.5
Release: alt1

Summary: A simple oscilloscope/vectorscope/spectroscope for your terminal
License: MIT
Group: Development/Tools
Url: https://github.com/alemidev/scope-tui
Vcs: https://github.com/alemidev/scope-tui.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libalsa-devel

%description
A simple oscilloscope/vectorscope/spectroscope for your terminal.

%prep
%setup -a1
%rust_prep

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install scope-tui

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/scope-tui

%changelog
* Tue Jul 07 2026 Mikhail Nogin <joycap@altlinux.org> 0.3.5-alt1
- Initial built for Sisyphus.
