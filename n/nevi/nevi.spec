%define _unpackaged_files_terminate_build 1
%def_with check

Name: nevi
Version: 0.3.0
Release: alt1
Summary: Fast terminal editor
License: MIT
Group: Editors
URL: https://github.com/anthonyamaro15/nevi
VCS: https://github.com/anthonyamaro15/nevi

ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-fix-help-command.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cmake
BuildRequires: libssl-devel

%if_with check
BuildRequires: /dev/pts
%endif

%description
A fast, Neovim-inspired terminal editor written in Rust.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Thu Aug 27 2026 Vladislav Eliseev <general@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
