%define _unpackaged_files_terminate_build 1

Name:           perl-Method-Signatures-Simple
Version:        1.07
Release:        alt1
Summary:        Basic method declarations with signatures, without source filters
License:        GPL+ or Artistic
Group: Development/Perl
Url:            https://metacpan.org/release/Method-Signatures-Simple
Source: %name-%version.tar
BuildArch:      noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Devel/Declare/MethodInstaller/Simple.pm)

%description
This module provides basic method and func keywords with simple
signatures. It's intentionally simple, and is supposed to be a
stepping stone for its bigger brothers MooseX::Method::Signatures and
Method::Signatures.  It only has a small benefit over regular subs,
so if you want more features, look at those modules.  But if you're
looking for a small amount of syntactic sugar, this might just be enough.

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
* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 1.07-alt1
- initial build for ALT
