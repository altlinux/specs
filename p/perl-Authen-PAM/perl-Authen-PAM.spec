%define dist Authen-PAM
Name: perl-%dist
Version: 0.16
Release: alt5

Summary: Perl interface to PAM library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch0: Authen-PAM-0.16-Fix-building-on-Perl-without-dot-in-INC.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libpam-devel perl-devel

%description
This module provides a Perl interface to the PAM library (Pluggable
Authentication Modules, a flexible mechanism for authenticating users).

%prep
%setup -q -n %dist-%version
%patch0 -p1
sed -i- 's/die/warn/' test.pl

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Authen
%perl_vendor_autolib/Authen

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5
- support for perl 5.26

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2.3
- rebuilt for perl-5.14

* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2.2
- rebuilt

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt2.1
- rebuilt with perl 5.12

* Tue Oct 04 2005 Alexey Tourbin <at@altlinux.ru> 0.16-alt2
- 0.16 (release)
- alt-static.patch merged upstream (cpan #13477)
- alt-posix.patch merged upstream (cpan #13478)

* Thu Jun 30 2005 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- 0.14 -> 0.16 (development release)
- PAM.xs: made plain C functions static (cpan #13477)
- PAM.pm: explicitly specified import list for POSIX module (cpan #13478)
- specfile cleanup
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.14-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.14-alt1
- 0.14

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.13-alt2
- rebuild with new perl

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.13-alt1
- Rebuilt in new environment
- 0.13
- Some spec cleanup

* Mon Nov 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.12-alt1
- Adopted for Sisyphus

* Thu Nov 08 2001 François Pons <fpons@mandrakesoft.com> 0.12-1mdk
- 0.12.

* Tue Oct 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.11-3mdk
- BuildRequires: pam-devel perl-devel

* Mon Jul  2 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.11-2mdk
- rebuild

* Thu Apr 19 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 0.11-1.1mdk
- removed samples from doc
- changed spec name

* Thu Apr 12 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 0.11-1mdk
- First Mandrake release

