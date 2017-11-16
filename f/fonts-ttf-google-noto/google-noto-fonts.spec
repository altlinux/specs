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
Release:        alt1_4
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
Source109: import.info

%description
%common_desc


%package -n fonts-ttf-google-noto-common
Group: System/Fonts/True type
Summary:        Common files for Noto fonts

%description -n fonts-ttf-google-noto-common
Common files for Google Noto fonts.

%package -n %{fontname}-kufi-arabic-fonts
Summary:	Kufi Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-kufi-arabic-fonts
%common_desc
Noto font Kufi Arabic.

%files -n %{fontname}-kufi-arabic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoKufiArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-kufi-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-kufi-arabic.conf
%{_datadir}/appdata/%{fontname}-kufi-arabic.metainfo.xml


%package -n %{fontname}-naskh-arabic-fonts
Summary:	Naskh Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-naskh-arabic-fonts
%common_desc
Noto font Naskh Arabic.

%files -n %{fontname}-naskh-arabic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoNaskhArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-naskh-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-naskh-arabic.conf
%{_datadir}/appdata/%{fontname}-naskh-arabic.metainfo.xml


%package -n %{fontname}-naskh-arabic-ui-fonts
Summary:	Naskh Arabic UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-naskh-arabic-ui-fonts
%common_desc
Noto font Naskh Arabic UI.

%files -n %{fontname}-naskh-arabic-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoNaskhArabicUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-naskh-arabic-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-naskh-arabic-ui.conf
%{_datadir}/appdata/%{fontname}-naskh-arabic-ui.metainfo.xml


%package -n %{fontname}-sans-fonts
Summary:	Sans font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-fonts
%common_desc
Noto font Sans.

%files -n %{fontname}-sans-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSans-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans.conf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n %{fontname}-sans-ui-fonts
Summary:	Sans UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-ui-fonts
%common_desc
Noto font Sans UI.

%files -n %{fontname}-sans-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ui.conf
%{_datadir}/appdata/%{fontname}-sans-ui.metainfo.xml


%package -n %{fontname}-sans-armenian-fonts
Summary:	Sans Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-armenian-fonts
%common_desc
Noto font Sans Armenian.

%files -n %{fontname}-sans-armenian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-armenian.conf
%{_datadir}/appdata/%{fontname}-sans-armenian.metainfo.xml


%package -n %{fontname}-sans-avestan-fonts
Summary:	Sans Avestan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-avestan-fonts
%common_desc
Noto font Sans Avestan.

%files -n %{fontname}-sans-avestan-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansAvestan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-avestan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-avestan.conf
%{_datadir}/appdata/%{fontname}-sans-avestan.metainfo.xml


%package -n %{fontname}-sans-balinese-fonts
Summary:	Sans Balinese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-balinese-fonts
%common_desc
Noto font Sans Balinese.

%files -n %{fontname}-sans-balinese-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBalinese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-balinese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-balinese.conf
%{_datadir}/appdata/%{fontname}-sans-balinese.metainfo.xml


%package -n %{fontname}-sans-bamum-fonts
Summary:	Sans Bamum font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-bamum-fonts
%common_desc
Noto font Sans Bamum.

%files -n %{fontname}-sans-bamum-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBamum-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bamum.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bamum.conf
%{_datadir}/appdata/%{fontname}-sans-bamum.metainfo.xml


%package -n %{fontname}-sans-batak-fonts
Summary:	Sans Batak font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-batak-fonts
%common_desc
Noto font Sans Batak.

%files -n %{fontname}-sans-batak-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBatak-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-batak.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-batak.conf
%{_datadir}/appdata/%{fontname}-sans-batak.metainfo.xml


%package -n %{fontname}-sans-bengali-fonts
Summary:	Sans Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-bengali-fonts
%common_desc
Noto font Sans Bengali.

%files -n %{fontname}-sans-bengali-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali.conf
%{_datadir}/appdata/%{fontname}-sans-bengali.metainfo.xml


%package -n %{fontname}-sans-bengali-ui-fonts
Summary:	Sans Bengali UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-bengali-ui-fonts
%common_desc
Noto font Sans Bengali UI.

%files -n %{fontname}-sans-bengali-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBengaliUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali-ui.conf
%{_datadir}/appdata/%{fontname}-sans-bengali-ui.metainfo.xml


%package -n %{fontname}-sans-brahmi-fonts
Summary:	Sans Brahmi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-brahmi-fonts
%common_desc
Noto font Sans Brahmi.

%files -n %{fontname}-sans-brahmi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBrahmi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-brahmi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-brahmi.conf
%{_datadir}/appdata/%{fontname}-sans-brahmi.metainfo.xml


%package -n %{fontname}-sans-buginese-fonts
Summary:	Sans Buginese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-buginese-fonts
%common_desc
Noto font Sans Buginese.

%files -n %{fontname}-sans-buginese-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBuginese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buginese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buginese.conf
%{_datadir}/appdata/%{fontname}-sans-buginese.metainfo.xml


%package -n %{fontname}-sans-buhid-fonts
Summary:	Sans Buhid font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-buhid-fonts
%common_desc
Noto font Sans Buhid.

%files -n %{fontname}-sans-buhid-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansBuhid-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buhid.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buhid.conf
%{_datadir}/appdata/%{fontname}-sans-buhid.metainfo.xml


