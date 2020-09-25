%define voice cmu_us_awb_cg
%define voicepath us/%voice
%define festival_version 2.5
Name:		festvox_%{voice}
Version:	2.5
Release:	alt1
Group:		Sound
License:	MIT
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: US English male speaker, Clustergen, "awb"
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
Provides:	festvox-us = %festival_version
BuildArch:	noarch

# will not work with older festivals
Conflicts:	festival < %festival_version
Requires:	festival >= %festival_version

#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2
Source0:	http://festvox.org/packed/festival/%version/voices/festvox_%{voice}.tar

%description
Clustergen "awb" (US English male) voice for festival.

%prep
%setup -q -c

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

install -d $VOICE_DIR/%{voicepath}/
cp -a festival/lib/voices/%{voicepath}/* $VOICE_DIR/%{voicepath}/

%files
%{_datadir}/festival/*

%changelog
* Thu Sep 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1
- new version

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- 2.0.95 beta release at 18-Apr-2010
