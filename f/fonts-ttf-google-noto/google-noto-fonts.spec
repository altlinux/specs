# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname google-noto-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname google-noto
%global fontconf %{fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global commit 86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552

Name:           fonts-ttf-google-noto
Version:        20161022
Release:        alt2_5
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
Group:          System/Fonts/True type
License:        OFL
URL:            https://github.com/googlei18n/noto-fonts/
# downloaded from https://github.com/googlei18n/noto-fonts/tree/86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552 -> download [zip]
# link https://codeload.github.com/googlei18n/noto-fonts/zip/86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552
Source0:        noto-fonts-%{commit}.zip
Source2:        66-%{fontconf}-sans.conf
Source3:        66-%{fontconf}-sans-armenian.conf
Source4:        66-%{fontconf}-sans-avestan.conf
Source5:        66-%{fontconf}-sans-bengali.conf
Source6:        66-%{fontconf}-sans-bengali-ui.conf
Source7:        66-%{fontconf}-sans-brahmi.conf
Source8:        66-%{fontconf}-sans-carian.conf
Source9:        66-%{fontconf}-sans-cherokee.conf
Source10:       66-%{fontconf}-sans-coptic.conf
Source11:       66-%{fontconf}-sans-deseret.conf
Source12:       66-%{fontconf}-sans-devanagari.conf
Source13:       66-%{fontconf}-sans-devanagari-ui.conf
Source14:       66-%{fontconf}-sans-egyptian-hieroglyphs.conf
Source15:       66-%{fontconf}-sans-ethiopic.conf
Source16:       66-%{fontconf}-sans-georgian.conf
Source17:       66-%{fontconf}-sans-glagolitic.conf
Source18:       66-%{fontconf}-sans-hebrew.conf
Source19:       66-%{fontconf}-sans-imperial-aramaic.conf
Source20:       66-%{fontconf}-sans-kaithi.conf
Source21:       66-%{fontconf}-sans-kannada.conf
Source22:       66-%{fontconf}-sans-kayah-li.conf
Source23:       66-%{fontconf}-sans-kharoshthi.conf
Source24:       66-%{fontconf}-sans-khmer.conf
Source25:       66-%{fontconf}-sans-khmer-ui.conf
Source26:       66-%{fontconf}-sans-lao.conf
Source27:       66-%{fontconf}-sans-lao-ui.conf
Source28:       66-%{fontconf}-sans-lisu.conf
Source29:       66-%{fontconf}-sans-lycian.conf
Source30:       66-%{fontconf}-sans-lydian.conf
Source31:       66-%{fontconf}-sans-malayalam.conf
Source32:       66-%{fontconf}-sans-malayalam-ui.conf
Source33:       66-%{fontconf}-sans-mandaic.conf
Source34:       66-%{fontconf}-sans-meetei-mayek.conf
Source35:       66-%{fontconf}-sans-nko.conf
Source36:       66-%{fontconf}-sans-old-south-arabian.conf
Source37:       66-%{fontconf}-sans-old-turkic.conf
Source38:       66-%{fontconf}-sans-osmanya.conf
Source39:       66-%{fontconf}-sans-phoenician.conf
Source40:       66-%{fontconf}-sans-shavian.conf
Source41:       66-%{fontconf}-sans-symbols.conf
Source42:       66-%{fontconf}-sans-tagalog.conf
Source43:       66-%{fontconf}-sans-tai-tham.conf
Source44:       66-%{fontconf}-sans-tamil.conf
Source45:       66-%{fontconf}-sans-tamil-ui.conf
Source46:       66-%{fontconf}-sans-telugu.conf
Source47:       66-%{fontconf}-sans-thai.conf
Source48:       66-%{fontconf}-sans-thai-ui.conf
Source49:       66-%{fontconf}-sans-ugaritic.conf
Source50:       66-%{fontconf}-sans-ui.conf
Source51:       66-%{fontconf}-sans-vai.conf
Source52:       66-%{fontconf}-serif-armenian.conf
Source53:       66-%{fontconf}-serif.conf
Source54:       66-%{fontconf}-serif-georgian.conf
Source55:       66-%{fontconf}-serif-khmer.conf
Source56:       66-%{fontconf}-serif-lao.conf
Source57:       66-%{fontconf}-serif-thai.conf
Source58:       66-%{fontconf}-sans-kannada-ui.conf
Source59:       66-%{fontconf}-sans-telugu-ui.conf
Source60:       66-%{fontconf}-sans-gujarati.conf
Source61:       66-%{fontconf}-sans-gujarati-ui.conf
Source62:       66-%{fontconf}-sans-hanunoo.conf
Source63:       66-%{fontconf}-sans-tai-viet.conf
Source64:       66-%{fontconf}-kufi-arabic.conf
Source65:       66-%{fontconf}-naskh-arabic.conf
Source66:       66-%{fontconf}-naskh-arabic-ui.conf
Source67:       66-%{fontconf}-sans-balinese.conf
Source68:       66-%{fontconf}-sans-bamum.conf
Source69:       66-%{fontconf}-sans-batak.conf
Source70:       66-%{fontconf}-sans-buginese.conf
Source71:       66-%{fontconf}-sans-buhid.conf
Source72:       66-%{fontconf}-sans-canadian-aboriginal.conf
Source73:       66-%{fontconf}-sans-cham.conf
Source74:       66-%{fontconf}-sans-cuneiform.conf
Source75:       66-%{fontconf}-sans-cypriot.conf
Source76:       66-%{fontconf}-sans-gothic.conf
Source77:       66-%{fontconf}-sans-gurmukhi.conf
Source78:       66-%{fontconf}-sans-gurmukhi-ui.conf
Source79:       66-%{fontconf}-sans-inscriptional-pahlavi.conf
Source80:       66-%{fontconf}-sans-inscriptional-parthian.conf
Source81:       66-%{fontconf}-sans-javanese.conf
Source82:       66-%{fontconf}-sans-lepcha.conf
Source83:       66-%{fontconf}-sans-limbu.conf
Source84:       66-%{fontconf}-sans-linear-b.conf
Source85:       66-%{fontconf}-sans-mongolian.conf
Source86:       66-%{fontconf}-sans-myanmar.conf
Source87:       66-%{fontconf}-sans-myanmar-ui.conf
Source88:       66-%{fontconf}-sans-new-tai-lue.conf
Source89:       66-%{fontconf}-sans-ogham.conf
Source90:       66-%{fontconf}-sans-ol-chiki.conf
Source91:       66-%{fontconf}-sans-old-italic.conf
Source92:       66-%{fontconf}-sans-old-persian.conf
Source93:       66-%{fontconf}-sans-phags-pa.conf
Source94:       66-%{fontconf}-sans-rejang.conf
Source95:       66-%{fontconf}-sans-runic.conf
Source96:       66-%{fontconf}-sans-samaritan.conf
Source97:       66-%{fontconf}-sans-saurashtra.conf
Source98:       66-%{fontconf}-sans-sinhala.conf
Source99:       66-%{fontconf}-sans-sundanese.conf
Source100:      66-%{fontconf}-sans-syloti-nagri.conf
Source101:      66-%{fontconf}-sans-syriac-eastern.conf
Source102:      66-%{fontconf}-sans-syriac-estrangela.conf
Source103:      66-%{fontconf}-sans-syriac-western.conf
Source104:      66-%{fontconf}-sans-tai-le.conf
Source105:      66-%{fontconf}-sans-tifinagh.conf
Source106:      66-%{fontconf}-sans-yi.conf
Source107:      66-%{fontconf}-sans-tagbanwa.conf
Source108:      66-%{fontconf}-sans-thaana.conf

Source156:      66-%{fontconf}-sans-oriya.conf
Source157:      66-%{fontconf}-sans-oriya-ui.conf
Source158:      66-%{fontconf}-nastaliq-urdu.conf
Source159:      66-%{fontconf}-sans-tibetan.conf
Source160:      66-%{fontconf}-mono.conf
Source161:      66-%{fontconf}-serif-bengali.conf
Source162:      66-%{fontconf}-serif-devanagari.conf
Source163:      66-%{fontconf}-serif-gujarati.conf
Source164:      66-%{fontconf}-serif-kannada.conf
Source165:      66-%{fontconf}-serif-malayalam.conf
Source166:      66-%{fontconf}-serif-tamil.conf
Source167:      66-%{fontconf}-serif-telugu.conf

# Add appstream metadata files
Source200:      %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontforge libfontforge
BuildRequires:  fontpackages-devel
%global _fontdir  %_ttffontsdir/%{fontname}
Source109: import.info

%description
%common_desc


%package -n fonts-ttf-google-noto-common
Group: System/Fonts/True type
Summary:        Common files for Noto fonts

%description -n fonts-ttf-google-noto-common
Common files for Google Noto fonts.

%package -n fonts-ttf-google-noto-kufi-arabic
Summary:	Kufi Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-kufi-arabic = 20161022-alt1_4
Obsoletes:	%{fontname}-kufi-arabic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-kufi-arabic
%common_desc
Noto font Kufi Arabic.

%files -n fonts-ttf-google-noto-kufi-arabic
%dir %{_fontdir}
%{_fontdir}/NotoKufiArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-kufi-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-kufi-arabic.conf
%{_datadir}/appdata/%{fontname}-kufi-arabic.metainfo.xml


%package -n fonts-ttf-google-noto-naskh-arabic
Summary:	Naskh Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-naskh-arabic fonts-ttf-google-noto-naskh-arabic-ui
Obsoletes:	%{fontname}-naskh-arabic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-naskh-arabic
%common_desc
Noto font Naskh Arabic.

%files -n fonts-ttf-google-noto-naskh-arabic
%dir %{_fontdir}
%{_fontdir}/NotoNaskhArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-naskh-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-naskh-arabic.conf
%{_datadir}/appdata/%{fontname}-naskh-arabic.metainfo.xml


%package -n fonts-ttf-google-noto-naskh-arabic-ui
Summary:	Naskh Arabic UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-naskh-arabic-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-naskh-arabic-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-naskh-arabic-ui
%common_desc
Noto font Naskh Arabic UI.

%files -n fonts-ttf-google-noto-naskh-arabic-ui
%dir %{_fontdir}
%{_fontdir}/NotoNaskhArabicUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-naskh-arabic-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-naskh-arabic-ui.conf
%{_datadir}/appdata/%{fontname}-naskh-arabic-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans
Summary:	Sans font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans fonts-ttf-google-noto-sans-armenian fonts-ttf-google-noto-sans-avestan fonts-ttf-google-noto-sans-balinese fonts-ttf-google-noto-sans-bamum fonts-ttf-google-noto-sans-batak fonts-ttf-google-noto-sans-bengali fonts-ttf-google-noto-sans-bengali-ui fonts-ttf-google-noto-sans-brahmi fonts-ttf-google-noto-sans-buginese fonts-ttf-google-noto-sans-buhid fonts-ttf-google-noto-sans-canadian-aboriginal fonts-ttf-google-noto-sans-carian fonts-ttf-google-noto-sans-cham fonts-ttf-google-noto-sans-cherokee fonts-ttf-google-noto-sans-coptic fonts-ttf-google-noto-sans-cuneiform fonts-ttf-google-noto-sans-cypriot fonts-ttf-google-noto-sans-deseret fonts-ttf-google-noto-sans-devanagari fonts-ttf-google-noto-sans-devanagari-ui fonts-ttf-google-noto-sans-egyptian-hieroglyphs fonts-ttf-google-noto-sans-ethiopic fonts-ttf-google-noto-sans-georgian fonts-ttf-google-noto-sans-glagolitic fonts-ttf-google-noto-sans-gothic fonts-ttf-google-noto-sans-gujarati fonts-ttf-google-noto-sans-gujarati-ui fonts-ttf-google-noto-sans-gurmukhi fonts-ttf-google-noto-sans-gurmukhi-ui fonts-ttf-google-noto-sans-hanunno fonts-ttf-google-noto-sans-hebrew fonts-ttf-google-noto-sans-imperial-aramaic fonts-ttf-google-noto-sans-inscriptional-pahlavi fonts-ttf-google-noto-sans-inscriptional-parthian fonts-ttf-google-noto-sans-javanese fonts-ttf-google-noto-sans-kaithi fonts-ttf-google-noto-sans-kannada fonts-ttf-google-noto-sans-kannada-ui fonts-ttf-google-noto-sans-kayah-li fonts-ttf-google-noto-sans-kharoshthi fonts-ttf-google-noto-sans-khmer fonts-ttf-google-noto-sans-khmer-ui fonts-ttf-google-noto-sans-lao fonts-ttf-google-noto-sans-lao-ui fonts-ttf-google-noto-sans-lepcha fonts-ttf-google-noto-sans-limbu fonts-ttf-google-noto-sans-linearb fonts-ttf-google-noto-sans-lisu fonts-ttf-google-noto-sans-lycian fonts-ttf-google-noto-sans-lydian fonts-ttf-google-noto-sans-malayalam fonts-ttf-google-noto-sans-malayalam-ui fonts-ttf-google-noto-sans-mandaic fonts-ttf-google-noto-sans-meeteimayek fonts-ttf-google-noto-sans-mongolian fonts-ttf-google-noto-sans-myanmar fonts-ttf-google-noto-sans-myanmar-ui fonts-ttf-google-noto-sans-new-tai-lue fonts-ttf-google-noto-sans-nko fonts-ttf-google-noto-sans-ogham fonts-ttf-google-noto-sans-ol-chiki fonts-ttf-google-noto-sans-old-italic fonts-ttf-google-noto-sans-old-persian fonts-ttf-google-noto-sans-old-south-arabian fonts-ttf-google-noto-sans-old-turkic fonts-ttf-google-noto-sans-oriya fonts-ttf-google-noto-sans-oriya-ui fonts-ttf-google-noto-sans-osmanya fonts-ttf-google-noto-sans-phags-pa fonts-ttf-google-noto-sans-phoenician fonts-ttf-google-noto-sans-rejang fonts-ttf-google-noto-sans-runic fonts-ttf-google-noto-sans-samaritan fonts-ttf-google-noto-sans-saurashtra fonts-ttf-google-noto-sans-shavian fonts-ttf-google-noto-sans-sinhala fonts-ttf-google-noto-sans-sundanese fonts-ttf-google-noto-sans-syloti-nagri fonts-ttf-google-noto-sans-symbols fonts-ttf-google-noto-sans-syriac-eastern fonts-ttf-google-noto-sans-syriac-estrangela fonts-ttf-google-noto-sans-syriac-western fonts-ttf-google-noto-sans-tagalog fonts-ttf-google-noto-sans-tagbanwa fonts-ttf-google-noto-sans-tai-le fonts-ttf-google-noto-sans-tai-tham fonts-ttf-google-noto-sans-tai-viet fonts-ttf-google-noto-sans-tamil fonts-ttf-google-noto-sans-tamil-ui fonts-ttf-google-noto-sans-telugu fonts-ttf-google-noto-sans-telugu-ui fonts-ttf-google-noto-sans-thaana fonts-ttf-google-noto-sans-thai fonts-ttf-google-noto-sans-thai-ui fonts-ttf-google-noto-sans-tibetan fonts-ttf-google-noto-sans-tifinagh fonts-ttf-google-noto-sans-ugaritic fonts-ttf-google-noto-sans-ui fonts-ttf-google-noto-sans-vai fonts-ttf-google-noto-sans-yi
Obsoletes:	%{fontname}-sans-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans
%common_desc
Noto font Sans.

%files -n fonts-ttf-google-noto-sans
%dir %{_fontdir}
%{_fontdir}/NotoSans-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans.conf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n fonts-ttf-google-noto-sans-ui
Summary:	Sans UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ui
%common_desc
Noto font Sans UI.

%files -n fonts-ttf-google-noto-sans-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ui.conf
%{_datadir}/appdata/%{fontname}-sans-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-armenian
Summary:	Sans Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-armenian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-armenian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-armenian
%common_desc
Noto font Sans Armenian.

%files -n fonts-ttf-google-noto-sans-armenian
%dir %{_fontdir}
%{_fontdir}/NotoSansArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-armenian.conf
%{_datadir}/appdata/%{fontname}-sans-armenian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-avestan
Summary:	Sans Avestan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-avestan = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-avestan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-avestan
%common_desc
Noto font Sans Avestan.

%files -n fonts-ttf-google-noto-sans-avestan
%dir %{_fontdir}
%{_fontdir}/NotoSansAvestan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-avestan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-avestan.conf
%{_datadir}/appdata/%{fontname}-sans-avestan.metainfo.xml


%package -n fonts-ttf-google-noto-sans-balinese
Summary:	Sans Balinese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-balinese = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-balinese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-balinese
%common_desc
Noto font Sans Balinese.

%files -n fonts-ttf-google-noto-sans-balinese
%dir %{_fontdir}
%{_fontdir}/NotoSansBalinese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-balinese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-balinese.conf
%{_datadir}/appdata/%{fontname}-sans-balinese.metainfo.xml


%package -n fonts-ttf-google-noto-sans-bamum
Summary:	Sans Bamum font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bamum = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-bamum-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bamum
%common_desc
Noto font Sans Bamum.

%files -n fonts-ttf-google-noto-sans-bamum
%dir %{_fontdir}
%{_fontdir}/NotoSansBamum-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bamum.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bamum.conf
%{_datadir}/appdata/%{fontname}-sans-bamum.metainfo.xml


%package -n fonts-ttf-google-noto-sans-batak
Summary:	Sans Batak font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-batak = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-batak-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-batak
%common_desc
Noto font Sans Batak.

%files -n fonts-ttf-google-noto-sans-batak
%dir %{_fontdir}
%{_fontdir}/NotoSansBatak-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-batak.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-batak.conf
%{_datadir}/appdata/%{fontname}-sans-batak.metainfo.xml


%package -n fonts-ttf-google-noto-sans-bengali
Summary:	Sans Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bengali fonts-ttf-google-noto-sans-bengali-ui
Obsoletes:	%{fontname}-sans-bengali-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali
%common_desc
Noto font Sans Bengali.

%files -n fonts-ttf-google-noto-sans-bengali
%dir %{_fontdir}
%{_fontdir}/NotoSansBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali.conf
%{_datadir}/appdata/%{fontname}-sans-bengali.metainfo.xml


%package -n fonts-ttf-google-noto-sans-bengali-ui
Summary:	Sans Bengali UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bengali-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-bengali-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali-ui
%common_desc
Noto font Sans Bengali UI.

%files -n fonts-ttf-google-noto-sans-bengali-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansBengaliUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali-ui.conf
%{_datadir}/appdata/%{fontname}-sans-bengali-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-brahmi
Summary:	Sans Brahmi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-brahmi = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-brahmi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-brahmi
%common_desc
Noto font Sans Brahmi.

%files -n fonts-ttf-google-noto-sans-brahmi
%dir %{_fontdir}
%{_fontdir}/NotoSansBrahmi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-brahmi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-brahmi.conf
%{_datadir}/appdata/%{fontname}-sans-brahmi.metainfo.xml


%package -n fonts-ttf-google-noto-sans-buginese
Summary:	Sans Buginese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-buginese = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-buginese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-buginese
%common_desc
Noto font Sans Buginese.

%files -n fonts-ttf-google-noto-sans-buginese
%dir %{_fontdir}
%{_fontdir}/NotoSansBuginese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buginese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buginese.conf
%{_datadir}/appdata/%{fontname}-sans-buginese.metainfo.xml


%package -n fonts-ttf-google-noto-sans-buhid
Summary:	Sans Buhid font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-buhid = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-buhid-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-buhid
%common_desc
Noto font Sans Buhid.

%files -n fonts-ttf-google-noto-sans-buhid
%dir %{_fontdir}
%{_fontdir}/NotoSansBuhid-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buhid.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buhid.conf
%{_datadir}/appdata/%{fontname}-sans-buhid.metainfo.xml


%package -n fonts-ttf-google-noto-sans-canadian-aboriginal
Summary:	Sans Canadian Aboriginal font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-canadian-aboriginal = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-canadian-aboriginal-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-canadian-aboriginal
%common_desc
Noto font Sans Canadian Aboriginal.

%files -n fonts-ttf-google-noto-sans-canadian-aboriginal
%dir %{_fontdir}
%{_fontdir}/NotoSansCanadianAboriginal-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%{_datadir}/appdata/%{fontname}-sans-canadian-aboriginal.metainfo.xml


%package -n fonts-ttf-google-noto-sans-carian
Summary:	Sans Carian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-carian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-carian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-carian
%common_desc
Noto font Sans Carian.

%files -n fonts-ttf-google-noto-sans-carian
%dir %{_fontdir}
%{_fontdir}/NotoSansCarian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-carian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-carian.conf
%{_datadir}/appdata/%{fontname}-sans-carian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-cham
Summary:	Sans Cham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cham = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-cham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cham
%common_desc
Noto font Sans Cham.

%files -n fonts-ttf-google-noto-sans-cham
%dir %{_fontdir}
%{_fontdir}/NotoSansCham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cham.conf
%{_datadir}/appdata/%{fontname}-sans-cham.metainfo.xml


%package -n fonts-ttf-google-noto-sans-cherokee
Summary:	Sans Cherokee font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cherokee = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-cherokee-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cherokee
%common_desc
Noto font Sans Cherokee.

%files -n fonts-ttf-google-noto-sans-cherokee
%dir %{_fontdir}
%{_fontdir}/NotoSansCherokee-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cherokee.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cherokee.conf
%{_datadir}/appdata/%{fontname}-sans-cherokee.metainfo.xml


%package -n fonts-ttf-google-noto-sans-coptic
Summary:	Sans Coptic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-coptic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-coptic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-coptic
%common_desc
Noto font Sans Coptic.

%files -n fonts-ttf-google-noto-sans-coptic
%dir %{_fontdir}
%{_fontdir}/NotoSansCoptic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-coptic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-coptic.conf
%{_datadir}/appdata/%{fontname}-sans-coptic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-cuneiform
Summary:	Sans Cuneiform font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cuneiform = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-cuneiform-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cuneiform
%common_desc
Noto font Sans Cuneiform.

%files -n fonts-ttf-google-noto-sans-cuneiform
%dir %{_fontdir}
%{_fontdir}/NotoSansCuneiform-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cuneiform.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cuneiform.conf
%{_datadir}/appdata/%{fontname}-sans-cuneiform.metainfo.xml


%package -n fonts-ttf-google-noto-sans-cypriot
Summary:	Sans Cypriot font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cypriot = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-cypriot-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cypriot
%common_desc
Noto font Sans Cypriot.

%files -n fonts-ttf-google-noto-sans-cypriot
%dir %{_fontdir}
%{_fontdir}/NotoSansCypriot-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cypriot.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cypriot.conf
%{_datadir}/appdata/%{fontname}-sans-cypriot.metainfo.xml


%package -n fonts-ttf-google-noto-sans-deseret
Summary:	Sans Deseret font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-deseret = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-deseret-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-deseret
%common_desc
Noto font Sans Deseret.

%files -n fonts-ttf-google-noto-sans-deseret
%dir %{_fontdir}
%{_fontdir}/NotoSansDeseret-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-deseret.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-deseret.conf
%{_datadir}/appdata/%{fontname}-sans-deseret.metainfo.xml


%package -n fonts-ttf-google-noto-sans-devanagari
Summary:	Sans Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-devanagari fonts-ttf-google-noto-sans-devanagari-ui
Obsoletes:	%{fontname}-sans-devanagari-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari
%common_desc
Noto font Sans Devanagari.

%files -n fonts-ttf-google-noto-sans-devanagari
%dir %{_fontdir}
%{_fontdir}/NotoSansDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari.conf
%{_datadir}/appdata/%{fontname}-sans-devanagari.metainfo.xml


%package -n fonts-ttf-google-noto-sans-devanagari-ui
Summary:	Sans Devanagari UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-devanagari-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-devanagari-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari-ui
%common_desc
Noto font Sans Devanagari UI.

%files -n fonts-ttf-google-noto-sans-devanagari-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansDevanagariUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari-ui.conf
%{_datadir}/appdata/%{fontname}-sans-devanagari-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
Summary:	Sans Egyptian Hieroglyphs font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-egyptian-hieroglyphs = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-egyptian-hieroglyphs-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%common_desc
Noto font Sans Egyptian Hieroglyphs.

%files -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%dir %{_fontdir}
%{_fontdir}/NotoSansEgyptianHieroglyphs-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%{_datadir}/appdata/%{fontname}-sans-egyptian-hieroglyphs.metainfo.xml


%package -n fonts-ttf-google-noto-sans-ethiopic
Summary:	Sans Ethiopic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ethiopic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-ethiopic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ethiopic
%common_desc
Noto font Sans Ethiopic.

%files -n fonts-ttf-google-noto-sans-ethiopic
%dir %{_fontdir}
%{_fontdir}/NotoSansEthiopic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ethiopic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ethiopic.conf
%{_datadir}/appdata/%{fontname}-sans-ethiopic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-georgian
Summary:	Sans Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-georgian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-georgian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-georgian
%common_desc
Noto font Sans Georgian.

%files -n fonts-ttf-google-noto-sans-georgian
%dir %{_fontdir}
%{_fontdir}/NotoSansGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-georgian.conf
%{_datadir}/appdata/%{fontname}-sans-georgian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-glagolitic
Summary:	Sans Glagolitic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-glagolitic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-glagolitic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-glagolitic
%common_desc
Noto font Sans Glagolitic.

%files -n fonts-ttf-google-noto-sans-glagolitic
%dir %{_fontdir}
%{_fontdir}/NotoSansGlagolitic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-glagolitic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-glagolitic.conf
%{_datadir}/appdata/%{fontname}-sans-glagolitic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-gothic
Summary:	Sans Gothic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gothic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-gothic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gothic
%common_desc
Noto font Sans Gothic.

%files -n fonts-ttf-google-noto-sans-gothic
%dir %{_fontdir}
%{_fontdir}/NotoSansGothic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gothic.conf
%{_datadir}/appdata/%{fontname}-sans-gothic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-gujarati
Summary:	Sans Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gujarati fonts-ttf-google-noto-sans-gujarati-ui
Obsoletes:	%{fontname}-sans-gujarati-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gujarati
%common_desc
Noto font Sans Gujarati.

%files -n fonts-ttf-google-noto-sans-gujarati
%dir %{_fontdir}
%{_fontdir}/NotoSansGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gujarati.conf
%{_datadir}/appdata/%{fontname}-sans-gujarati.metainfo.xml


%package -n fonts-ttf-google-noto-sans-gujarati-ui
Summary:	Sans Gujarati UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gujarati-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-gujarati-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gujarati-ui
%common_desc
Noto font Sans Gujarati UI.

%files -n fonts-ttf-google-noto-sans-gujarati-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansGujaratiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gujarati-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gujarati-ui.conf
%{_datadir}/appdata/%{fontname}-sans-gujarati-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-gurmukhi
Summary:	Sans Gurmukhi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gurmukhi fonts-ttf-google-noto-sans-gurmukhi-ui
Obsoletes:	%{fontname}-sans-gurmukhi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gurmukhi
%common_desc
Noto font Sans Gurmukhi.

%files -n fonts-ttf-google-noto-sans-gurmukhi
%dir %{_fontdir}
%{_fontdir}/NotoSansGurmukhi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gurmukhi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gurmukhi.conf
%{_datadir}/appdata/%{fontname}-sans-gurmukhi.metainfo.xml


%package -n fonts-ttf-google-noto-sans-gurmukhi-ui
Summary:	Sans Gurmukhi UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gurmukhi-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-gurmukhi-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gurmukhi-ui
%common_desc
Noto font Sans Gurmukhi UI.

%files -n fonts-ttf-google-noto-sans-gurmukhi-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansGurmukhiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gurmukhi-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gurmukhi-ui.conf
%{_datadir}/appdata/%{fontname}-sans-gurmukhi-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-hanunno
Summary:	Sans Hanunoo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-hanunno = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-hanunoo-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{fontname}-sans-hanunno < %EVR

%description -n fonts-ttf-google-noto-sans-hanunno
%common_desc
Noto font Sans Hanunoo.

%files -n fonts-ttf-google-noto-sans-hanunno
%dir %{_fontdir}
%{_fontdir}/NotoSansHanunoo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hanunoo.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hanunoo.conf
%{_datadir}/appdata/%{fontname}-sans-hanunoo.metainfo.xml


%package -n fonts-ttf-google-noto-sans-hebrew
Summary:	Sans Hebrew font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-hebrew = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-hebrew-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-hebrew
%common_desc
Noto font Sans Hebrew.

%files -n fonts-ttf-google-noto-sans-hebrew
%dir %{_fontdir}
%{_fontdir}/NotoSansHebrew-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hebrew.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hebrew.conf
%{_datadir}/appdata/%{fontname}-sans-hebrew.metainfo.xml


%package -n fonts-ttf-google-noto-sans-imperial-aramaic
Summary:	Sans Imperial Aramaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-imperial-aramaic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-imperial-aramaic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-imperial-aramaic
%common_desc
Noto font Sans Imperial Aramaic.

%files -n fonts-ttf-google-noto-sans-imperial-aramaic
%dir %{_fontdir}
%{_fontdir}/NotoSansImperialAramaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-imperial-aramaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-imperial-aramaic.conf
%{_datadir}/appdata/%{fontname}-sans-imperial-aramaic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
Summary:	Sans Inscriptional Pahlavi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-inscriptional-pahlavi = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-inscriptional-pahlavi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
%common_desc
Noto font Sans Inscriptional Pahlavi.

%files -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
%dir %{_fontdir}
%{_fontdir}/NotoSansInscriptionalPahlavi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%{_datadir}/appdata/%{fontname}-sans-inscriptional-pahlavi.metainfo.xml


%package -n fonts-ttf-google-noto-sans-inscriptional-parthian
Summary:	Sans Inscriptional Parthian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-inscriptional-parthian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-inscriptional-parthian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-inscriptional-parthian
%common_desc
Noto font Sans Inscriptional Parthian.

%files -n fonts-ttf-google-noto-sans-inscriptional-parthian
%dir %{_fontdir}
%{_fontdir}/NotoSansInscriptionalParthian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%{_datadir}/appdata/%{fontname}-sans-inscriptional-parthian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-javanese
Summary:	Sans Javanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-javanese = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-javanese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-javanese
%common_desc
Noto font Sans Javanese.

%files -n fonts-ttf-google-noto-sans-javanese
%dir %{_fontdir}
%{_fontdir}/NotoSansJavanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-javanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-javanese.conf
%{_datadir}/appdata/%{fontname}-sans-javanese.metainfo.xml


%package -n fonts-ttf-google-noto-sans-kaithi
Summary:	Sans Kaithi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kaithi = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-kaithi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kaithi
%common_desc
Noto font Sans Kaithi.

%files -n fonts-ttf-google-noto-sans-kaithi
%dir %{_fontdir}
%{_fontdir}/NotoSansKaithi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kaithi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kaithi.conf
%{_datadir}/appdata/%{fontname}-sans-kaithi.metainfo.xml


%package -n fonts-ttf-google-noto-sans-kannada
Summary:	Sans Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kannada fonts-ttf-google-noto-sans-kannada-ui
Obsoletes:	%{fontname}-sans-kannada-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada
%common_desc
Noto font Sans Kannada.

%files -n fonts-ttf-google-noto-sans-kannada
%dir %{_fontdir}
%{_fontdir}/NotoSansKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada.conf
%{_datadir}/appdata/%{fontname}-sans-kannada.metainfo.xml


%package -n fonts-ttf-google-noto-sans-kannada-ui
Summary:	Sans Kannada UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kannada-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-kannada-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada-ui
%common_desc
Noto font Sans Kannada UI.

%files -n fonts-ttf-google-noto-sans-kannada-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansKannadaUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada-ui.conf
%{_datadir}/appdata/%{fontname}-sans-kannada-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-kayah-li
Summary:	Sans Kayah Li font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kayah-li = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-kayah-li-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kayah-li
%common_desc
Noto font Sans Kayah Li.

%files -n fonts-ttf-google-noto-sans-kayah-li
%dir %{_fontdir}
%{_fontdir}/NotoSansKayahLi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kayah-li.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kayah-li.conf
%{_datadir}/appdata/%{fontname}-sans-kayah-li.metainfo.xml


%package -n fonts-ttf-google-noto-sans-kharoshthi
Summary:	Sans Kharoshthi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kharoshthi = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-kharoshthi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kharoshthi
%common_desc
Noto font Sans Kharoshthi.

%files -n fonts-ttf-google-noto-sans-kharoshthi
%dir %{_fontdir}
%{_fontdir}/NotoSansKharoshthi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kharoshthi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kharoshthi.conf
%{_datadir}/appdata/%{fontname}-sans-kharoshthi.metainfo.xml


%package -n fonts-ttf-google-noto-sans-khmer
Summary:	Sans Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khmer fonts-ttf-google-noto-sans-khmer-ui
Obsoletes:	%{fontname}-sans-khmer-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer
%common_desc
Noto font Sans Khmer.

%files -n fonts-ttf-google-noto-sans-khmer
%dir %{_fontdir}
%{_fontdir}/NotoSansKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer.conf
%{_datadir}/appdata/%{fontname}-sans-khmer.metainfo.xml


%package -n fonts-ttf-google-noto-sans-khmer-ui
Summary:	Sans Khmer UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khmer-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-khmer-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer-ui
%common_desc
Noto font Sans Khmer UI.

%files -n fonts-ttf-google-noto-sans-khmer-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansKhmerUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer-ui.conf
%{_datadir}/appdata/%{fontname}-sans-khmer-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lao
Summary:	Sans Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lao fonts-ttf-google-noto-sans-lao-ui
Obsoletes:	%{fontname}-sans-lao-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao
%common_desc
Noto font Sans Lao.

%files -n fonts-ttf-google-noto-sans-lao
%dir %{_fontdir}
%{_fontdir}/NotoSansLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao.conf
%{_datadir}/appdata/%{fontname}-sans-lao.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lao-ui
Summary:	Sans Lao UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lao-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-lao-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao-ui
%common_desc
Noto font Sans Lao UI.

%files -n fonts-ttf-google-noto-sans-lao-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansLaoUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao-ui.conf
%{_datadir}/appdata/%{fontname}-sans-lao-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lepcha
Summary:	Sans Lepcha font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lepcha = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-lepcha-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lepcha
%common_desc
Noto font Sans Lepcha.

%files -n fonts-ttf-google-noto-sans-lepcha
%dir %{_fontdir}
%{_fontdir}/NotoSansLepcha-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lepcha.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lepcha.conf
%{_datadir}/appdata/%{fontname}-sans-lepcha.metainfo.xml


%package -n fonts-ttf-google-noto-sans-limbu
Summary:	Sans Limbu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-limbu = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-limbu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-limbu
%common_desc
Noto font Sans Limbu.

%files -n fonts-ttf-google-noto-sans-limbu
%dir %{_fontdir}
%{_fontdir}/NotoSansLimbu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-limbu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-limbu.conf
%{_datadir}/appdata/%{fontname}-sans-limbu.metainfo.xml


%package -n fonts-ttf-google-noto-sans-linearb
Summary:	Sans Linear B font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-linearb = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-linear-b-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{fontname}-sans-linearb < %EVR

%description -n fonts-ttf-google-noto-sans-linearb
%common_desc
Noto font Sans Linear B.

%files -n fonts-ttf-google-noto-sans-linearb
%dir %{_fontdir}
%{_fontdir}/NotoSansLinearB-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-linear-b.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-linear-b.conf
%{_datadir}/appdata/%{fontname}-sans-linear-b.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lisu
Summary:	Sans Lisu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lisu = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-lisu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lisu
%common_desc
Noto font Sans Lisu.

%files -n fonts-ttf-google-noto-sans-lisu
%dir %{_fontdir}
%{_fontdir}/NotoSansLisu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lisu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lisu.conf
%{_datadir}/appdata/%{fontname}-sans-lisu.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lycian
Summary:	Sans Lycian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lycian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-lycian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lycian
%common_desc
Noto font Sans Lycian.

%files -n fonts-ttf-google-noto-sans-lycian
%dir %{_fontdir}
%{_fontdir}/NotoSansLycian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lycian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lycian.conf
%{_datadir}/appdata/%{fontname}-sans-lycian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-lydian
Summary:	Sans Lydian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lydian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-lydian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lydian
%common_desc
Noto font Sans Lydian.

%files -n fonts-ttf-google-noto-sans-lydian
%dir %{_fontdir}
%{_fontdir}/NotoSansLydian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lydian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lydian.conf
%{_datadir}/appdata/%{fontname}-sans-lydian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-malayalam
Summary:	Sans Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-malayalam fonts-ttf-google-noto-sans-malayalam-ui
Obsoletes:	%{fontname}-sans-malayalam-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam
%common_desc
Noto font Sans Malayalam.

%files -n fonts-ttf-google-noto-sans-malayalam
%dir %{_fontdir}
%{_fontdir}/NotoSansMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam.conf
%{_datadir}/appdata/%{fontname}-sans-malayalam.metainfo.xml


%package -n fonts-ttf-google-noto-sans-malayalam-ui
Summary:	Sans Malayalam UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-malayalam-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-malayalam-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam-ui
%common_desc
Noto font Sans Malayalam UI.

%files -n fonts-ttf-google-noto-sans-malayalam-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansMalayalamUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam-ui.conf
%{_datadir}/appdata/%{fontname}-sans-malayalam-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-mandaic
Summary:	Sans Mandaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mandaic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-mandaic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mandaic
%common_desc
Noto font Sans Mandaic.

%files -n fonts-ttf-google-noto-sans-mandaic
%dir %{_fontdir}
%{_fontdir}/NotoSansMandaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mandaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mandaic.conf
%{_datadir}/appdata/%{fontname}-sans-mandaic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-meeteimayek
Summary:	Sans Meetei Mayek font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-meeteimayek = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-meetei-mayek-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{fontname}-sans-meeteimayek < %EVR

%description -n fonts-ttf-google-noto-sans-meeteimayek
%common_desc
Noto font Sans Meetei Mayek.

%files -n fonts-ttf-google-noto-sans-meeteimayek
%dir %{_fontdir}
%{_fontdir}/NotoSansMeeteiMayek-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-meetei-mayek.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-meetei-mayek.conf
%{_datadir}/appdata/%{fontname}-sans-meetei-mayek.metainfo.xml


%package -n fonts-ttf-google-noto-sans-mongolian
Summary:	Sans Mongolian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mongolian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-mongolian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mongolian
%common_desc
Noto font Sans Mongolian.

%files -n fonts-ttf-google-noto-sans-mongolian
%dir %{_fontdir}
%{_fontdir}/NotoSansMongolian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mongolian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mongolian.conf
%{_datadir}/appdata/%{fontname}-sans-mongolian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-myanmar
Summary:	Sans Myanmar font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-myanmar fonts-ttf-google-noto-sans-myanmar-ui
Obsoletes:	%{fontname}-sans-myanmar-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar
%common_desc
Noto font Sans Myanmar.

%files -n fonts-ttf-google-noto-sans-myanmar
%dir %{_fontdir}
%{_fontdir}/NotoSansMyanmar-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar.conf
%{_datadir}/appdata/%{fontname}-sans-myanmar.metainfo.xml


%package -n fonts-ttf-google-noto-sans-myanmar-ui
Summary:	Sans Myanmar UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-myanmar-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-myanmar-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar-ui
%common_desc
Noto font Sans Myanmar UI.

%files -n fonts-ttf-google-noto-sans-myanmar-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansMyanmarUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar-ui.conf
%{_datadir}/appdata/%{fontname}-sans-myanmar-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-new-tai-lue
Summary:	Sans New Tai Lue font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-new-tai-lue = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-new-tai-lue-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-new-tai-lue
%common_desc
Noto font Sans New Tai Lue.

%files -n fonts-ttf-google-noto-sans-new-tai-lue
%dir %{_fontdir}
%{_fontdir}/NotoSansNewTaiLue-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-new-tai-lue.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-new-tai-lue.conf
%{_datadir}/appdata/%{fontname}-sans-new-tai-lue.metainfo.xml


%package -n fonts-ttf-google-noto-sans-nko
Summary:	Sans NKo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-nko = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-nko-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-nko
%common_desc
Noto font Sans NKo.

%files -n fonts-ttf-google-noto-sans-nko
%dir %{_fontdir}
%{_fontdir}/NotoSansNKo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-nko.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-nko.conf
%{_datadir}/appdata/%{fontname}-sans-nko.metainfo.xml


%package -n fonts-ttf-google-noto-sans-ogham
Summary:	Sans Ogham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ogham = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-ogham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ogham
%common_desc
Noto font Sans Ogham.

%files -n fonts-ttf-google-noto-sans-ogham
%dir %{_fontdir}
%{_fontdir}/NotoSansOgham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ogham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ogham.conf
%{_datadir}/appdata/%{fontname}-sans-ogham.metainfo.xml


%package -n fonts-ttf-google-noto-sans-ol-chiki
Summary:	Sans Ol Chiki font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ol-chiki = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-ol-chiki-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ol-chiki
%common_desc
Noto font Sans Ol Chiki.

%files -n fonts-ttf-google-noto-sans-ol-chiki
%dir %{_fontdir}
%{_fontdir}/NotoSansOlChiki-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ol-chiki.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ol-chiki.conf
%{_datadir}/appdata/%{fontname}-sans-ol-chiki.metainfo.xml


%package -n fonts-ttf-google-noto-sans-old-italic
Summary:	Sans Old Italic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-italic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-old-italic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-italic
%common_desc
Noto font Sans Old Italic.

%files -n fonts-ttf-google-noto-sans-old-italic
%dir %{_fontdir}
%{_fontdir}/NotoSansOldItalic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-italic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-italic.conf
%{_datadir}/appdata/%{fontname}-sans-old-italic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-old-persian
Summary:	Sans Old Persian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-persian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-old-persian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-persian
%common_desc
Noto font Sans Old Persian.

%files -n fonts-ttf-google-noto-sans-old-persian
%dir %{_fontdir}
%{_fontdir}/NotoSansOldPersian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-persian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-persian.conf
%{_datadir}/appdata/%{fontname}-sans-old-persian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-old-south-arabian
Summary:	Sans Old South Arabian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-south-arabian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-old-south-arabian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-south-arabian
%common_desc
Noto font Sans Old South Arabian.

%files -n fonts-ttf-google-noto-sans-old-south-arabian
%dir %{_fontdir}
%{_fontdir}/NotoSansOldSouthArabian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-south-arabian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-south-arabian.conf
%{_datadir}/appdata/%{fontname}-sans-old-south-arabian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-old-turkic
Summary:	Sans Old Turkic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-turkic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-old-turkic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-turkic
%common_desc
Noto font Sans Old Turkic.

%files -n fonts-ttf-google-noto-sans-old-turkic
%dir %{_fontdir}
%{_fontdir}/NotoSansOldTurkic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-turkic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-turkic.conf
%{_datadir}/appdata/%{fontname}-sans-old-turkic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-osmanya
Summary:	Sans Osmanya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-osmanya = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-osmanya-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-osmanya
%common_desc
Noto font Sans Osmanya.

%files -n fonts-ttf-google-noto-sans-osmanya
%dir %{_fontdir}
%{_fontdir}/NotoSansOsmanya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-osmanya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-osmanya.conf
%{_datadir}/appdata/%{fontname}-sans-osmanya.metainfo.xml


%package -n fonts-ttf-google-noto-sans-phags-pa
Summary:	Sans Phags Pa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-phags-pa = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-phags-pa-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-phags-pa
%common_desc
Noto font Sans Phags Pa.

%files -n fonts-ttf-google-noto-sans-phags-pa
%dir %{_fontdir}
%{_fontdir}/NotoSansPhagsPa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phags-pa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phags-pa.conf
%{_datadir}/appdata/%{fontname}-sans-phags-pa.metainfo.xml


%package -n fonts-ttf-google-noto-sans-phoenician
Summary:	Sans Phoenician font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-phoenician = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-phoenician-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-phoenician
%common_desc
Noto font Sans Phoenician.

%files -n fonts-ttf-google-noto-sans-phoenician
%dir %{_fontdir}
%{_fontdir}/NotoSansPhoenician-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phoenician.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phoenician.conf
%{_datadir}/appdata/%{fontname}-sans-phoenician.metainfo.xml


%package -n fonts-ttf-google-noto-sans-rejang
Summary:	Sans Rejang font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-rejang = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-rejang-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-rejang
%common_desc
Noto font Sans Rejang.

%files -n fonts-ttf-google-noto-sans-rejang
%dir %{_fontdir}
%{_fontdir}/NotoSansRejang-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-rejang.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-rejang.conf
%{_datadir}/appdata/%{fontname}-sans-rejang.metainfo.xml


%package -n fonts-ttf-google-noto-sans-runic
Summary:	Sans Runic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-runic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-runic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-runic
%common_desc
Noto font Sans Runic.

%files -n fonts-ttf-google-noto-sans-runic
%dir %{_fontdir}
%{_fontdir}/NotoSansRunic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-runic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-runic.conf
%{_datadir}/appdata/%{fontname}-sans-runic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-shavian
Summary:	Sans Shavian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-shavian = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-shavian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-shavian
%common_desc
Noto font Sans Shavian.

%files -n fonts-ttf-google-noto-sans-shavian
%dir %{_fontdir}
%{_fontdir}/NotoSansShavian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-shavian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-shavian.conf
%{_datadir}/appdata/%{fontname}-sans-shavian.metainfo.xml


%package -n fonts-ttf-google-noto-sans-samaritan
Summary:	Sans Samaritan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-samaritan = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-samaritan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-samaritan
%common_desc
Noto font Sans Samaritan.

%files -n fonts-ttf-google-noto-sans-samaritan
%dir %{_fontdir}
%{_fontdir}/NotoSansSamaritan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-samaritan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-samaritan.conf
%{_datadir}/appdata/%{fontname}-sans-samaritan.metainfo.xml


%package -n fonts-ttf-google-noto-sans-saurashtra
Summary:	Sans Saurashtra font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-saurashtra = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-saurashtra-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-saurashtra
%common_desc
Noto font Sans Saurashtra.

%files -n fonts-ttf-google-noto-sans-saurashtra
%dir %{_fontdir}
%{_fontdir}/NotoSansSaurashtra-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-saurashtra.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-saurashtra.conf
%{_datadir}/appdata/%{fontname}-sans-saurashtra.metainfo.xml


%package -n fonts-ttf-google-noto-sans-sinhala
Summary:	Sans Sinhala font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sinhala = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-sinhala-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sinhala
%common_desc
Noto font Sans Sinhala.

%files -n fonts-ttf-google-noto-sans-sinhala
%dir %{_fontdir}
%{_fontdir}/NotoSansSinhala-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sinhala.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sinhala.conf
%{_datadir}/appdata/%{fontname}-sans-sinhala.metainfo.xml


%package -n fonts-ttf-google-noto-sans-sundanese
Summary:	Sans Sundanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sundanese = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-sundanese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sundanese
%common_desc
Noto font Sans Sundanese.

%files -n fonts-ttf-google-noto-sans-sundanese
%dir %{_fontdir}
%{_fontdir}/NotoSansSundanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sundanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sundanese.conf
%{_datadir}/appdata/%{fontname}-sans-sundanese.metainfo.xml


%package -n fonts-ttf-google-noto-sans-syloti-nagri
Summary:	Sans Syloti Nagri font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syloti-nagri = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-syloti-nagri-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syloti-nagri
%common_desc
Noto font Sans Syloti Nagri.

%files -n fonts-ttf-google-noto-sans-syloti-nagri
%dir %{_fontdir}
%{_fontdir}/NotoSansSylotiNagri-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syloti-nagri.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syloti-nagri.conf
%{_datadir}/appdata/%{fontname}-sans-syloti-nagri.metainfo.xml


%package -n fonts-ttf-google-noto-sans-symbols
Summary:	Sans Symbols font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-symbols = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-symbols-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-symbols
%common_desc
Noto font Sans Symbols.

%files -n fonts-ttf-google-noto-sans-symbols
%dir %{_fontdir}
%{_fontdir}/NotoSansSymbols-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-symbols.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-symbols.conf
%{_datadir}/appdata/%{fontname}-sans-symbols.metainfo.xml


%package -n fonts-ttf-google-noto-sans-syriac-eastern
Summary:	Sans Syriac Eastern font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-eastern = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-syriac-eastern-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-eastern
%common_desc
Noto font Sans Syriac Eastern.

%files -n fonts-ttf-google-noto-sans-syriac-eastern
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacEastern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-eastern.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-eastern.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-eastern.metainfo.xml


%package -n fonts-ttf-google-noto-sans-syriac-estrangela
Summary:	Sans Syriac Estrangela font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-estrangela = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-syriac-estrangela-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-estrangela
%common_desc
Noto font Sans Syriac Estrangela.

%files -n fonts-ttf-google-noto-sans-syriac-estrangela
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacEstrangela-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-estrangela.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-estrangela.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-estrangela.metainfo.xml


%package -n fonts-ttf-google-noto-sans-syriac-western
Summary:	Sans Syriac Western font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-western = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-syriac-western-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-western
%common_desc
Noto font Sans Syriac Western.

%files -n fonts-ttf-google-noto-sans-syriac-western
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacWestern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-western.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-western.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-western.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tagalog
Summary:	Sans Tagalog font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tagalog = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tagalog-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tagalog
%common_desc
Noto font Sans Tagalog.

%files -n fonts-ttf-google-noto-sans-tagalog
%dir %{_fontdir}
%{_fontdir}/NotoSansTagalog-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagalog.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagalog.conf
%{_datadir}/appdata/%{fontname}-sans-tagalog.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tagbanwa
Summary:	Sans Tagbanwa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tagbanwa = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tagbanwa-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tagbanwa
%common_desc
Noto font Sans Tagbanwa.

%files -n fonts-ttf-google-noto-sans-tagbanwa
%dir %{_fontdir}
%{_fontdir}/NotoSansTagbanwa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagbanwa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagbanwa.conf
%{_datadir}/appdata/%{fontname}-sans-tagbanwa.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tai-le
Summary:	Sans Tai Le font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-le = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tai-le-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-le
%common_desc
Noto font Sans Tai Le.

%files -n fonts-ttf-google-noto-sans-tai-le
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiLe-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-le.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-le.conf
%{_datadir}/appdata/%{fontname}-sans-tai-le.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tai-tham
Summary:	Sans Tai Tham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-tham = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tai-tham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-tham
%common_desc
Noto font Sans Tai Tham.

%files -n fonts-ttf-google-noto-sans-tai-tham
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiTham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-tham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-tham.conf
%{_datadir}/appdata/%{fontname}-sans-tai-tham.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tai-viet
Summary:	Sans Tai Viet font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-viet = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tai-viet-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-viet
%common_desc
Noto font Sans Tai Viet.

%files -n fonts-ttf-google-noto-sans-tai-viet
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiViet-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-viet.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-viet.conf
%{_datadir}/appdata/%{fontname}-sans-tai-viet.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tamil
Summary:	Sans Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tamil fonts-ttf-google-noto-sans-tamil-ui
Obsoletes:	%{fontname}-sans-tamil-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil
%common_desc
Noto font Sans Tamil.

%files -n fonts-ttf-google-noto-sans-tamil
%dir %{_fontdir}
%{_fontdir}/NotoSansTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil.conf
%{_datadir}/appdata/%{fontname}-sans-tamil.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tamil-ui
Summary:	Sans Tamil UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tamil-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tamil-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil-ui
%common_desc
Noto font Sans Tamil UI.

%files -n fonts-ttf-google-noto-sans-tamil-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansTamilUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil-ui.conf
%{_datadir}/appdata/%{fontname}-sans-tamil-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-telugu
Summary:	Sans Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-telugu fonts-ttf-google-noto-sans-telugu-ui
Obsoletes:	%{fontname}-sans-telugu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-telugu
%common_desc
Noto font Sans Telugu.

%files -n fonts-ttf-google-noto-sans-telugu
%dir %{_fontdir}
%{_fontdir}/NotoSansTelugu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-telugu.conf
%{_datadir}/appdata/%{fontname}-sans-telugu.metainfo.xml


%package -n fonts-ttf-google-noto-sans-telugu-ui
Summary:	Sans Telugu UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-telugu-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-telugu-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-telugu-ui
%common_desc
Noto font Sans Telugu UI.

%files -n fonts-ttf-google-noto-sans-telugu-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansTeluguUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-telugu-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-telugu-ui.conf
%{_datadir}/appdata/%{fontname}-sans-telugu-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-thaana
Summary:	Sans Thaana font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thaana = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-thaana-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thaana
%common_desc
Noto font Sans Thaana.

%files -n fonts-ttf-google-noto-sans-thaana
%dir %{_fontdir}
%{_fontdir}/NotoSansThaana-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thaana.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thaana.conf
%{_datadir}/appdata/%{fontname}-sans-thaana.metainfo.xml


%package -n fonts-ttf-google-noto-sans-thai
Summary:	Sans Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thai fonts-ttf-google-noto-sans-thai-ui
Obsoletes:	%{fontname}-sans-thai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai
%common_desc
Noto font Sans Thai.

%files -n fonts-ttf-google-noto-sans-thai
%dir %{_fontdir}
%{_fontdir}/NotoSansThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai.conf
%{_datadir}/appdata/%{fontname}-sans-thai.metainfo.xml


%package -n fonts-ttf-google-noto-sans-thai-ui
Summary:	Sans Thai UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thai-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-thai-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai-ui
%common_desc
Noto font Sans Thai UI.

%files -n fonts-ttf-google-noto-sans-thai-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansThaiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai-ui.conf
%{_datadir}/appdata/%{fontname}-sans-thai-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tifinagh
Summary:	Sans Tifinagh font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tifinagh = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tifinagh-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tifinagh
%common_desc
Noto font Sans Tifinagh.

%files -n fonts-ttf-google-noto-sans-tifinagh
%dir %{_fontdir}
%{_fontdir}/NotoSansTifinagh-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tifinagh.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tifinagh.conf
%{_datadir}/appdata/%{fontname}-sans-tifinagh.metainfo.xml


%package -n fonts-ttf-google-noto-sans-ugaritic
Summary:	Sans Ugaritic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ugaritic = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-ugaritic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ugaritic
%common_desc
Noto font Sans Ugaritic.

%files -n fonts-ttf-google-noto-sans-ugaritic
%dir %{_fontdir}
%{_fontdir}/NotoSansUgaritic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ugaritic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ugaritic.conf
%{_datadir}/appdata/%{fontname}-sans-ugaritic.metainfo.xml


%package -n fonts-ttf-google-noto-sans-vai
Summary:	Sans Vai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-vai = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-vai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-vai
%common_desc
Noto font Sans Vai.

%files -n fonts-ttf-google-noto-sans-vai
%dir %{_fontdir}
%{_fontdir}/NotoSansVai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-vai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-vai.conf
%{_datadir}/appdata/%{fontname}-sans-vai.metainfo.xml


%package -n fonts-ttf-google-noto-sans-yi
Summary:	Sans Yi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-yi = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-yi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-yi
%common_desc
Noto font Sans Yi.

%files -n fonts-ttf-google-noto-sans-yi
%dir %{_fontdir}
%{_fontdir}/NotoSansYi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-yi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-yi.conf
%{_datadir}/appdata/%{fontname}-sans-yi.metainfo.xml


%package -n fonts-ttf-google-noto-serif
Summary:	Serif font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif fonts-ttf-google-noto-serif-armenian fonts-ttf-google-noto-serif-bengali fonts-ttf-google-noto-serif-devanagari fonts-ttf-google-noto-serif-georgian fonts-ttf-google-noto-serif-gujarati fonts-ttf-google-noto-serif-kannada fonts-ttf-google-noto-serif-khmer fonts-ttf-google-noto-serif-lao fonts-ttf-google-noto-serif-malayalam fonts-ttf-google-noto-serif-tamil fonts-ttf-google-noto-serif-telugu fonts-ttf-google-noto-serif-thai
Obsoletes:	%{fontname}-serif-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif
%common_desc
Noto font Serif.

%files -n fonts-ttf-google-noto-serif
%dir %{_fontdir}
%{_fontdir}/NotoSerif-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif.conf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n fonts-ttf-google-noto-serif-armenian
Summary:	Serif Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-armenian = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-armenian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-armenian
%common_desc
Noto font Serif Armenian.

%files -n fonts-ttf-google-noto-serif-armenian
%dir %{_fontdir}
%{_fontdir}/NotoSerifArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-armenian.conf
%{_datadir}/appdata/%{fontname}-serif-armenian.metainfo.xml


%package -n fonts-ttf-google-noto-serif-georgian
Summary:	Serif Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-georgian = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-georgian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-georgian
%common_desc
Noto font Serif Georgian.

%files -n fonts-ttf-google-noto-serif-georgian
%dir %{_fontdir}
%{_fontdir}/NotoSerifGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-georgian.conf
%{_datadir}/appdata/%{fontname}-serif-georgian.metainfo.xml


%package -n fonts-ttf-google-noto-serif-khmer
Summary:	Serif Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-khmer = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-khmer-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-khmer
%common_desc
Noto font Serif Khmer.

%files -n fonts-ttf-google-noto-serif-khmer
%dir %{_fontdir}
%{_fontdir}/NotoSerifKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-khmer.conf
%{_datadir}/appdata/%{fontname}-serif-khmer.metainfo.xml


%package -n fonts-ttf-google-noto-serif-lao
Summary:	Serif Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-lao = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-lao-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-lao
%common_desc
Noto font Serif Lao.

%files -n fonts-ttf-google-noto-serif-lao
%dir %{_fontdir}
%{_fontdir}/NotoSerifLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-lao.conf
%{_datadir}/appdata/%{fontname}-serif-lao.metainfo.xml


%package -n fonts-ttf-google-noto-serif-thai
Summary:	Serif Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-thai = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-thai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-thai
%common_desc
Noto font Serif Thai.

%files -n fonts-ttf-google-noto-serif-thai
%dir %{_fontdir}
%{_fontdir}/NotoSerifThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-thai.conf
%{_datadir}/appdata/%{fontname}-serif-thai.metainfo.xml


%package -n fonts-ttf-google-noto-sans-oriya
Summary:	Sans Oriya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-oriya fonts-ttf-google-noto-sans-oriya-ui
Obsoletes:	%{fontname}-sans-oriya-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-oriya
%common_desc
Noto font Sans Oriya.

%files -n fonts-ttf-google-noto-sans-oriya
%dir %{_fontdir}
%{_fontdir}/NotoSansOriya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-oriya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-oriya.conf
%{_datadir}/appdata/%{fontname}-sans-oriya.metainfo.xml


%package -n fonts-ttf-google-noto-sans-oriya-ui
Summary:	Sans Oriya UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-oriya-ui = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-oriya-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-oriya-ui
%common_desc
Noto font Sans Oriya UI.

%files -n fonts-ttf-google-noto-sans-oriya-ui
%dir %{_fontdir}
%{_fontdir}/NotoSansOriyaUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-oriya-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-oriya-ui.conf
%{_datadir}/appdata/%{fontname}-sans-oriya-ui.metainfo.xml


%package -n fonts-ttf-google-noto-sans-tibetan
Summary:	Sans Tibetan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tibetan = 20161022-alt1_4
Obsoletes:	%{fontname}-sans-tibetan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tibetan
%common_desc
Noto font Sans Tibetan.

%files -n fonts-ttf-google-noto-sans-tibetan
%dir %{_fontdir}
%{_fontdir}/NotoSansTibetan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tibetan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tibetan.conf
%{_datadir}/appdata/%{fontname}-sans-tibetan.metainfo.xml


%package -n fonts-ttf-google-noto-nastaliq-urdu
Summary:	Nastaliq Urdu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-nastaliq-urdu = 20161022-alt1_4
Obsoletes:	%{fontname}-nastaliq-urdu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-nastaliq-urdu
%common_desc
Noto font Nastaliq Urdu.

%files -n fonts-ttf-google-noto-nastaliq-urdu
%dir %{_fontdir}
%{_fontdir}/NotoNastaliqUrdu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-nastaliq-urdu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-nastaliq-urdu.conf
%{_datadir}/appdata/%{fontname}-nastaliq-urdu.metainfo.xml


%package -n fonts-ttf-google-noto-mono
Summary:	Mono font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-mono = 20161022-alt1_4
Obsoletes:	%{fontname}-mono-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-mono
%common_desc
Noto font Mono.

%files -n fonts-ttf-google-noto-mono
%dir %{_fontdir}
%{_fontdir}/NotoMono-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-mono.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-mono.conf
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml


%package -n fonts-ttf-google-noto-serif-bengali
Summary:	Serif Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-bengali = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-bengali-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-bengali
%common_desc
Noto font Serif Bengali.

%files -n fonts-ttf-google-noto-serif-bengali
%dir %{_fontdir}
%{_fontdir}/NotoSerifBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-bengali.conf
%{_datadir}/appdata/%{fontname}-serif-bengali.metainfo.xml


%package -n fonts-ttf-google-noto-serif-devanagari
Summary:	Serif Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-devanagari = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-devanagari-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-devanagari
%common_desc
Noto font Serif Devanagari.

%files -n fonts-ttf-google-noto-serif-devanagari
%dir %{_fontdir}
%{_fontdir}/NotoSerifDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-devanagari.conf
%{_datadir}/appdata/%{fontname}-serif-devanagari.metainfo.xml


%package -n fonts-ttf-google-noto-serif-gujarati
Summary:	Serif Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-gujarati = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-gujarati-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-gujarati
%common_desc
Noto font Serif Gujarati.

%files -n fonts-ttf-google-noto-serif-gujarati
%dir %{_fontdir}
%{_fontdir}/NotoSerifGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gujarati.conf
%{_datadir}/appdata/%{fontname}-serif-gujarati.metainfo.xml


%package -n fonts-ttf-google-noto-serif-kannada
Summary:	Serif Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-kannada = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-kannada-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-kannada
%common_desc
Noto font Serif Kannada.

%files -n fonts-ttf-google-noto-serif-kannada
%dir %{_fontdir}
%{_fontdir}/NotoSerifKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-kannada.conf
%{_datadir}/appdata/%{fontname}-serif-kannada.metainfo.xml


%package -n fonts-ttf-google-noto-serif-malayalam
Summary:	Serif Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-malayalam = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-malayalam-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-malayalam
%common_desc
Noto font Serif Malayalam.

%files -n fonts-ttf-google-noto-serif-malayalam
%dir %{_fontdir}
%{_fontdir}/NotoSerifMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-malayalam.conf
%{_datadir}/appdata/%{fontname}-serif-malayalam.metainfo.xml


%package -n fonts-ttf-google-noto-serif-tamil
Summary:	Serif Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-tamil = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-tamil-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tamil
%common_desc
Noto font Serif Tamil.

%files -n fonts-ttf-google-noto-serif-tamil
%dir %{_fontdir}
%{_fontdir}/NotoSerifTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil.conf
%{_datadir}/appdata/%{fontname}-serif-tamil.metainfo.xml


%package -n fonts-ttf-google-noto-serif-telugu
Summary:	Serif Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-telugu = 20161022-alt1_4
Obsoletes:	%{fontname}-serif-telugu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-telugu
%common_desc
Noto font Serif Telugu.

%files -n fonts-ttf-google-noto-serif-telugu
%dir %{_fontdir}
%{_fontdir}/NotoSerifTelugu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-telugu.conf
%{_datadir}/appdata/%{fontname}-serif-telugu.metainfo.xml

%prep
%setup -q -n noto-fonts-86b2e553c3e3e4d6614dadd1fa0a7a6dafd74552


%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p unhinted/Noto*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p hinted/Noto*.ttf %{buildroot}%{_fontdir}



install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add appstream metadata
install -Dm 0644 -p %{SOURCE200} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

for f in \
        kufi-arabic naskh-arabic naskh-arabic-ui \
        sans sans-armenian sans-avestan sans-balinese sans-bamum \
        sans-batak sans-bengali sans-bengali-ui sans-brahmi \
        sans-buginese sans-buhid sans-canadian-aboriginal sans-carian \
        sans-cham sans-cherokee sans-coptic sans-cuneiform \
        sans-cypriot sans-deseret sans-devanagari sans-devanagari-ui \
        sans-egyptian-hieroglyphs sans-ethiopic sans-georgian \
        sans-glagolitic sans-gothic sans-gujarati sans-gujarati-ui \
        sans-gurmukhi sans-gurmukhi-ui sans-hanunoo sans-hebrew \
        sans-imperial-aramaic sans-inscriptional-pahlavi \
        sans-inscriptional-parthian sans-javanese \
        sans-kaithi sans-kannada sans-kannada-ui sans-kayah-li \
        sans-kharoshthi sans-khmer sans-khmer-ui sans-lao \
        sans-lao-ui sans-lepcha sans-limbu sans-linear-b sans-lisu \
        sans-lycian sans-lydian sans-malayalam sans-malayalam-ui \
        sans-mandaic sans-meetei-mayek sans-mongolian sans-myanmar \
        sans-myanmar-ui sans-new-tai-lue sans-nko sans-ogham \
        sans-ol-chiki sans-old-italic sans-old-persian \
        sans-old-south-arabian sans-old-turkic sans-osmanya \
        sans-phags-pa sans-phoenician sans-rejang sans-runic \
        sans-samaritan sans-saurashtra sans-shavian sans-sinhala \
        sans-sundanese sans-syloti-nagri sans-symbols sans-syriac-eastern \
        sans-syriac-estrangela sans-syriac-western sans-tagalog \
        sans-tagbanwa sans-tai-le sans-tai-tham sans-tai-viet \
        sans-tamil sans-tamil-ui sans-telugu sans-telugu-ui \
        sans-thaana sans-thai sans-thai-ui sans-tifinagh \
        sans-ugaritic sans-ui sans-vai sans-yi \
        serif serif-armenian serif-georgian serif-khmer serif-lao serif-thai \
        sans-oriya sans-oriya-ui sans-tibetan nastaliq-urdu mono \
        serif-bengali serif-devanagari serif-gujarati serif-kannada \
        serif-malayalam serif-tamil serif-telugu \
        ; do
  fconf=$(basename -a %{_sourcedir}/*-%{fontconf}-$f.conf)
  if [ "$(echo $fconf | wc -w)" -ne 1 ]; then
     echo "Did not find unique \*-%{fontconf}-$f.conf file"
     exit 1
  fi
  install -m 0644 -p %{_sourcedir}/${fconf} \
        %{buildroot}%{_fontconfig_templatedir}/${fconf}
  ln -s %{_fontconfig_templatedir}/${fconf} \
        %{buildroot}%{_fontconfig_confdir}/${fconf}

  meta=%{fontname}-$f.metainfo.xml
  echo '<?xml version="1.0" encoding="UTF-8"?>' > $meta
  echo '<!-- Copyright 2014 Parag Nemade <pnemade AT redhat DOT com> -->' >> $meta
  echo '<component type="font">' >> $meta
  echo "  <id>google-noto-$f</id>" >> $meta
  echo '  <metadata_license>CC-BY-3.0</metadata_license>' >> $meta
  echo '  <extends>google-noto</extends>' >> $meta
  echo '</component>' >> $meta

  install -Dm 0644 -p %{fontname}-$f.metainfo.xml \
          %{buildroot}%{_datadir}/appdata/%{fontname}-$f.metainfo.xml
done


%files -n fonts-ttf-google-noto-common
%doc --no-dereference LICENSE
%doc README.md FAQ.md
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 20161022-alt2_5
- update to new release by fcimport

* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 20161022-alt2_4
- fixed font package names

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 20161022-alt1_4
- fixed fontconfig tag (closes: #34207)

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20141001-alt1_1
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 20130807-alt1_2
- converted for ALT Linux by srpmconvert tools

