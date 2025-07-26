%define _unpackaged_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: lomiri-keyboard
Version: 1.0.3
Release: alt1

Summary: Lomiri on-screen keyboard
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-keyboard

Source: %name-%version.tar

# sync with version 1.0.3-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-base-devel
BuildRequires: maliit-framework-devel
BuildRequires: pkgconfig(libpinyin)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: libpresage-devel
BuildRequires: pkgconfig(anthy)
BuildRequires: pkgconfig(chewing)
BuildRequires: /usr/bin/text2ngram

Requires: lomiri-keyboard-data

%description
Lomiri Keyboard based on Maliit-Keyboard

Maliit provides a flexible and cross-platform input method framework.
It has a plugin-based client-server architecture where applications act
as clients and communicate with the Maliit server via input context
plugins. The communication link currently uses D-Bus. Maliit is an open
source framework (LGPL 2) with open source plugins (BSD).

Lomiri-Keyboard on-screen keyboard is a Maliit plugin.

%package data
Group: Graphical desktop/Other
BuildArch: noarch
Summary: Lomiri on-screen keyboard

%description data
Lomiri Keyboard based on Maliit-Keyboard

Maliit provides a flexible and cross-platform input method framework.
It has a plugin-based client-server architecture where applications act
as clients and communicate with the Maliit server via input context
plugins. The communication link currently uses D-Bus. Maliit is an open
source framework (LGPL 2) with open source plugins (BSD).

Lomiri-Keyboard on-screen keyboard is a Maliit plugin.

%package devel
Group: Development/C++
Summary: Lomiri on-screen keyboard - development files

%description devel
Lomiri Keyboard based on Maliit-Keyboard

Maliit provides a flexible and cross-platform input method framework.
It has a plugin-based client-server architecture where applications act
as clients and communicate with the Maliit server via input context
plugins. The communication link currently uses D-Bus. Maliit is an open
source framework (LGPL 2) with open source plugins (BSD).

This package contains development files for lomiri-keyboard.

%package -n lomiri-keyboard-arabic
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-ar
Summary: Lomiri on-screen keyboard data files - Arabic
%description -n lomiri-keyboard-arabic
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Arabic

%package -n lomiri-keyboard-azerbaijani
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-az
Summary: Lomiri on-screen keyboard data files - Azerbaijani
%description -n lomiri-keyboard-azerbaijani
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Azerbaijani

%package -n lomiri-keyboard-belarusian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-be
Summary: Lomiri on-screen keyboard data files - Belarusian
%description -n lomiri-keyboard-belarusian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Belarusian

%package -n lomiri-keyboard-bengali
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-bn
Summary: Lomiri on-screen keyboard data files - Bengali National Layout
%description -n lomiri-keyboard-bengali
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Bengali National Layout

%package -n lomiri-keyboard-bengali-avro
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-bn
Summary: Lomiri on-screen keyboard data files - Bengali Avro Phonetic
%description -n lomiri-keyboard-bengali-avro
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Bengali Avro Phonetic

%package -n lomiri-keyboard-bengali-probhat
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: lomiri-keyboard-bengali
Requires: hunspell-bn
Summary: Lomiri on-screen keyboard data files - Bengali Probhat Layout
%description -n lomiri-keyboard-bengali-probhat
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Bengali Probhat Layout

%package -n lomiri-keyboard-bosnian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Summary: Lomiri on-screen keyboard data files - Bosnian
%description -n lomiri-keyboard-bosnian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Bosnian

%package -n lomiri-keyboard-bulgarian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-bg
Summary: Lomiri on-screen keyboard data files - Bulgarian
%description -n lomiri-keyboard-bulgarian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Bulgarian

%package -n lomiri-keyboard-catalan
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-ca
Summary: Lomiri on-screen keyboard data files - Catalan
%description -n lomiri-keyboard-catalan
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Catalan

%package -n lomiri-keyboard-chinese-chewing
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Summary: Lomiri on-screen keyboard data files - Chinese Chewing
%description -n lomiri-keyboard-chinese-chewing
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Chinese Chewing

%package -n lomiri-keyboard-chinese-pinyin
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Summary: Lomiri on-screen keyboard data files - Chinese Pinyin
%description -n lomiri-keyboard-chinese-pinyin
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Chinese Pinyin

