%define _unpackaged_files_terminate_build 1
%define dist MooseX-Has-Sugar
Name: perl-%dist
Version: 0.05070422
Release: alt1

Summary: Sugar Syntax for moose 'has' fields
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/K/KE/KENTNL/MooseX-Has-Sugar-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Module-Build perl-MooseX-Types perl-Test-Fatal perl-namespace-autoclean

%description
Moose "has" syntax is generally fine, but sometimes one gets bothered
with the constant typing of string quotes for things.

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
* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.05070422-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.05070421-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.05070419-alt1
- initial revision
