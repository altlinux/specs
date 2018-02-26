%define voice ellpc11k
%define voicepath spanish/el_diphone
%define version	1.95
%define release	alt1

Name:		festvox_%{voice}
Version:	%{version}
Release:	%{release}
Group:		Sound
Copyright:	non-commercial use
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: Castilian Spanish male speaker
Requires:	festival
Provides:	festvox
BuildArch:	noarch

Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2

%description
   Castilian Spanish male speaker using residual excited LPC diphone.
   Requires no further lexicons, not complete but adequate.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/festvox
install -d $VOICE_DIR/%{voicepath}/group
install -m 644 festival/lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
install -m 644 festival/lib/voices/%{voicepath}/group/* $VOICE_DIR/%{voicepath}/group
#install -m 644 festival/lib/voices/%{voicepath}/*.* $VOICE_DIR/%{voicepath}/

%files
%doc festival/lib/voices/%{voicepath}/COPYING
%{_datadir}/festival/*

%changelog
* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
