%define dist Test-Fatal
Name: perl-%dist
Version: 0.006
Release: alt1

Summary: Simple helpers for testing code with exceptions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Test-Fatal-0.006.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Try-Tiny perl-devel

%description
Test::Fatal is an alternative to the popular Test::Exception.  It does much
less, but should allow greater flexibility in testing exception-throwing code
with about the same amount of typing.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.003-alt1
- initial revision, for MooseX::Types
