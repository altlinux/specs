%define _unpackaged_files_terminate_build 1
%define dist Parallel-ForkManager
Name: perl-%dist
Version: 1.19
Release: alt1

Summary: A simple parallel processing fork manager
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/Y/YA/YANICK/Parallel-ForkManager-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-devel perl(Test/Warn.pm)

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%dir %perl_vendor_privlib/Parallel
%perl_vendor_privlib/Parallel/ForkManager.pm

%changelog
* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.7.9-alt1
- 0.7.5 -> 0.7.9

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.7.5-alt1
- initial revision
