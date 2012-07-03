%define dist HTML-SimpleParse
Name: perl-%dist
Version: 0.12
Release: alt2.1.1

Summary: A bare-bones but effective HTML parser
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat May 15 2004
BuildRequires: perl-Module-Build perl-devel

%description
A bare-bones but effective HTML parser. Use the HTML::SimpleParse module
when you need to retrieve HTML syntax without building a hierarchical
tree of HTML content, matching tags, verifying contexts and so on.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/HTML*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.12-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat May 15 2004 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt with Module::Build

* Tue Jul 29 2003 Stanislav Ievlev <inger@altlinux.ru> 0.12-alt1
- 0.12

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 0.11-ipl3mdk
- 0.11

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.10-ipl3mdk
- rebuild with new perl

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 0.10-ipl2mdk
- Rebuilt with perl-5.6.1

* Mon Jan 29 2001 Mikhail Zabaluev <zabaluev@parascript.com> 0.10-ipl1mdk
- Changed:
  + adapted spec for Sisyphus
  + verbose description in English and Russian

* Tue Nov 14 2000 François Pons <fpons@mandrakesoft.com> 0.10-3mdk
- updated license to the perl one (as mentioned in license).

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 0.10-2mdk
- macroszifications.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 0.10-1mdk
- make a noarch package.
- 0.10.

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.08-2mdk
- fixed group
- rebuild with new perl
- fixed location

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 0.08-1mdk
- upgraded to 0.08

* Mon Sep 06 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- created rpm
