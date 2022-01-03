Name:     gcompris-qt-data
Version:  20211229
Release:  alt1

Summary:  Contains optional data for gcompris-qt (words, background music)
License:  GPL and other
Group:    Other
Url:      https://github.com/gcompris/GCompris-data

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Contains optional data for gcompris-qt (words, background music).

%define lang_subpkg(l:n:) \
%define langcode %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package -n gcompris-qt-voices-%langcode\
Group: Games/Educational\
Summary: %langname voices for gcompris-qt\
BuildArch: noarch\
Requires: gcompris-qt\
\
%description -n gcompris-qt-voices-%langcode\
%langname voices for gcompris-qt.\
\
%files -n gcompris-qt-voices-%langcode\
%_datadir/gcompris-qt/voices/%langcode\

# see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# and https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes
%lang_subpkg -l af -n Afrikaans
%lang_subpkg -l ar -n Arabic
%lang_subpkg -l ast -n Asturian
%lang_subpkg -l bg -n Bulgarian
%lang_subpkg -l br -n Breton
%lang_subpkg -l ca -n Catalan
%lang_subpkg -l cs -n Czech
%lang_subpkg -l da -n Danish
%lang_subpkg -l de -n German
%lang_subpkg -l el -n Greek
%lang_subpkg -l en -n English
%lang_subpkg -l eo -n Esperanto
%lang_subpkg -l es -n Spanish
%lang_subpkg -l eu -n Basque
%lang_subpkg -l fi -n Finnish
%lang_subpkg -l fr -n French
%lang_subpkg -l ga -n Irish
%lang_subpkg -l gd -n "Gaelic; Scottish Gaelic"
%lang_subpkg -l he -n Hebrew
%lang_subpkg -l hi -n Hindi
%lang_subpkg -l hu -n Hungarian
%lang_subpkg -l id -n Indonesian
%lang_subpkg -l it -n Italian
%lang_subpkg -l kn -n Kannada
%lang_subpkg -l lt -n Lithuanian
%lang_subpkg -l mr -n Marathi
%lang_subpkg -l nb -n "Norwegian (Bokmal)"
%lang_subpkg -l nn -n "Norwegian (Nynorsk)"
%lang_subpkg -l nl -n Dutch
%lang_subpkg -l pa -n Panjabi
%lang_subpkg -l pl -n Polish
%lang_subpkg -l pt -n Portuguese
%lang_subpkg -l pt_BR -n "Portuguese (Brazil)"
%lang_subpkg -l ro -n Romanian
%lang_subpkg -l ru -n Russian
%lang_subpkg -l sk -n Slovakian
%lang_subpkg -l sl -n Slovenian
%lang_subpkg -l so -n Somali
%lang_subpkg -l sr -n Serbian
%lang_subpkg -l sv -n Swedish
%lang_subpkg -l th -n Thai
%lang_subpkg -l tr -n Turkish
%lang_subpkg -l ur -n Urdu
%lang_subpkg -l zh_CN -n "Chinese (Simplified)"
%lang_subpkg -l zh_TW -n "Chinese (Traditional)"

%prep
%setup

%install
mkdir -p %buildroot%_datadir/gcompris-qt
cp -aL voices %buildroot%_datadir/gcompris-qt
cp -a background-music/backgroundMusic %buildroot%_datadir/gcompris-qt
cp -a words/words words/words.qrc %buildroot%_datadir/gcompris-qt
rm -f %buildroot%_datadir/gcompris-qt/voices/{HOWTO_ENCODE,LICENSE,README.md,*.sh}
rm %buildroot%_datadir/gcompris-qt/voices/check_voices.py

%files
%_datadir/gcompris-qt/backgroundMusic/
%_datadir/gcompris-qt/words
%_datadir/gcompris-qt/words.qrc

%changelog
* Sun Jan 02 2022 Andrey Cherepanov <cas@altlinux.org> 20211229-alt1
- New version.

* Mon Apr 08 2019 Andrey Cherepanov <cas@altlinux.org> 20190304-alt1
- Initial build for Sisyphus.
