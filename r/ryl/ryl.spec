%global _unpackaged_files_terminate_build 1
%def_with check

Name: ryl
Version: 0.28.0
Release: alt1
Summary: Fast YAML linter and formatter
License: MIT OR Apache-2.0
Group: Development/Tools
URL: https://ryl-docs.pages.dev
VCS: https://github.com/owenlamont/ryl

Source: %name-%version.tar
Source1: vendor.tar

Patch: ryl-chroot-tests.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: git-core
%endif

%description
ryl is a fast YAML linter and formatter written in Rust. It checks YAML
style, applies safe lint fixes, and formats files with configurable layout.
It reads YAML as 1.2 and, by default, writes output a YAML 1.1 reader also
understands.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test --test integration

%files
%_bindir/%name

%changelog
* Wed Nov 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.28.0-alt1
- Initial build for ALT.
