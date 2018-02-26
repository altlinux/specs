%define voice us2
%define voicepath english/%{voice}_mbrola
%define version	1.95
%define release	alt1

Name:		festvox_%{voice}
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival wrapper for MBROLA voice %{voice}: American English male speaker
Requires:	festival, festlex_POSLEX, festlex_CMU
Requires:	mbrola-voice-%{voice}
Provides:	festvox
BuildArch:	noarch
AutoReqProv:	no

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2

%description
Festival wrapper for MBROLA voice %{voice}: 
 American English male speaker using the MBROLA us2 database
 This requires the MBROLA prorgram and us2 English database (~6Meg)
 available from http://tcts.fpms.ac.be/synthesis/mbrola.html.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

cd festival

install -d $VOICE_DIR/%{voicepath}/festvox
install -m 644 lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
install -m 644 lib/voices/%{voicepath}/us* $VOICE_DIR/%{voicepath}/

%files
%{_datadir}/festival/*

%changelog
* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