%package -n lomiri-keyboard-croatian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-hr
Summary: Lomiri on-screen keyboard data files - Croatian
%description -n lomiri-keyboard-croatian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Croatian

%package -n lomiri-keyboard-czech
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-cs
Summary: Lomiri on-screen keyboard data files - Czech
%description -n lomiri-keyboard-czech
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Czech

%package -n lomiri-keyboard-danish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-da
Summary: Lomiri on-screen keyboard data files - Danish
%description -n lomiri-keyboard-danish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Danish

%package -n lomiri-keyboard-dutch
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-nl
Summary: Lomiri on-screen keyboard data files - Dutch
%description -n lomiri-keyboard-dutch
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Dutch

%package -n lomiri-keyboard-emoji
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: libqt5-qml
Summary: Lomiri on-screen keyboard data files - Emoji
%description -n lomiri-keyboard-emoji
Lomiri Keyboard based on Maliit-Keyboard
.
Data files for the Lomiri virtual keyboard - Emoji

%package -n lomiri-keyboard-english
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: ispell-en
Summary: Lomiri on-screen keyboard data files - English
%description -n lomiri-keyboard-english
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - English

%package -n lomiri-keyboard-english-dvorak
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: lomiri-keyboard-english,
Requires: ispell-en
Summary: Lomiri on-screen keyboard data files - English Dvorak
%description -n lomiri-keyboard-english-dvorak
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - English Dvorak

%package -n lomiri-keyboard-esperanto
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-eo
Summary: Lomiri on-screen keyboard data files - Esperanto
%description -n lomiri-keyboard-esperanto
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Esperanto

%package -n lomiri-keyboard-persian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-fa
Summary: Lomiri on-screen keyboard data files - Persian
%description -n lomiri-keyboard-persian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Persian

%package -n lomiri-keyboard-finnish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: aspell-fi
Summary: Lomiri on-screen keyboard data files - Finnish
%description -n lomiri-keyboard-finnish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Finnish

%package -n lomiri-keyboard-french
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-fr
Summary: Lomiri on-screen keyboard data files - French
%description -n lomiri-keyboard-french
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - French

%package -n lomiri-keyboard-german
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-de
Summary: Lomiri on-screen keyboard data files - German
%description -n lomiri-keyboard-german
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - German

%package -n lomiri-keyboard-greek
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-el,
Summary: Lomiri on-screen keyboard data files - Greek
%description -n lomiri-keyboard-greek
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Greek

%package -n lomiri-keyboard-hebrew
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: aspell-he
Summary: Lomiri on-screen keyboard data files - Hebrew
%description -n lomiri-keyboard-hebrew
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Hebrew

%package -n lomiri-keyboard-hungarian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-hu
Summary: Lomiri on-screen keyboard data files - Hungarian
%description -n lomiri-keyboard-hungarian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Hungarian

%package -n lomiri-keyboard-icelandic
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-is
Summary: Lomiri on-screen keyboard data files - Icelandic
%description -n lomiri-keyboard-icelandic
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Icelandic

%package -n lomiri-keyboard-italian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-it
Summary: Lomiri on-screen keyboard data files - Italian
%description -n lomiri-keyboard-italian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Italian

%package -n lomiri-keyboard-japanese
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: libanthy
Summary: Lomiri on-screen keyboard data files - Japanese
%description -n lomiri-keyboard-japanese
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Japanese

%package -n lomiri-keyboard-latvian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-lv
Summary: Lomiri on-screen keyboard data files - Latvian
%description -n lomiri-keyboard-latvian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Latvian

%package -n lomiri-keyboard-lithuanian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-lt
Summary: Lomiri on-screen keyboard data files - Lithuanian
%description -n lomiri-keyboard-lithuanian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Lithuanian

%package -n lomiri-keyboard-macedonian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-mk
Summary: Lomiri on-screen keyboard data files - Macedonian
%description -n lomiri-keyboard-macedonian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Macedonian

%package -n lomiri-keyboard-korean
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-ko
Summary: Lomiri on-screen keyboard data files - Korean
%description -n lomiri-keyboard-korean
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Korean

%package -n lomiri-keyboard-norwegian-bokmal
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-nb
Summary: Lomiri on-screen keyboard data files - Norwegian Bokmal
%description -n lomiri-keyboard-norwegian-bokmal
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Norwegian Bokmal

