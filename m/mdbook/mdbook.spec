
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

Name:    mdbook
Version: 0.4.25
Release: alt1

Summary: Create modern online books from Markdown files
License: MPL-2.0
Group:   Development/Documentation
Url:     https://github.com/rust-lang/mdBook

Source:   %name-%version.tar
Source1:  vendor.tar

Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
mdBook is a command line tool to create books with Markdown. It
is ideal for creating product or API documentation, tutorials,
course materials or anything that requires a clean, easily
navigable and customizable presentation.
* Lightweight Markdown syntax helps you focus more on your content
* Integrated search support
* Color syntax highlighting for code blocks for many
  different languages
* Theme files allow customizing the formatting of the output
* Preprocessors can provide extensions for custom syntax
  and modifying content
* Backends can render the output to multiple formats
* Written in Rust for speed, safety, and simplicity
* Automated testing of Rust code samples

%package    guide
Summary:    mdbook user guide
Group:      Documentation
BuildArch:  noarch

%description guide
mdBook is a command line tool to create books with Markdown.
This package contains its user guide.

%prep
%setup
%patch -p1
tar -xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build
target/release/mdbook build guide

%install
%rust_install

mkdir -p %buildroot%_sysconfdir/bash_completion.d
target/release/mdbook completions bash \
    > %buildroot%_sysconfdir/bash_completion.d/mdbook

%check
%rust_test

%files
%_bindir/*
%_sysconfdir/bash_completion.d/*
%doc README.md CHANGELOG.md

%files guide
%doc guide/book

%changelog
* Sat Jan 07 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.25-alt1
- 0.4.25

* Thu Oct 13 2022 Ivan A. Melnikov <iv@altlinux.org> 0.4.21-alt1
- Initial build for Sisyphus
