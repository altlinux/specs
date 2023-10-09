%define _unpackaged_files_terminate_build 1
%define dist EV
Name: perl-%dist
Version: 4.34
Release: alt1

Summary: Perl interface to libev, a high performance full-featured event loop
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: perl-AnyEvent perl-common-sense perl-devel perl-podlators perl(Canary/Stability.pm)

%description
This module provides an interface to libev
(<http://software.schmorp.de/pkg/libev.html>). While the documentation
below is comprehensive, one might also consult the documentation of
libev itself (<http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod> or
perldoc EV::libev) for more subtle details on watcher semantics or some
discussion on the available backends, or how to force a specific backend
with "LIBEV_FLAGS", or just about in any case because it has much more
detailed information.

%prep
%setup -q -n %{dist}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/EV*
%perl_vendor_autolib/EV

%changelog
* Mon Oct 09 2023 Igor Vlasenko <viy@altlinux.org> 4.34-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.33-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 4.32-alt1
- automated CPAN update

* Wed Dec 25 2019 Igor Vlasenko <viy@altlinux.ru> 4.31-alt1
- automated CPAN update

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.30-alt1
- automated CPAN update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 4.27-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.25-alt1.1
- rebuild with new perl 5.28.1

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 4.25-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.22-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.22-alt1.1
- rebuild with new perl 5.24.1

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 4.22-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.21-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 4.21-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1.1
- rebuild with new perl 5.20.1

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.17-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 4.16-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 4.15-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.15-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 4.11-alt1
- 4.03 -> 4.11
- built for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 4.03-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 3.9-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1
- automated CPAN update

* Mon Oct 19 2009 Michael Bochkaryov <misha@altlinux.ru> 3.8-alt1
- initial build for ALT Linux Sisyphus
