%define speechd_moduledir %_libdir/speech-dispatcher-modules
%define speechd_confdir   %_datadir/speech-dispatcher/modules
%define tgsb_cxxflags %optflags -fPIC -Wall

Name: tgspeechbox
Version: 3.01
Release: alt1
Summary: Formant speech synthesis engine (LF glottal model, 26+ languages)
Summary(ru_RU.UTF-8): Формантный синтезатор речи с LF-моделью голосового источника и поддержкой 26+ языков

License: MIT
Group: Sound
Url: https://github.com/tgeczy/TGSpeechBox
Vcs: https://github.com/tgeczy/TGSpeechBox

Source0: %name-%version.tar
Source1: COPYING.GPLv3

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libstdc++-devel-static

Requires: %name-data = %EVR

%description
TGSpeechBox is a free formant speech synthesizer (fork of NV Speech
Player) generating speech with an LF-inspired glottal model, Fujisaki
pitch contours and coarticulation. This package provides the
IPA-to-PCM renderer (tgsbRender) and the tgsb-speak wrapper script.

Feed it IPA (e.g. from espeak-ng --ipa) and it renders raw PCM.
It does not do text-to-IPA conversion itself.

%description -l ru_RU.UTF-8
TGSpeechBox - свободный формантный синтезатор речи (форк NV Speech
Player), использующий LF-модель голосового источника, питч-контуры
Фудзисаки и коартикуляцию. Пакет содержит рендерер IPA-to-PCM
(tgsbRender) и обёртку tgsb-speak.
Сам по себе текст в IPA не превращает - для этого нужен внешний
фонемайзер, например espeak-ng.

%package data
Summary: Language and phoneme data for TGSpeechBox
Summary(ru_RU.UTF-8): Языковые и фонемные данные для TGSpeechBox
Group: Sound
BuildArch: noarch

%description data
Architecture-independent phoneme and language pack data (YAML)
used by tgsbRender and the native Speech Dispatcher module.

%description data -l ru_RU.UTF-8
Архитектурно-независимые данные фонем и языковых пакетов (YAML),
используемые tgsbRender и нативным модулем Speech Dispatcher.

%package -n speech-dispatcher-module-tgspeechbox
Summary: Speech Dispatcher integration for TGSpeechBox (generic + native module)
Summary(ru_RU.UTF-8): Интеграция TGSpeechBox с Speech Dispatcher (generic и нативный модуль)
Group: Sound
License: GPLv3
Requires: %name = %EVR
Requires: speech-dispatcher

%description -n speech-dispatcher-module-tgspeechbox
Speech Dispatcher integration for TGSpeechBox: the persistent native
module (sd_tgsb), which loads the engine once at startup instead of
spawning a process per utterance, and the generic-mode config
(tgsb-generic.conf) that drives tgsb-speak per utterance. The native
module is GPLv3 because it functionally depends on espeak-ng at
runtime, unlike the MIT core engine.

%description -n speech-dispatcher-module-tgspeechbox -l ru_RU.UTF-8
Интеграция TGSpeechBox с Speech Dispatcher: постоянный нативный
модуль (sd_tgsb), загружающий движок один раз при старте, без
порождения процесса на каждую фразу, и generic-конфиг
(tgsb-generic.conf) для tgsb-speak. Нативный модуль распространяется
под GPLv3, поскольку функционально зависит от espeak-ng в рантайме,
в отличие от MIT-ядра.

%prep
%setup -q
install -pm644 %SOURCE1 COPYING.GPLv3

%build
%make_build -f Makefile.linux STATIC=1 CXX="%__cxx" AR="%__ar" CXXFLAGS="%tgsb_cxxflags"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%speechd_moduledir
mkdir -p %buildroot%speechd_confdir
mkdir -p %buildroot%_datadir/%name/packs/lang
mkdir -p %buildroot%_datadir/%name/packs/dict

install -pm755 build/tgsbRender %buildroot%_bindir/
install -pm755 build/sd_tgsb %buildroot%speechd_moduledir/

install -pm755 extras/speech-dispatcher/tgsb-speak %buildroot%_bindir/
install -pm644 extras/speech-dispatcher/tgsb-generic.conf %buildroot%speechd_confdir/
install -pm644 extras/speech-dispatcher/tgsb-native.conf  %buildroot%speechd_confdir/

install -pm644 packs/phonemes.yaml %buildroot%_datadir/%name/packs/
cp -a packs/lang/*.yaml %buildroot%_datadir/%name/packs/lang/
[ -d packs/dict ] && cp -a packs/dict/. %buildroot%_datadir/%name/packs/dict/ || :

%check
tmpfile=$(mktemp)
printf 'h\u0259\u02c8lo\u028a w\u025c\u02d0ld' \
    | ./build/tgsbRender --lang en-us --packdir packs > "$tmpfile"
test -s "$tmpfile"
rm -f "$tmpfile"

%files
%doc LICENSE
%doc readme.md Developers.md Tuning.md Dictionary-editing.md README-linux.md
%_bindir/tgsbRender
%_bindir/tgsb-speak

%files data
%dir %_datadir/%name
%_datadir/%name/packs

%files -n speech-dispatcher-module-tgspeechbox
%doc COPYING.GPLv3
%speechd_moduledir/sd_tgsb
%speechd_confdir/tgsb-generic.conf
%speechd_confdir/tgsb-native.conf

%changelog
* Fri Jul 31 2026 Dina Tagantseva <dinchik@altlinux.org> 3.01-alt1
- Initial build for Sisyphus.

