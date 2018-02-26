%define zipname mbr301h
Name: mbrola
Summary: MBROLA speech synthesizer
Version: 3.01
Release: alt6
License: no-charge distributable for non-commercial, non-military use
Group: Sound
URL: http://tcts.fpms.ac.be/synthesis/mbrola.html
Source0: %{zipname}.zip
#claims to be amd64, but isn't :(
#Source1: mbrola.zip
Packager: Igor Vlasenko <viy@altlinux.org>
ExclusiveArch: %ix86
Requires: mbrola-voice
Requires: freespeech

# Automatically added by buildreq on Thu Oct 26 2006 (-bi)
BuildRequires: unzip

%description
MBROLA is a  speech synthesizer  based  on the concatenation  of
diphones. It takes a list of phonemes as input, together with prosodic
information  (duration of phonemes  and a piecewise linear description
of  pitch), and produces  speech samples  on 16  bits (linear), at the
sampling frequency of the diphone database. 

It is therefore NOT a Text-To-Speech  (TTS) synthesizer, since it does
not accept raw text as input.  In  order to obtain  a full TTS system,
you need to use this synthesizer in combination with a text processing
system that produces phonetic and prosodic commands such as festival or freespeech.

This program may not be sold or incorporated into any product which is
sold without prior permission from the author.

When no  charge is made, this  program  may be copied  and distributed
freely, provided that   this notice  is  copied  and distributed  with
it. Each time you redistribute  the program (or any  work based on the
program), the recipient   automatically receives  a license from   the
original  licensor to copy or distribute  the program subject to these
terms and conditions.  You may  not impose any further restrictions on
the recipients' exercise of   the rights granted  herein. You  are not
responsible for enforcing compliance by third parties to this License.

%prep
%setup -q -c 

%build

%install

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m 755 mbrola-linux-i386 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc readme.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}

%changelog
* Wed Nov 17 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt6
- Added req to freespeech

* Wed Nov 17 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt5
- Removed VoiceMan configuration entry (now included into freespeech package)

* Mon Jun 28 2010 Michael Pozhidaev <msp@altlinux.ru> 3.01-alt4
- VoiceMan config entry updated to server version 1.5.0

* Fri Oct 17 2008 Igor Vlasenko <viy@altlinux.ru> 3.01-alt3.1
- added missing mbrola.voiceman

* Fri Sep 05 2008 Igor Vlasenko <viy@altlinux.ru> 3.01-alt3
- added voiceman support (thanks to Michael Pozhidaev)

* Thu Oct 26 2006 Igor Vlasenko <viy@altlinux.ru> 3.01-alt2
-  chosen proper mbrola binary

* Tue Oct 24 2006 Igor Vlasenko <viy@altlinux.ru> 3.01-alt1
 - first build for Sisyphus

