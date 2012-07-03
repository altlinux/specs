%define dist Template-Toolkit
Name: perl-Template
Version: 2.22
Release: alt1.2

Summary: Perl Template Toolkit
License: GPL or Artistic
Group: Development/Perl

URL: http://www.template-toolkit.org
Source: %dist-%version.tar.gz
Patch: Template-Toolkit-2.22-alt-no-apache.patch

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-AppConfig perl-CGI perl-Date-Calc perl-HTML-Parser perl-Image-Info perl-Math-Complex perl-Pod-POM perl-devel perl-podlators perl-unicore

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build TT_XS_ENABLE=y TT_XS_DEFAULT=y TT_ACCEPT=y \
    INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc	README Changes TODO HACKING INSTALL

	%perl_vendor_archlib/Template.pm
%dir	%perl_vendor_archlib/Template
	%perl_vendor_archlib/Template/*.pm
%doc	%perl_vendor_archlib/Template/*.pod
%dir	%perl_vendor_archlib/Template/Namespace
	%perl_vendor_archlib/Template/Namespace/*.pm
%dir	%perl_vendor_archlib/Template/Plugin
	%perl_vendor_archlib/Template/Plugin/*.pm
%dir	%perl_vendor_archlib/Template/Stash
	%perl_vendor_archlib/Template/Stash/*.pm

%doc	%perl_vendor_archlib/Template/Manual
%doc	%perl_vendor_archlib/Template/Tutorial

%dir	%perl_vendor_archlib/Template/Tools
%doc	%perl_vendor_archlib/Template/Tools/*.pod

%dir	%perl_vendor_autolib/Template
	%perl_vendor_autolib/Template/Stash

	%_bindir/tpage
	%_bindir/ttree
	%_man1dir/tpage.*
	%_man1dir/ttree.*

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.22-alt1.2
- rebuilt for perl-5.14
- disabled dependency on Apache::Util (ALT#24241)

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt1.1
- rebuilt with perl 5.12

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 2.22-alt1
- 2.19 -> 2.22

* Fri Apr 25 2008 Alexey Tourbin <at@altlinux.ru> 2.19-alt1
- 2.15 -> 2.19
- packaged extras under %_datadir/tt2

* Tue Jun 13 2006 Alexey Tourbin <at@altlinux.ru> 2.15-alt1
- 2.14 -> 2.15
- excerpt from Changes:
  * Moved all XML plugins and related tests into a separate Template-XML
    distribution.
  * Moved DBI plugin and tests into Template-DBI distribution.
  * Moved GD plugins and tests into Template-GD distribution.

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 2.14-alt1
- 2.13 -> 2.14
- disabled gd test 7 because of libpng-1.2.7 optimizations

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.10 -> 2.13
- dropped `hack provides', recent file(1) is required for build

* Mon Sep 29 2003 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- 2.10
- full-fetaured build with all additional modules present
- all test enabled except autoform and dbi

* Tue Aug 19 2003 Alexey Gladkov <legion@altlinux.ru> 2.09-alt1.1
- Temporarily hack provides.

* Thu May 01 2003 Alexey Gladkov <legion@altlinux.ru> 2.09-alt1
- First build for ALTLinux
- spec modifications for Sisyphus
- new version 2.09

* Tue Feb 25 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.08-2mdk
- removed buildrequires perl(XML::DOM), redundant with perl-libxml-enno

* Sun Sep 22 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.08-1mdk
- new version
- adjust requires and buildrequires
- misc spec file fixes

* Fri Jul 19 2002 Pixel <pixel@mandrakesoft.com> 2.07-1mdk
- new release
- rebuild for perl 5.8.0
- cleanup
- drop the patch (!?)

* Wed Apr 10 2002 Warly <warly@mandrakesoft.com> 2.06-1mdk
- mandrake packages

* Sat Nov 10 2001 Aleksey Nogin <ayn2@cornell.edu>
- initial package, adapted from perl-Digest-MD5
