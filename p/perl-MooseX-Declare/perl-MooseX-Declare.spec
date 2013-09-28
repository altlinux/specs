BuildRequires: perl(Module/Build/Tiny.pm)
%define _unpackaged_files_terminate_build 1
%define dist MooseX-Declare
Name: perl-%dist
Version: 0.37
Release: alt1

Summary: Declarative syntax for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Declare-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Method-Signatures perl-MooseX-Role-Parameterized perl-Test-Exception perl-Test-NoWarnings perl(Test/Fatal.pm) perl(Test/CheckDeps.pm)

%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5.  When used, it sets up the "class" and "role" keywords.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
