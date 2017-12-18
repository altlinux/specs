%define _unpackaged_files_terminate_build 1
%define module Net-DNS

# hack to save perl autodep finder from crashing (suggested by Alexey Tourbin)
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MNet::DNS'

Name: perl-%module
Version: 1.14
Release: alt1

Packager: Vladimir Didenko <cow@altlinux.org>

Summary: Net::DNS is a DNS resolver implemented in Perl
License: Perl
Group: Development/Perl
BuildArch: noarch

Url: %CPAN %module
# another URL: http://www.net-dns.org/
Source0: http://www.cpan.org/authors/id/N/NL/NLNETLABS/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Digest-BubbleBabble perl-Digest-HMAC perl-IO-Socket-INET6 perl-Net-IP perl-Test-Pod

%description
Net::DNS is a DNS resolver implemented in Perl. It allows the programmer to
perform nearly any type of DNS query from a Perl script.

%prep
%setup -q -n %{module}-%{version}

# Fix test that will not succeed in Sisyphus build environment.
#sed -i- 's/tests=>12/tests=>11/; s/use Net::DNS::Nameserver;/exit;/' t/11-inet6.t

# Try to fix another failing test.
#sed -i- '/sock->sockaddr/s/;/ if $sock;/' t/01-resolver.t

%build
%perl_vendor_build --no-online-tests

%install
%perl_vendor_install

%files
%doc Changes README demo contrib
%perl_vendor_privlib/Net
#%perl_vendor_autolib/Net
# no more installed
#exclude %perl_vendor_archlib/Net/DNS/Resolver/Cygwin.pm
#exclude %perl_vendor_archlib/Net/DNS/Resolver/Win32.pm

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1.1
- rebuild with new perl 5.20.1

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Mon Nov 11 2013 Vladimir Didenko <cow@altlinux.org> 0.72-alt3
- fix memory leak (closes: #29564)

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt2
- built for perl 5.18

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.68-alt1
- 0.68
- built for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.66-alt1.2
- rebuilt for perl-5.14
- fixed failing test in hasher

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1.1
- rebuilt with perl 5.12

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.66-alt1
- 0.66

* Mon Oct 05 2009 Victor Forsyuk <force@altlinux.org> 0.65-alt1
- 0.65

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.63-alt1
- 0.63

* Wed Jan 09 2008 Victor Forsyuk <force@altlinux.org> 0.62-alt1
- 0.62

* Mon Aug 13 2007 Victor Forsyuk <force@altlinux.org> 0.61-alt1
- 0.61
- Build with support for IPv6 transport.

* Tue Jun 26 2007 Victor Forsyuk <force@altlinux.org> 0.60-alt1
- 0.60 (this version fixes potential security problems).

* Fri Jan 19 2007 Victor Forsyuk <force@altlinux.org> 0.59-alt1
- 0.59
- Better Summary and %%description.
- Updated BuildRequires.

* Sun Apr 17 2005 DH <dh@altlinux.ru> 0.49-alt1
- New version
- Minor changes in spec
- Bug 6500

* Sat Nov 13 2004 DH <dh@altlinux.ru> 0.48-alt1
- New version

* Sat Apr 17 2004 DH <dh@altlinux.ru> 0.47-alt1
- New version

* Sun Dec 14 2003 DH <dh@altlinux.ru> 0.44-alt1
- New version

* Tue Oct 7 2003 DH <dh@dh.net.ru> 0.41-alt2
- Bugs (Win32.pm)

* Mon Oct 6 2003 DH <dh@dh.net.ru> 0.41-alt1
- New version
- Patch which remove Win32.pm /*dirty, but works*/
- Patch for DNS::Resolver (eval for init)

* Sun Sep 7 2003 DH <dh@dh.net.ru> 0.40-alt1
- New version
- Minor changes in spec

* Sun Jun 1 2003 DH <dh@dh.net.ru> 0.37-alt1
- New version
- Minor changes in spec

* Fri Mar 21 2003 DH <dh@dh.net.ru> 0.34-alt1
- New version
- Add patch disabling online tests

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.29-alt1
- rebuild with new perl

* Wed Dec 26 2001 DH <dh@dh.net.ru> 0.12-alt1
- First release.
