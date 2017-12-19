%define dist XML-LibXML
%def_without bootstrap
Name: perl-%dist
Version: 2.0132
Release: alt1

Summary: Perl binding for libxml2
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

Provides: perl-XML-LibXML-Common = 0.13-alt99
Obsoletes: perl-XML-LibXML-Common < 0.13-alt99

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libxml2-devel perl-Devel-CheckLib perl-Test-Differences perl-Test-Pod perl-URI perl-XML-NamespaceSupport

%if_with bootstrap
BuildRequires: perl-XML-SAX-Base
%define _without_test 1
%else
BuildRequires: perl-XML-SAX
%endif

%description
This module is an interface to the Gnome libxml2 DOM and SAX parser and
the DOM tree.  It also provides an XML::XPath-like findnodes() interface,
providing access to the XPath API in libxml2.

%prep
%setup -n %dist-%version
rm -r inc
%patch -p1

%if_with bootstrap
# bootstrap: disable build dependency on XML::SAX
mv t/14sax.t t/14sax.t.orig
mv t/48_SAX_Builder_rt_91433.t t/48_SAX_Builder_rt_91433.t.orig
%endif

%build
%perl_vendor_build INC=-I/usr/include/libxml2 LIBS=-lxml2

%install
%perl_vendor_install

%files
%doc	Changes README HACKING.txt docs example
%dir	%perl_vendor_archlib/XML
	%perl_vendor_archlib/XML/LibXML.pm
%doc	%perl_vendor_archlib/XML/LibXML.pod
%dir	%perl_vendor_archlib/XML/LibXML
	%perl_vendor_archlib/XML/LibXML/*.pm
%doc	%perl_vendor_archlib/XML/LibXML/*.pod
%dir	%perl_vendor_archlib/XML/LibXML/SAX
	%perl_vendor_archlib/XML/LibXML/SAX/*.pm
%doc	%perl_vendor_archlib/XML/LibXML/SAX/*.pod
	%perl_vendor_autolib/XML

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.0132-alt1
- automated CPAN update

* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.0129-alt2
- unbootstrap

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.0129-alt1.1
- rebuild with new perl 5.26.1

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.0129-alt1
- automated CPAN update

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 2.0128-alt1.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.0128-alt1.1
- rebuild with new perl 5.24.1

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.0128-alt1
- automated CPAN update

* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.0124-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 2.0122-alt1.2
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.0122-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.0122-alt1
- automated CPAN update

* Sat Dec 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.0117-alt2.2
- unbootstrap

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.0117-alt2.1
- rebuild with new perl 5.20.1

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 2.0117-alt2
- build fixes for bootstrap mode

* Wed Nov 12 2014 Dmitry V. Levin <ldv@altlinux.org> 2.0117-alt1
- 2.0116 -> 2.0117.

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.0116-alt1
- new version 2.0116

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0106-alt1
- 2.0103 -> 2.0106

* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0103-alt2
- enabled build dependency on XML::SAX

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0103-alt1
- 2.0014 -> 2.0103
- disabled build dependency on XML::SAX

* Wed Mar 27 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0014-alt1
- 2.0004 -> 2.0014

* Sun Sep 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.0004-alt2
- enabled build dependency on XML::SAX

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 2.0004-alt1
- 2.0002 -> 2.0004
- built fot perl-5.16
- disabled build dependency on XML::SAX

* Wed Jul 18 2012 Dmitry V. Levin <ldv@altlinux.org> 2.0002-alt1
- 1.96 -> 2.0002

* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.96-alt1
- 1.88 -> 1.96
- enabled build dependency on XML::SAX

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.88-alt1
- 1.70 -> 1.88
- built for perl-5.14
- disabled build dependency on XML::SAX

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 1.70-alt2
- fixed building without zlib-devel

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.70-alt1.1
- rebuilt with perl 5.12
- fixed build

* Sat Mar 27 2010 Alexey Tourbin <at@altlinux.ru> 1.70-alt1
- 1.69 -> 1.70
- provides and obsoletes perl-XML-LibXML-Common

* Thu Jul 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.69-alt1.1
- Rebuilt to fix build of perl-XML-LibXSLT package.

* Wed Nov 12 2008 Alexey Tourbin <at@altlinux.ru> 1.69-alt1
- 1.68 -> 1.69

* Sat Nov 08 2008 Alexey Tourbin <at@altlinux.ru> 1.68-alt1
- 1.66 -> 1.68

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 1.66-alt2
- relaxed dependency on perl-XML-SAX

* Fri Feb 22 2008 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.65 -> 1.66

* Tue Oct 02 2007 Alexey Tourbin <at@altlinux.ru> 1.65-alt1
- 1.63+svn669 -> 1.65

* Sun Jul 22 2007 Alexey Tourbin <at@altlinux.ru> 1.63-alt2
- merged fixes from svn://axkit.org/XML-LibXML (revision 669)

* Mon Apr 16 2007 Alexey Tourbin <at@altlinux.ru> 1.63-alt1
- 1.62 -> 1.63

* Mon Nov 20 2006 Alexey Tourbin <at@altlinux.ru> 1.62-alt1
- 1.61_2 -> 1.62

* Wed Nov 15 2006 Alexey Tourbin <at@altlinux.ru> 1.61-alt1
- 1.60 -> 1.61_2
- imported sources into git and built with gear
- decoupled perl-XML-LibXML-Common
- compiled with CCFLAGS=-fvisibility=hidden to hide C symbols
- fixed @ARGV handling in Makefile.PL, so that PRINT_PREREQ works (cpan #23286)

* Sun Aug 27 2006 Alexey Tourbin <at@altlinux.ru> 1.60-alt1
- 1.59 -> 1.60

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 1.59-alt1
- 1.58 -> 1.59

* Tue May 30 2006 Alexey Tourbin <at@altlinux.ru> 1.58-alt5
- removed post/preun scriplets (should fix #8175)

* Fri Dec 17 2004 Alexey Tourbin <at@altlinux.ru> 1.58-alt4
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Tue Aug 03 2004 Alexey Tourbin <at@altlinux.ru> 1.58-alt3
- reworked %%post and %%preun scriplets

* Wed Apr 28 2004 Alexey Tourbin <at@altlinux.ru> 1.58-alt2
- packaged %dist-Common-0.13 here (laziness is virtue)
- added triggers to register/unregister XML::LibXML::SAX::Parser

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 1.58-alt1
- 1.56 -> 1.58, things kind of work!

* Tue Jan 13 2004 Alexey Tourbin <at@altlinux.ru> 1.56-alt2
- fixed duplicate `extern' (gcc3.3)
- 02parse test disabled (recent libxml2 broken)

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 1.56-alt1
- 1.56
- buildreq applied (fixes build in the hasher)
- descriptions updated

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 1.54-alt1
- 1.54

* Wed Nov 20 2002 Stanislav Ievlev <inger@altlinux.ru> 1.53-alt1
- Initial release
