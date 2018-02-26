%define voice cmu_us_slt_arctic_hts
%define voicepath us/%voice

Name:		festvox_%{voice}
Version:	2.0.95
Release:	alt2
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: US English female speaker, HTS based, "slt"
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

# will not work with older festivals
Conflicts:	festival < 2.0
Requires:	festival >= 2.0

#Source0:	http://www.speech.cs.cmu.edu/awb/fftest/festvox_%{voice}.tar.bz2
#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2
Source0:	http://festvox.org/packed/festival/2.0.95/festvox_%{voice}.tar
Patch:		festvox_cmu_us_slt_arctic_hts-2.0.95-slt-proclaimvoice.patch

%description
Based on the CMU_ARTIC "slt" (US English female)
using Nagoya Institute of Technology's HTS based synthesizer

%prep
%setup -q -c
%patch -p1

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/festvox
install -d $VOICE_DIR/%{voicepath}/hts
install -m 644 festival/lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
install -m 644 festival/lib/voices/%{voicepath}/hts/* $VOICE_DIR/%{voicepath}/hts
#install -m 644 festival/lib/voices/%{voicepath}/*.* $VOICE_DIR/%{voicepath}/

%files
%doc festival/lib/voices/%{voicepath}/COPYING
%doc festival/lib/voices/%{voicepath}/README
%{_datadir}/festival/*

%changelog
* Wed Aug 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt2
- added proclaim voice patch

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- updated to 2.0.95 beta release at 18-Apr-2010 

* Fri Dec 29 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
 - updated 2006.12.26 from awb to unofficial 1.96

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
