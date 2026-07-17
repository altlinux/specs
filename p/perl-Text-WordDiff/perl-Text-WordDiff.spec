%define _unpackaged_files_terminate_build 1
%define dist Text-WordDiff

Name: perl-%dist
Version: 0.09
Release: alt1

Summary: Track changes between documents
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl
URL: https://metacpan.org/release/%dist

# Source-url: https://cpan.metacpan.org/authors/id/T/TI/TIMK/%dist-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Algorithm-Diff perl-HTML-Parser perl-Module-Build

%description
This module is a variation on the lovely Text::Diff module. Rather than
generating line-level diffs, however, it generates word-level diffs. This
can be useful for tracking changes in narrative documents, such as those
written in HTML, Markdown, plain text, or any other format that can be
broken down into words.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/Text/*

%changelog
* Thu Jul 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- initial build for ALT Sisyphus

