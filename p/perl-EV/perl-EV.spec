%define dist EV
Name: perl-%dist
Version: 4.03
Release: alt2

Summary: Perl interface to libev, a high performance full-featured event loop
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: perl-AnyEvent perl-common-sense perl-devel perl-podlators

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
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes COPYING README
%perl_vendor_archlib/EV*
%perl_vendor_autolib/EV

%changelog
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
