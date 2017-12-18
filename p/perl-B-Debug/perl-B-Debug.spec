%define _unpackaged_files_terminate_build 1
Name: perl-B-Debug
Version: 1.26
Release: alt1
Summary: B::Debug - Walk Perl syntax tree, printing debug info about ops

Group: Development/Perl
License: Perl
Url: %CPAN B-Debug

Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/B-Debug-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n B-Debug-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/B/Debug.pm
%doc Changes README Artistic Copying

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt1
- 1.17 -> 1.18
- built as plain srpm

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt1
- New version 1.17

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- initial build
