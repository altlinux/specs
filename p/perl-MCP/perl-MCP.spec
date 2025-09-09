%define _unpackaged_files_terminate_build 1

Name: perl-MCP
Version: 0.0.5
Release: alt1
Summary: Connect Perl with AI using the Model Context Protocol (MCP).
License: MIT
Group: Development/Perl
Url: https://metacpan.org/release/MCP
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(Crypt/Misc.pm) perl(Mojo/Base.pm) perl(JSON/Validator.pm) perl(YAML/PP.pm)

%description
Currently this module is focused on tool calling, but it will be extended to support other
MCP features in the future. At its core, MCP is all about text processing,
making it a great fit for Perl.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*

%changelog
* Mon Sep 08 2025 Alexandr Antonov <aas@altlinux.org> 0.0.5-alt1
- initial build for ALT
