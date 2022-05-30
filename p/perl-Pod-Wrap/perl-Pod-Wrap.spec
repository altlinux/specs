%define _unpackaged_files_terminate_build 1
%define sname Pod-Wrap

Name:  perl-Pod-Wrap
Version: 0.01
Release: alt1
Summary: Wrap pod paragraphs, leaving verbatim text and code alone
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Pod-Wrap
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(Module/Build.pm) perl(Pod/Parser.pm)

%description
This is a Pod::Parser subclass, based on Pod::Stripper. It parses perl
files, wrapping pod text, and leaving everything else intact. It prints
it's output to wherever you point it to (like you do with Pod::Parser (and
Pod::Stripper)).

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%_bindir/*
%perl_vendorlib/*
%_man1dir/*

%changelog
* Thu May 26 2022 Alexandr Antonov <aas@altlinux.org> 0.01-alt1
- initial build for ALT

