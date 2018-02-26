%define voice cmu_us_bdl_arctic_hts
%define voicepath us/%voice

Name:		festvox_%{voice}
Version:	1.96
Release:	alt1
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: US English male speaker, HTS based, "bdl"
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

Source0:	http://www.speech.cs.cmu.edu/awb/fftest/festvox_%{voice}.tar.bz2
#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2

%description
Based on the CMU_ARTIC "bdl" (US English male)
using Nagoya Institute of Technology's HTS based synthesizer

%prep
%setup -q -c

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
* Fri Dec 29 2006 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
 - updated 2006.12.26 from awb to unofficial 1.96

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
