%define _unpackaged_files_terminate_build 1
%define dist Net-Pcap
Name: perl-%dist
Version: 0.21
Release: alt1

Summary: Interface to pcap(3) LBL packet capture library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/C/CO/CORION/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libpcap-devel perl-Test-Exception perl-Test-Pod perl-podlators

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library.
The README for libpcap describes itself as:

"a system-independent interface for user-level packet capture.
libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection,
security monitoring, network debugging, etc."

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/pcapinfo
%_man1dir/pcapinfo.1*
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 0.21-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.20-alt1
- automated CPAN update

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 0.19-alt1
- automated CPAN update

* Sat Apr 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2.1
- rebuild: hack around alt bug 38332

* Sat Mar 02 2019 Sergey Y. Afonin <asy@altlinux.ru> 0.18-alt2
- added patches from Fedora Core:
  Net-Pcap-0.18-Adapt-a-test-to-libpcap-1.8.0.patch
  Net-Pcap-0.18-Fix-build-with-libpcap-1.9.0.patch

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.1
- rebuild with new perl 5.24.1

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- 0.16 -> 0.17

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt2.1
- rebuilt with perl 5.12

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.16-alt2
- fixed directory ownership viloation

* Wed Mar 05 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.16-alt1
- new version

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.14-alt1
- new version

* Tue Jul 27 2004 Alexander V. Denisov <rupor at altlinux dot ru> 0.05-alt1
- Initial build for ALTLinux
