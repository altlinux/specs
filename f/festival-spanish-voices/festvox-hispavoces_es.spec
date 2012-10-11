Name:		festival-spanish-voices
Version:	1.0.0
Release:	alt1
Group:		Sound
Copyright:	GPL2+
URL:		http://v4.guadalinex.org/guadalinex-toro/pool-test/main/f/festival-spanish-voices
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Spanish voices "PAL" and "SFL" for Festival
Requires:	festival >= 1.96
BuildArch:	noarch
AutoReqProv:	no

Source0:	http://v4.guadalinex.org/guadalinex-toro/pool-test/main/f/festival-spanish-voices/festival-spanish-voices_1.0.0.orig.tar
#Source0:	http://v4.guadalinex.org/guadalinex-toro/pool-test/main/f/festival-spanish-voices/festival-spanish-voices-%{version}.tar
Source1:	COPYING.hispavoces

%description
This is a diphone-based Spanish voices for the Festival speech synthesis
system.

%package -n festvox_hispavoces_es_pal_diphone
Group: Sound
Summary: Male Spanish voice "PAL" for Festival
Requires: festival
Provides: festvox
#Provides: festival-voice
BuildArch: noarch

%package -n festvox_hispavoces_es_sfl_diphone
Group: Sound
Summary: Female Spanish voice "SFL" for Festival
Requires: festival
Provides: festvox
#Provides: festival-voice
BuildArch: noarch

%description -n festvox_hispavoces_es_sfl_diphone
Female Castillian-Spanish (es_ES) voice "SFL" for Festival.

This is a diphone-based male Spanish voice for the Festival speech synthesis
system. These original audio files were recorded by a professional voice
talent in a recording studio.

This voice was developed by the Consejeria de Innovacion, Ciencia y Empresa
of the Junta de Andalucia on a project awarded to MP Sistemas in
collaboration with Intelligent Dialogue Systems (INDISYS).

The primary objective was to integrate a higher-quality diphone-based
Spanish voice in Guadalinex v4.0, an Ubuntu-based Linux distribution
promoted by the Government of Andalusia (Spain). See
http://www.guadalinex.org for more information.

%description -n festvox_hispavoces_es_pal_diphone
Male Castillian-Spanish (es_ES) voice "PAL" for Festival.

This is a diphone-based male Spanish voice for the Festival speech synthesis
system. These original audio files were recorded by a professional voice
talent in a recording studio.

This voice was developed by the Consejeria de Innovacion, Ciencia y Empresa
of the Junta de Andalucia on a project awarded to MP Sistemas in
collaboration with Intelligent Dialogue Systems (INDISYS).

The primary objective was to integrate a higher-quality diphone-based
Spanish voice in Guadalinex v4.0, an Ubuntu-based Linux distribution
promoted by the Government of Andalusia (Spain). See
http://www.guadalinex.org for more information.

%prep
%setup -q -n festival-spanish-voices-%version
#-%{version}

%build

%install
VOICE_DIR=$RPM_BUILD_ROOT%{_datadir}/festival/voices

mkdir -p $RPM_BUILD_ROOT%{_datadir}/festival/voices/es/
cp -a */ $RPM_BUILD_ROOT%{_datadir}/festival/voices/es/

%files -n festvox_hispavoces_es_pal_diphone
%dir %{_datadir}/festival/voices/es/JuntaDeAndalucia_es_pa_diphone/
%{_datadir}/festival/voices/es/JuntaDeAndalucia_es_pa_diphone/*

%files -n festvox_hispavoces_es_sfl_diphone
%dir %{_datadir}/festival/voices/es/JuntaDeAndalucia_es_sf_diphone/
%{_datadir}/festival/voices/es/JuntaDeAndalucia_es_sf_diphone/*

%changelog
* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial release for Sisyphus