%package -n lomiri-keyboard-polish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-pl
Summary: Lomiri on-screen keyboard data files - Polish
%description -n lomiri-keyboard-polish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Polish

%package -n lomiri-keyboard-portuguese
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-pt
Summary: Lomiri on-screen keyboard data files - Portuguese
%description -n lomiri-keyboard-portuguese
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Portuguese

%package -n lomiri-keyboard-romanian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-ro
Summary: Lomiri on-screen keyboard data files - Romanian
%description -n lomiri-keyboard-romanian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Romanian

%package -n lomiri-keyboard-russian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-ru-aot
Summary: Lomiri on-screen keyboard data files - Russian
%description -n lomiri-keyboard-russian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Russian

%package -n lomiri-keyboard-slovenian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-sl
Summary: Lomiri on-screen keyboard data files - Slovenian
%description -n lomiri-keyboard-slovenian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Slovenian

%package -n lomiri-keyboard-serbian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-sr
Summary: Lomiri on-screen keyboard data files - Serbian
%description -n lomiri-keyboard-serbian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Serbian

%package -n lomiri-keyboard-scottish-gaelic
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-gd
Summary: Lomiri on-screen keyboard data files - Scottish Gaelic
%description -n lomiri-keyboard-scottish-gaelic
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Scottish Gaelic

%package -n lomiri-keyboard-spanish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-es
Summary: Lomiri on-screen keyboard data files - Spanish
%description -n lomiri-keyboard-spanish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Spanish

%package -n lomiri-keyboard-swedish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-sv
Summary: Lomiri on-screen keyboard data files - Swedish
%description -n lomiri-keyboard-swedish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Swedish

%package -n lomiri-keyboard-swiss-french
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-fr
Summary: Lomiri on-screen keyboard data files - Swiss French
%description -n lomiri-keyboard-swiss-french
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Swiss French

%package -n lomiri-keyboard-thai
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-th
Summary: Lomiri on-screen keyboard data files - Thai
%description -n lomiri-keyboard-thai
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Thai

%package -n lomiri-keyboard-turkish
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Summary: Lomiri on-screen keyboard data files - Turkish
%description -n lomiri-keyboard-turkish
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Turkish

%package -n lomiri-keyboard-ukrainian
Group: Graphical desktop/Other
Requires: lomiri-keyboard
Requires: hunspell-uk
Summary: Lomiri on-screen keyboard data files - Ukrainian
%description -n lomiri-keyboard-ukrainian
Lomiri Keyboard based on Maliit-Keyboard

Data files for the Lomiri virtual keyboard - Ukrainian

%prep
%setup
%patch -p1

%build
%qmake_qt5 \
           MALIIT_DEFAULT_PROFILE=lomiri \
           CONFIG+=debug \
           CONFIG+=nodoc \
           CONFIG+=enable-presage \
           CONFIG+=enable-hunspell \
           CONFIG+=enable-pinyin \
           CONFIG+=notests
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

mkdir -p %buildroot%_sysconfdir/xdg/maliit.org/
install -pD -m644 %_builddir/%name-%version/debian/server.conf %buildroot%_sysconfdir/xdg/maliit.org/server.conf

mkdir -p %buildroot%_sysconfdir/xdg/maliit.org/ %buildroot%_userunitdir/lomiri-keyboard.service
install -pD -m644 debian/systemd/maliit-server.service %buildroot%_userunitdir/lomiri-keyboard.service

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.BSD COPYING.CC-BY README.md STYLING VERSION
%_sysconfdir/xdg/maliit.org/server.conf
%dir /usr/lib/lomiri-keyboard
/usr/lib/lomiri-keyboard/libwesternsupport.a
%_userunitdir/lomiri-keyboard.service
%_libdir/maliit/plugins/liblomiri-keyboard-plugin.so

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-keyboard.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-keyboard.mo