%package -n %{fontname}-sans-canadian-aboriginal-fonts
Summary:	Sans Canadian Aboriginal font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-canadian-aboriginal-fonts
%common_desc
Noto font Sans Canadian Aboriginal.

%files -n %{fontname}-sans-canadian-aboriginal-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCanadianAboriginal-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%{_datadir}/appdata/%{fontname}-sans-canadian-aboriginal.metainfo.xml


%package -n %{fontname}-sans-carian-fonts
Summary:	Sans Carian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-carian-fonts
%common_desc
Noto font Sans Carian.

%files -n %{fontname}-sans-carian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCarian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-carian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-carian.conf
%{_datadir}/appdata/%{fontname}-sans-carian.metainfo.xml


%package -n %{fontname}-sans-cham-fonts
Summary:	Sans Cham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-cham-fonts
%common_desc
Noto font Sans Cham.

%files -n %{fontname}-sans-cham-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cham.conf
%{_datadir}/appdata/%{fontname}-sans-cham.metainfo.xml


%package -n %{fontname}-sans-cherokee-fonts
Summary:	Sans Cherokee font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-cherokee-fonts
%common_desc
Noto font Sans Cherokee.

%files -n %{fontname}-sans-cherokee-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCherokee-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cherokee.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cherokee.conf
%{_datadir}/appdata/%{fontname}-sans-cherokee.metainfo.xml


%package -n %{fontname}-sans-coptic-fonts
Summary:	Sans Coptic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-coptic-fonts
%common_desc
Noto font Sans Coptic.

%files -n %{fontname}-sans-coptic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCoptic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-coptic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-coptic.conf
%{_datadir}/appdata/%{fontname}-sans-coptic.metainfo.xml


%package -n %{fontname}-sans-cuneiform-fonts
Summary:	Sans Cuneiform font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-cuneiform-fonts
%common_desc
Noto font Sans Cuneiform.

%files -n %{fontname}-sans-cuneiform-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCuneiform-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cuneiform.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cuneiform.conf
%{_datadir}/appdata/%{fontname}-sans-cuneiform.metainfo.xml


%package -n %{fontname}-sans-cypriot-fonts
Summary:	Sans Cypriot font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-cypriot-fonts
%common_desc
Noto font Sans Cypriot.

%files -n %{fontname}-sans-cypriot-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansCypriot-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cypriot.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cypriot.conf
%{_datadir}/appdata/%{fontname}-sans-cypriot.metainfo.xml


%package -n %{fontname}-sans-deseret-fonts
Summary:	Sans Deseret font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-deseret-fonts
%common_desc
Noto font Sans Deseret.

%files -n %{fontname}-sans-deseret-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansDeseret-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-deseret.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-deseret.conf
%{_datadir}/appdata/%{fontname}-sans-deseret.metainfo.xml


%package -n %{fontname}-sans-devanagari-fonts
Summary:	Sans Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-devanagari-fonts
%common_desc
Noto font Sans Devanagari.

%files -n %{fontname}-sans-devanagari-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari.conf
%{_datadir}/appdata/%{fontname}-sans-devanagari.metainfo.xml


%package -n %{fontname}-sans-devanagari-ui-fonts
Summary:	Sans Devanagari UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-devanagari-ui-fonts
%common_desc
Noto font Sans Devanagari UI.

%files -n %{fontname}-sans-devanagari-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansDevanagariUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari-ui.conf
%{_datadir}/appdata/%{fontname}-sans-devanagari-ui.metainfo.xml


%package -n %{fontname}-sans-egyptian-hieroglyphs-fonts
Summary:	Sans Egyptian Hieroglyphs font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-egyptian-hieroglyphs-fonts
%common_desc
Noto font Sans Egyptian Hieroglyphs.

%files -n %{fontname}-sans-egyptian-hieroglyphs-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansEgyptianHieroglyphs-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%{_datadir}/appdata/%{fontname}-sans-egyptian-hieroglyphs.metainfo.xml


%package -n %{fontname}-sans-ethiopic-fonts
Summary:	Sans Ethiopic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-ethiopic-fonts
%common_desc
Noto font Sans Ethiopic.

%files -n %{fontname}-sans-ethiopic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansEthiopic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ethiopic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ethiopic.conf
%{_datadir}/appdata/%{fontname}-sans-ethiopic.metainfo.xml


%package -n %{fontname}-sans-georgian-fonts
Summary:	Sans Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-georgian-fonts
%common_desc
Noto font Sans Georgian.

%files -n %{fontname}-sans-georgian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-georgian.conf
%{_datadir}/appdata/%{fontname}-sans-georgian.metainfo.xml


%package -n %{fontname}-sans-glagolitic-fonts
Summary:	Sans Glagolitic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-glagolitic-fonts
%common_desc
Noto font Sans Glagolitic.

%files -n %{fontname}-sans-glagolitic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGlagolitic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-glagolitic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-glagolitic.conf
%{_datadir}/appdata/%{fontname}-sans-glagolitic.metainfo.xml


%package -n %{fontname}-sans-gothic-fonts
Summary:	Sans Gothic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-gothic-fonts
%common_desc
Noto font Sans Gothic.

%files -n %{fontname}-sans-gothic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGothic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gothic.conf
%{_datadir}/appdata/%{fontname}-sans-gothic.metainfo.xml


