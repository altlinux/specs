%define _unpackaged_files_terminate_build 1
%define module Test-Output

Name: perl-%module
Version: 1.034
Release: alt1

Summary: Utilities to test STDOUT and STDERR messages
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/B/BD/BDFOY/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Sub-Exporter perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Tester perl(Capture/Tiny.pm)

%description
Test::Output provides a simple interface for testing output sent to STDOUT or
STDERR. A number of different utilities are included to try and be as flexible
as possible to the tester.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.pod
%perl_vendor_privlib/Test/

%changelog
* Sat Jul 08 2023 Igor Vlasenko <viy@altlinux.org> 1.034-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 1.033-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1.032-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.031-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Wed Apr 27 2011 Victor Forsiuk <force@altlinux.org> 1.01-alt1
- 1.01

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- Initial build.
