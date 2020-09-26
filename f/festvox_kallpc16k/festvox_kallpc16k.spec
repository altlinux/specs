%define voice kallpc16k
%define voicepath english/kal_diphone
%define version	1.95
%define release	alt2

Name:		festvox_%{voice}
Version:	%{version}
Release:	%{release}
Group:		Sound
License:	MIT
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: American English male speaker (KAL, 16KHz sampling)
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

Source0:	http://festvox.org/packed/festival/2.5/voices/festvox_kallpc16k.tar

%description
American English male speaker (KAL) using residual excited LPC diphone database
at 16KHz sampling.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/festvox
install -d $VOICE_DIR/%{voicepath}/group
install -m 644 festival/lib/voices/%{voicepath}/festvox/* $VOICE_DIR/%{voicepath}/festvox
install -m 644 festival/lib/voices/%{voicepath}/group/* $VOICE_DIR/%{voicepath}/group

%files
%doc festival/lib/voices/%{voicepath}/COPYING
%{_datadir}/festival/*

%changelog
* Sat Sep 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.95-alt2
- fixed license

* Tue Sep 26 2006 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- initial release for Sisyphus
