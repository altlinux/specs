%define dist Digest-MD2
Name: perl-%dist
Version: 2.03
Release: alt2.3

Summary: Perl interface to the MD2 Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
The Digest::MD2 module allows you to use the RSA Data Security Inc.
MD2 Message Digest algorithm from within Perl programs.  The algorithm
takes as input a message of arbitrary length and produces as output
a 128-bit "fingerprint" or "message digest" of the input.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.03-alt2.3
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.03-alt2.2
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.03-alt2.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.03-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Oct 30 2003 Alexey Tourbin <at@altlinux.ru> 2.03-alt1
- 2.03
- descriptions updated

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 2.01-alt1
- 2.01

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 2.00-alt3
- rebuild with new perl

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 2.00-alt2
- Rebuilt with new perl.

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.00-alt1
- First build for Sisyphus
- Some spec cleanup

* Sun Jun 24 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.00-2mdk
- Clean the file list.

* Fri Jun 22 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.00-1mdk
- First release, was in perl-Digest-MD5 package before.