%package -n %{fontname}-sans-gujarati-fonts
Summary:	Sans Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-gujarati-fonts
%common_desc
Noto font Sans Gujarati.

%files -n %{fontname}-sans-gujarati-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gujarati.conf
%{_datadir}/appdata/%{fontname}-sans-gujarati.metainfo.xml


%package -n %{fontname}-sans-gujarati-ui-fonts
Summary:	Sans Gujarati UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-gujarati-ui-fonts
%common_desc
Noto font Sans Gujarati UI.

%files -n %{fontname}-sans-gujarati-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGujaratiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gujarati-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gujarati-ui.conf
%{_datadir}/appdata/%{fontname}-sans-gujarati-ui.metainfo.xml


%package -n %{fontname}-sans-gurmukhi-fonts
Summary:	Sans Gurmukhi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-gurmukhi-fonts
%common_desc
Noto font Sans Gurmukhi.

%files -n %{fontname}-sans-gurmukhi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGurmukhi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gurmukhi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gurmukhi.conf
%{_datadir}/appdata/%{fontname}-sans-gurmukhi.metainfo.xml


%package -n %{fontname}-sans-gurmukhi-ui-fonts
Summary:	Sans Gurmukhi UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-gurmukhi-ui-fonts
%common_desc
Noto font Sans Gurmukhi UI.

%files -n %{fontname}-sans-gurmukhi-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansGurmukhiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gurmukhi-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gurmukhi-ui.conf
%{_datadir}/appdata/%{fontname}-sans-gurmukhi-ui.metainfo.xml


%package -n %{fontname}-sans-hanunoo-fonts
Summary:	Sans Hanunoo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Obsoletes:	fonts-ttf-%{fontname}-sans-hanunno < %EVR

%description -n %{fontname}-sans-hanunoo-fonts
%common_desc
Noto font Sans Hanunoo.

%files -n %{fontname}-sans-hanunoo-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansHanunoo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hanunoo.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hanunoo.conf
%{_datadir}/appdata/%{fontname}-sans-hanunoo.metainfo.xml


%package -n %{fontname}-sans-hebrew-fonts
Summary:	Sans Hebrew font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-hebrew-fonts
%common_desc
Noto font Sans Hebrew.

%files -n %{fontname}-sans-hebrew-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansHebrew-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hebrew.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hebrew.conf
%{_datadir}/appdata/%{fontname}-sans-hebrew.metainfo.xml


%package -n %{fontname}-sans-imperial-aramaic-fonts
Summary:	Sans Imperial Aramaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-imperial-aramaic-fonts
%common_desc
Noto font Sans Imperial Aramaic.

%files -n %{fontname}-sans-imperial-aramaic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansImperialAramaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-imperial-aramaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-imperial-aramaic.conf
%{_datadir}/appdata/%{fontname}-sans-imperial-aramaic.metainfo.xml


%package -n %{fontname}-sans-inscriptional-pahlavi-fonts
Summary:	Sans Inscriptional Pahlavi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-inscriptional-pahlavi-fonts
%common_desc
Noto font Sans Inscriptional Pahlavi.

%files -n %{fontname}-sans-inscriptional-pahlavi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansInscriptionalPahlavi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%{_datadir}/appdata/%{fontname}-sans-inscriptional-pahlavi.metainfo.xml


%package -n %{fontname}-sans-inscriptional-parthian-fonts
Summary:	Sans Inscriptional Parthian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-inscriptional-parthian-fonts
%common_desc
Noto font Sans Inscriptional Parthian.

%files -n %{fontname}-sans-inscriptional-parthian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansInscriptionalParthian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%{_datadir}/appdata/%{fontname}-sans-inscriptional-parthian.metainfo.xml


%package -n %{fontname}-sans-javanese-fonts
Summary:	Sans Javanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-javanese-fonts
%common_desc
Noto font Sans Javanese.

%files -n %{fontname}-sans-javanese-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansJavanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-javanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-javanese.conf
%{_datadir}/appdata/%{fontname}-sans-javanese.metainfo.xml


%package -n %{fontname}-sans-kaithi-fonts
Summary:	Sans Kaithi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-kaithi-fonts
%common_desc
Noto font Sans Kaithi.

%files -n %{fontname}-sans-kaithi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKaithi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kaithi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kaithi.conf
%{_datadir}/appdata/%{fontname}-sans-kaithi.metainfo.xml


%package -n %{fontname}-sans-kannada-fonts
Summary:	Sans Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-kannada-fonts
%common_desc
Noto font Sans Kannada.

%files -n %{fontname}-sans-kannada-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada.conf
%{_datadir}/appdata/%{fontname}-sans-kannada.metainfo.xml


%package -n %{fontname}-sans-kannada-ui-fonts
Summary:	Sans Kannada UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-kannada-ui-fonts
%common_desc
Noto font Sans Kannada UI.

%files -n %{fontname}-sans-kannada-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKannadaUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada-ui.conf
%{_datadir}/appdata/%{fontname}-sans-kannada-ui.metainfo.xml


%package -n %{fontname}-sans-kayah-li-fonts
Summary:	Sans Kayah Li font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-kayah-li-fonts
%common_desc
Noto font Sans Kayah Li.

