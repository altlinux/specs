%define _unpackaged_files_terminate_build 1
%define _emacspeakdir %_datadir/emacs/site-lisp/emacspeak

Name: ru_emacspeak
Version: 50.0.22
Release: alt3

Summary: speech output interface to Emacs
License: GPLv2+ and BSD
Group: Accessibility
Url: https://poretsky.github.io/packages/index-ru.html
VCS: https://github.com/poretsky/emacspeak

Source: %name-%version.tar
Source1: 80keybindings.el
Source2: 80site-defaults.el
Source3: emacspeak.conf

# alt patches
Patch0: python-base-dep-remove.patch
Patch1: ru_emacspeak-fix-voice-setup-defvar.patch
Patch2: ru_emacspeak-fix-proced-cl-case-otherwise.patch

Requires: multispeech
Requires: tclx
Conflicts: emacspeak

%filter_from_requires \,/etc/emacspeak.conf,d

BuildRequires(pre): rpm-macros-emacs rpm-macros-python
BuildRequires: rpm-build-emacs rpm-build-python
BuildRequires: emacs-speedbar >= 7.1
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: tcl-devel
BuildRequires: makeinfo
BuildRequires: perl-libwww
BuildRequires: perl-HTML-TableExtract
BuildRequires: libsox-devel
BuildRequires: libespeak-devel
BuildRequires: csound
BuildRequires: xsltproc

%description
Emacspeak is a speech output system that will allow someone who
 cannot see to work directly on a UNIX system.

 Emacspeak is built on
 top of Emacs.  Once Emacs is started with Emacspeak loaded, users get
 spoken feedback for all actions.  As Emacs can do everything,
 they get speech feedback for everything they do.

 This package also includes speech server written in Tcl to support
 the DECtalk Express speech synthesizer and remote speech server
 access scripts.  For other synthesizers, look for separate
 speech server packages such as emacspeak-espeak, emacspeak-outloud,
 multispeech and eflite.

%package doc
Summary: Doc files for %name
Group: Documentation
BuildArch: noarch

%description doc
Emacspeak is a speech output system that will allow someone who
 cannot see to work directly on a UNIX system.

 This package contains additional documentation in html and pdf
 formats.

%package espeak
Summary: Espeak speech server for Emacspeak
Group: Sound
Requires: %name = %EVR

%description espeak
Emacspeak is a speech output system that will allow someone who
 cannot see to work directly on a UNIX system.

 This package provides additional speech output for Emacspeak
 via eSpeak speech synthesizer.

%package outloud
Summary: IBM ViaVoice Outloud speech server for Emacspeak
Group: Sound
Requires: %name = %EVR

%description outloud
Emacspeak is a speech output system that will allow someone who
 cannot see to work directly on a UNIX system.

 This package allows one to use IBM ViaVoice Outloud speech synthesizer
 for speech output in Emacspeak.

%package pan-chimes
Summary: Pan-chimes auditory icons theme for Emacspeak
Group: Sound
Requires: %name = %EVR

%description pan-chimes
This theme is made up mostly of different chimes and short notes
 from various instruments with autopan effect applied.
 The icons are high-quality 44K-stereo.

 When the package is installed, you can switch Emacspeak to use
 this theme by command emacspeak-sounds-select-theme
 bound by default to control-e ).

%package pan-chimes-doc
Summary: Doc files for pan-chimes
Group: Documentation
BuildArch: noarch

%description pan-chimes-doc
%summary

%package classic
Summary: Classic auditory icons theme for Emacspeak
Group: Sound
Requires: %name = %EVR

%description classic
This theme is made up of the original default-8k sounds
 that have been converted to 44.1k stereo format.

 When the package is installed, you can switch Emacspeak to use
 this theme by command emacspeak-sounds-select-theme
 bound by default to control-e ).

%prep
%setup

# applying debian patches
while read -r f; do
    echo "Applying $f..." >&2
    patch -p1 < debian/patches/"$f"
done < debian/patches/series

# applying alt patches
%autopatch -p1

%build
pushd debian
ln -s templates emacspeak-espeak.templates
ln -s templates emacspeak-outloud.templates
popd

make -C servers/native-espeak
make -C servers/linux-outloud

# Generate 3D auditory icon theme using csound
ln -s /usr/share/samples/hrtf*.dat sounds/3d/src/
pushd sounds/3d/src
for file in *.csd; do
    [ "$file" != "interactive.csd" ] && csound -o ../${file%%csd}wav "$file" || true
done
popd

make -C lisp config
make -C lisp/g-client config

# Remove global-voice-lock-mode from cus-load before it causes issues
sed -i '/global-voice-lock-mode/d' lisp/emacspeak-cus-load.el

