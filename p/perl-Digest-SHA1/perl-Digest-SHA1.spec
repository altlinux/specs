%define dist Digest-SHA1
Name: perl-%dist
Version: 2.13
Release: alt3

Summary: Perl interface to the SHA1 algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs. The algorithm takes
as input a message of arbitrary length and produces as output
a 160-bit "fingerprint" or "message digest" of the input.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Digest
%perl_vendor_archlib/Digest

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.13-alt3
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.13-alt2
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.13-alt1.1
- rebuilt with perl 5.12

* Mon Aug 09 2010 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.12 -> 2.13

* Sun May 24 2009 Alexey Tourbin <at@altlinux.ru> 2.12-alt1
- 2.11 -> 2.12

* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 2.11-alt3
- rebuild

* Thu Apr 19 2007 Alexey Tourbin <at@altlinux.ru> 2.11-alt2
- cleanup

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 2.11-alt1
- 2.10 -> 2.11

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 2.10-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Sun May 09 2004 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- 2.07 -> 2.10
- reset.patch dropped, dependency on Digest/base.pm added instead

* Thu Dec 11 2003 Alexey Tourbin <at@altlinux.ru> 2.07-alt2
- reset.patch: `reset' method restored (fixes Digest::HMAC)

* Sat Dec 06 2003 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- 2.07
- description updated

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 2.02-alt1
- 2.02

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 2.01-alt2
- rebuild with new key

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2.01-alt1
- 2.01

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 2.00-alt2
- Rebuilt with new perl

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.00-alt1
- First build for Sisyphus
- Some spec cleanup

* Sun Jun 24 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.00-2mdk
- Clean file list.

* Fri Jun 22 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.00-1mdk
- First release, was in perl-Digest-MD5 package before.
