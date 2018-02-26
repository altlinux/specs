Name: perl-SGMLSpm
Version: 1.03ii
Release: alt6

Summary: Perl library for parsing the output of nsgmls
License: GPL
Group: Publishing

URL: http://search.cpan.org/dist/SGMLSpm/
Source: http://www.cpan.org/modules/by-module/SGMLS/SGMLSpm-%version.tar.gz

BuildArch: noarch

Requires: jade >= 1.2.1

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%prep
%setup -q -n SGMLSpm

%install
mkdir -p %buildroot%_bindir %buildroot%perl_vendor_privlib
make install_system BINDIR=%buildroot%_bindir PERL5DIR=%buildroot%perl_vendor_privlib

%files
%doc BUGS DOC/ elisp
%_bindir/sgmlspl
%perl_vendor_privlib/SGMLS*
%perl_vendor_privlib/skel.pl

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 1.03ii-alt6
- rebuilt

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 1.03ii-alt5
- Spec cleanups.

* Wed Nov 20 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.03ii-alt4
- rebuilt for perl 5.8.0, returning from orphaned
- new perl macros and directories

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.03ii-alt3
- Rebuilt with perl-5.6.1

* Tue Jun 12 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3ii-alt2
- specfile cleanup
- AutoReqProv: perl

* Thu May 31 2001 AEN <aen@logic.ru> 1.0.3ii-alt1
- build fo Sisyphus

* Fri Jan 12 2001 Camille Begnis <camille@mandrakesoft.com> 1.03ii-1mdk
- New for Mandrake
- Mandrakized from ftp://sources.redhat.com/pub/docbook-tools/new-trials/SPECS/perl-SGMLSpm.spec