%files -n %{fontname}-sans-kayah-li-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKayahLi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kayah-li.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kayah-li.conf
%{_datadir}/appdata/%{fontname}-sans-kayah-li.metainfo.xml


%package -n %{fontname}-sans-kharoshthi-fonts
Summary:	Sans Kharoshthi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-kharoshthi-fonts
%common_desc
Noto font Sans Kharoshthi.

%files -n %{fontname}-sans-kharoshthi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKharoshthi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kharoshthi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kharoshthi.conf
%{_datadir}/appdata/%{fontname}-sans-kharoshthi.metainfo.xml


%package -n %{fontname}-sans-khmer-fonts
Summary:	Sans Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-khmer-fonts
%common_desc
Noto font Sans Khmer.

%files -n %{fontname}-sans-khmer-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer.conf
%{_datadir}/appdata/%{fontname}-sans-khmer.metainfo.xml


%package -n %{fontname}-sans-khmer-ui-fonts
Summary:	Sans Khmer UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-khmer-ui-fonts
%common_desc
Noto font Sans Khmer UI.

%files -n %{fontname}-sans-khmer-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansKhmerUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer-ui.conf
%{_datadir}/appdata/%{fontname}-sans-khmer-ui.metainfo.xml


%package -n %{fontname}-sans-lao-fonts
Summary:	Sans Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lao-fonts
%common_desc
Noto font Sans Lao.

%files -n %{fontname}-sans-lao-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao.conf
%{_datadir}/appdata/%{fontname}-sans-lao.metainfo.xml


%package -n %{fontname}-sans-lao-ui-fonts
Summary:	Sans Lao UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lao-ui-fonts
%common_desc
Noto font Sans Lao UI.

%files -n %{fontname}-sans-lao-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLaoUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao-ui.conf
%{_datadir}/appdata/%{fontname}-sans-lao-ui.metainfo.xml


%package -n %{fontname}-sans-lepcha-fonts
Summary:	Sans Lepcha font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lepcha-fonts
%common_desc
Noto font Sans Lepcha.

%files -n %{fontname}-sans-lepcha-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLepcha-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lepcha.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lepcha.conf
%{_datadir}/appdata/%{fontname}-sans-lepcha.metainfo.xml


%package -n %{fontname}-sans-limbu-fonts
Summary:	Sans Limbu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-limbu-fonts
%common_desc
Noto font Sans Limbu.

%files -n %{fontname}-sans-limbu-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLimbu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-limbu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-limbu.conf
%{_datadir}/appdata/%{fontname}-sans-limbu.metainfo.xml


%package -n %{fontname}-sans-linear-b-fonts
Summary:	Sans Linear B font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Obsoletes:	fonts-ttf-%{fontname}-sans-linearb < %EVR

%description -n %{fontname}-sans-linear-b-fonts
%common_desc
Noto font Sans Linear B.

%files -n %{fontname}-sans-linear-b-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLinearB-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-linear-b.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-linear-b.conf
%{_datadir}/appdata/%{fontname}-sans-linear-b.metainfo.xml


%package -n %{fontname}-sans-lisu-fonts
Summary:	Sans Lisu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lisu-fonts
%common_desc
Noto font Sans Lisu.

%files -n %{fontname}-sans-lisu-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLisu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lisu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lisu.conf
%{_datadir}/appdata/%{fontname}-sans-lisu.metainfo.xml


%package -n %{fontname}-sans-lycian-fonts
Summary:	Sans Lycian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lycian-fonts
%common_desc
Noto font Sans Lycian.

%files -n %{fontname}-sans-lycian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLycian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lycian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lycian.conf
%{_datadir}/appdata/%{fontname}-sans-lycian.metainfo.xml


%package -n %{fontname}-sans-lydian-fonts
Summary:	Sans Lydian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-lydian-fonts
%common_desc
Noto font Sans Lydian.

%files -n %{fontname}-sans-lydian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansLydian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lydian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lydian.conf
%{_datadir}/appdata/%{fontname}-sans-lydian.metainfo.xml


%package -n %{fontname}-sans-malayalam-fonts
Summary:	Sans Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-malayalam-fonts
%common_desc
Noto font Sans Malayalam.

%files -n %{fontname}-sans-malayalam-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam.conf
%{_datadir}/appdata/%{fontname}-sans-malayalam.metainfo.xml


%package -n %{fontname}-sans-malayalam-ui-fonts
Summary:	Sans Malayalam UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-malayalam-ui-fonts
%common_desc
Noto font Sans Malayalam UI.

%files -n %{fontname}-sans-malayalam-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMalayalamUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam-ui.conf
%{_datadir}/appdata/%{fontname}-sans-malayalam-ui.metainfo.xml


%package -n %{fontname}-sans-mandaic-fonts
Summary:	Sans Mandaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-mandaic-fonts
%common_desc
Noto font Sans Mandaic.

%files -n %{fontname}-sans-mandaic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMandaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mandaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mandaic.conf
%{_datadir}/appdata/%{fontname}-sans-mandaic.metainfo.xml


%package -n %{fontname}-sans-meetei-mayek-fonts
Summary:	Sans Meetei Mayek font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR
Obsoletes:	fonts-ttf-%{fontname}-sans-meeteimayek < %EVR

