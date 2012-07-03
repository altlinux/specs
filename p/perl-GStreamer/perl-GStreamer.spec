%define dist GStreamer
Name: perl-%dist
Version: 0.16
Release: alt2

Summary: Perl interface to the GStreamer library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
