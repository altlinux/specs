%define _unpackaged_files_terminate_build 1
%define dist PPIx-EditorTools
Name: perl-PPIx-EditorTools
Version: 0.21
Release: alt1

Summary: PPIx::EditorTools - Utility methods and base class for manipulating Perl
License: Perl
Group: Development/Perl

Url: %CPAN %dist
Source0: http://www.cpan.org/authors/id/Y/YA/YANICK/%{dist}-%{version}.tar.gz

BuildRequires: perl-devel perl-Test-Differences perl-Class-XSAccessor perl-PPI perl-Test-Most perl-Test-Warn perl-Test-Exception perl-Test-Deep perl-Try-Tiny perl-Pod-Parser
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.mkdn Changes CONTRIBUTORS README LICENSE
%perl_vendor_privlib/PPIx/EditorTools*
%doc Changes README

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sun Sep 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- 0.15 -> 0.17
- built as plain srpm

* Wed Oct 26 2011 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11
- Few perl-Test-* required for tests

* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- New version 0.10

* Mon Jan 25 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