%description -n %{fontname}-sans-meetei-mayek-fonts
%common_desc
Noto font Sans Meetei Mayek.

%files -n %{fontname}-sans-meetei-mayek-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMeeteiMayek-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-meetei-mayek.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-meetei-mayek.conf
%{_datadir}/appdata/%{fontname}-sans-meetei-mayek.metainfo.xml


%package -n %{fontname}-sans-mongolian-fonts
Summary:	Sans Mongolian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-mongolian-fonts
%common_desc
Noto font Sans Mongolian.

%files -n %{fontname}-sans-mongolian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMongolian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mongolian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mongolian.conf
%{_datadir}/appdata/%{fontname}-sans-mongolian.metainfo.xml


%package -n %{fontname}-sans-myanmar-fonts
Summary:	Sans Myanmar font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-myanmar-fonts
%common_desc
Noto font Sans Myanmar.

%files -n %{fontname}-sans-myanmar-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMyanmar-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar.conf
%{_datadir}/appdata/%{fontname}-sans-myanmar.metainfo.xml


%package -n %{fontname}-sans-myanmar-ui-fonts
Summary:	Sans Myanmar UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-myanmar-ui-fonts
%common_desc
Noto font Sans Myanmar UI.

%files -n %{fontname}-sans-myanmar-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansMyanmarUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar-ui.conf
%{_datadir}/appdata/%{fontname}-sans-myanmar-ui.metainfo.xml


%package -n %{fontname}-sans-new-tai-lue-fonts
Summary:	Sans New Tai Lue font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-new-tai-lue-fonts
%common_desc
Noto font Sans New Tai Lue.

%files -n %{fontname}-sans-new-tai-lue-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansNewTaiLue-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-new-tai-lue.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-new-tai-lue.conf
%{_datadir}/appdata/%{fontname}-sans-new-tai-lue.metainfo.xml


%package -n %{fontname}-sans-nko-fonts
Summary:	Sans NKo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-nko-fonts
%common_desc
Noto font Sans NKo.

%files -n %{fontname}-sans-nko-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansNKo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-nko.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-nko.conf
%{_datadir}/appdata/%{fontname}-sans-nko.metainfo.xml


%package -n %{fontname}-sans-ogham-fonts
Summary:	Sans Ogham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-ogham-fonts
%common_desc
Noto font Sans Ogham.

%files -n %{fontname}-sans-ogham-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOgham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ogham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ogham.conf
%{_datadir}/appdata/%{fontname}-sans-ogham.metainfo.xml


%package -n %{fontname}-sans-ol-chiki-fonts
Summary:	Sans Ol Chiki font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-ol-chiki-fonts
%common_desc
Noto font Sans Ol Chiki.

%files -n %{fontname}-sans-ol-chiki-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOlChiki-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ol-chiki.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ol-chiki.conf
%{_datadir}/appdata/%{fontname}-sans-ol-chiki.metainfo.xml


%package -n %{fontname}-sans-old-italic-fonts
Summary:	Sans Old Italic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-old-italic-fonts
%common_desc
Noto font Sans Old Italic.

%files -n %{fontname}-sans-old-italic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOldItalic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-italic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-italic.conf
%{_datadir}/appdata/%{fontname}-sans-old-italic.metainfo.xml


%package -n %{fontname}-sans-old-persian-fonts
Summary:	Sans Old Persian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-old-persian-fonts
%common_desc
Noto font Sans Old Persian.

%files -n %{fontname}-sans-old-persian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOldPersian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-persian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-persian.conf
%{_datadir}/appdata/%{fontname}-sans-old-persian.metainfo.xml


%package -n %{fontname}-sans-old-south-arabian-fonts
Summary:	Sans Old South Arabian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-old-south-arabian-fonts
%common_desc
Noto font Sans Old South Arabian.

%files -n %{fontname}-sans-old-south-arabian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOldSouthArabian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-south-arabian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-south-arabian.conf
%{_datadir}/appdata/%{fontname}-sans-old-south-arabian.metainfo.xml


%package -n %{fontname}-sans-old-turkic-fonts
Summary:	Sans Old Turkic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-old-turkic-fonts
%common_desc
Noto font Sans Old Turkic.

%files -n %{fontname}-sans-old-turkic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOldTurkic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-turkic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-turkic.conf
%{_datadir}/appdata/%{fontname}-sans-old-turkic.metainfo.xml


%package -n %{fontname}-sans-osmanya-fonts
Summary:	Sans Osmanya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-osmanya-fonts
%common_desc
Noto font Sans Osmanya.

%files -n %{fontname}-sans-osmanya-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOsmanya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-osmanya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-osmanya.conf
%{_datadir}/appdata/%{fontname}-sans-osmanya.metainfo.xml


%package -n %{fontname}-sans-phags-pa-fonts
Summary:	Sans Phags Pa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-phags-pa-fonts
%common_desc
Noto font Sans Phags Pa.

%files -n %{fontname}-sans-phags-pa-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansPhagsPa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phags-pa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phags-pa.conf
%{_datadir}/appdata/%{fontname}-sans-phags-pa.metainfo.xml


%package -n %{fontname}-sans-phoenician-fonts
Summary:	Sans Phoenician font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-phoenician-fonts
%common_desc
Noto font Sans Phoenician.

