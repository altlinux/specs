%define dist B-Hooks-EndOfScope
Name: perl-%dist
Version: 0.09
Release: alt1

Summary: Execute code after a scope finished compilation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FL/FLORA/B-Hooks-EndOfScope-0.09.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 12 2010
BuildRequires: perl-Module-Install perl-Sub-Exporter perl-Variable-Magic

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B*

%changelog
* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- initial revision, for namespace::clean
