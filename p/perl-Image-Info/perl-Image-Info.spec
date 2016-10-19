%define _unpackaged_files_terminate_build 1
%define dist Image-Info
Name: perl-%dist
Version: 1.39
Release: alt1

Summary: Extract meta information from image files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SR/SREZIC/Image-Info-%{version}.tar.gz

Patch0: Image-Info-1.38-alt-req-perlio.patch
Patch1: Image-Info-1.31-alt-req-zlib.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-IO-Compress perl-Image-Xbm perl-Image-Xpm perl-Test-Pod perl-Test-Pod-Coverage perl-XML-Simple

%description
This Perl extention allows you to extract meta information from
various types of image files.  In this release the following file
formats are supported:

   JPEG (plain JFIF and Exif)
   PNG
   GIF
   PBM/PGM/PPM
   SVG
   XBM/XPM
   BMP/DIB/RLE

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES CREDITS README
%perl_vendor_privlib/Image
%exclude %perl_vendor_privlib/Bundle/Image

%changelog
* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.31 -> 1.32

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.31-alt2
- rebilt as plain src.rpm

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Thu Aug 05 2010 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.28 -> 1.30

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- fixed unpackaged directory

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.27 -> 1.28

* Tue Mar 04 2008 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.24 -> 1.27

* Mon Apr 23 2007 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.22 -> 1.24

* Fri Aug 11 2006 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.16 -> 1.22

* Thu Apr 07 2005 Alexey Tourbin <at@altlinux.ru> 1.16-alt3
- clarified dependencies on Compress::Zlib and PerlIO::scalar
- updated description

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.16-alt2
- rebuild in new environment
- enabled XBM and XPM support
- manual pages not packaged (use perldoc)

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.15 -> 1.16

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.15

* Mon Sep 29 2003 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- initial revision (this module is required for full-featured perl-Template)
- XBM and XPM support diasabled (additional modules required)
