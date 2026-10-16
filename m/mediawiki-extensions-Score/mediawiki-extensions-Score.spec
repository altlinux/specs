%define oname Score
%define mwversion 1.46
%define commit c9da006
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.46
Release: alt1

Summary: MediaWiki extension to render musical scores (LilyPond, ABC) with the <score> tag

License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:Score

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# commands called by the extension scripts (scripts/*.sh)
Requires: /usr/bin/lilypond /usr/bin/abc2ly /usr/bin/gs
Requires: /usr/bin/fluidsynth fluid-soundfont-gm /usr/bin/lame
# lilypond (Guile) fails with 'invalid or unknown character encoding LATIN1' without it
Requires: glibc-gconv-modules

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
Source: %oname-%version.tar

%description
Score is a MediaWiki extension which renders musical scores written in
LilyPond, ABC or other notations inside the <score> tag into PNG images
(or SVG), with optional MIDI and Ogg/MP3 audio.

The rendering programs (LilyPond, Ghostscript, FluidSynth with a sound
font, LAME) are run locally. ImageMagick (convert) is needed only if
$wgScoreTrim is enabled together with $wgUseImageMagick.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{tests,cypress,Gruntfile.js,package.json,package-lock.json,composer.json,cypress.config.ts}
cat >> %buildroot%_mediawiki_settings_dir/50-%oname.php <<'EOF2'
// LilyPond 2.23.12 and newer has no safe mode, the input is trusted to the
// extension limits only; set to true only for an older LilyPond
$wgScoreSafeMode = false;
// sound font from fluid-soundfont-gm
$wgScoreSoundfont = '/usr/share/soundfonts/FluidR3_GM.sf2';
EOF2

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.46-alt1
- initial build for Sisyphus (REL1_46 snapshot c9da006, MediaWiki 1.46)
