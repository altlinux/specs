%define voice msu_ru_nsh_clunits
%define voicepath russian/%voice

Name:		festvox_%{voice}
Version:	0.5
Release:	alt1
Group:		Sound
Copyright:	X11-style
URL:		http://festlang.berlios.de/russian.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: a clustergen voice for Russian Language.
Requires:	festival >= 1.96
Provides:	festvox
Obsoletes:	festvox_msu_ru_nsh_diphone < 0.2-alt2
BuildArch:	noarch
AutoReqProv:	no

Source0:	http://prdownload.berlios.de/festlang/%{voice}-%{version}.tar

%description
Festival voice: a clustergen synthesizer voice for Russian Language.

Note, that you should select russian voice with (voice_msu_ru_nsh_cg)
on start and all russian text should have UTF-8 encoding.


%prep
%setup -q -n %{voice} 
#-%{version}

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/
#install -m 644 ./festvox/*.scm $VOICE_DIR/%{voicepath}/festvox
mv ./*/ $VOICE_DIR/%{voicepath}/

%files
%doc COPYING README
%{_datadir}/festival/voices/*

%changelog
* Thu Feb 26 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- initial release for Sisyphus
