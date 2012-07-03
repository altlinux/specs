%define dist Audio-PortAudio
Name: perl-%dist
Version: 0.03
Release: alt1.2

Summary: Perl portable interface for audio IO using libportaudio
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libportaudio2-devel perl-devel

%description
Audio::PortAudio is an object oriented interface to the PortAudio library
( http://www.portaudio.com/ ). It provides flexible multi-channel audio
input & output on a variety of different platforms.

%prep
%setup -q -n %dist-%version

%ifdef __BTE
# no audio facilities in restricted environment
%def_without test
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Audio
%perl_vendor_autolib/Audio

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1.1
- rebuilt with perl 5.12

* Sun Oct 18 2009 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- initial build for ALT Linux Sisyphus
