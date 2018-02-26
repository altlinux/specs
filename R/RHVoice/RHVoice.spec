Name: RHVoice
Version: 0.3
Release: alt3
Packager: Michael Pozhidaev <msp@altlinux.org>

Summary: RHVoice is a Russian speech synthesizer written by Olga Yakovleva
Group: Sound
License: %gpl3plus

# Automatically added by buildreq on Mon Jan 31 2011
BuildRequires: flite-devel libunistring-devel

BuildRequires: rpm-build-licenses rpm-macros-tts
Requires: tts-base

Source: RHVoice-%version.tar.gz
Source2: rhvoice.voiceman
Source3: rhvoice-en.voiceman

%description
RHVoice is a Russian speech synthesizer written by Olga Yakovleva.
It uses the following free software components:
* Russian speech database and Russian language description for
  Festival by Nickolay V. Shmyrev (https://developer.berlios.de/projects/festlang)
  The phoneset and almost all of the main lts rules are used as is,
  but I've made changes in other parts, either to simplify conversion
  to the flite format, or to add new features, or just to understand
  how it all works.
* The voice has been trained with The HMM-based Speech Synthesis
  System (HTS) (http://hts.sp.nitech.ac.jp)
* The hts_engine API is used for runtime speech generation
  (http://hts-engine.sourceforge.net/)
  Since the library does not support streaming synthesis, the original
  version has been modified to implement this functionality, and the
  synthesizer distribution includes this patched version.
* The C implementation of the Russian text analyzer uses Flite
  (http://www.speech.cs.cmu.edu/flite)
  I used the flite's implementation of English language support as an
  example, some functions were used as a starting point.
* the stress information for the stress dictionary has been extracted
  from the test dictionary in the RuLex package by Igor B. Poretsky
  (http://poretsky.homelinux.net/packages/)
* GNU libunistring is used for working with unicode text
  (http://www.gnu.org/software/libunistring/)

%prep
%setup -q 
%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install
%__install -pD -m 644 %SOURCE2 %buildroot%_ttsdir/rhvoice.voiceman
%__install -pD -m 644 %SOURCE3 %buildroot%_ttsdir/rhvoice-en.voiceman

%preun
%tts_unregister rhvoice
%tts_unregister rhvoice-en

%files
%doc AUTHOR ChangeLog COPYING NEWS README
%_ttsdir/*
%_bindir/*
%_datadir/rhvoice

%changelog
* Thu Apr 07 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt3
- Added VoiceMan configuration for English in translit mode

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt2
- Added tts_unregister call to preun section
- tts-devel buildreq replaced by rpm-macros-tts

* Mon Jan 31 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt1
- New version with fixed flite sprintf bug and autotools support

* Wed Jul 28 2010 Michael Pozhidaev <msp@altlinux.ru> 0.1-alt1
- First release for ALT Linux Sisyphus