%files -n %{fontname}-sans-phoenician-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansPhoenician-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phoenician.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phoenician.conf
%{_datadir}/appdata/%{fontname}-sans-phoenician.metainfo.xml


%package -n %{fontname}-sans-rejang-fonts
Summary:	Sans Rejang font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-rejang-fonts
%common_desc
Noto font Sans Rejang.

%files -n %{fontname}-sans-rejang-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansRejang-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-rejang.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-rejang.conf
%{_datadir}/appdata/%{fontname}-sans-rejang.metainfo.xml


%package -n %{fontname}-sans-runic-fonts
Summary:	Sans Runic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-runic-fonts
%common_desc
Noto font Sans Runic.

%files -n %{fontname}-sans-runic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansRunic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-runic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-runic.conf
%{_datadir}/appdata/%{fontname}-sans-runic.metainfo.xml


%package -n %{fontname}-sans-shavian-fonts
Summary:	Sans Shavian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-shavian-fonts
%common_desc
Noto font Sans Shavian.

%files -n %{fontname}-sans-shavian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansShavian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-shavian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-shavian.conf
%{_datadir}/appdata/%{fontname}-sans-shavian.metainfo.xml


%package -n %{fontname}-sans-samaritan-fonts
Summary:	Sans Samaritan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-samaritan-fonts
%common_desc
Noto font Sans Samaritan.

%files -n %{fontname}-sans-samaritan-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSamaritan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-samaritan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-samaritan.conf
%{_datadir}/appdata/%{fontname}-sans-samaritan.metainfo.xml


%package -n %{fontname}-sans-saurashtra-fonts
Summary:	Sans Saurashtra font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-saurashtra-fonts
%common_desc
Noto font Sans Saurashtra.

%files -n %{fontname}-sans-saurashtra-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSaurashtra-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-saurashtra.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-saurashtra.conf
%{_datadir}/appdata/%{fontname}-sans-saurashtra.metainfo.xml


%package -n %{fontname}-sans-sinhala-fonts
Summary:	Sans Sinhala font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-sinhala-fonts
%common_desc
Noto font Sans Sinhala.

%files -n %{fontname}-sans-sinhala-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSinhala-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sinhala.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sinhala.conf
%{_datadir}/appdata/%{fontname}-sans-sinhala.metainfo.xml


%package -n %{fontname}-sans-sundanese-fonts
Summary:	Sans Sundanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-sundanese-fonts
%common_desc
Noto font Sans Sundanese.

%files -n %{fontname}-sans-sundanese-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSundanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sundanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sundanese.conf
%{_datadir}/appdata/%{fontname}-sans-sundanese.metainfo.xml


%package -n %{fontname}-sans-syloti-nagri-fonts
Summary:	Sans Syloti Nagri font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-syloti-nagri-fonts
%common_desc
Noto font Sans Syloti Nagri.

%files -n %{fontname}-sans-syloti-nagri-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSylotiNagri-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syloti-nagri.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syloti-nagri.conf
%{_datadir}/appdata/%{fontname}-sans-syloti-nagri.metainfo.xml


%package -n %{fontname}-sans-symbols-fonts
Summary:	Sans Symbols font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-symbols-fonts
%common_desc
Noto font Sans Symbols.

%files -n %{fontname}-sans-symbols-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSymbols-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-symbols.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-symbols.conf
%{_datadir}/appdata/%{fontname}-sans-symbols.metainfo.xml


%package -n %{fontname}-sans-syriac-eastern-fonts
Summary:	Sans Syriac Eastern font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-syriac-eastern-fonts
%common_desc
Noto font Sans Syriac Eastern.

%files -n %{fontname}-sans-syriac-eastern-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacEastern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-eastern.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-eastern.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-eastern.metainfo.xml


%package -n %{fontname}-sans-syriac-estrangela-fonts
Summary:	Sans Syriac Estrangela font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-syriac-estrangela-fonts
%common_desc
Noto font Sans Syriac Estrangela.

%files -n %{fontname}-sans-syriac-estrangela-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacEstrangela-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-estrangela.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-estrangela.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-estrangela.metainfo.xml


%package -n %{fontname}-sans-syriac-western-fonts
Summary:	Sans Syriac Western font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-syriac-western-fonts
%common_desc
Noto font Sans Syriac Western.

%files -n %{fontname}-sans-syriac-western-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansSyriacWestern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-western.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-western.conf
%{_datadir}/appdata/%{fontname}-sans-syriac-western.metainfo.xml


%package -n %{fontname}-sans-tagalog-fonts
Summary:	Sans Tagalog font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tagalog-fonts
%common_desc
Noto font Sans Tagalog.

%files -n %{fontname}-sans-tagalog-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTagalog-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagalog.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagalog.conf
%{_datadir}/appdata/%{fontname}-sans-tagalog.metainfo.xml


%package -n %{fontname}-sans-tagbanwa-fonts
Summary:	Sans Tagbanwa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tagbanwa-fonts
%common_desc
Noto font Sans Tagbanwa.

%files -n %{fontname}-sans-tagbanwa-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTagbanwa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagbanwa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagbanwa.conf
%{_datadir}/appdata/%{fontname}-sans-tagbanwa.metainfo.xml


%package -n %{fontname}-sans-tai-le-fonts
Summary:	Sans Tai Le font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tai-le-fonts
%common_desc
Noto font Sans Tai Le.

