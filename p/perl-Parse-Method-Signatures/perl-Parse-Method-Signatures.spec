%define dist Parse-Method-Signatures
Name: perl-%dist
Version: 1.003014
Release: alt1

Summary: Perl6 like method signature parser
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Traits perl-MooseX-Types-Structured perl-PPI perl-Pod-Escapes perl-Test-Differences perl-Test-Exception perl-aliased

%description
Inspired by Perl6::Signature but streamlined to just support the subset
deemed useful for TryCatch and MooseX::Method::Signatures.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Parse

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.003014-alt1
- initial revision
