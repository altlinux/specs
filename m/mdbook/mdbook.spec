
%define _unpackaged_files_terminate_build 1
%define _customdocdir %_docdir/%name

Name:    mdbook
Version: 0.5.3
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

%rust_prep

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
%doc README.md

%files guide
%doc guide/book

%changelog
* Wed May 20 2026 Ivan A. Melnikov <iv@altlinux.org> 0.5.3-alt1
- 0.5.3

* Fri Dec 12 2025 Ivan A. Melnikov <iv@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Nov 20 2025 Ivan A. Melnikov <iv@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Nov 18 2025 Aleksandr Dovydenkov <asd@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 15 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.52-alt1
- 0.4.52

* Mon May 26 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.51-alt1
- 0.4.51

* Fri May 23 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.50-alt1
- 0.4.50

* Tue May 06 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.49-alt1
- 0.4.49

* Tue Apr 01 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.48-alt1
- 0.4.48

* Mon Mar 10 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.47-alt1
- 0.4.47

* Tue Feb 18 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.45-alt1
- 0.4.45

* Wed Jan 29 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.44-alt1
- 0.4.44

* Mon Nov 25 2024 Ivan A. Melnikov <iv@altlinux.org> 0.4.43-alt1
- 0.4.43

* Thu Nov 07 2024 Ivan A. Melnikov <iv@altlinux.org> 0.4.42-alt1
- 0.4.42

* Wed Nov 06 2024 Ivan A. Melnikov <iv@altlinux.org> 0.4.41-alt1
- 0.4.41

* Sun Oct 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.4.40-alt1
- 0.4.40

* Mon Jul 17 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.32-alt1
- 0.4.32

* Fri Jun 30 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.31-alt1
- 0.4.31

* Thu Jun 08 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.30-alt1
- 0.4.30

* Mon Mar 06 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.28-alt1
- 0.4.28

* Tue Feb 14 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.27-alt1
- 0.4.27

* Thu Feb 09 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.26-alt1
- 0.4.26

* Sat Jan 07 2023 Ivan A. Melnikov <iv@altlinux.org> 0.4.25-alt1
- 0.4.25

* Thu Oct 13 2022 Ivan A. Melnikov <iv@altlinux.org> 0.4.21-alt1
- Initial build for Sisyphus
