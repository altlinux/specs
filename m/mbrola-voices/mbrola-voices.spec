%define _unpackaged_files_terminate_build 1

Name:    mbrola-voices
Version: 20200332
Release: alt2
BuildArch: noarch

Summary: Data files of mbrola speech synthesizer voices
License: AGPL-3.0-or-later
Group:   Sound
Url:     https://github.com/numediart/MBROLA-voices

Source: %name-%version.tar

#BuildRequires:

%description
%summary

%define install_voices :

%define voicepackage() \
%global install_voices %install_voices; installVoice %2 %1 \
%package %1            \
Summary: %1 %2 voice for MBROLA \
Group: Sound \
BuildArch: noarch \
Requires: mbrola \
Provides: mbrola-voice-%1 = %EVR \
Obsoletes: mbrola-voice-%1 < %EVR \
\
%description %1        \
%summary \
                       \
%files %1              \
%_datadir/mbrola/%1 \
%_datadir/festival/voices/%2/%{1}_mbrola/%1 \
%_datadir/doc/mbrola-voice-%{1}-%version/* \

%voicepackage en1 english
%voicepackage us1 english
%voicepackage us2 english
%voicepackage us3 english
%voicepackage af1 afrikaans
%voicepackage ar1 arabic
%voicepackage ar2 arabic
%voicepackage br1 portuguese
%voicepackage br2 portuguese
%voicepackage br3 portuguese
%voicepackage br4 portuguese
%voicepackage pt1 portuguese
%voicepackage bz1 breton
%voicepackage ca1 french
%voicepackage ca2 french
%voicepackage fr1 french
%voicepackage fr2 french
%voicepackage fr3 french
%voicepackage fr4 french
%voicepackage fr5 french
%voicepackage fr6 french
%voicepackage fr7 french
%voicepackage cn1 chinese
%voicepackage cr1 croatian
%voicepackage cz1 czech
%voicepackage cz2 czech
%voicepackage de1 german
%voicepackage de2 german
%voicepackage de3 german
%voicepackage de4 german
%voicepackage de5 german
%voicepackage de6 german
%voicepackage de7 german
%voicepackage de8 german
%voicepackage ee1 estonian
%voicepackage es1 spanish
%voicepackage es2 spanish
%voicepackage es3 spanish
%voicepackage es4 spanish
%voicepackage mx1 spanish
%voicepackage mx2 spanish
%voicepackage vz1 spanish
%voicepackage gr1 greek
%voicepackage gr2 greek
%voicepackage hb1 hebrew
%voicepackage hb2 hebrew
%voicepackage hn1 korean
%voicepackage hu1 hungarian
%voicepackage ic1 icelandic
%voicepackage id1 indonesian
%voicepackage in1 hindi
%voicepackage in2 hindi
%voicepackage ir1 iranian
%voicepackage it1 italian
%voicepackage it2 italian
%voicepackage it3 italian
%voicepackage it4 italian
%voicepackage jp1 japanese
%voicepackage jp2 japanese
%voicepackage jp3 japanese
%voicepackage la1 latin
%voicepackage lt1 lithuanian
%voicepackage lt2 lithuanian
%voicepackage ma1 malay
%voicepackage nl1 dutch
%voicepackage nl2 dutch
%voicepackage nl3 dutch
%voicepackage nz1 maori
%voicepackage pl1 polish
%voicepackage ro1 romanian
%voicepackage sw1 swedish
%voicepackage sw2 swedish
%voicepackage tl1 telugu
%voicepackage tr1 turkish
%voicepackage tr2 turkish

%package doc
Summary: Doc files for mbrola-voices
Group: Other
BuildArch: noarch

%description doc
%summary

%files doc
%_datadir/doc/%name-%version/LICENSE.md
%_datadir/doc/%name-%version/README.md

%prep
%setup

%install
mkdir -p %buildroot%_docdir/%name-%version
install -m 644 *.md %buildroot%_docdir/%name-%version

mkdir -p %buildroot%_datadir/mbrola

VOICE_DIR=%_datadir/festival/voices

installVoice() {
  local LANG_DIR="$VOICE_DIR/$1"
  local VOICE="$2"
  install -D -m 0644 data/$VOICE/$VOICE %buildroot$LANG_DIR/${VOICE}_mbrola/$VOICE/$VOICE
  ln -s $LANG_DIR/${VOICE}_mbrola/$VOICE %buildroot%_datadir/mbrola/$VOICE
  mkdir -p %buildroot%_datadir/doc/mbrola-voice-${VOICE}-%version/
  cp -r data/$VOICE/* %buildroot%_datadir/doc/mbrola-voice-${VOICE}-%version/
  rm %buildroot%_datadir/doc/mbrola-voice-${VOICE}-%version/$VOICE
}

%install_voices

%changelog
* Tue Oct 29 2024 Artem Semenov <savoptik@altlinux.org> 20200332-alt2
- Fix symlink/dir collision (thx Paul Wolneykien)

* Thu Aug 22 2024 Artem Semenov <savoptik@altlinux.org> 20200332-alt1
- Initial build for Sisyphus (ALT bug: 51044)
