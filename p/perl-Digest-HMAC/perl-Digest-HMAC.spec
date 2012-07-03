%define dist Digest-HMAC
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: Keyed-Hashing for Message Authentication
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-Digest-SHA perl-devel

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1.  The HMAC mechanism is described in
RFC 2104.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Digest

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.02 -> 1.03
- rebuilt as plain src.rpm

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.01 -> 1.02

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 1.01-alt5
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.01-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 1.01-alt4
- buildreq re-applied (fixes build in the hasher)
- description updated

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 1.01-alt3
- Rebuild with new perl.

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 1.01-alt2
- Rebuilt with new perl.

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.01-alt1
- First build for Sisyphus
- Some spec cleanup

* Sun Jun 24 2001 Christian Belisle <cbelisle@mandrakesoft.com> 1.01-3mdk
- Clean the file list (to build a good cpio). Thanx to Brian.

* Fri Jun 22 2001 Christian Belisle <cbelisle@mandrakesoft.com> 1.01-2mdk
- Added a make test for compilation
- Fixed a typo in the changelog's date.
- Added a Require for perl-Digest-SHA1.

* Fri Jun 22 2001 Christian Belisle <cbelisle@mandrakesoft.com> 1.01-1mdk
- First release, was in perl-Digest-MD5 package before.
