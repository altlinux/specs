%define _unpackaged_files_terminate_build 1

Name: pdf2svg
Version: 0.2.4
Release: alt1

Summary: converts PDF documents to SVG files (one per page)
License: GPL-2.0-only
Group: Office
Url: https://github.com/dawbarton/pdf2svg

Source: %name-%version.tar

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(poppler-glib)

%description
pdf2svg is a tiny command-line utility using Cairo and Poppler
to convert PDF documents into SVG files.  Multi-page PDF can be split up to
one SVG per page by passing a file naming specification.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc *.md
%_bindir/pdf2svg

%changelog
* Wed Dec 24 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus
