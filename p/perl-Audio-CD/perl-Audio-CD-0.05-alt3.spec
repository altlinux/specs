%define dist Audio-CD
Name: perl-%dist
Version: 0.05
Release: alt2.2

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
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2.2
- rebuitl for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2.1
- rebuilt with perl 5.12

* Wed Aug 16 2006 Led <led@altlinux.ru> 0.05-alt2
- fixed %%files

* Thu May 04 2005 Led <led@altlinux.ru> 0.05-alt1
- initial build
