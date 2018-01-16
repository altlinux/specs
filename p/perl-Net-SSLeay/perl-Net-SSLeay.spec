%define _unpackaged_files_terminate_build 1
%define dist Net-SSLeay
Name: perl-%dist
Version: 1.83
Release: alt1

Summary: Perl extension for using OpenSSL
License: BSD-style
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MI/MIKEM/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: libssl-devel openssl perl-Test-Exception perl-Test-NoWarnings perl-Test-Pod perl-Test-Warn perl-threads

%description
This module offers some high level convinience functions for accessing
web pages on SSL servers, a sslcat() function for writing your own
clients, and finally access to the SSL api of SSLeay/OpenSSL package
so you can write servers or clients for more complicated applications.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build LIBS='-lssl -lcrypto'

%install
%perl_vendor_install

%files
%doc Changes Credits README examples QuickRef README.OSX README.VMS README.Win32
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.83-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.82-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.81-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.68-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.66-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.66-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.63-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.62-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.61-alt1
- automated CPAN update

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.57-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 1.55-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- 1.48 -> 1.49

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 1.48-alt1
- 1.42 -> 1.48
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.42-alt1
- 1.36 -> 1.42
- built for perl-5.14
- rebuilt as plain src.rpm

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.36-alt1.1
- rebuilt with perl 5.12

* Wed Mar 03 2010 Alexey Tourbin <at@altlinux.ru> 1.36-alt1
- 1.35 -> 1.36

* Sun Aug 24 2008 Alexey Tourbin <at@altlinux.ru> 1.35-alt2
- rebuilt with libssl.so.7

* Sun Jul 27 2008 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.33_01 -> 1.35

* Fri Mar 07 2008 Alexey Tourbin <at@altlinux.ru> 1.33_01-alt1
- 1.25 -> 1.33_01
- changed license tag to "BSD-like" (that of OpenSSL)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.25-alt3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Mar 17 2005 Alexey Tourbin <at@altlinux.ru> 1.25-alt3
- sync with debian libnet-ssleay-perl_1.25-1.1:
  + fix insecure entropy source in SSLeay.pm (CAN-2005-0106)
  + fixes two outstanding memory leaks in SSLeay.pm
  + fixes broken usage of MIME::Base64 in example
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.25-alt2.1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.25-alt2.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 24 2004 Alexey Tourbin <at@altlinux.ru> 1.25-alt2
- don't contact external sites during tests when inside BTE
- updated description
- packaged QuickRef

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 1.25-alt1
- 1.22 -> 1.25
- package renamed: perl-Net_SSLeay -> perl-Net-SSLeay
- patch for Makefile.PL updated
- out-of-memory.patch: reduce big defaults (2G -> 200M)

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 1.22-alt1
- 1.22

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.21-alt2
- fixed library link

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.21-alt1
- rebuild with new perl

* Fri Jun 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.17-alt1
- 1.17

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.13-alt1
- 1.13

* Thu Nov 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.05-ipl8mdk
- Specfile cleanup.
- Added some more useless provides.

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.05-ipl7mdk
- Rebuilt with new perl again

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.05-ipl6mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Sep 1 2000 Philippe Libat <philippe@mandrakesoft.com> 1.05-4mdk
- corrected /usr/local/bin

* Thu Aug 31 2000 Philippe Libat <philippe@mandrakesoft.com> 1.05-3mdk
- doc
- macroszifications.

* Tue Aug 10 1999  Rex Wu <rex@intercept.com.tw>
- Spec file was generated.
