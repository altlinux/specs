%define _unpackaged_files_terminate_build 1
%filter_from_requires /^perl.MRO.Compat.pm./d

Name: perl-Moo
Version: 2.005005
Release: alt1

Summary: Moo - Minimalist Object Orientation (with Moose compatiblity)
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Moo.git
Url: %CPAN Moo
VCS: git+https://github.com/moose/Moo.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-Import-Into perl-Dist-CheckConflicts perl-devel perl-Class-Method-Modifiers perl-strictures perl-Test-Fatal perl-Text-Balanced perl-Filter-Simple perl-Module-Runtime perl-Role-Tiny perl-Devel-GlobalDestruction perl(Sub/Quote.pm)
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
%doc Changes README*
%perl_vendor_privlib/Moo*
%perl_vendor_privlib/Method/Generate/*
#perl_vendor_privlib/Method/Inliner.pm
%perl_vendor_privlib/oo.pm
%doc Changes

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 2.005005-alt1
- new version 2.005005

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 2.005004-alt1
- new version

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 2.005003-alt1
- new version

* Thu Nov 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.004004-alt1
- new version

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 2.004003-alt1
- new version

* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 2.004000-alt2
- build w/o perl-MRO-Compat

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 2.004000-alt1
- new version

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.003006-alt1
- new version

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.003004-alt1
- automated CPAN update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.003003-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.003002-alt1
- automated CPAN update

* Thu Jan 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.003000-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.002005-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.002004-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.001001-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.001000-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 2.000002-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.006001-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.005000-alt1
- automated CPAN update

* Wed Mar 12 2014 Vladimir Lettiev <crux@altlinux.ru> 1.004002-alt1
- 1.003001 -> 1.004002

* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 1.003001-alt1
- 1.002000 -> 1.003001

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.002000-alt1
- 1.002000

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000004-alt1
- 1.000003 -> 1.000004
- don't require Moose

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000003-alt1
- 0.009014 -> 1.000003

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.009014-alt1
- 0.009014

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.009011-alt1
- initial build
