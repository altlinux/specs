%define _unpackaged_files_terminate_build 1
%define dist Getopt-Euclid
Name: perl-%dist
Version: 0.4.6
Release: alt1

Summary: Executable Uniform Command-Line Interface Descriptions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BIGPRESH/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Module-Build perl-Perl-Tidy perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Balanced

%description
Getopt::Euclid uses your program's own documentation to create a command-line
argument parser. This ensures that your program's documented interface and
its actual interface always agree.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Getopt

%changelog
* Sat Jul 08 2023 Igor Vlasenko <viy@altlinux.org> 0.4.6-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.7-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.3.2-alt1
- 0.2.3 -> 0.3.2

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.2.3-alt1
- initial revision