%files data
%_datadir/glib-2.0/schemas/com.lomiri.keyboard.maliit.gschema.xml
%dir %_datadir/maliit/plugins/lomiri-keyboard/
%_datadir/maliit/plugins/lomiri-keyboard/*

%files devel
%dir %_includedir/lomiri-keyboard
%_includedir/lomiri-keyboard/languageplugininterface.h
%_includedir/lomiri-keyboard/westernlanguagesplugin.h

%files -n lomiri-keyboard-arabic
%dir /usr/lib/lomiri-keyboard/plugins/ar/
/usr/lib/lomiri-keyboard/plugins/ar/*

%files -n lomiri-keyboard-azerbaijani
%dir /usr/lib/lomiri-keyboard/plugins/az/
/usr/lib/lomiri-keyboard/plugins/az/*

%files -n lomiri-keyboard-belarusian
%dir /usr/lib/lomiri-keyboard/plugins/be/
/usr/lib/lomiri-keyboard/plugins/be/*

%files -n lomiri-keyboard-bengali
%dir /usr/lib/lomiri-keyboard/plugins/bn-avro/
/usr/lib/lomiri-keyboard/plugins/bn-avro/*

%files -n lomiri-keyboard-bengali-avro
%dir /usr/lib/lomiri-keyboard/plugins/bn/
/usr/lib/lomiri-keyboard/plugins/bn/*

%files -n lomiri-keyboard-bengali-probhat
%dir /usr/lib/lomiri-keyboard/plugins/bn-probhat/
/usr/lib/lomiri-keyboard/plugins/bn-probhat/*

%files -n lomiri-keyboard-bosnian
%dir /usr/lib/lomiri-keyboard/plugins/bs/
/usr/lib/lomiri-keyboard/plugins/bs/*

%files -n lomiri-keyboard-bulgarian
%dir /usr/lib/lomiri-keyboard/plugins/bg/
/usr/lib/lomiri-keyboard/plugins/bg/*

%files -n lomiri-keyboard-catalan
%dir /usr/lib/lomiri-keyboard/plugins/ca/
/usr/lib/lomiri-keyboard/plugins/ca/*

%files -n lomiri-keyboard-chinese-chewing
%dir /usr/lib/lomiri-keyboard/plugins/zh-hant/
/usr/lib/lomiri-keyboard/plugins/zh-hant/*

%files -n lomiri-keyboard-chinese-pinyin
%dir /usr/lib/lomiri-keyboard/plugins/zh-hans/
/usr/lib/lomiri-keyboard/plugins/zh-hans/*

%files -n lomiri-keyboard-croatian
%dir /usr/lib/lomiri-keyboard/plugins/hr/
/usr/lib/lomiri-keyboard/plugins/hr/*

%files -n lomiri-keyboard-czech
%dir /usr/lib/lomiri-keyboard/plugins/cs/
/usr/lib/lomiri-keyboard/plugins/cs/*

%files -n lomiri-keyboard-danish
%dir /usr/lib/lomiri-keyboard/plugins/da/
/usr/lib/lomiri-keyboard/plugins/da/*

%files -n lomiri-keyboard-dutch
%dir /usr/lib/lomiri-keyboard/plugins/nl/
/usr/lib/lomiri-keyboard/plugins/nl/*

%files -n lomiri-keyboard-emoji
%dir /usr/lib/lomiri-keyboard/plugins/emoji/
/usr/lib/lomiri-keyboard/plugins/emoji/*

%files -n lomiri-keyboard-english
%dir /usr/lib/lomiri-keyboard/plugins/en@dv/
/usr/lib/lomiri-keyboard/plugins/en@dv/*

%files -n lomiri-keyboard-english-dvorak
%dir /usr/lib/lomiri-keyboard/plugins/en/
/usr/lib/lomiri-keyboard/plugins/en/*

%files -n lomiri-keyboard-esperanto
%dir /usr/lib/lomiri-keyboard/plugins/eo/
/usr/lib/lomiri-keyboard/plugins/eo/*

%files -n lomiri-keyboard-persian
%dir /usr/lib/lomiri-keyboard/plugins/fi/
/usr/lib/lomiri-keyboard/plugins/fi/*

%files -n lomiri-keyboard-finnish
%dir /usr/lib/lomiri-keyboard/plugins/fr/
/usr/lib/lomiri-keyboard/plugins/fr/*

%files -n lomiri-keyboard-french
%dir /usr/lib/lomiri-keyboard/plugins/de/
/usr/lib/lomiri-keyboard/plugins/de/*

%files -n lomiri-keyboard-german
%dir /usr/lib/lomiri-keyboard/plugins/el/
/usr/lib/lomiri-keyboard/plugins/el/*

%files -n lomiri-keyboard-greek
%dir /usr/lib/lomiri-keyboard/plugins/he/
/usr/lib/lomiri-keyboard/plugins/he/*

%files -n lomiri-keyboard-hebrew
%dir /usr/lib/lomiri-keyboard/plugins/hu/
/usr/lib/lomiri-keyboard/plugins/hu/*

%files -n lomiri-keyboard-hungarian
%dir /usr/lib/lomiri-keyboard/plugins/is/
/usr/lib/lomiri-keyboard/plugins/is/*

%files -n lomiri-keyboard-icelandic
%dir /usr/lib/lomiri-keyboard/plugins/it/
/usr/lib/lomiri-keyboard/plugins/it/*

%files -n lomiri-keyboard-italian
%dir /usr/lib/lomiri-keyboard/plugins/ja/
/usr/lib/lomiri-keyboard/plugins/ja/*

%files -n lomiri-keyboard-japanese
%dir /usr/lib/lomiri-keyboard/plugins/ko/
/usr/lib/lomiri-keyboard/plugins/ko/*

%files -n lomiri-keyboard-latvian
%dir /usr/lib/lomiri-keyboard/plugins/lv/
/usr/lib/lomiri-keyboard/plugins/lv/*

%files -n lomiri-keyboard-lithuanian
%dir /usr/lib/lomiri-keyboard/plugins/lt/
/usr/lib/lomiri-keyboard/plugins/lt/*

%files -n lomiri-keyboard-macedonian
%dir /usr/lib/lomiri-keyboard/plugins/mk/
/usr/lib/lomiri-keyboard/plugins/mk/*

%files -n lomiri-keyboard-korean
%dir /usr/lib/lomiri-keyboard/plugins/nb/
/usr/lib/lomiri-keyboard/plugins/nb/*

%files -n lomiri-keyboard-norwegian-bokmal
%dir /usr/lib/lomiri-keyboard/plugins/fa/
/usr/lib/lomiri-keyboard/plugins/fa/*

%files -n lomiri-keyboard-polish
%dir /usr/lib/lomiri-keyboard/plugins/pl/
/usr/lib/lomiri-keyboard/plugins/pl/*

%files -n lomiri-keyboard-portuguese
%dir /usr/lib/lomiri-keyboard/plugins/pt/
/usr/lib/lomiri-keyboard/plugins/pt/*

%files -n lomiri-keyboard-romanian
%dir /usr/lib/lomiri-keyboard/plugins/ro/
/usr/lib/lomiri-keyboard/plugins/ro/*

%files -n lomiri-keyboard-russian
%dir /usr/lib/lomiri-keyboard/plugins/ru/
/usr/lib/lomiri-keyboard/plugins/ru/*

%files -n lomiri-keyboard-slovenian
%dir /usr/lib/lomiri-keyboard/plugins/gd/
/usr/lib/lomiri-keyboard/plugins/gd/*

%files -n lomiri-keyboard-serbian
%dir /usr/lib/lomiri-keyboard/plugins/sr/
/usr/lib/lomiri-keyboard/plugins/sr/*

%files -n lomiri-keyboard-scottish-gaelic
%dir /usr/lib/lomiri-keyboard/plugins/sl/
/usr/lib/lomiri-keyboard/plugins/sl/*

%files -n lomiri-keyboard-spanish
%dir /usr/lib/lomiri-keyboard/plugins/es/
/usr/lib/lomiri-keyboard/plugins/es/*

%files -n lomiri-keyboard-swedish
%dir /usr/lib/lomiri-keyboard/plugins/sv/
/usr/lib/lomiri-keyboard/plugins/sv/*

%files -n lomiri-keyboard-swiss-french
%dir /usr/lib/lomiri-keyboard/plugins/fr-ch/
/usr/lib/lomiri-keyboard/plugins/fr-ch/*

%files -n lomiri-keyboard-thai
%dir /usr/lib/lomiri-keyboard/plugins/th/
/usr/lib/lomiri-keyboard/plugins/th/*

%files -n lomiri-keyboard-turkish
%dir /usr/lib/lomiri-keyboard/plugins/tr/
/usr/lib/lomiri-keyboard/plugins/tr/*

%files -n lomiri-keyboard-ukrainian
%dir /usr/lib/lomiri-keyboard/plugins/uk/
/usr/lib/lomiri-keyboard/plugins/uk/*

%changelog
* Tue Jul 22 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
