BuildRequires: perl(Module/Build.pm)
%define dist XML-Twig
Name: perl-%dist
Version: 3.39
Release: alt1

Summary: A perl module for processing huge XML documents in tree mode
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: expat perl-HTML-Tree perl-IO-String perl-IO-stringy perl-Test-Pod perl-Tie-IxHash perl-XML-SAX-Writer perl-XML-Simple perl-XML-XPath perl-YAML perl-podlators perl-unicore

%description
This module provides a way to process XML documents. It is build on top
of XML::Parser.  The module offers a tree interface to the document, while
allowing you to output the parts of it that have been completely processed.

This package also contains the following utilities:

xml_pp		XML pretty printer
xml_grep	grep XML files looking for specific elements
xml_spellcheck	spellcheck XML files skipping tags
xml_split	cut a big XML file into smaller chunks
xml_merge	merge back XML files split with xml_split

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc	Change* README
	%_bindir/xml_*
	%_man1dir/xml_*
%dir	%perl_vendor_privlib/XML
	%perl_vendor_privlib/XML/Twig.pm
%dir	%perl_vendor_privlib/XML/Twig
	%perl_vendor_privlib/XML/Twig/XPath.pm

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.39-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.38-alt1
- automated CPAN update

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 3.37-alt1
- 3.29 -> 3.37

* Tue Jan 23 2007 Alexey Tourbin <at@altlinux.ru> 3.29-alt1
- 3.26 -> 3.29

* Fri Sep 01 2006 Alexey Tourbin <at@altlinux.ru> 3.26-alt2
- fixed test suite, which broke due to changes in perl-5.8.8@28443
  peephole optimiser; illegal division 0/0 is now ok at compile time
  because of the possibility of unreachable code
- packaged manual pages for xml_grep et al.

* Tue Jul 04 2006 Alexey Tourbin <at@altlinux.ru> 3.26-alt1
- 3.25 -> 3.26

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 3.25-alt1
- 3.21 -> 3.25

* Fri Sep 23 2005 Alexey Tourbin <at@altlinux.ru> 3.21-alt1
- 3.17 -> 3.21
- alt-xml_split.patch merged upstream (cpan #11911, #11912)

* Thu Mar 17 2005 Alexey Tourbin <at@altlinux.ru> 3.17-alt1
- 3.16 -> 3.17
- fixed bugs in xml_split (cpan #11911, #11912)
- license: GPL or Artistic (cpan #11725)

* Thu Mar 03 2005 Alexey Tourbin <at@altlinux.ru> 3.16-alt1
- 3.15 -> 3.16
- packaged xml_split and xml_merge
- updated license and filed minor license issue (cpan #11725)

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 3.15-alt2
- updated BuildRequires (with buildreq)
- manual pages not packaged (use perldoc)

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 3.15-alt1
- 3.11 -> 3.15
- buildreq reapplied (fewer tests skipped)
- packaged scripts (xml_grep et al), description updated

* Thu Oct 30 2003 Alexey Tourbin <at@altlinux.ru> 3.11-alt1
- 3.11
- descriptions updated

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 3.09-alt1
- 3.09

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 3.08-alt1
- rebuild with new perl

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 2.02-alt1
- We need it for foomatic too.

* Mon Jun 18 2001 Till Kamppeter <till@mandrakesoft.com> 2.02-1mdk
- Newly introduced for Foomatic.
