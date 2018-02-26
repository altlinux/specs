%define dist Parse-RecDescent
Name: perl-%dist
Version: 1.966_000
Release: alt1

Summary: Perl module for generating recursive-descent parsers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Text-Balanced

%description
Parse::RecDescent is a Perl module for parser generators.
It incrementally generates top-down recursive-descent text
parsers from simple yacc(1)-like grammar specifications.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README tutorial demo
%perl_vendor_privlib/Parse

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.966_000-alt1
- 1.965001 -> 1.966_000

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 1.965.001-alt1
- 1.96.0 -> 1.965001

* Mon Mar 09 2009 Alexey Tourbin <at@altlinux.ru> 1.96.0-alt2
- fixed $Parse::RecDescent::VERSION (rt.cpan.org #32288)

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 1.96.0-alt1
- 1.94 -> 1.96.0

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.94-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Tue Jun 10 2003 Alexey Tourbin <at@altlinux.ru> 1.94-alt1
- 1.80 (Jan 2001) -> 1.94 (Apr 2003), oh my...
- Text::Balanced was removed in 1.92; I will resotre it in perl-base
- specfile cleanup; more docs added

* Thu Oct 31 2002 Alexey Tourbin <at@altlinux.ru> 1.80-alt2
- rebuilt for perl-5.8 with new rpm macros

* Wed Jul 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.80-alt1
- ALT adaptions.

* Sun Jun 17 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.80-2mdk
- Rebuild against the latest perl.

* Wed Jan 31 2001 François Pons <fpons@mandrakesoft.com> 1.80-1mdk
- 1.80.

* Tue Nov 14 2000 François Pons <fpons@mandrakesoft.com> 1.79-2mdk
- fixed description.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.79-1mdk
- 1.79.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 1.78-4mdk
- macroszifications.
- noarch.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 1.78-3mdk
- removed perllocal.pod file.

* Sun Jul 09 2000 David BAUDENS <baudens@mandrakesoft.com> 1.78-2mdk
- Fix build
- Rename spec according to package's name & little spec cleanup
- Remove french description & summary (in po)

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.78-1mdk
- 1.78
- fixed group
- rebuild with new perl
- fixed location
- better patch for annoying /usr/local/bin/perl's

* Tue Nov 23 1999 François PONS <fpons@mandrakesoft.com>
- upgraded to version 1.77
- Build release.

* Tue Oct 19 1999 François PONS <fpons@mandrakesoft.com>
- upgraded to version 1.70

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix bogus spec

* Tue Jul 22 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- add french description
- write a real english description

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 source
- Mandrake adaptation
