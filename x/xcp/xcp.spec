%def_without check

Name: xcp
Version: 0.10.0
Release: alt1
Summary: An extended cp
License: GPL-3.0
Group: File tools
Url: https://github.com/tarka/xcp
Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-fix-i586-armh-build.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
xcp is a (partial) clone of the Unix cp command. It is not intended
as a full replacement, but as a companion utility with some more
user-friendly feedback and some optimisations that make sense under
certain tasks.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%ifarch i586 armh
%patch1 -p1
%endif

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Sun Jun 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.0-alt1
- Initial build for ALT.
