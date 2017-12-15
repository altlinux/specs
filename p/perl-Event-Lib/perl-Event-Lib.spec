%define dist Event-Lib
Name: perl-%dist
Version: 1.03
Release: alt5.1.1.1.1

Summary: Perl extentions for event-based programming
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch1: Event-Lib-tests-fork.patch

# in 5.16 get_sv("$", FALSE) returns NULL sometimes
# use getpid() call instead
Patch2: Event-Lib-getpid.patch

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libevent-devel perl-Test-Fork perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is a Perl wrapper around libevent(3) as available from
<http://www.monkey.org/~provos/libevent/>.  It allows to execute a function
whenever a given event on a filehandle happens, a timeout occurs or a signal
is received.

%prep
%setup -q -n %dist-%version
%patch1 -p1
%patch2 -p2
if [ %version = 1.03 ]; then
#Known to fail - Upstream emailed
rm t/20_signal.t
rm t/51_cleanup_persistent.t
rm t/90_leak.t
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Event
%perl_vendor_autolib/Event

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5.1
- rebuild with new perl 5.20.1

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5
- fixed build before perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt3
- rebuilt for perl-5.16
- fixed build

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2.2
- rebuilt for perl-5.14

* Sat Jun 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2.1.1
- rebuilt with libevent2

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2.1
- rebuilt with perl 5.12

* Mon Jul 13 2009 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- fix tests with fork

* Sat Aug 23 2008 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- Initial build for Sisyphus
