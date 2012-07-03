# TODO: some kind of rpm-macros-festival?
%define voicedir %{_datadir}/festival/voices
#define voice cmu_us_awb_arctic_hts
#define voicepath us/#voice

Name:		festvox_nitech_us_arctic_hts_voices
Version:	2.0.95
Release:	alt1
Group:		Sound
Copyright:	X11-style
URL:		http://hts.sp.nitech.ac.jp
Packager:	Igor Vlasenko <viy@altlinux.org>
Summary:	Festival voices: HTS VOICES (use Nagoya Institute of Technology's HTS based synthesizer)
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox
Provides:	festival-voice
BuildArch:	noarch

### HTS VOICES (use Nagoya Institute of Technology's HTS based synthesizer)
# The Festvox site packages older versions of these as cmu_us_*_hts.
# These are from <http://hts.sp.nitech.ac.jp/>.
# And, ugh, the files seem to be only served via a script, not directly.
%define nitechhtsversion 0.20080627
%define nitechhtsversion 2.1
%define nitechbaseURL http://hts.sp.nitech.ac.jp/archives/%nitechhtsversion
%define nitechhtsTIMESTAMP 0.20080627
Source: %name-%version.tar
#Source220: %{nitechbaseURL}/festvox_nitech_us_awb_arctic_hts-%nitechhtsversion.tar.bz2
#Source221: %{nitechbaseURL}/festvox_nitech_us_bdl_arctic_hts-%nitechhtsversion.tar.bz2
#Source222: %{nitechbaseURL}/festvox_nitech_us_clb_arctic_hts-%nitechhtsversion.tar.bz2
#Source223: %{nitechbaseURL}/festvox_nitech_us_jmk_arctic_hts-%nitechhtsversion.tar.bz2
#Source224: %{nitechbaseURL}/festvox_nitech_us_rms_arctic_hts-%nitechhtsversion.tar.bz2
#Source225: %{nitechbaseURL}/festvox_nitech_us_slt_arctic_hts-%nitechhtsversion.tar.bz2

Requires: festival >= 2.0
Conflicts: festival < 2.0

#--------------------------------------
# patches from fedora festival 1.96-4
#--------------------------------------
# For some reason, the Nitech voices (and the previous CMU versions) fail to
# define proclaim_voice, which makes them not show up in the voice
# descriptions, which makes gnome-speech not show them.
# already applied in hts-2.1
# Patch90: festival-1.96-nitech-proclaimvoice.patch

# already applied in hts-2.1
# Cure "SIOD ERROR: unbound variable : f2b_f0_lr_start"
#Patch91: festival-1.96-nitech-fixmissingrequire.patch

# already applied in hts-2.1
# An apparent copy-paste error in these voices -- slt is referenced
# in all of them.
# Patch92: festival-1.96-nitech-sltreferences.patch


%description
Set of voices from Nagoya Institute of Technology.
they are HTS VOICES (use Nagoya Institute of Technology's HTS based synthesizer).

%package -n festvox_nitech_us_awb_arctic_hts
Group: Sound
Summary: Scottish-accent US English male speaker "AWB" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-awb-arctic-hts

%package -n festvox_nitech_us_bdl_arctic_hts
Group: Sound
Summary: US English male speaker "BDL" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-bdl-arctic-hts

%package -n festvox_nitech_us_clb_arctic_hts
Group: Sound
Summary: US English female speaker "CLB" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-clb-arctic-hts

%package -n festvox_nitech_us_jmk_arctic_hts
Group: Sound
Summary: Canadian-accent US English male speaker "JMK" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-jmk-arctic-hts

%package -n festvox_nitech_us_rms_arctic_hts
Group: Sound
Summary: US English male speaker "RMS" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-rms-arctic-hts

%package -n festvox_nitech_us_slt_arctic_hts
Group: Sound
Summary: US English female speaker "SLT" for Festival
Version: %{nitechhtsTIMESTAMP}
Requires:	festival, festlex_POSLEX, festlex_CMU
Provides:	festvox, festival-voice
Provides:	festvox-slt-arctic-hts

%description -n festvox_nitech_us_awb_arctic_hts
US English male speaker ("AWB") for Festival. AWB is a native Scottish
English speaker, but the voice uses the US English front end.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1138 utterances spoken by a Scottish English male speaker. The
speaker is very experienced in building synthetic voices and matched
prompted US English, though his vowels are very different from US English
vowels. Scottish English speakers will probably find synthesizers based on
this voice strange. Unlike the other CMU_ARCTIC databases this was recorded
in 16 bit 16KHz mono without EGG, on a Dell Laptop in a quiet office. The
database was automatically labelled using CMU Sphinx using the FestVox
labelling scripts. No hand correction has been made.


%description -n festvox_nitech_us_bdl_arctic_hts
US English male speaker ("BDL") for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using CMU Sphinx using
the FestVox labelling scripts. No hand correction has been made.


%description -n festvox_nitech_us_clb_arctic_hts
US English female speaker ("CLB") for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English female speaker. The
speaker is experienced in building synthetic voices. This was recorded at
16bit 32KHz, in a sound proof room, in stereo, one channel was the waveform,
the other EGG. The database was automatically labelled using CMU Sphinx
using the FestVox labelling scripts. No hand correction has been made.


%description -n festvox_nitech_us_jmk_arctic_hts
US English male speaker ("JMK") voice for Festival. JMK is a native Canadian
English speaker, but the voice uses the US English front end.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1138 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using CMU Sphinx using
the FestVox labelling scripts. No hand correction has been made.

%description -n festvox_nitech_us_rms_arctic_hts
US English male speaker ("RMS") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English male speaker. The speaker
is experienced in building synthetic voices. This was recorded at 16bit
32KHz, in a sound proof room, in stereo, one channel was the waveform, the
other EGG. The database was automatically labelled using EHMM an HMM labeler
that is included in the FestVox distribution. No hand correction has been
made.

%description -n festvox_nitech_us_slt_arctic_hts
US English female speaker ("SLT") voice for Festival.

This is a HMM-based Speech Synthesis System (HTS) voice from the Nagoya
Institute of Technology, trained using the CMU ARCTIC database. This voice
is based on 1132 utterances spoken by a US English female speaker. The
speaker is experienced in building synthetic voices. This was recorded at
16bit 32KHz, in a sound proof room, in stereo, one channel was the waveform,
the other EGG. The database was automatically labelled using CMU Sphinx
using the FestVox labelling scripts. No hand correction has been made.

%prep
#setup -q -n festival -D -T -b 220
#setup -q -n festival -D -T -b 221
#setup -q -n festival -D -T -b 222
#setup -q -n festival -D -T -b 223
#setup -q -n festival -D -T -b 224
#setup -q -n festival -D -T -b 225
%setup -q
# no backups for these patches because 
# the voice directories are copied wholesale
#patch90 -p1

%build

# install the voices
pushd lib/voices
  # get the licenses. This is probably too clever by half, but oh well.
  for f in $( find . -name COPYING ); do
    n=$( echo $f | sed 's/.*\/\(.*\)\/COPYING/COPYING.\1/' )
    mv $f $OLDPWD/$n
  done
  # ditch the readme files -- these aren't very useful. 
  # Except keep a README.htsvoice, because it contains license information.
  cp us/nitech_us_awb_arctic_hts/hts/README.htsvoice $OLDPWD/README.htsvoice
  find . -name 'README*' -exec rm {} \;
popd
# kludge! nitech_us_awb_arctic_hts is missing its COPYING file. It should
# be the same as the other nitech files, though, so just copy one.
cp COPYING.nitech_us_bdl_arctic_hts COPYING.nitech_us_awb_arctic_hts

#cp -a lib/voices $RPM_BUILD_ROOT%{_datadir}/festival/lib

%install
VOICE_DIR=$RPM_BUILD_ROOT%{voicedir}
for voice in \
    nitech_us_awb_arctic_hts \
    nitech_us_bdl_arctic_hts \
    nitech_us_clb_arctic_hts \
    nitech_us_jmk_arctic_hts \
    nitech_us_rms_arctic_hts \
    nitech_us_slt_arctic_hts \
; do 
    voicepath=us/$voice
install -d $VOICE_DIR/$voicepath/festvox
install -d $VOICE_DIR/$voicepath/hts
install -m 644 lib/voices/$voicepath/festvox/* $VOICE_DIR/$voicepath/festvox
install -m 644 lib/voices/$voicepath/hts/* $VOICE_DIR/$voicepath/hts
#install -m 644 lib/voices/$voicepath/*.* $VOICE_DIR/$voicepath}
done

%files -n festvox_nitech_us_awb_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_awb_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_awb_arctic_hts

%files -n festvox_nitech_us_bdl_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_bdl_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_bdl_arctic_hts

%files -n festvox_nitech_us_clb_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_clb_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_clb_arctic_hts

%files -n festvox_nitech_us_jmk_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_jmk_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_jmk_arctic_hts

%files -n festvox_nitech_us_rms_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_rms_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_rms_arctic_hts

%files -n festvox_nitech_us_slt_arctic_hts
%defattr(-,root,root)
%doc COPYING.nitech_us_slt_arctic_hts COPYING.hts README.htsvoice
%dir %{voicedir}
%dir %{voicedir}/us
%{voicedir}/us/nitech_us_slt_arctic_hts

%changelog
* Wed Aug 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.95-alt1
- updated to hts-2.1

* Sat Sep 27 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt2
- added Provides: festival-voice

* Fri Aug 01 2008 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- initial release for Sisyphus
