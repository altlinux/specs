%define dist XML-Parser
Name: perl-%dist
Version: 2.44
Release: alt2.1.1

Summary: Perl module for parsing XML files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libexpat-devel perl-devel perl-libwww

%description
XML::Parser is a Perl module for parsing XML documents.
It is built on top of XML::Parser::Expat, which is
a lower level interface to James Clark's expat library.

%prep
%setup -q -n %dist-%version
%patch -p1
cp -av samples examples
rm examples/REC-xml-19980210.xml

%build
%perl_vendor_build

# only *.enc files should be installed
find blib/lib/XML/Parser/Encodings -type f -not -name '*.enc' -print -delete

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/XML
%perl_vendor_autolib/XML

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.44-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.44-alt2.1
- rebuild with new perl 5.24.1

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.44-alt2
- dropped at@'s patch perl-XML-Parser-2.34-alt-style-subs.patch

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.44-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.44-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.43-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.41-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 2.41-alt4
- built for perl 5.18

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 2.41-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.41-alt2
- rebuilt for perl-5.14

* Wed Aug 10 2011 Alexey Tourbin <at@altlinux.ru> 2.41-alt1
- 2.40 -> 2.41

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 2.40-alt1
- 2.36 -> 2.40

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.36-alt2.1
- rebuilt for perl-5.12

* Fri Apr 10 2009 Alexey Tourbin <at@altlinux.ru> 2.36-alt2
- converted ISO-8859-* encoding names to uppercase

* Mon Mar 03 2008 Alexey Tourbin <at@altlinux.ru> 2.36-alt1
- 2.34 -> 2.36
- updated iso-8859-* and windows-125x encodings

* Mon Oct 16 2006 Alexey Tourbin <at@altlinux.ru> 2.34-alt6
- imported sources into git and built with gear
- patches from Joris van Rantwijk now really applied

* Sat Aug 12 2006 Alexey Tourbin <at@altlinux.ru> 2.34-alt5
- fix for carsh on utf8 stream (Joris van Rantwijk, cpan #19859, deb #378411)
- fix for off-by-one buffer overflow (Joris van Rantwijk, cpan #19860)

* Sun Jun 26 2005 Alexey Tourbin <at@altlinux.ru> 2.34-alt4
- added support for XSLoader (cpan #13420)

* Mon Jun 13 2005 Alexey Tourbin <at@altlinux.ru> 2.34-alt3
- don't ignore user exceptions when using Style => "Subs" (cpan #13204)
- removed examples/REC-xml-19980210.xml (156K)

* Thu Mar 10 2005 Alexey Tourbin <at@altlinux.ru> 2.34-alt2
- ACK NMU: re-added Cyrillic and Hebrew encodings (cpan #11917)
- updated BuildRequires
- manual pages not packaged (use perldoc)

* Mon Mar 07 2005 LAKostis <lakostis at altlinux.ru> 2.34-alt1.2
- add cyrillic encodings from livejournal cvs.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.34-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 2.34-alt1
- 2.34
- buildreq applied

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.org> 2.31-alt2
- rebuild with new perl

* Wed May 29 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.31-alt1
- New version
- Require libexpat, not expat

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.30-alt2
- Rebuilt with new perl.

* Tue Jul 03 2001 Mikhail Zabaluev <mhz@altlinux.ru> 2.30-alt1
- 2.30, shared expat is supported
- ALTified spec

* Thu Jul  6 2000 Mikhail Zabaluev <mookid@sigent.ru> 2.29-2mdk_mhz
- added documentation files
- cleaned out files, build

* Tue Jun 13 2000 Vincent Danen <vdanen@linux-mandrake.com> 2.29-1mdk
- initial specfile
- bzip sources
