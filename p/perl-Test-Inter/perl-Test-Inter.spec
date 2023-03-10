%define _unpackaged_files_terminate_build 1
%define dist Test-Inter
Name: perl-%dist
Version: 1.10
Release: alt1

Summary: Framework for more readable interactive test scripts
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SB/SBECK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Module-Build perl-Storable perl-Test-Pod perl-Test-Pod-Coverage perl(File/Find/Rule.pm)

%description
This is another framework for writing test scripts. It is loosely
inspired by Test::More, and has most of it's functionality, but it is
not a drop-in replacement.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README examples
%dir	%perl_vendor_privlib/Test
	%perl_vendor_privlib/Test/Inter.pm
%doc	%perl_vendor_privlib/Test/Inter.pod

%changelog
* Fri Mar 10 2023 Igor Vlasenko <viy@altlinux.org> 1.10-alt1
- automated CPAN update

* Sun Mar 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision (for Date::Manip)
