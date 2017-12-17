%define dist Audio-CD
Name: perl-%dist
Version: 0.05
Release: alt4.1.1.1.1

Summary: Perl interface to libcdaudio
License: Artistic
Group: Sound

URL: %CPAN %dist
Source: http://www.vanhemert.co.uk/files/Audio-CD-0.05.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libcdaudio-devel perl-devel

%description
This module was created for adding CDDB support to Xmms::shell and cd
tray eject.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Audio
%perl_vendor_autolib/Audio

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2.2
- rebuitl for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2.1
- rebuilt with perl 5.12

* Wed Aug 16 2006 Led <led@altlinux.ru> 0.05-alt2
- fixed %%files

* Thu May 04 2005 Led <led@altlinux.ru> 0.05-alt1
- initial build
