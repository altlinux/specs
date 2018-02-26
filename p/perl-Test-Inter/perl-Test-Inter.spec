%define dist Test-Inter
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: Framework for more readable interactive test scripts
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SB/SBECK/Test-Inter-1.03.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Module-Build perl-Storable perl-Test-Pod perl-Test-Pod-Coverage

%description
This is another framework for writing test scripts. It is loosely
inspired by Test::More, and has most of it's functionality, but it is
not a drop-in replacement.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/Test
	%perl_vendor_privlib/Test/Inter.pm
%doc	%perl_vendor_privlib/Test/Inter.pod

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision (for Date::Manip)
