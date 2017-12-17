%define dist GStreamer
Name: perl-%dist
Version: 0.20
Release: alt1.1.1.1

Summary: Perl interface to the GStreamer library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/X/XA/XAOC/GStreamer-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: gst-plugins-base gstreamer-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib-devel perl-podlators

%description
This module allows you to use the GStreamer library from Perl.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc NEWS README
%perl_vendor_archlib/GStreamer*
%perl_vendor_autolib/GStreamer

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1
- rebuild with new perl 5.22.0

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- 0.16 -> 0.17
- built for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt2
- fix build

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1.1
- rebuilt with perl 5.12

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- new version 0.15 (with rpmrb script)

* Fri Dec 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- initial build for ALT Linux Sisyphus