%files -n %{fontname}-sans-tai-le-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiLe-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-le.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-le.conf
%{_datadir}/appdata/%{fontname}-sans-tai-le.metainfo.xml


%package -n %{fontname}-sans-tai-tham-fonts
Summary:	Sans Tai Tham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tai-tham-fonts
%common_desc
Noto font Sans Tai Tham.

%files -n %{fontname}-sans-tai-tham-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiTham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-tham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-tham.conf
%{_datadir}/appdata/%{fontname}-sans-tai-tham.metainfo.xml


%package -n %{fontname}-sans-tai-viet-fonts
Summary:	Sans Tai Viet font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tai-viet-fonts
%common_desc
Noto font Sans Tai Viet.

%files -n %{fontname}-sans-tai-viet-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTaiViet-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-viet.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-viet.conf
%{_datadir}/appdata/%{fontname}-sans-tai-viet.metainfo.xml


%package -n %{fontname}-sans-tamil-fonts
Summary:	Sans Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tamil-fonts
%common_desc
Noto font Sans Tamil.

%files -n %{fontname}-sans-tamil-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil.conf
%{_datadir}/appdata/%{fontname}-sans-tamil.metainfo.xml


%package -n %{fontname}-sans-tamil-ui-fonts
Summary:	Sans Tamil UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tamil-ui-fonts
%common_desc
Noto font Sans Tamil UI.

%files -n %{fontname}-sans-tamil-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTamilUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil-ui.conf
%{_datadir}/appdata/%{fontname}-sans-tamil-ui.metainfo.xml


%package -n %{fontname}-sans-telugu-fonts
Summary:	Sans Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-telugu-fonts
%common_desc
Noto font Sans Telugu.

%files -n %{fontname}-sans-telugu-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTelugu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-telugu.conf
%{_datadir}/appdata/%{fontname}-sans-telugu.metainfo.xml


%package -n %{fontname}-sans-telugu-ui-fonts
Summary:	Sans Telugu UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-telugu-ui-fonts
%common_desc
Noto font Sans Telugu UI.

%files -n %{fontname}-sans-telugu-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTeluguUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-telugu-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-telugu-ui.conf
%{_datadir}/appdata/%{fontname}-sans-telugu-ui.metainfo.xml


%package -n %{fontname}-sans-thaana-fonts
Summary:	Sans Thaana font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-thaana-fonts
%common_desc
Noto font Sans Thaana.

%files -n %{fontname}-sans-thaana-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansThaana-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thaana.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thaana.conf
%{_datadir}/appdata/%{fontname}-sans-thaana.metainfo.xml


%package -n %{fontname}-sans-thai-fonts
Summary:	Sans Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-thai-fonts
%common_desc
Noto font Sans Thai.

%files -n %{fontname}-sans-thai-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai.conf
%{_datadir}/appdata/%{fontname}-sans-thai.metainfo.xml


%package -n %{fontname}-sans-thai-ui-fonts
Summary:	Sans Thai UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-thai-ui-fonts
%common_desc
Noto font Sans Thai UI.

%files -n %{fontname}-sans-thai-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansThaiUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai-ui.conf
%{_datadir}/appdata/%{fontname}-sans-thai-ui.metainfo.xml


%package -n %{fontname}-sans-tifinagh-fonts
Summary:	Sans Tifinagh font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tifinagh-fonts
%common_desc
Noto font Sans Tifinagh.

%files -n %{fontname}-sans-tifinagh-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTifinagh-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tifinagh.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tifinagh.conf
%{_datadir}/appdata/%{fontname}-sans-tifinagh.metainfo.xml


%package -n %{fontname}-sans-ugaritic-fonts
Summary:	Sans Ugaritic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-ugaritic-fonts
%common_desc
Noto font Sans Ugaritic.

%files -n %{fontname}-sans-ugaritic-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansUgaritic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ugaritic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ugaritic.conf
%{_datadir}/appdata/%{fontname}-sans-ugaritic.metainfo.xml


%package -n %{fontname}-sans-vai-fonts
Summary:	Sans Vai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-vai-fonts
%common_desc
Noto font Sans Vai.

%files -n %{fontname}-sans-vai-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansVai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-vai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-vai.conf
%{_datadir}/appdata/%{fontname}-sans-vai.metainfo.xml


%package -n %{fontname}-sans-yi-fonts
Summary:	Sans Yi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-yi-fonts
%common_desc
Noto font Sans Yi.

%files -n %{fontname}-sans-yi-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansYi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-yi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-yi.conf
%{_datadir}/appdata/%{fontname}-sans-yi.metainfo.xml


%package -n %{fontname}-serif-fonts
Summary:	Serif font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-fonts
%common_desc
Noto font Serif.

%files -n %{fontname}-serif-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerif-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif.conf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n %{fontname}-serif-armenian-fonts
Summary:	Serif Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-armenian-fonts
%common_desc
Noto font Serif Armenian.

%files -n %{fontname}-serif-armenian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-armenian.conf
%{_datadir}/appdata/%{fontname}-serif-armenian.metainfo.xml


%package -n %{fontname}-serif-georgian-fonts
Summary:	Serif Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-georgian-fonts
%common_desc
Noto font Serif Georgian.