cd lisp && mkdir -p /tmp/emacspeak-sounds && \
emacs -batch -q -no-site-file \
    --eval '(setq file-name-handler-alist nil gc-cons-threshold 64000000 load-source-file-function nil)' \
    --eval '(defvar emacspeak-sounds-directory "/tmp/emacspeak-sounds/")' \
    -l ./emacspeak-load-path.el \
    -f batch-byte-compile voice-setup.el
cd ..

# Regenerate cus-load after voice-setup is compiled
make -C lisp emacspeak-cus-load.el

make -C lisp

make -C etc tips.html applications.html
make -C info
make -C blog-archive

%install
mkdir -pv %buildroot
mkdir -pv %buildroot%_emacspeakdir/{blurbs,servers,sounds}
mkdir -pv %buildroot%_libdir/emacspeak
mkdir -pv %buildroot%_docdir/emacspeak
mkdir -pv %buildroot%_bindir
mkdir -pv %buildroot%_sbindir
mkdir -pv %buildroot%_sysconfdir/emacs/site-start.d

# classic
mkdir -pv %buildroot%_emacspeakdir/sounds
cp -r sounds/classic %buildroot%_emacspeakdir/sounds/

# docs HTML
mkdir -pv %buildroot%_docdir/emacspeek/html
cp -v debian/*.html %buildroot%_docdir/emacspeek/html/
cp -v info/html/* %buildroot%_docdir/emacspeek/html/
cp -rv info/introducing-emacspeak %buildroot%_docdir/emacspeek/html/
cp -rv info/turning-twenty %buildroot%_docdir/emacspeek/html/

# espeak
mkdir -pv %buildroot%_emacspeakdir/blurbs
cp -v debian/espeak.blurb %buildroot%_emacspeakdir/blurbs/
mkdir -pv %buildroot%_libdir/emacspeak/native-espeak
cp -v servers/native-espeak/tclespeak.so %buildroot%_libdir/emacspeak/native-espeak/
mkdir -pv %buildroot%_emacspeakdir/servers
cp -rv servers/espeak %buildroot%_emacspeakdir/servers/
ln -s %_libdir/emacspeak/native-espeak %buildroot%_emacspeakdir/servers/native-espeak

# outloud
mkdir -pv %buildroot%_libdir/emacspeak/linux-outloud/
cp -v servers/linux-outloud/atcleci.so %buildroot%_libdir/emacspeak/linux-outloud/
cp -v servers/linux-outloud/eci.ini %buildroot%_libdir/emacspeak/linux-outloud/
cp -v debian/outloud.blurb %buildroot%_emacspeakdir/blurbs/
cp -v servers/outloud %buildroot%_emacspeakdir/servers/
cp -v servers/linux-outloud/asoundrc %buildroot%_libdir/emacspeak/linux-outloud/asoundrc
cp -v servers/linux-outloud/simple-asoundrc %buildroot%_libdir/emacspeak/linux-outloud/simple-asoundrc
ln -s %_libdir/emacspeak/linux-outloud %buildroot%_emacspeakdir/servers/linux-outloud

# pan-chimes
mkdir -pv %buildroot%_emacspeakdir/sounds/pan-chimes
cp -v sounds/pan-chimes/*.wav %buildroot%_emacspeakdir/sounds/pan-chimes/
install -m 644 sounds/pan-chimes/define-theme.el %buildroot%_emacspeakdir/sounds/pan-chimes/define-theme.el
mkdir -pv %buildroot%_docdir/emacspeak/pan-chimes
install -m 644 sounds/pan-chimes/README %buildroot%_docdir/emacspeak/pan-chimes/README
install -m 755 sounds/pan-chimes/apply-pan.sh %buildroot%_docdir/emacspeak/pan-chimes/apply-pan.sh

# emacspeak
install -D -m 644 debian/emacspeakconfig %buildroot%_sbindir/emacspeakconfig
install -D -m 644 debian/emacspeak.conf %buildroot%_sysconfdir/emacspeak
install -m 755 debian/dtk-exp.blurb %buildroot%_emacspeakdir/blurbs/dtk-exp.blurb
install -m 755 debian/ssh-dtk-exp.blurb %buildroot%_emacspeakdir/blurbs/ssh-dtk-exp.blurb
install -m 755 debian/ssh-outloud.blurb %buildroot%_emacspeakdir/blurbs/ssh-outloud.blurb
cp -rv etc %buildroot%_emacspeakdir/
cp -rv lisp %buildroot%_emacspeakdir/
cp -rv media %buildroot%_emacspeakdir/
cp -rv js %buildroot%_emacspeakdir/
cp -rv xsl %buildroot%_emacspeakdir/
install -m 644 Makefile %buildroot%_emacspeakdir/Makefile
install -m 644 README %buildroot%_emacspeakdir/README
install -m 444 sounds/emacspeak.mp3 %buildroot%_emacspeakdir//sounds/emacspeak.mp3
mkdir -pv %buildroot%_emacspeakdir/sounds/3d
cp -v sounds/3d/*.wav %buildroot%_emacspeakdir/sounds/3d/
install -m 644 sounds/3d/define-theme.el %buildroot%_emacspeakdir/sounds/3d/define-theme.el
cp -rv sounds/prompts %buildroot%_emacspeakdir/sounds/prompts
install -m 755 servers/dtk-exp %buildroot%_emacspeakdir/servers/dtk-exp
install -m 755 servers/speech-server %buildroot%_emacspeakdir/servers/speech-server
install -m 755 servers/ssh-dtk-exp %buildroot%_emacspeakdir/servers/ssh-dtk-exp
install -m 755 servers/ssh-outloud %buildroot%_emacspeakdir/servers/ssh-outloud
install -m 755 servers/tts-lib.tcl %buildroot%_emacspeakdir/servers/tts-lib.tcl
install -m 755 servers/.servers %buildroot%_emacspeakdir/servers/.servers
mkdir -pv %buildroot%_docdir/emacspeak
ln -sr %buildroot%_emacspeakdir/etc/NEWS %buildroot%_docdir/emacspeak/NEWS
ln -sr %buildroot%_emacspeakdir/etc/applications.html %buildroot%_docdir/emacspeak/applications.html
ln -sr %buildroot%_emacspeakdir/etc/tips.html %buildroot%_docdir/emacspeak/tips.html
ln -sr %buildroot%_emacspeakdir/etc/remote.txt %buildroot%_docdir/emacspeak/remote.txt
ln -sr %buildroot%_emacspeakdir/etc/install.org %buildroot%_docdir/emacspeak/install.org
mkdir -pv %buildroot%_bindir
ln -sr %buildroot%_emacspeakdir/etc/emacspeak.sh %buildroot%_bindir/emacspeak

install -m 755 %SOURCE3 %buildroot%_sysconfdir/emacspeak.conf

# emacsen install
FLAVOR=emacs
PACKAGE=emacspeak

ELDIR=%buildroot%_emacspeakdir/
ELCDIR=%buildroot%_emacspeakdir/
ELDIR_REL=../../../emacs/site-lisp/${PACKAGE}

echo install/${PACKAGE}: Handling install for emacsen flavor ${FLAVOR}

SITEFLAG="--no-site-file"

# Prevent gnupg to write to /root/.gnupg which leaves files behind on purge
export GNUPGHOME=`mktemp -d /tmp/gnupg.XXXXXX`

if [ -d ${ELCDIR} ]; then
    if [ ${FLAVOR} = emacs ]; then
        find ${ELCDIR}/lisp \( -name '*.elc' -o -name '*-cus-load.el' -o -name '*-loaddefs.el' \) -delete
        rm -f ${ELCDIR}/compile.log.gz
    else
        rm -rf ${ELCDIR}
    fi
fi

install -m 755 -d ${ELCDIR}/lisp/g-client

cd ${ELCDIR}/lisp
if [ ${FLAVOR} != emacs ]; then
    find ../${ELDIR_REL}/lisp \( -name '*.el' -o -name Makefile \) -maxdepth 1 -exec ln -s {} \; 2>/dev/null
fi
for file in *.elc
do [ -e "${file%%.elc}.el" ] || rm -f $file
done

cd g-client
if [ ${FLAVOR} != emacs ]; then
    find ../../${ELDIR_REL}/lisp/g-client -maxdepth 1 -mindepth 1 -not -name '*.in' -not -name indent-files.el -exec ln -s {} \; 2>/dev/null
fi
for file in *.elc
do [ -e "${file%%.elc}.el" ] || rm -f $file
done

cd ${ELCDIR}
if [ ${FLAVOR} != emacs ]; then
    for target in blurbs etc Makefile README media js servers sounds xsl
    do [ -e $target ] || ln -s ${ELDIR_REL}/$target
    done
fi
find -L . -type l -lname '*' -delete
touch .nosearch

# Create server symlinks AFTER emacsen cleanup
ln -sr %buildroot%_libdir/emacspeak/native-espeak %buildroot%_emacspeakdir/servers/native-espeak
ln -sr %buildroot%_libdir/emacspeak/linux-outloud %buildroot%_emacspeakdir/servers/linux-outloud

make -ks EMACS=${FLAVOR}

find lisp -name '*~' -delete
if [ ${FLAVOR} != emacs ]
then rm -f Makefile lisp/Makefile
fi

rm -rf ${GNUPGHOME}

# configs from Poretsky.
mkdir -pv %buildroot%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot%_sysconfdir/emacs/site-start.d/80keybindings.el
install -m 644 %SOURCE2 %buildroot%_sysconfdir/emacs/site-start.d/80site-defaults.el

# Clean up the installation tree
pushd %buildroot%_emacspeakdir
    pushd lisp
        rm -v external-code-readme.org README
        pushd g-client
            rm -rv *.html *.org COPYING rfc-imap-search
        popd
    popd
    pushd etc
        rm -f Makefile NEWS-* COPYRIGHT applications.dtd applications.mp applications.rnc applications.xml applications.xsl bootstrap.sh fetchmailrc iheart-player tips.xml tips.xsl youtube-dl-readme .youtube-dl.repos
    popd
popd

%post
chmod -R go+rX %_emacspeakdir/sounds
chmod -R go+rX %_emacspeakdir/media

%files
%_sbindir/emacspeakconfig
%config(noreplace) %_sysconfdir/emacspeak
%config(noreplace) %_sysconfdir/emacspeak.conf
%config(noreplace) %_sysconfdir/emacs/site-start.d/80keybindings.el
%config(noreplace) %_sysconfdir/emacs/site-start.d/80site-defaults.el
%_emacspeakdir/blurbs/dtk-exp.blurb
%_emacspeakdir/blurbs/ssh-dtk-exp.blurb
%_emacspeakdir/blurbs/ssh-outloud.blurb
%dir %_emacspeakdir/etc
%_emacspeakdir/etc/*
%_emacspeakdir/etc/.nosearch
%dir %_emacspeakdir/lisp
%_emacspeakdir/lisp/*
  %dir %_emacspeakdir/media
  %_emacspeakdir/media/*
  %_emacspeakdir/media/.nosearch
%dir %_emacspeakdir/js
%_emacspeakdir/js/*
%_emacspeakdir/js/.indium.json
%dir %_emacspeakdir/xsl
%_emacspeakdir/xsl/*
%_emacspeakdir/xsl/.nosearch
%_emacspeakdir/Makefile
%_emacspeakdir/README
%_emacspeakdir/sounds/emacspeak.mp3
%dir %_emacspeakdir/sounds/3d
%_emacspeakdir/sounds/3d/*.wav
%_emacspeakdir/sounds/3d/define-theme.el
%_emacspeakdir/sounds/prompts/*
%_emacspeakdir/servers/dtk-exp
%_emacspeakdir/servers/speech-server
%_emacspeakdir/servers/ssh-dtk-exp
%_emacspeakdir/servers/ssh-outloud
%_emacspeakdir/servers/tts-lib.tcl
%_emacspeakdir/servers/.servers
%_bindir/emacspeak
%_emacspeakdir/.nosearch

%files classic
%dir %_emacspeakdir/sounds/classic
%_emacspeakdir/sounds/classic/*

%files doc
%_docdir/emacspeek/html/*
%dir %_docdir/emacspeak
%_docdir/emacspeak/NEWS
%_docdir/emacspeak/applications.html
%_docdir/emacspeak/tips.html
%_docdir/emacspeak/remote.txt
%_docdir/emacspeak/install.org

%files espeak
%_emacspeakdir/blurbs/espeak.blurb
%_libdir/emacspeak/native-espeak/tclespeak.so
%_emacspeakdir/servers/espeak
%_emacspeakdir/servers/native-espeak

%files outloud
%_libdir/emacspeak/linux-outloud/atcleci.so
%_libdir/emacspeak/linux-outloud/eci.ini
%_emacspeakdir/blurbs/outloud.blurb
%_emacspeakdir/servers/outloud
%_libdir/emacspeak/linux-outloud/asoundrc
%_libdir/emacspeak/linux-outloud/simple-asoundrc
%_emacspeakdir/servers/linux-outloud

%files pan-chimes
%_emacspeakdir/sounds/pan-chimes/*.wav
%_emacspeakdir/sounds/pan-chimes/define-theme.el

%files pan-chimes-doc
%_docdir/emacspeak/pan-chimes/README
%_docdir/emacspeak/pan-chimes/apply-pan.sh

%changelog
* Thu Jun 11 2026 Artem Semenov <savoptik@altlinux.org> 50.0.22-alt3
- Added req to tclx

* Fri Jun 05 2026 Artem Semenov <savoptik@altlinux.org> 50.0.22-alt2
- Moved docs to doc subpackages

* Wed Jun 03 2026 Artem Semenov <savoptik@altlinux.org> 50.0.22-alt1
- Restructure install section for proper ALT packaging (thx Timofei Fedotov)
- Fix misplaced sit-for in cl-case otherwise clause (thx Timofei Fedotov)
- Fix global-voice-lock-mode initialization for Emacs 29 (thx Timofei Fedotov)
- Initial build for Sisyphus (ALT bug: 52268)
