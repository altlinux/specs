%global _unpackaged_files_terminate_build 1
%def_with check

Name: agf
Version: 0.15.0
Release: alt1
Summary: Find, search, and resume AI coding-agent sessions
License: MIT
Group: Development/Tools
URL: https://crates.io/crates/agf
VCS: https://github.com/subinium/agf

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: python3-module-pyte
BuildRequires: /dev/pts
%endif

%description
agf is a local-first fuzzy finder for AI coding-agent sessions.
Search the sessions your terminal agents already keep locally,
then resume the right one in a keystroke.

%prep
%setup -a1
%rust_prep
sed -i '/importlib\.metadata\.version("wcwidth")/d' \
    tests/support/runtime_screen_test.py

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Sun Sep 06 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.0-alt1
- Initial build for ALT.
