Name: perl-strictures
Version: 2.000005
Release: alt1

Summary: strictures - turn on strict and make all warnings fatal
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/p5sagit/strictures.git
Url: %CPAN strictures
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel
BuildArch: noarch

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/strictures*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.000005-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.000003-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.000002-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.000001-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.005005-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.005004-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.004004-alt1
- 1.004002 -> 1.004004

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.004002-alt1
- 1.002002 -> 1.004002

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.002002-alt1
- initial build
