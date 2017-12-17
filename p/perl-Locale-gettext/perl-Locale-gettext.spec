%define dist gettext
Name: perl-Locale-gettext
Version: 1.07
Release: alt1.1.1.1

Summary: Gettext routines for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: perl-Locale-gettext-%version-%release.patch

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Encode perl-devel

%description
Locale::gettext module permits access from perl to the gettext() family
of functions for retrieving message strings from databases constructed
to internationalize software.

%prep
%setup -n %dist-%version
%patch -p1

%build
# non-POSIX locale required for tests
export LC_ALL=en_US
%perl_vendor_build LIBS=

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_autolib/Locale
%perl_vendor_archlib/Locale

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- new version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt7.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt7
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt6
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt5
- rebuilt for perl-5.14

* Sun Dec 26 2010 Dmitry V. Levin <ldv@altlinux.org> 1.05-alt4
- Fixed conflict between Locale::Gettext and POSIX
  (closes: #24826).
- Resurrected changes lost in 1.05-alt3.

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt3.1
- rebuilt with perl 5.12

* Sun Apr 12 2009 Alexey Tourbin <at@altlinux.ru> 1.05-alt3
- rebuild

* Thu Apr 19 2007 Alexey Tourbin <at@altlinux.ru> 1.05-alt2
- cleanup

* Thu Jun 02 2005 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.04 -> 1.05
- removed emulation code
- clarified dependency on Encode

* Wed Feb 02 2005 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.03 -> 1.04
- manual pages not packaged (use perldoc)

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.01 -> 1.03
- renamed: perl-%dist -> %name

* Thu Sep 11 2003 Alexey Tourbin <at@altlinux.ru> 1.01-alt3
- buildreq applied

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.org> 1.01-alt2
- rebuild with new perl

* Tue Aug 21 2001 Stanislav Ievlev <inger@altlinux.ru> 1.01-alt1
- 1.01

* Thu Jun 14 2001 Pixel <pixel@mandrakesoft.com> 1.0-9mdk
- rebuild for new rpm

* Fri Jun 01 2001 Stefan van der Eijk <stefan@eijk.nu> 1.0-8mdk
- BuildRequires: gettext-devel perl-devel

* Thu Mar 22 2001 Pixel <pixel@mandrakesoft.com> 1.0-7mdk
- require perl-base instead of perl

* Thu Feb 22 2001 Pixel <pixel@mandrakesoft.com> 1.0-6mdk
- a lot of cleanup

* Wed Feb 14 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-5mdk
- adapted to mdk
- cleaned and fixed the spec file

* Wed Aug 11 1999 Motonobu Ichimura <g95j0116@mn.waseda.ac.jp>
- use BuildRoot and some changes added
- fixed .packlist
