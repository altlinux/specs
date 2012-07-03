%define dist XML-LibXSLT
Name: perl-%dist
Version: 1.73
Release: alt1

Summary: Perl interface to the Gnome libxslt library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Oct 12 2011
BuildRequires: libxslt-devel perl-XML-LibXML perl-devel zlib-devel

%description
This module is a fast XSLT library, based on the Gnome libxslt engine.
The libxslt processor is fast, highly standards compliant, with
practically all of XSLT 1.0 being supported in version 0.9 of libxslt.

%prep
%setup -q -n %dist-%version

# disable dependency on perl libs like gdbm
sed -i- '/Config{libs}/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/XML
%perl_vendor_autolib/XML

%changelog
* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 1.73-alt1
- 1.70 -> 1.73
- built for perl-5.14
- built as plain src.rpm

* Thu May 05 2011 Alexey Tourbin <at@altlinux.ru> 1.70-alt2
- fixed building without zlib-devel

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.70-alt1.1
- rebuilt with perl 5.12

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 1.70-alt1
- 1.68 -> 1.70

* Sat Nov 08 2008 Alexey Tourbin <at@altlinux.ru> 1.68-alt1
- 1.66 -> 1.68

* Fri Feb 22 2008 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.63 -> 1.66

* Sat Oct 27 2007 Alexey Tourbin <at@altlinux.ru> 1.63-alt1
- 1.62 -> 1.63

* Mon Aug 20 2007 Alexey Tourbin <at@altlinux.ru> 1.62-alt2
- changed src.rpm packaging to keep upstream tarball unchanged

* Tue Nov 21 2006 Alexey Tourbin <at@altlinux.ru> 1.62-alt1
- 1.61 -> 1.62

* Sat Nov 18 2006 Alexey Tourbin <at@altlinux.ru> 1.61-alt1
- 1.60 -> 1.61
- imported sources into git and built with gear
- fixed test suite for new libxslt-1.1.18 (cpan #23467)

* Sun Aug 27 2006 Alexey Tourbin <at@altlinux.ru> 1.60-alt1
- 1.59 -> 1.60

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 1.59-alt1
- 1.58 -> 1.59
- benchmark.pl not packaged

* Mon Aug 08 2005 Alexey Tourbin <at@altlinux.ru> 1.58-alt1
- 1.57 -> 1.58
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.57-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 1.57-alt1
- 1.57, Sisyphus release, thanks to Michael Bochkaryov

* Fri Apr 9 2004 Michael Bochkaryov <misha@kyivstar.net> 1.53-ks0
- Initial release
