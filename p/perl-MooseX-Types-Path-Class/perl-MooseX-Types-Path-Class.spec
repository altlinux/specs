%define dist MooseX-Types-Path-Class
Name: perl-%dist
Version: 0.06
Release: alt1

Summary: A Path::Class type library for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TH/THEPLER/MooseX-Types-Path-Class-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-MooseX-Types perl-Path-Class perl-Test-Pod perl-Test-Pod-Coverage

%description
MooseX::Types::Path::Class creates common Moose types,
coercions and option specifications useful for dealing
with Path::Class objects as Moose attributes.

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
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
