%define _unpackaged_files_terminate_build 1

Name: cicero
Version: 0.7.2
Release: alt1

Summary: French and English Text-To-Speech for MBROLA
License: GPL-2.0-only
Group: Sound
Url: https://github.com/npitre/cicero
Vcs: https://github.com/npitre/cicero.git

Source: %name-%version.tar
Patch0: %name-%version-alt-python3.patch
Patch1: %name-%version-alt-oss-dsp.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3

Requires: mbrola
Requires: mbrola-voices-fr1

%add_python3_req_skip app_brltty_es app_shell config main mbrola_prog oss_dsp phonetizer profiling setencoding sndoutput tracing ttp version

%description
Cicero is a small, fast and free text-to-speech engine for French
(and some English) written in Python. It converts text to phonemes
using context-sensitive rules and relies on MBROLA to produce audio.

It was designed for blind users and for use with screen review
software, mainly BRLTTY through its ExternalSpeech (es) driver.
Sound output goes through the OSS /dev/dsp device (ALSA OSS
emulation, snd-pcm-oss).

%prep
%setup
%patch0 -p1
%patch1 -p1

sed -e 's|/home/foo/cicero/|%_datadir/%name/|' \
    -e "s|^mbrola_prog_path = .*|mbrola_prog_path = '%_bindir/mbrola'|" \
    -e "s|^mbrola_voice = .*|mbrola_voice = '%_datadir/mbrola/fr1/fr1'|" \
    config.py.sample > config.py

%build

%install
mkdir -p %buildroot%_datadir/%name
install -pm644 *.py rules.fr rules.en checklist.fr checklist.en \
    %buildroot%_datadir/%name/
rm %buildroot%_datadir/%name/config.py

install -pDm644 config.py %buildroot%_sysconfdir/%name/config.py
ln -s %_sysconfdir/%name/config.py %buildroot%_datadir/%name/config.py

mkdir -p %buildroot%_bindir
for p in tts_shell:cicero-shell tts_brltty_es:cicero \
         bulktalk:cicero-bulktalk saypho:cicero-saypho \
         wphons:cicero-wphons testfilters:cicero-testfilters \
         regress:cicero-regress; do
    cat > %buildroot%_bindir/${p#*:} <<EOF
#!/bin/sh
exec %__python3 %_datadir/%name/${p%%:*}.py "\$@"
EOF
    chmod 755 %buildroot%_bindir/${p#*:}
done

%check
mkdir check
sed -e "s|%_datadir/%name/|$PWD/|" config.py > check/config.py
cd check
PYTHONPATH=.. %__python3 -B -c "import runpy; runpy.run_path('../regress.py')" | tee regress.log
grep -qx '0 regression found in [0-9]* checks' regress.log

%files
%doc COPYING README LISEZ-MOI TODO rule_format.txt
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.py
%_bindir/cicero
%_bindir/cicero-*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Tue Nov 10 2026 Dina Tagantseva <dinchik@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus.
