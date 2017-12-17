Name: perl-TokyoCabinet
Version: 1.34
Release: alt4.1.1.1.1

Summary: TokyoCabinet - Perl module
License: LGPL
Group: Development/Perl

URL: http://fallabs.com/tokyocabinet/perlpkg/
Source: tokyocabinet-perl-%version.tar

Provides: perl-tokyocabinet = %version

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: bzlib-devel libtokyocabinet-devel perl-Encode perl-devel zlib-devel

%description
TokyoCabinet perl module.

%package doc
Summary: Documentation for Perl binding to the Tokyo Cabinet
Group: Documentation
Provides: %name-doc-html = %version
Conflicts: %name < %version
BuildArch: noarch

%description doc
Documentation for Perl binding to the Tokyo Cabinet.

%prep
%setup -n tokyocabinet-perl-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm %buildroot%perl_vendor_archlib/*.pl

%define pkgdocdir %_docdir/%name-%version
mkdir -p %buildroot%pkgdocdir/{example,html}
cp -a doc/* %buildroot%pkgdocdir/html/
cp -a example/* %buildroot%pkgdocdir/example/

%files
%perl_vendor_archlib/TokyoCabinet*
%perl_vendor_autolib/TokyoCabinet

%files doc
%pkgdocdir

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.34-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.34-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.34-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt3
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.34-alt2
- rebuilt for perl-5.14

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt1
- 1.34
- updated URL
- dropped packager tag

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.33-alt1.1
- rebuilt with perl 5.12

* Wed Nov 11 2009 Led <led@altlinux.ru> 1.33-alt1
- 1.33

* Mon Jul 20 2009 Led <led@altlinux.ru> 1.32-alt2
- docs moved into separate subpackage

* Mon Jul 20 2009 Led <led@altlinux.ru> 1.32-alt1
- 1.32

* Thu Jul 16 2009 Led <led@altlinux.ru> 1.31-alt1
- 1.31

* Sat Jul 11 2009 Led <led@altlinux.ru> 1.30-alt1
- 1.30

* Sat Jun 27 2009 Led <led@altlinux.ru> 1.29-alt1
- 1.29

* Sun May 24 2009 Led <led@altlinux.ru> 1.28-alt1
- 1.28

* Sun Apr 26 2009 Led <led@altlinux.ru> 1.26-alt1
- 1.26

* Tue Apr 07 2009 Led <led@altlinux.ru> 1.25-alt1
- 1.25

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.24-alt1
- 1.24

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.23-alt1
- 1.23

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.22-alt1
- 1.22

* Mon Dec 15 2008 Led <led@altlinux.ru> 1.20-alt1
- 1.20

* Mon Dec 15 2008 Led <led@altlinux.ru> 1.19-alt2
- rebuild with libtokyocabinet.so.6

* Sun Dec 07 2008 Led <led@altlinux.ru> 1.19-alt1
- 1.19

* Thu Oct 30 2008 Led <led@altlinux.ru> 1.18-alt1
- 1.18

* Tue Sep 09 2008 Led <led@altlinux.ru> 1.16-alt1
- 1.16

* Fri Aug 29 2008 Led <led@altlinux.ru> 1.15-alt1
- 1.15

* Thu Aug 07 2008 Led <led@altlinux.ru> 1.14-alt1
- 1.14

* Thu Jul 31 2008 Led <led@altlinux.ru> 1.13-alt1
- initial build
