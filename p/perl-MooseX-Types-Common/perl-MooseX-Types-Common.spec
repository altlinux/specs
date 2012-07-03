%define dist MooseX-Types-Common
Name: perl-%dist
Version: 0.001003
Release: alt1

Summary: A library of commonly used type constraints
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AR/ARCANEZ/MooseX-Types-Common-0.001003.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 14 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-MooseX-Types perl-Test-Exception

%description
A set of commonly-used type constraints that do not ship with Moose by default.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.001003-alt1
- automated CPAN update

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.001002-alt1
- initial revision
