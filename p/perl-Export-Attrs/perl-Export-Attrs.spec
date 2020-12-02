%define _unpackaged_files_terminate_build 1

Name: perl-Export-Attrs
Version: 0.1.0
Release: alt1
Summary: The Perl 6 'is export(...)' trait as a Perl 5 attribute
License: GPL-1.0+  or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Export-Attrs
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-devel perl(Module/Build/Tiny.pm) perl(Attribute/Handlers.pm) perl(PadWalker.pm)

%description
This module is a fork of Perl6::Export::Attrs created to restore
compatibility with Perl6::Export::Attrs version 0.0.3.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/Export*

%changelog
* Wed Dec 02 2020 Alexandr Antonov <aas@altlinux.org> 0.1.0-alt1
- initial build for ALT