%files -n %{fontname}-serif-georgian-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-georgian.conf
%{_datadir}/appdata/%{fontname}-serif-georgian.metainfo.xml


%package -n %{fontname}-serif-khmer-fonts
Summary:	Serif Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-khmer-fonts
%common_desc
Noto font Serif Khmer.

%files -n %{fontname}-serif-khmer-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-khmer.conf
%{_datadir}/appdata/%{fontname}-serif-khmer.metainfo.xml


%package -n %{fontname}-serif-lao-fonts
Summary:	Serif Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-lao-fonts
%common_desc
Noto font Serif Lao.

%files -n %{fontname}-serif-lao-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-lao.conf
%{_datadir}/appdata/%{fontname}-serif-lao.metainfo.xml


%package -n %{fontname}-serif-thai-fonts
Summary:	Serif Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-thai-fonts
%common_desc
Noto font Serif Thai.

%files -n %{fontname}-serif-thai-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-thai.conf
%{_datadir}/appdata/%{fontname}-serif-thai.metainfo.xml


%package -n %{fontname}-sans-oriya-fonts
Summary:	Sans Oriya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-oriya-fonts
%common_desc
Noto font Sans Oriya.

%files -n %{fontname}-sans-oriya-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOriya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-oriya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-oriya.conf
%{_datadir}/appdata/%{fontname}-sans-oriya.metainfo.xml


%package -n %{fontname}-sans-oriya-ui-fonts
Summary:	Sans Oriya UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-oriya-ui-fonts
%common_desc
Noto font Sans Oriya UI.

%files -n %{fontname}-sans-oriya-ui-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansOriyaUI-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-oriya-ui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-oriya-ui.conf
%{_datadir}/appdata/%{fontname}-sans-oriya-ui.metainfo.xml


%package -n %{fontname}-sans-tibetan-fonts
Summary:	Sans Tibetan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-sans-tibetan-fonts
%common_desc
Noto font Sans Tibetan.

%files -n %{fontname}-sans-tibetan-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSansTibetan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tibetan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tibetan.conf
%{_datadir}/appdata/%{fontname}-sans-tibetan.metainfo.xml


%package -n %{fontname}-nastaliq-urdu-fonts
Summary:	Nastaliq Urdu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-nastaliq-urdu-fonts
%common_desc
Noto font Nastaliq Urdu.

%files -n %{fontname}-nastaliq-urdu-fonts
%dir %{_fontdir}
%{_fontdir}/NotoNastaliqUrdu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-nastaliq-urdu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-nastaliq-urdu.conf
%{_datadir}/appdata/%{fontname}-nastaliq-urdu.metainfo.xml


%package -n %{fontname}-mono-fonts
Summary:	Mono font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-mono-fonts
%common_desc
Noto font Mono.

%files -n %{fontname}-mono-fonts
%dir %{_fontdir}
%{_fontdir}/NotoMono-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-mono.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-mono.conf
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml


%package -n %{fontname}-serif-bengali-fonts
Summary:	Serif Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-bengali-fonts
%common_desc
Noto font Serif Bengali.

%files -n %{fontname}-serif-bengali-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-bengali.conf
%{_datadir}/appdata/%{fontname}-serif-bengali.metainfo.xml


%package -n %{fontname}-serif-devanagari-fonts
Summary:	Serif Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-devanagari-fonts
%common_desc
Noto font Serif Devanagari.

%files -n %{fontname}-serif-devanagari-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-devanagari.conf
%{_datadir}/appdata/%{fontname}-serif-devanagari.metainfo.xml


%package -n %{fontname}-serif-gujarati-fonts
Summary:	Serif Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-gujarati-fonts
%common_desc
Noto font Serif Gujarati.

%files -n %{fontname}-serif-gujarati-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gujarati.conf
%{_datadir}/appdata/%{fontname}-serif-gujarati.metainfo.xml


%package -n %{fontname}-serif-kannada-fonts
Summary:	Serif Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-kannada-fonts
%common_desc
Noto font Serif Kannada.

%files -n %{fontname}-serif-kannada-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-kannada.conf
%{_datadir}/appdata/%{fontname}-serif-kannada.metainfo.xml


%package -n %{fontname}-serif-malayalam-fonts
Summary:	Serif Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-malayalam-fonts
%common_desc
Noto font Serif Malayalam.

%files -n %{fontname}-serif-malayalam-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-malayalam.conf
%{_datadir}/appdata/%{fontname}-serif-malayalam.metainfo.xml


%package -n %{fontname}-serif-tamil-fonts
Summary:	Serif Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-tamil-fonts
%common_desc
Noto font Serif Tamil.

%files -n %{fontname}-serif-tamil-fonts
%dir %{_fontdir}
%{_fontdir}/NotoSerifTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil.conf
%{_datadir}/appdata/%{fontname}-serif-tamil.metainfo.xml


%package -n %{fontname}-serif-telugu-fonts
Summary:	Serif Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{fontname}-common = %EVR

%description -n %{fontname}-serif-telugu-fonts
%common_desc
Noto font Serif Telugu.

%files -n %{fontname}-serif-telugu-fonts
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
%doc LICENSE
%doc README.md FAQ.md
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 20161022-alt1_4
- fixed fontconfig tag (closes: #34207)

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20141001-alt1_1
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 20130807-alt1_2
- converted for ALT Linux by srpmconvert tools

