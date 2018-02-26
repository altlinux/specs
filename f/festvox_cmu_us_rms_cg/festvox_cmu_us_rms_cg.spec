%define voice cmu_us_rms_cg
%define voicepath us/%voice

Name:		festvox_%{voice}
Version:	2.0.95
Release:	alt1
Group:		Sound
Copyright:	X11-style
URL:		http://www.cstr.ed.ac.uk/projects/festival.html
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voice: US English male speaker, Clustergen, "rms"
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
BuildArch:	noarch

# will not work with older festivals
Conflicts:	festival < 2.0
Requires:	festival >= 2.0

#Source0:	http://www.cstr.ed.ac.uk/downloads/festival/1.95/festvox_%{voice}.tar.bz2
Source0:	http://festvox.org/packed/festival/2.0.95/festvox_%{voice}.tar

%description
Clustergen "rms" (US English male) voice for festival.

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
* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- 2.0.95 beta release at 18-Apr-2010
