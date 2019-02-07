Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname google-noto-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _fontname google-noto
%global _fontnamevf google-noto-vf
%global _fontvfdir %{_fontbasedir}/%{_fontnamevf}
%global fontname %{_fontname}
%global fontconf %{_fontname}
%global common_desc Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported scripts. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all scripts available\
in Unicode.\
%{nil}

%global commit a5e21f60336d8b9b76a0f230d07dd59e12d6da80
%global hprio	65
%global mprio	66
%global lprio	67

Name:           fonts-ttf-google-noto
Version:        20181223
Release:        alt1_1
Summary:        Hinted and Non Hinted OpenType fonts for Unicode scripts
License:        OFL
URL:            https://github.com/googlei18n/noto-fonts/
# downloaded from https://github.com/googlei18n/noto-fonts/commits/a5e21f60336d8b9b76a0f230d07dd59e12d6da80 -> download [zip]
# link https://github.com/googlei18n/noto-fonts/archive/a5e21f60336d8b9b76a0f230d07dd59e12d6da80.zip
Source0:        noto-fonts-%{commit}.zip
Source3:        %{mprio}-%{fontconf}-sans-armenian.conf
Source5:        %{mprio}-%{fontconf}-sans-bengali.conf
Source6:        %{lprio}-%{fontconf}-sans-bengali-ui.conf
Source9:        %{mprio}-%{fontconf}-sans-cherokee.conf
Source10:       %{mprio}-%{fontconf}-sans-coptic.conf
Source12:       %{mprio}-%{fontconf}-sans-devanagari.conf
Source13:       %{lprio}-%{fontconf}-sans-devanagari-ui.conf
Source15:       %{mprio}-%{fontconf}-sans-ethiopic.conf
Source16:       %{mprio}-%{fontconf}-sans-georgian.conf
Source18:       %{mprio}-%{fontconf}-sans-hebrew.conf
Source21:       %{mprio}-%{fontconf}-sans-kannada.conf
Source24:       %{mprio}-%{fontconf}-sans-khmer.conf
Source25:       %{lprio}-%{fontconf}-sans-khmer-ui.conf
Source26:       %{mprio}-%{fontconf}-sans-lao.conf
Source27:       %{lprio}-%{fontconf}-sans-lao-ui.conf
Source28:       %{mprio}-%{fontconf}-sans-lisu.conf
Source31:       %{mprio}-%{fontconf}-sans-malayalam.conf
Source32:       %{lprio}-%{fontconf}-sans-malayalam-ui.conf
Source34:       %{mprio}-%{fontconf}-sans-meetei-mayek.conf
Source35:       %{mprio}-%{fontconf}-sans-nko.conf
Source40:       %{mprio}-%{fontconf}-sans-shavian.conf
Source42:       %{mprio}-%{fontconf}-sans-tagalog.conf
Source44:       %{mprio}-%{fontconf}-sans-tamil.conf
Source45:       %{lprio}-%{fontconf}-sans-tamil-ui.conf
Source46:       %{mprio}-%{fontconf}-sans-telugu.conf
Source47:       %{mprio}-%{fontconf}-sans-thai.conf
Source48:       %{lprio}-%{fontconf}-sans-thai-ui.conf
Source51:       %{mprio}-%{fontconf}-sans-vai.conf
Source52:       %{mprio}-%{fontconf}-serif-armenian.conf
Source54:       %{mprio}-%{fontconf}-serif-georgian.conf
Source55:       %{mprio}-%{fontconf}-serif-khmer.conf
Source56:       %{mprio}-%{fontconf}-serif-lao.conf
Source57:       %{mprio}-%{fontconf}-serif-thai.conf
Source58:       %{lprio}-%{fontconf}-sans-kannada-ui.conf
Source59:       %{lprio}-%{fontconf}-sans-telugu-ui.conf
Source60:       %{mprio}-%{fontconf}-sans-gujarati.conf
Source61:       %{lprio}-%{fontconf}-sans-gujarati-ui.conf
Source62:       %{mprio}-%{fontconf}-sans-hanunoo.conf
Source64:       %{mprio}-%{fontconf}-kufi-arabic.conf
Source65:       %{mprio}-%{fontconf}-naskh-arabic.conf
Source66:       %{lprio}-%{fontconf}-naskh-arabic-ui.conf
Source67:       %{mprio}-%{fontconf}-serif-balinese.conf
Source68:       %{mprio}-%{fontconf}-sans-bamum.conf
Source69:       %{mprio}-%{fontconf}-sans-batak.conf
Source70:       %{mprio}-%{fontconf}-sans-buginese.conf
Source71:       %{mprio}-%{fontconf}-sans-buhid.conf
Source72:       %{mprio}-%{fontconf}-sans-canadian-aboriginal.conf
Source73:       %{mprio}-%{fontconf}-sans-cham.conf
Source74:       %{mprio}-%{fontconf}-sans-cuneiform.conf
Source75:       %{mprio}-%{fontconf}-sans-cypriot.conf
Source76:       %{mprio}-%{fontconf}-sans-gothic.conf
Source77:       %{mprio}-%{fontconf}-sans-gurmukhi.conf
Source78:       %{lprio}-%{fontconf}-sans-gurmukhi-ui.conf
Source81:       %{mprio}-%{fontconf}-sans-javanese.conf
Source82:       %{mprio}-%{fontconf}-sans-lepcha.conf
Source83:       %{mprio}-%{fontconf}-sans-limbu.conf
Source85:       %{mprio}-%{fontconf}-sans-mongolian.conf
Source86:       %{mprio}-%{fontconf}-sans-myanmar.conf
Source87:       %{lprio}-%{fontconf}-sans-myanmar-ui.conf
Source88:       %{mprio}-%{fontconf}-sans-new-tai-lue.conf
Source89:       %{mprio}-%{fontconf}-sans-ogham.conf
Source90:       %{mprio}-%{fontconf}-sans-ol-chiki.conf
Source94:       %{mprio}-%{fontconf}-sans-rejang.conf
Source95:       %{mprio}-%{fontconf}-sans-runic.conf
Source97:       %{mprio}-%{fontconf}-sans-saurashtra.conf
Source98:       %{hprio}-%{fontconf}-sans-sinhala.conf
Source99:       %{mprio}-%{fontconf}-sans-sundanese.conf
Source101:      %{mprio}-%{fontconf}-sans-syriac-eastern.conf
Source102:      %{mprio}-%{fontconf}-sans-syriac-estrangela.conf
Source103:      %{mprio}-%{fontconf}-sans-syriac-western.conf
Source105:      %{mprio}-%{fontconf}-sans-tifinagh.conf
Source107:      %{mprio}-%{fontconf}-sans-tagbanwa.conf
Source108:      %{mprio}-%{fontconf}-sans-thaana.conf

Source156:      %{mprio}-%{fontconf}-sans-oriya.conf
Source157:      %{lprio}-%{fontconf}-sans-oriya-ui.conf
Source158:      %{mprio}-%{fontconf}-nastaliq-urdu.conf
Source159:      %{mprio}-%{fontconf}-sans-tibetan.conf
Source161:      %{mprio}-%{fontconf}-serif-bengali.conf
Source162:      %{mprio}-%{fontconf}-serif-devanagari.conf
Source163:      %{mprio}-%{fontconf}-serif-gujarati.conf
Source164:      %{mprio}-%{fontconf}-serif-kannada.conf
Source165:      %{mprio}-%{fontconf}-serif-malayalam.conf
Source166:      %{mprio}-%{fontconf}-serif-tamil.conf
Source167:      %{mprio}-%{fontconf}-serif-telugu.conf

# Add appstream metadata files
Source200:      %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source49: import.info

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
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-kufi-arabic = 20161022-alt1_4
Obsoletes:	%{_fontname}-kufi-arabic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-kufi-arabic
%common_desc
Noto font Kufi Arabic.

%files -n fonts-ttf-google-noto-kufi-arabic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoKufiArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-kufi-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-kufi-arabic.conf
%{_datadir}/appdata/%{_fontname}-kufi-arabic.metainfo.xml

%package -n fonts-ttf-google-noto-music
Summary:	Music font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-music = 20161022-alt1_4
Obsoletes:	%{_fontname}-music-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-music
%common_desc
Noto font Music.

%files -n fonts-ttf-google-noto-music
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoMusic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-music.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-music.conf
%{_datadir}/appdata/%{_fontname}-music.metainfo.xml

%package -n fonts-ttf-google-noto-naskh-arabic
Summary:	Naskh Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-naskh-arabic = 20161022-alt1_4
Obsoletes:	%{_fontname}-naskh-arabic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-naskh-arabic
%common_desc
Noto font Naskh Arabic.

%files -n fonts-ttf-google-noto-naskh-arabic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoNaskhArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-naskh-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-naskh-arabic.conf
%{_datadir}/appdata/%{_fontname}-naskh-arabic.metainfo.xml

%package -n fonts-ttf-google-noto-naskh-arabic-ui
Summary:	Naskh Arabic UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-naskh-arabic-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-naskh-arabic-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-naskh-arabic-ui
%common_desc
Noto font Naskh Arabic UI.

%files -n fonts-ttf-google-noto-naskh-arabic-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoNaskhArabicUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-naskh-arabic-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-naskh-arabic-ui.conf
%{_datadir}/appdata/%{_fontname}-naskh-arabic-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans
Summary:	Sans font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans
%common_desc
Noto font Sans.

%files -n fonts-ttf-google-noto-sans
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSans-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans.conf
%{_datadir}/appdata/%{_fontname}-sans.metainfo.xml

%package -n fonts-ttf-google-noto-sans-display
Summary:	Sans Display font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-display = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-display-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-sans-ui < %EVR

%description -n fonts-ttf-google-noto-sans-display
%common_desc
Noto font Sans Display.

%files -n fonts-ttf-google-noto-sans-display
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansDisplay-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-display.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-display.conf
%{_datadir}/appdata/%{_fontname}-sans-display.metainfo.xml

%package -n fonts-ttf-google-noto-sans-adlam
Summary:	Sans Adlam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-adlam = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-adlam-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-adlam
%common_desc
Noto font Sans Adlam.

%files -n fonts-ttf-google-noto-sans-adlam
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansAdlam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-adlam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-adlam.conf
%{_datadir}/appdata/%{_fontname}-sans-adlam.metainfo.xml

%package -n fonts-ttf-google-noto-sans-adlam-unjoined
Summary:	Sans Adlam Unjoined font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-adlam-unjoined = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-adlam-unjoined-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-adlam-unjoined
%common_desc
Noto font Sans Adlam Unjoined.

%files -n fonts-ttf-google-noto-sans-adlam-unjoined
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansAdlamUnjoined-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-adlam-unjoined.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-adlam-unjoined.conf
%{_datadir}/appdata/%{_fontname}-sans-adlam-unjoined.metainfo.xml

%package -n fonts-ttf-google-noto-sans-anatolian-hieroglyphs
Summary:	Sans Anatolian Hieroglyphs font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-anatolian-hieroglyphs = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-anatolian-hieroglyphs-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-anatolian-hieroglyphs
%common_desc
Noto font Sans Anatolian Hieroglyphs.

%files -n fonts-ttf-google-noto-sans-anatolian-hieroglyphs
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansAnatolianHieroglyphs-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-anatolian-hieroglyphs.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-anatolian-hieroglyphs.conf
%{_datadir}/appdata/%{_fontname}-sans-anatolian-hieroglyphs.metainfo.xml

%package -n fonts-ttf-google-noto-sans-arabic
Summary:	Sans Arabic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-arabic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-arabic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-arabic
%common_desc
Noto font Sans Arabic.

%files -n fonts-ttf-google-noto-sans-arabic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansArabic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-arabic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-arabic.conf
%{_datadir}/appdata/%{_fontname}-sans-arabic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-arabic-ui
Summary:	Sans Arabic UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-arabic-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-arabic-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-arabic-ui
%common_desc
Noto font Sans Arabic UI.

%files -n fonts-ttf-google-noto-sans-arabic-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansArabicUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-arabic-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-arabic-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-arabic-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-armenian
Summary:	Sans Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-armenian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-armenian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-armenian
%common_desc
Noto font Sans Armenian.

%files -n fonts-ttf-google-noto-sans-armenian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-armenian.conf
%{_datadir}/appdata/%{_fontname}-sans-armenian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-avestan
Summary:	Sans Avestan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-avestan = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-avestan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-avestan
%common_desc
Noto font Sans Avestan.

%files -n fonts-ttf-google-noto-sans-avestan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansAvestan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-avestan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-avestan.conf
%{_datadir}/appdata/%{_fontname}-sans-avestan.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bamum
Summary:	Sans Bamum font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bamum = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bamum-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bamum
%common_desc
Noto font Sans Bamum.

%files -n fonts-ttf-google-noto-sans-bamum
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBamum-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bamum.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bamum.conf
%{_datadir}/appdata/%{_fontname}-sans-bamum.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bassa-vah
Summary:	Sans Bassa Vah font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bassa-vah = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bassa-vah-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bassa-vah
%common_desc
Noto font Sans Bassa Vah.

%files -n fonts-ttf-google-noto-sans-bassa-vah
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBassaVah-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bassa-vah.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bassa-vah.conf
%{_datadir}/appdata/%{_fontname}-sans-bassa-vah.metainfo.xml

%package -n fonts-ttf-google-noto-sans-batak
Summary:	Sans Batak font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-batak = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-batak-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-batak
%common_desc
Noto font Sans Batak.

%files -n fonts-ttf-google-noto-sans-batak
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBatak-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-batak.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-batak.conf
%{_datadir}/appdata/%{_fontname}-sans-batak.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bengali
Summary:	Sans Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bengali = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bengali-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali
%common_desc
Noto font Sans Bengali.

%files -n fonts-ttf-google-noto-sans-bengali
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali.conf
%{_datadir}/appdata/%{_fontname}-sans-bengali.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bengali-ui
Summary:	Sans Bengali UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bengali-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bengali-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali-ui
%common_desc
Noto font Sans Bengali UI.

%files -n fonts-ttf-google-noto-sans-bengali-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBengaliUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-bengali-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-bengali-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-bengali-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bhaiksuki
Summary:	Sans Bhaiksuki font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-bhaiksuki = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bhaiksuki-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bhaiksuki
%common_desc
Noto font Sans Bhaiksuki.

%files -n fonts-ttf-google-noto-sans-bhaiksuki
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBhaiksuki-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bhaiksuki.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bhaiksuki.conf
%{_datadir}/appdata/%{_fontname}-sans-bhaiksuki.metainfo.xml

%package -n fonts-ttf-google-noto-sans-brahmi
Summary:	Sans Brahmi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-brahmi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-brahmi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-brahmi
%common_desc
Noto font Sans Brahmi.

%files -n fonts-ttf-google-noto-sans-brahmi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBrahmi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-brahmi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-brahmi.conf
%{_datadir}/appdata/%{_fontname}-sans-brahmi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-buginese
Summary:	Sans Buginese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-buginese = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-buginese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-buginese
%common_desc
Noto font Sans Buginese.

%files -n fonts-ttf-google-noto-sans-buginese
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBuginese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buginese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buginese.conf
%{_datadir}/appdata/%{_fontname}-sans-buginese.metainfo.xml

%package -n fonts-ttf-google-noto-sans-buhid
Summary:	Sans Buhid font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-buhid = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-buhid-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-buhid
%common_desc
Noto font Sans Buhid.

%files -n fonts-ttf-google-noto-sans-buhid
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansBuhid-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-buhid.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-buhid.conf
%{_datadir}/appdata/%{_fontname}-sans-buhid.metainfo.xml

%package -n fonts-ttf-google-noto-sans-canadian-aboriginal
Summary:	Sans Canadian Aboriginal font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-canadian-aboriginal = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-canadian-aboriginal-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-canadian-aboriginal
%common_desc
Noto font Sans Canadian Aboriginal.

%files -n fonts-ttf-google-noto-sans-canadian-aboriginal
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCanadianAboriginal-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-canadian-aboriginal.conf
%{_datadir}/appdata/%{_fontname}-sans-canadian-aboriginal.metainfo.xml

%package -n fonts-ttf-google-noto-sans-caucasian-albanian
Summary:	Sans Caucasian Albanian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-caucasian-albanian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-caucasian-albanian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-caucasian-albanian
%common_desc
Noto font Sans Caucasian Albanian.

%files -n fonts-ttf-google-noto-sans-caucasian-albanian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCaucasianAlbanian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-caucasian-albanian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-caucasian-albanian.conf
%{_datadir}/appdata/%{_fontname}-sans-caucasian-albanian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-carian
Summary:	Sans Carian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-carian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-carian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-carian
%common_desc
Noto font Sans Carian.

%files -n fonts-ttf-google-noto-sans-carian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCarian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-carian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-carian.conf
%{_datadir}/appdata/%{_fontname}-sans-carian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-chakma
Summary:	Sans Chakma font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-chakma = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-chakma-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-chakma
%common_desc
Noto font Sans Chakma.

%files -n fonts-ttf-google-noto-sans-chakma
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansChakma-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-chakma.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-chakma.conf
%{_datadir}/appdata/%{_fontname}-sans-chakma.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cham
Summary:	Sans Cham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cham = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cham
%common_desc
Noto font Sans Cham.

%files -n fonts-ttf-google-noto-sans-cham
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cham.conf
%{_datadir}/appdata/%{_fontname}-sans-cham.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cherokee
Summary:	Sans Cherokee font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cherokee = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cherokee-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cherokee
%common_desc
Noto font Sans Cherokee.

%files -n fonts-ttf-google-noto-sans-cherokee
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCherokee-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cherokee.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cherokee.conf
%{_datadir}/appdata/%{_fontname}-sans-cherokee.metainfo.xml

%package -n fonts-ttf-google-noto-sans-coptic
Summary:	Sans Coptic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-coptic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-coptic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-coptic
%common_desc
Noto font Sans Coptic.

%files -n fonts-ttf-google-noto-sans-coptic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCoptic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-coptic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-coptic.conf
%{_datadir}/appdata/%{_fontname}-sans-coptic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cuneiform
Summary:	Sans Cuneiform font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cuneiform = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cuneiform-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cuneiform
%common_desc
Noto font Sans Cuneiform.

%files -n fonts-ttf-google-noto-sans-cuneiform
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCuneiform-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cuneiform.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cuneiform.conf
%{_datadir}/appdata/%{_fontname}-sans-cuneiform.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cypriot
Summary:	Sans Cypriot font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-cypriot = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cypriot-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cypriot
%common_desc
Noto font Sans Cypriot.

%files -n fonts-ttf-google-noto-sans-cypriot
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansCypriot-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cypriot.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cypriot.conf
%{_datadir}/appdata/%{_fontname}-sans-cypriot.metainfo.xml

%package -n fonts-ttf-google-noto-sans-deseret
Summary:	Sans Deseret font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-deseret = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-deseret-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-deseret
%common_desc
Noto font Sans Deseret.

%files -n fonts-ttf-google-noto-sans-deseret
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansDeseret-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-deseret.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-deseret.conf
%{_datadir}/appdata/%{_fontname}-sans-deseret.metainfo.xml

%package -n fonts-ttf-google-noto-sans-devanagari
Summary:	Sans Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-devanagari = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-devanagari-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari
%common_desc
Noto font Sans Devanagari.

%files -n fonts-ttf-google-noto-sans-devanagari
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari.conf
%{_datadir}/appdata/%{_fontname}-sans-devanagari.metainfo.xml

%package -n fonts-ttf-google-noto-sans-devanagari-ui
Summary:	Sans Devanagari UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-devanagari-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-devanagari-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari-ui
%common_desc
Noto font Sans Devanagari UI.

%files -n fonts-ttf-google-noto-sans-devanagari-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansDevanagariUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-devanagari-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-devanagari-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-devanagari-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-duployan
Summary:	Sans Duployan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-duployan = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-duployan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-duployan
%common_desc
Noto font Sans Duployan.

%files -n fonts-ttf-google-noto-sans-duployan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansDuployan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-duployan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-duployan.conf
%{_datadir}/appdata/%{_fontname}-sans-duployan.metainfo.xml

%package -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
Summary:	Sans Egyptian Hieroglyphs font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-egyptian-hieroglyphs = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-egyptian-hieroglyphs-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%common_desc
Noto font Sans Egyptian Hieroglyphs.

%files -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansEgyptianHieroglyphs-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-egyptian-hieroglyphs.conf
%{_datadir}/appdata/%{_fontname}-sans-egyptian-hieroglyphs.metainfo.xml

%package -n fonts-ttf-google-noto-sans-elbasan
Summary:	Sans Elbasan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-elbasan = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-elbasan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-elbasan
%common_desc
Noto font Sans Elbasan.

%files -n fonts-ttf-google-noto-sans-elbasan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansElbasan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-elbasan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-elbasan.conf
%{_datadir}/appdata/%{_fontname}-sans-elbasan.metainfo.xml

%package -n fonts-ttf-google-noto-sans-ethiopic
Summary:	Sans Ethiopic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ethiopic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-ethiopic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ethiopic
%common_desc
Noto font Sans Ethiopic.

%files -n fonts-ttf-google-noto-sans-ethiopic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansEthiopic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ethiopic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ethiopic.conf
%{_datadir}/appdata/%{_fontname}-sans-ethiopic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-georgian
Summary:	Sans Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-georgian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-georgian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-georgian
%common_desc
Noto font Sans Georgian.

%files -n fonts-ttf-google-noto-sans-georgian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-georgian.conf
%{_datadir}/appdata/%{_fontname}-sans-georgian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-glagolitic
Summary:	Sans Glagolitic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-glagolitic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-glagolitic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-glagolitic
%common_desc
Noto font Sans Glagolitic.

%files -n fonts-ttf-google-noto-sans-glagolitic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGlagolitic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-glagolitic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-glagolitic.conf
%{_datadir}/appdata/%{_fontname}-sans-glagolitic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-gothic
Summary:	Sans Gothic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gothic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-gothic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gothic
%common_desc
Noto font Sans Gothic.

%files -n fonts-ttf-google-noto-sans-gothic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGothic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gothic.conf
%{_datadir}/appdata/%{_fontname}-sans-gothic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-grantha
Summary:	Sans Grantha font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-grantha = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-grantha-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-grantha
%common_desc
Noto font Sans Grantha.

%files -n fonts-ttf-google-noto-sans-grantha
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGrantha-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-grantha.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-grantha.conf
%{_datadir}/appdata/%{_fontname}-sans-grantha.metainfo.xml

%package -n fonts-ttf-google-noto-sans-gujarati
Summary:	Sans Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gujarati = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-gujarati-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gujarati
%common_desc
Noto font Sans Gujarati.

%files -n fonts-ttf-google-noto-sans-gujarati
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gujarati.conf
%{_datadir}/appdata/%{_fontname}-sans-gujarati.metainfo.xml

%package -n fonts-ttf-google-noto-sans-gujarati-ui
Summary:	Sans Gujarati UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gujarati-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-gujarati-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gujarati-ui
%common_desc
Noto font Sans Gujarati UI.

%files -n fonts-ttf-google-noto-sans-gujarati-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGujaratiUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-gujarati-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-gujarati-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-gujarati-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-gurmukhi
Summary:	Sans Gurmukhi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gurmukhi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-gurmukhi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gurmukhi
%common_desc
Noto font Sans Gurmukhi.

%files -n fonts-ttf-google-noto-sans-gurmukhi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGurmukhi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-gurmukhi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-gurmukhi.conf
%{_datadir}/appdata/%{_fontname}-sans-gurmukhi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-gurmukhi-ui
Summary:	Sans Gurmukhi UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-gurmukhi-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-gurmukhi-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-gurmukhi-ui
%common_desc
Noto font Sans Gurmukhi UI.

%files -n fonts-ttf-google-noto-sans-gurmukhi-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansGurmukhiUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-gurmukhi-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-gurmukhi-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-gurmukhi-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-hanunno
Summary:	Sans Hanunoo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-hanunno = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-hanunoo-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-sans-hanunno < %EVR

%description -n fonts-ttf-google-noto-sans-hanunno
%common_desc
Noto font Sans Hanunoo.

%files -n fonts-ttf-google-noto-sans-hanunno
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansHanunoo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hanunoo.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hanunoo.conf
%{_datadir}/appdata/%{_fontname}-sans-hanunoo.metainfo.xml

%package -n fonts-ttf-google-noto-sans-hatran
Summary:	Sans Hatran font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-hatran = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-hatran-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-hatran
%common_desc
Noto font Sans Hatran.

%files -n fonts-ttf-google-noto-sans-hatran
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansHatran-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hatran.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hatran.conf
%{_datadir}/appdata/%{_fontname}-sans-hatran.metainfo.xml

%package -n fonts-ttf-google-noto-sans-hebrew
Summary:	Sans Hebrew font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-hebrew = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-hebrew-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-hebrew
%common_desc
Noto font Sans Hebrew.

%files -n fonts-ttf-google-noto-sans-hebrew
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansHebrew-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hebrew.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hebrew.conf
%{_datadir}/appdata/%{_fontname}-sans-hebrew.metainfo.xml

%package -n fonts-ttf-google-noto-sans-imperial-aramaic
Summary:	Sans Imperial Aramaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-imperial-aramaic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-imperial-aramaic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-imperial-aramaic
%common_desc
Noto font Sans Imperial Aramaic.

%files -n fonts-ttf-google-noto-sans-imperial-aramaic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansImperialAramaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-imperial-aramaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-imperial-aramaic.conf
%{_datadir}/appdata/%{_fontname}-sans-imperial-aramaic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
Summary:	Sans Inscriptional Pahlavi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-inscriptional-pahlavi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-inscriptional-pahlavi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
%common_desc
Noto font Sans Inscriptional Pahlavi.

%files -n fonts-ttf-google-noto-sans-inscriptional-pahlavi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansInscriptionalPahlavi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-pahlavi.conf
%{_datadir}/appdata/%{_fontname}-sans-inscriptional-pahlavi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-inscriptional-parthian
Summary:	Sans Inscriptional Parthian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-inscriptional-parthian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-inscriptional-parthian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-inscriptional-parthian
%common_desc
Noto font Sans Inscriptional Parthian.

%files -n fonts-ttf-google-noto-sans-inscriptional-parthian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansInscriptionalParthian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-inscriptional-parthian.conf
%{_datadir}/appdata/%{_fontname}-sans-inscriptional-parthian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-javanese
Summary:	Sans Javanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-javanese = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-javanese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-javanese
%common_desc
Noto font Sans Javanese.

%files -n fonts-ttf-google-noto-sans-javanese
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansJavanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-javanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-javanese.conf
%{_datadir}/appdata/%{_fontname}-sans-javanese.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kaithi
Summary:	Sans Kaithi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kaithi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kaithi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kaithi
%common_desc
Noto font Sans Kaithi.

%files -n fonts-ttf-google-noto-sans-kaithi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKaithi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kaithi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kaithi.conf
%{_datadir}/appdata/%{_fontname}-sans-kaithi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kannada
Summary:	Sans Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kannada = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kannada-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada
%common_desc
Noto font Sans Kannada.

%files -n fonts-ttf-google-noto-sans-kannada
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada.conf
%{_datadir}/appdata/%{_fontname}-sans-kannada.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kannada-ui
Summary:	Sans Kannada UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kannada-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kannada-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada-ui
%common_desc
Noto font Sans Kannada UI.

%files -n fonts-ttf-google-noto-sans-kannada-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKannadaUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-kannada-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-kannada-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-kannada-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kayah-li
Summary:	Sans Kayah Li font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kayah-li = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kayah-li-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kayah-li
%common_desc
Noto font Sans Kayah Li.

%files -n fonts-ttf-google-noto-sans-kayah-li
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKayahLi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kayah-li.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kayah-li.conf
%{_datadir}/appdata/%{_fontname}-sans-kayah-li.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kharoshthi
Summary:	Sans Kharoshthi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-kharoshthi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kharoshthi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kharoshthi
%common_desc
Noto font Sans Kharoshthi.

%files -n fonts-ttf-google-noto-sans-kharoshthi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKharoshthi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kharoshthi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kharoshthi.conf
%{_datadir}/appdata/%{_fontname}-sans-kharoshthi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khmer
Summary:	Sans Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khmer = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khmer-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer
%common_desc
Noto font Sans Khmer.

%files -n fonts-ttf-google-noto-sans-khmer
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer.conf
%{_datadir}/appdata/%{_fontname}-sans-khmer.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khmer-ui
Summary:	Sans Khmer UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khmer-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khmer-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer-ui
%common_desc
Noto font Sans Khmer UI.

%files -n fonts-ttf-google-noto-sans-khmer-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKhmerUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-khmer-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-khmer-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-khmer-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khojki
Summary:	Sans Khojki font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khojki = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khojki-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khojki
%common_desc
Noto font Sans Khojki.

%files -n fonts-ttf-google-noto-sans-khojki
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKhojki-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khojki.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khojki.conf
%{_datadir}/appdata/%{_fontname}-sans-khojki.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khudawadi
Summary:	Sans Khudawadi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-khudawadi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khudawadi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khudawadi
%common_desc
Noto font Sans Khudawadi.

%files -n fonts-ttf-google-noto-sans-khudawadi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansKhudawadi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khudawadi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khudawadi.conf
%{_datadir}/appdata/%{_fontname}-sans-khudawadi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lao
Summary:	Sans Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lao = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lao-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao
%common_desc
Noto font Sans Lao.

%files -n fonts-ttf-google-noto-sans-lao
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao.conf
%{_datadir}/appdata/%{_fontname}-sans-lao.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lao-ui
Summary:	Sans Lao UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lao-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lao-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao-ui
%common_desc
Noto font Sans Lao UI.

%files -n fonts-ttf-google-noto-sans-lao-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLaoUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-lao-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-lao-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-lao-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lepcha
Summary:	Sans Lepcha font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lepcha = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lepcha-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lepcha
%common_desc
Noto font Sans Lepcha.

%files -n fonts-ttf-google-noto-sans-lepcha
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLepcha-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lepcha.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lepcha.conf
%{_datadir}/appdata/%{_fontname}-sans-lepcha.metainfo.xml

%package -n fonts-ttf-google-noto-sans-limbu
Summary:	Sans Limbu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-limbu = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-limbu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-limbu
%common_desc
Noto font Sans Limbu.

%files -n fonts-ttf-google-noto-sans-limbu
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLimbu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-limbu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-limbu.conf
%{_datadir}/appdata/%{_fontname}-sans-limbu.metainfo.xml

%package -n fonts-ttf-google-noto-sans-linear-a
Summary:	Sans Linear A font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-linear-a = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-linear-a-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-linear-a
%common_desc
Noto font Sans Linear A.

%files -n fonts-ttf-google-noto-sans-linear-a
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLinearA-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-linear-a.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-linear-a.conf
%{_datadir}/appdata/%{_fontname}-sans-linear-a.metainfo.xml

%package -n fonts-ttf-google-noto-sans-linearb
Summary:	Sans Linear B font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-linearb = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-linear-b-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-sans-linearb < %EVR

%description -n fonts-ttf-google-noto-sans-linearb
%common_desc
Noto font Sans Linear B.

%files -n fonts-ttf-google-noto-sans-linearb
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLinearB-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-linear-b.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-linear-b.conf
%{_datadir}/appdata/%{_fontname}-sans-linear-b.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lisu
Summary:	Sans Lisu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lisu = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lisu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lisu
%common_desc
Noto font Sans Lisu.

%files -n fonts-ttf-google-noto-sans-lisu
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLisu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lisu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lisu.conf
%{_datadir}/appdata/%{_fontname}-sans-lisu.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lycian
Summary:	Sans Lycian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lycian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lycian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lycian
%common_desc
Noto font Sans Lycian.

%files -n fonts-ttf-google-noto-sans-lycian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLycian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lycian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lycian.conf
%{_datadir}/appdata/%{_fontname}-sans-lycian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lydian
Summary:	Sans Lydian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-lydian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lydian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lydian
%common_desc
Noto font Sans Lydian.

%files -n fonts-ttf-google-noto-sans-lydian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansLydian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lydian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lydian.conf
%{_datadir}/appdata/%{_fontname}-sans-lydian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mahajani
Summary:	Sans Mahajani font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mahajani = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mahajani-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mahajani
%common_desc
Noto font Sans Mahajani.

%files -n fonts-ttf-google-noto-sans-mahajani
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMahajani-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mahajani.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mahajani.conf
%{_datadir}/appdata/%{_fontname}-sans-mahajani.metainfo.xml

%package -n fonts-ttf-google-noto-sans-malayalam
Summary:	Sans Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-malayalam = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-malayalam-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam
%common_desc
Noto font Sans Malayalam.

%files -n fonts-ttf-google-noto-sans-malayalam
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam.conf
%{_datadir}/appdata/%{_fontname}-sans-malayalam.metainfo.xml

%package -n fonts-ttf-google-noto-sans-malayalam-ui
Summary:	Sans Malayalam UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-malayalam-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-malayalam-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam-ui
%common_desc
Noto font Sans Malayalam UI.

%files -n fonts-ttf-google-noto-sans-malayalam-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMalayalamUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-malayalam-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-malayalam-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-malayalam-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mandaic
Summary:	Sans Mandaic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mandaic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mandaic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mandaic
%common_desc
Noto font Sans Mandaic.

%files -n fonts-ttf-google-noto-sans-mandaic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMandaic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mandaic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mandaic.conf
%{_datadir}/appdata/%{_fontname}-sans-mandaic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-manichaean
Summary:	Sans Manichaean font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-manichaean = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-manichaean-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-manichaean
%common_desc
Noto font Sans Manichaean.

%files -n fonts-ttf-google-noto-sans-manichaean
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansManichaean-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-manichaean.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-manichaean.conf
%{_datadir}/appdata/%{_fontname}-sans-manichaean.metainfo.xml

%package -n fonts-ttf-google-noto-sans-marchen
Summary:	Sans Marchen font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-marchen = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-marchen-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-marchen
%common_desc
Noto font Sans Marchen.

%files -n fonts-ttf-google-noto-sans-marchen
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMarchen-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-marchen.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-marchen.conf
%{_datadir}/appdata/%{_fontname}-sans-marchen.metainfo.xml

%package -n fonts-ttf-google-noto-sans-math
Summary:	Sans Math font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-math-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-math-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-math
%common_desc
Noto font Sans Math.

%files -n fonts-ttf-google-noto-sans-math
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMath-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-math.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-math.conf
%{_datadir}/appdata/%{_fontname}-sans-math.metainfo.xml

%package -n fonts-ttf-google-noto-sans-meeteimayek
Summary:	Sans Meetei Mayek font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-meeteimayek = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-meetei-mayek-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-sans-meeteimayek < %EVR

%description -n fonts-ttf-google-noto-sans-meeteimayek
%common_desc
Noto font Sans Meetei Mayek.

%files -n fonts-ttf-google-noto-sans-meeteimayek
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMeeteiMayek-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-meetei-mayek.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-meetei-mayek.conf
%{_datadir}/appdata/%{_fontname}-sans-meetei-mayek.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mende-kikakui
Summary:	Sans Mende Kikakui font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mende-kikakui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mende-kikakui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mende-kikakui
%common_desc
Noto font Sans Mende Kikakui.

%files -n fonts-ttf-google-noto-sans-mende-kikakui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMendeKikakui-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mende-kikakui.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mende-kikakui.conf
%{_datadir}/appdata/%{_fontname}-sans-mende-kikakui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-meroitic
Summary:	Sans Meroitic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-meroitic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-meroitic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-meroitic
%common_desc
Noto font Sans Meroitic.

%files -n fonts-ttf-google-noto-sans-meroitic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMeroitic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-meroitic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-meroitic.conf
%{_datadir}/appdata/%{_fontname}-sans-meroitic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-miao
Summary:	Sans Miao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-miao = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-miao-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-miao
%common_desc
Noto font Sans Miao.

%files -n fonts-ttf-google-noto-sans-miao
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMiao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-miao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-miao.conf
%{_datadir}/appdata/%{_fontname}-sans-miao.metainfo.xml

%package -n fonts-ttf-google-noto-sans-modi
Summary:	Sans Modi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-modi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-modi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-modi
%common_desc
Noto font Sans Modi.

%files -n fonts-ttf-google-noto-sans-modi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansModi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-modi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-modi.conf
%{_datadir}/appdata/%{_fontname}-sans-modi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mongolian
Summary:	Sans Mongolian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mongolian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mongolian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mongolian
%common_desc
Noto font Sans Mongolian.

%files -n fonts-ttf-google-noto-sans-mongolian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMongolian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mongolian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mongolian.conf
%{_datadir}/appdata/%{_fontname}-sans-mongolian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mro
Summary:	Sans Mro font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mro = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mro-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mro
%common_desc
Noto font Sans Mro.

%files -n fonts-ttf-google-noto-sans-mro
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMro-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mro.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mro.conf
%{_datadir}/appdata/%{_fontname}-sans-mro.metainfo.xml

%package -n fonts-ttf-google-noto-sans-multani
Summary:	Sans Multani font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-multani = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-multani-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-multani
%common_desc
Noto font Sans Multani.

%files -n fonts-ttf-google-noto-sans-multani
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMultani-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-multani.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-multani.conf
%{_datadir}/appdata/%{_fontname}-sans-multani.metainfo.xml

%package -n fonts-ttf-google-noto-sans-myanmar
Summary:	Sans Myanmar font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-myanmar = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-myanmar-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar
%common_desc
Noto font Sans Myanmar.

%files -n fonts-ttf-google-noto-sans-myanmar
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMyanmar-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar.conf
%{_datadir}/appdata/%{_fontname}-sans-myanmar.metainfo.xml

%package -n fonts-ttf-google-noto-sans-myanmar-ui
Summary:	Sans Myanmar UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-myanmar-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-myanmar-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar-ui
%common_desc
Noto font Sans Myanmar UI.

%files -n fonts-ttf-google-noto-sans-myanmar-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMyanmarUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-myanmar-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-myanmar-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-myanmar-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-nabataean
Summary:	Sans Nabataean font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-nabataean = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-nabataean-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-nabataean
%common_desc
Noto font Sans Nabataean.

%files -n fonts-ttf-google-noto-sans-nabataean
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansNabataean-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-nabataean.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-nabataean.conf
%{_datadir}/appdata/%{_fontname}-sans-nabataean.metainfo.xml

%package -n fonts-ttf-google-noto-sans-new-tai-lue
Summary:	Sans New Tai Lue font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-new-tai-lue = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-new-tai-lue-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-new-tai-lue
%common_desc
Noto font Sans New Tai Lue.

%files -n fonts-ttf-google-noto-sans-new-tai-lue
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansNewTaiLue-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-new-tai-lue.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-new-tai-lue.conf
%{_datadir}/appdata/%{_fontname}-sans-new-tai-lue.metainfo.xml

%package -n fonts-ttf-google-noto-sans-newa
Summary:	Sans Newa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-newa = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-newa-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-newa
%common_desc
Noto font Sans Newa.

%files -n fonts-ttf-google-noto-sans-newa
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansNewa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-newa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-newa.conf
%{_datadir}/appdata/%{_fontname}-sans-newa.metainfo.xml

%package -n fonts-ttf-google-noto-sans-nko
Summary:	Sans NKo font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-nko = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-nko-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-nko
%common_desc
Noto font Sans NKo.

%files -n fonts-ttf-google-noto-sans-nko
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansNKo-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-nko.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-nko.conf
%{_datadir}/appdata/%{_fontname}-sans-nko.metainfo.xml

%package -n fonts-ttf-google-noto-sans-ogham
Summary:	Sans Ogham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ogham = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-ogham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ogham
%common_desc
Noto font Sans Ogham.

%files -n fonts-ttf-google-noto-sans-ogham
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOgham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ogham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ogham.conf
%{_datadir}/appdata/%{_fontname}-sans-ogham.metainfo.xml

%package -n fonts-ttf-google-noto-sans-ol-chiki
Summary:	Sans Ol Chiki font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ol-chiki = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-ol-chiki-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ol-chiki
%common_desc
Noto font Sans Ol Chiki.

%files -n fonts-ttf-google-noto-sans-ol-chiki
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOlChiki-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ol-chiki.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ol-chiki.conf
%{_datadir}/appdata/%{_fontname}-sans-ol-chiki.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-hungarian
Summary:	Sans Old Hungarian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-hungarian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-hungarian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-hungarian
%common_desc
Noto font Sans Old Hungarian.

%files -n fonts-ttf-google-noto-sans-old-hungarian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldHungarian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-hungarian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-hungarian.conf
%{_datadir}/appdata/%{_fontname}-sans-old-hungarian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-italic
Summary:	Sans Old Italic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-italic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-italic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-italic
%common_desc
Noto font Sans Old Italic.

%files -n fonts-ttf-google-noto-sans-old-italic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldItalic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-italic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-italic.conf
%{_datadir}/appdata/%{_fontname}-sans-old-italic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-north-arabian
Summary:	Sans Old North Arabian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-north-arabian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-north-arabian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-north-arabian
%common_desc
Noto font Sans Old North Arabian.

%files -n fonts-ttf-google-noto-sans-old-north-arabian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldNorthArabian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-north-arabian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-north-arabian.conf
%{_datadir}/appdata/%{_fontname}-sans-old-north-arabian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-permic
Summary:	Sans Old Permic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-permic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-permic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-permic
%common_desc
Noto font Sans Old Permic.

%files -n fonts-ttf-google-noto-sans-old-permic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldPermic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-permic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-permic.conf
%{_datadir}/appdata/%{_fontname}-sans-old-permic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-persian
Summary:	Sans Old Persian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-persian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-persian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-persian
%common_desc
Noto font Sans Old Persian.

%files -n fonts-ttf-google-noto-sans-old-persian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldPersian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-persian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-persian.conf
%{_datadir}/appdata/%{_fontname}-sans-old-persian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-south-arabian
Summary:	Sans Old South Arabian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-south-arabian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-south-arabian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-south-arabian
%common_desc
Noto font Sans Old South Arabian.

%files -n fonts-ttf-google-noto-sans-old-south-arabian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldSouthArabian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-south-arabian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-south-arabian.conf
%{_datadir}/appdata/%{_fontname}-sans-old-south-arabian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-old-turkic
Summary:	Sans Old Turkic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-old-turkic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-old-turkic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-old-turkic
%common_desc
Noto font Sans Old Turkic.

%files -n fonts-ttf-google-noto-sans-old-turkic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOldTurkic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-old-turkic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-old-turkic.conf
%{_datadir}/appdata/%{_fontname}-sans-old-turkic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-osage
Summary:	Sans Osage font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-osage = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-osage-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-osage
%common_desc
Noto font Sans Osage.

%files -n fonts-ttf-google-noto-sans-osage
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOsage-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-osage.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-osage.conf
%{_datadir}/appdata/%{_fontname}-sans-osage.metainfo.xml

%package -n fonts-ttf-google-noto-sans-osmanya
Summary:	Sans Osmanya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-osmanya = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-osmanya-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-osmanya
%common_desc
Noto font Sans Osmanya.

%files -n fonts-ttf-google-noto-sans-osmanya
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOsmanya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-osmanya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-osmanya.conf
%{_datadir}/appdata/%{_fontname}-sans-osmanya.metainfo.xml

%package -n fonts-ttf-google-noto-sans-pahawh-hmong
Summary:	Sans Pahawh Hmong font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-pahawh-hmong = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-pahawh-hmong-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-pahawh-hmong
%common_desc
Noto font Sans Pahawh Hmong.

%files -n fonts-ttf-google-noto-sans-pahawh-hmong
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPahawhHmong-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-pahawh-hmong.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-pahawh-hmong.conf
%{_datadir}/appdata/%{_fontname}-sans-pahawh-hmong.metainfo.xml

%package -n fonts-ttf-google-noto-sans-palmyrene
Summary:	Sans Palmyrene font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-palmyrene = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-palmyrene-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-palmyrene
%common_desc
Noto font Sans Palmyrene.

%files -n fonts-ttf-google-noto-sans-palmyrene
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPalmyrene-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-palmyrene.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-palmyrene.conf
%{_datadir}/appdata/%{_fontname}-sans-palmyrene.metainfo.xml

%package -n fonts-ttf-google-noto-sans-pau-cin-hau
Summary:	Sans Pau Cin Hau font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-pau-cin-hau = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-pau-cin-hau-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-pau-cin-hau
%common_desc
Noto font Sans Pau Cin Hau.

%files -n fonts-ttf-google-noto-sans-pau-cin-hau
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPauCinHau-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-pau-cin-hau.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-pau-cin-hau.conf
%{_datadir}/appdata/%{_fontname}-sans-pau-cin-hau.metainfo.xml

%package -n fonts-ttf-google-noto-sans-phags-pa
Summary:	Sans Phags Pa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-phags-pa = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-phags-pa-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-phags-pa
%common_desc
Noto font Sans Phags Pa.

%files -n fonts-ttf-google-noto-sans-phags-pa
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPhagsPa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phags-pa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phags-pa.conf
%{_datadir}/appdata/%{_fontname}-sans-phags-pa.metainfo.xml

%package -n fonts-ttf-google-noto-sans-phoenician
Summary:	Sans Phoenician font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-phoenician = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-phoenician-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-phoenician
%common_desc
Noto font Sans Phoenician.

%files -n fonts-ttf-google-noto-sans-phoenician
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPhoenician-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-phoenician.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-phoenician.conf
%{_datadir}/appdata/%{_fontname}-sans-phoenician.metainfo.xml

%package -n fonts-ttf-google-noto-sans-psalter-pahlavi
Summary:	Sans Psalter Pahlavi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-psalter-pahlavi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-psalter-pahlavi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-psalter-pahlavi
%common_desc
Noto font Sans Psalter Pahlavi.

%files -n fonts-ttf-google-noto-sans-psalter-pahlavi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansPsalterPahlavi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-psalter-pahlavi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-psalter-pahlavi.conf
%{_datadir}/appdata/%{_fontname}-sans-psalter-pahlavi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-rejang
Summary:	Sans Rejang font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-rejang = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-rejang-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-rejang
%common_desc
Noto font Sans Rejang.

%files -n fonts-ttf-google-noto-sans-rejang
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansRejang-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-rejang.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-rejang.conf
%{_datadir}/appdata/%{_fontname}-sans-rejang.metainfo.xml

%package -n fonts-ttf-google-noto-sans-runic
Summary:	Sans Runic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-runic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-runic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-runic
%common_desc
Noto font Sans Runic.

%files -n fonts-ttf-google-noto-sans-runic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansRunic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-runic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-runic.conf
%{_datadir}/appdata/%{_fontname}-sans-runic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-samaritan
Summary:	Sans Samaritan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-samaritan = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-samaritan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-samaritan
%common_desc
Noto font Sans Samaritan.

%files -n fonts-ttf-google-noto-sans-samaritan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSamaritan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-samaritan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-samaritan.conf
%{_datadir}/appdata/%{_fontname}-sans-samaritan.metainfo.xml

%package -n fonts-ttf-google-noto-sans-saurashtra
Summary:	Sans Saurashtra font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-saurashtra = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-saurashtra-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-saurashtra
%common_desc
Noto font Sans Saurashtra.

%files -n fonts-ttf-google-noto-sans-saurashtra
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSaurashtra-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-saurashtra.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-saurashtra.conf
%{_datadir}/appdata/%{_fontname}-sans-saurashtra.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sharada
Summary:	Sans Sharada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sharada = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sharada-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sharada
%common_desc
Noto font Sans Sharada.

%files -n fonts-ttf-google-noto-sans-sharada
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSharada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sharada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sharada.conf
%{_datadir}/appdata/%{_fontname}-sans-sharada.metainfo.xml

%package -n fonts-ttf-google-noto-sans-shavian
Summary:	Sans Shavian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-shavian = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-shavian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-shavian
%common_desc
Noto font Sans Shavian.

%files -n fonts-ttf-google-noto-sans-shavian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansShavian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-shavian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-shavian.conf
%{_datadir}/appdata/%{_fontname}-sans-shavian.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sinhala
Summary:	Sans Sinhala font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sinhala = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sinhala-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sinhala
%common_desc
Noto font Sans Sinhala.

%files -n fonts-ttf-google-noto-sans-sinhala
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSinhala-*.*tf
%{_fontconfig_templatedir}/%{hprio}-%{fontconf}-sans-sinhala.conf
%config(noreplace) %{_fontconfig_confdir}/%{hprio}-%{fontconf}-sans-sinhala.conf
%{_datadir}/appdata/%{_fontname}-sans-sinhala.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sinhala-ui
Summary:	Sans Sinhala UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sinhala-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sinhala-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sinhala-ui
%common_desc
Noto font Sans Sinhala UI.

%files -n fonts-ttf-google-noto-sans-sinhala-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSinhalaUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-sinhala-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-sinhala-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-sinhala-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sora-sompeng
Summary:	Sans Sora Sompeng font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sora-sompeng = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sora-sompeng-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sora-sompeng
%common_desc
Noto font Sans Sora Sompeng.

%files -n fonts-ttf-google-noto-sans-sora-sompeng
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSoraSompeng-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sora-sompeng.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sora-sompeng.conf
%{_datadir}/appdata/%{_fontname}-sans-sora-sompeng.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sundanese
Summary:	Sans Sundanese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-sundanese = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sundanese-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sundanese
%common_desc
Noto font Sans Sundanese.

%files -n fonts-ttf-google-noto-sans-sundanese
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSundanese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-sundanese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-sundanese.conf
%{_datadir}/appdata/%{_fontname}-sans-sundanese.metainfo.xml

%package -n fonts-ttf-google-noto-sans-syloti-nagri
Summary:	Sans Syloti Nagri font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syloti-nagri = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-syloti-nagri-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syloti-nagri
%common_desc
Noto font Sans Syloti Nagri.

%files -n fonts-ttf-google-noto-sans-syloti-nagri
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSylotiNagri-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syloti-nagri.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syloti-nagri.conf
%{_datadir}/appdata/%{_fontname}-sans-syloti-nagri.metainfo.xml

%package -n fonts-ttf-google-noto-sans-symbols
Summary:	Sans Symbols font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-symbols = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-symbols-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-symbols
%common_desc
Noto font Sans Symbols.

%files -n fonts-ttf-google-noto-sans-symbols
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSymbols-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-symbols.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-symbols.conf
%{_datadir}/appdata/%{_fontname}-sans-symbols.metainfo.xml

%package -n fonts-ttf-google-noto-sans-symbols2
Summary:	Sans Symbols2 font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-symbols2 = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-symbols2-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-symbols2
%common_desc
Noto font Sans Symbols2.

%files -n fonts-ttf-google-noto-sans-symbols2
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSymbols2-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-symbols2.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-symbols2.conf
%{_datadir}/appdata/%{_fontname}-sans-symbols2.metainfo.xml

%package -n fonts-ttf-google-noto-sans-syriac
Summary:	Sans Syriac font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-syriac-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac
%common_desc
Noto font Sans Syriac.

%files -n fonts-ttf-google-noto-sans-syriac
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSyriac-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac.conf
%{_datadir}/appdata/%{_fontname}-sans-syriac.metainfo.xml

%package -n fonts-ttf-google-noto-sans-syriac-eastern
Summary:	Sans Syriac Eastern font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-eastern = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-syriac-eastern-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-eastern
%common_desc
Noto font Sans Syriac Eastern.

%files -n fonts-ttf-google-noto-sans-syriac-eastern
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSyriacEastern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-eastern.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-eastern.conf
%{_datadir}/appdata/%{_fontname}-sans-syriac-eastern.metainfo.xml

%package -n fonts-ttf-google-noto-sans-syriac-estrangela
Summary:	Sans Syriac Estrangela font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-estrangela = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-syriac-estrangela-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-estrangela
%common_desc
Noto font Sans Syriac Estrangela.

%files -n fonts-ttf-google-noto-sans-syriac-estrangela
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSyriacEstrangela-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-estrangela.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-estrangela.conf
%{_datadir}/appdata/%{_fontname}-sans-syriac-estrangela.metainfo.xml

%package -n fonts-ttf-google-noto-sans-syriac-western
Summary:	Sans Syriac Western font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-syriac-western = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-syriac-western-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-syriac-western
%common_desc
Noto font Sans Syriac Western.

%files -n fonts-ttf-google-noto-sans-syriac-western
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansSyriacWestern-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-syriac-western.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-syriac-western.conf
%{_datadir}/appdata/%{_fontname}-sans-syriac-western.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tagalog
Summary:	Sans Tagalog font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tagalog = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tagalog-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tagalog
%common_desc
Noto font Sans Tagalog.

%files -n fonts-ttf-google-noto-sans-tagalog
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTagalog-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagalog.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagalog.conf
%{_datadir}/appdata/%{_fontname}-sans-tagalog.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tagbanwa
Summary:	Sans Tagbanwa font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tagbanwa = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tagbanwa-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tagbanwa
%common_desc
Noto font Sans Tagbanwa.

%files -n fonts-ttf-google-noto-sans-tagbanwa
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTagbanwa-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tagbanwa.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tagbanwa.conf
%{_datadir}/appdata/%{_fontname}-sans-tagbanwa.metainfo.xml

%package -n fonts-ttf-google-noto-sans-takri
Summary:	Sans Takri font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-takri = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-takri-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-takri
%common_desc
Noto font Sans Takri.

%files -n fonts-ttf-google-noto-sans-takri
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTakri-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-takri.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-takri.conf
%{_datadir}/appdata/%{_fontname}-sans-takri.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tai-le
Summary:	Sans Tai Le font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-le = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tai-le-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-le
%common_desc
Noto font Sans Tai Le.

%files -n fonts-ttf-google-noto-sans-tai-le
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTaiLe-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-le.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-le.conf
%{_datadir}/appdata/%{_fontname}-sans-tai-le.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tai-tham
Summary:	Sans Tai Tham font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-tham = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tai-tham-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-tham
%common_desc
Noto font Sans Tai Tham.

%files -n fonts-ttf-google-noto-sans-tai-tham
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTaiTham-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-tham.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-tham.conf
%{_datadir}/appdata/%{_fontname}-sans-tai-tham.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tai-viet
Summary:	Sans Tai Viet font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tai-viet = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tai-viet-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tai-viet
%common_desc
Noto font Sans Tai Viet.

%files -n fonts-ttf-google-noto-sans-tai-viet
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTaiViet-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tai-viet.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tai-viet.conf
%{_datadir}/appdata/%{_fontname}-sans-tai-viet.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tamil
Summary:	Sans Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tamil = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tamil-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil
%common_desc
Noto font Sans Tamil.

%files -n fonts-ttf-google-noto-sans-tamil
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil.conf
%{_datadir}/appdata/%{_fontname}-sans-tamil.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tamil-ui
Summary:	Sans Tamil UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tamil-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tamil-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil-ui
%common_desc
Noto font Sans Tamil UI.

%files -n fonts-ttf-google-noto-sans-tamil-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTamilUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-tamil-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-tamil-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-tamil-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-telugu
Summary:	Sans Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-telugu = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-telugu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-telugu
%common_desc
Noto font Sans Telugu.

%files -n fonts-ttf-google-noto-sans-telugu
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTelugu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-telugu.conf
%{_datadir}/appdata/%{_fontname}-sans-telugu.metainfo.xml

%package -n fonts-ttf-google-noto-sans-telugu-ui
Summary:	Sans Telugu UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-telugu-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-telugu-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-telugu-ui
%common_desc
Noto font Sans Telugu UI.

%files -n fonts-ttf-google-noto-sans-telugu-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTeluguUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-telugu-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-telugu-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-telugu-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thaana
Summary:	Sans Thaana font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thaana = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thaana-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thaana
%common_desc
Noto font Sans Thaana.

%files -n fonts-ttf-google-noto-sans-thaana
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansThaana-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thaana.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thaana.conf
%{_datadir}/appdata/%{_fontname}-sans-thaana.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thai
Summary:	Sans Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thai = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai
%common_desc
Noto font Sans Thai.

%files -n fonts-ttf-google-noto-sans-thai
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai.conf
%{_datadir}/appdata/%{_fontname}-sans-thai.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thai-ui
Summary:	Sans Thai UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thai-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thai-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai-ui
%common_desc
Noto font Sans Thai UI.

%files -n fonts-ttf-google-noto-sans-thai-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansThaiUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-thai-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-thai-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-thai-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tifinagh
Summary:	Sans Tifinagh font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tifinagh = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tifinagh-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tifinagh
%common_desc
Noto font Sans Tifinagh.

%files -n fonts-ttf-google-noto-sans-tifinagh
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTifinagh-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tifinagh.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tifinagh.conf
%{_datadir}/appdata/%{_fontname}-sans-tifinagh.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tirhuta
Summary:	Sans Tirhuta font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tirhuta = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tirhuta-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tirhuta
%common_desc
Noto font Sans Tirhuta.

%files -n fonts-ttf-google-noto-sans-tirhuta
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTirhuta-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tirhuta.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tirhuta.conf
%{_datadir}/appdata/%{_fontname}-sans-tirhuta.metainfo.xml

%package -n fonts-ttf-google-noto-sans-ugaritic
Summary:	Sans Ugaritic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-ugaritic = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-ugaritic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ugaritic
%common_desc
Noto font Sans Ugaritic.

%files -n fonts-ttf-google-noto-sans-ugaritic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansUgaritic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ugaritic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ugaritic.conf
%{_datadir}/appdata/%{_fontname}-sans-ugaritic.metainfo.xml

%package -n fonts-ttf-google-noto-sans-vai
Summary:	Sans Vai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-vai = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-vai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-vai
%common_desc
Noto font Sans Vai.

%files -n fonts-ttf-google-noto-sans-vai
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansVai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-vai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-vai.conf
%{_datadir}/appdata/%{_fontname}-sans-vai.metainfo.xml

%package -n fonts-ttf-google-noto-sans-warang-citi
Summary:	Sans Warang Citi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-warang-citi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-warang-citi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-warang-citi
%common_desc
Noto font Sans Warang Citi.

%files -n fonts-ttf-google-noto-sans-warang-citi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansWarangCiti-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-warang-citi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-warang-citi.conf
%{_datadir}/appdata/%{_fontname}-sans-warang-citi.metainfo.xml

%package -n fonts-ttf-google-noto-sans-yi
Summary:	Sans Yi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-yi = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-yi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-yi
%common_desc
Noto font Sans Yi.

%files -n fonts-ttf-google-noto-sans-yi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansYi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-yi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-yi.conf
%{_datadir}/appdata/%{_fontname}-sans-yi.metainfo.xml

%package -n fonts-ttf-google-noto-serif
Summary:	Serif font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif
%common_desc
Noto font Serif.

%files -n fonts-ttf-google-noto-serif
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerif-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif.conf
%{_datadir}/appdata/%{_fontname}-serif.metainfo.xml

%package -n fonts-ttf-google-noto-serif-ahom
Summary:	Serif Ahom font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-ahom = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-ahom-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-ahom
%common_desc
Noto font Serif Ahom.

%files -n fonts-ttf-google-noto-serif-ahom
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifAhom-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-ahom.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-ahom.conf
%{_datadir}/appdata/%{_fontname}-serif-ahom.metainfo.xml

%package -n fonts-ttf-google-noto-serif-armenian
Summary:	Serif Armenian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-armenian = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-armenian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-armenian
%common_desc
Noto font Serif Armenian.

%files -n fonts-ttf-google-noto-serif-armenian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifArmenian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-armenian.conf
%{_datadir}/appdata/%{_fontname}-serif-armenian.metainfo.xml

%package -n fonts-ttf-google-noto-serif-balinese
Summary:	Serif Balinese font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-balinese = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-balinese-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-sans-balinese < %EVR

%description -n fonts-ttf-google-noto-serif-balinese
%common_desc
Noto font Serif Balinese.

%files -n fonts-ttf-google-noto-serif-balinese
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifBalinese-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-balinese.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-balinese.conf
%{_datadir}/appdata/%{_fontname}-serif-balinese.metainfo.xml

%package -n fonts-ttf-google-noto-serif-display
Summary:	Serif Display font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-display = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-display-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-display
%common_desc
Noto font Serif Display.

%files -n fonts-ttf-google-noto-serif-display
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifDisplay-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-serif-display.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-serif-display.conf
%{_datadir}/appdata/%{_fontname}-serif-display.metainfo.xml

%package -n fonts-ttf-google-noto-serif-ethiopic
Summary:	Serif Ethiopic font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-ethiopic = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-ethiopic-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-ethiopic
%common_desc
Noto font Serif Ethiopic.

%files -n fonts-ttf-google-noto-serif-ethiopic
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifEthiopic-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-ethiopic.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-ethiopic.conf
%{_datadir}/appdata/%{_fontname}-serif-ethiopic.metainfo.xml

%package -n fonts-ttf-google-noto-serif-georgian
Summary:	Serif Georgian font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-georgian = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-georgian-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-georgian
%common_desc
Noto font Serif Georgian.

%files -n fonts-ttf-google-noto-serif-georgian
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifGeorgian-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-georgian.conf
%{_datadir}/appdata/%{_fontname}-serif-georgian.metainfo.xml

%package -n fonts-ttf-google-noto-serif-hebrew
Summary:	Serif Hebrew font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-hebrew = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-hebrew-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-hebrew
%common_desc
Noto font Serif Hebrew.

%files -n fonts-ttf-google-noto-serif-hebrew
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifHebrew-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-hebrew.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-hebrew.conf
%{_datadir}/appdata/%{_fontname}-serif-hebrew.metainfo.xml

%package -n fonts-ttf-google-noto-serif-khmer
Summary:	Serif Khmer font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-khmer = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-khmer-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-khmer
%common_desc
Noto font Serif Khmer.

%files -n fonts-ttf-google-noto-serif-khmer
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifKhmer-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-khmer.conf
%{_datadir}/appdata/%{_fontname}-serif-khmer.metainfo.xml

%package -n fonts-ttf-google-noto-serif-lao
Summary:	Serif Lao font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-lao = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-lao-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-lao
%common_desc
Noto font Serif Lao.

%files -n fonts-ttf-google-noto-serif-lao
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifLao-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-lao.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-lao.conf
%{_datadir}/appdata/%{_fontname}-serif-lao.metainfo.xml

%package -n fonts-ttf-google-noto-serif-myanmar
Summary:	Serif Myanmar font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-myanmar = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-myanmar-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-myanmar
%common_desc
Noto font Serif Myanmar.

%files -n fonts-ttf-google-noto-serif-myanmar
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifMyanmar-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-myanmar.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-myanmar.conf
%{_datadir}/appdata/%{_fontname}-serif-myanmar.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tamil-slanted
Summary:	Serif Tamil Slanted font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-tamil-slanted = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tamil-slanted-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tamil-slanted
%common_desc
Noto font Serif Tamil Slanted.

%files -n fonts-ttf-google-noto-serif-tamil-slanted
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifTamilSlanted-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil-slanted.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil-slanted.conf
%{_datadir}/appdata/%{_fontname}-serif-tamil-slanted.metainfo.xml

%package -n fonts-ttf-google-noto-serif-thai
Summary:	Serif Thai font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-thai = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-thai-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-thai
%common_desc
Noto font Serif Thai.

%files -n fonts-ttf-google-noto-serif-thai
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifThai-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-thai.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-thai.conf
%{_datadir}/appdata/%{_fontname}-serif-thai.metainfo.xml

%package -n fonts-ttf-google-noto-sans-oriya
Summary:	Sans Oriya font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-oriya = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-oriya-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-oriya
%common_desc
Noto font Sans Oriya.

%files -n fonts-ttf-google-noto-sans-oriya
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOriya-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-oriya.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-oriya.conf
%{_datadir}/appdata/%{_fontname}-sans-oriya.metainfo.xml

%package -n fonts-ttf-google-noto-sans-oriya-ui
Summary:	Sans Oriya UI font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-oriya-ui = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-oriya-ui-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-oriya-ui
%common_desc
Noto font Sans Oriya UI.

%files -n fonts-ttf-google-noto-sans-oriya-ui
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansOriyaUI-*.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-oriya-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-oriya-ui.conf
%{_datadir}/appdata/%{_fontname}-sans-oriya-ui.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tibetan
Summary:	Sans Tibetan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-tibetan = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tibetan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tibetan
%common_desc
Noto font Sans Tibetan.

%files -n fonts-ttf-google-noto-sans-tibetan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansTibetan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tibetan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tibetan.conf
%{_datadir}/appdata/%{_fontname}-sans-tibetan.metainfo.xml

%package -n fonts-ttf-google-noto-nastaliq-urdu
Summary:	Nastaliq Urdu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-nastaliq-urdu = 20161022-alt1_4
Obsoletes:	%{_fontname}-nastaliq-urdu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-nastaliq-urdu
%common_desc
Noto font Nastaliq Urdu.

%files -n fonts-ttf-google-noto-nastaliq-urdu
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoNastaliqUrdu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-nastaliq-urdu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-nastaliq-urdu.conf
%{_datadir}/appdata/%{_fontname}-nastaliq-urdu.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mono
Summary:	Sans Mono font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-mono = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mono-fonts = 20161022-alt1_4
Obsoletes:	fonts-ttf-%{_fontname}-mono < %EVR

%description -n fonts-ttf-google-noto-sans-mono
%common_desc
Noto font Sans Mono.

%files -n fonts-ttf-google-noto-sans-mono
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSansMono-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono.conf
%{_datadir}/appdata/%{_fontname}-sans-mono.metainfo.xml

%package -n fonts-ttf-google-noto-serif-bengali
Summary:	Serif Bengali font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-bengali = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-bengali-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-bengali
%common_desc
Noto font Serif Bengali.

%files -n fonts-ttf-google-noto-serif-bengali
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifBengali-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-bengali.conf
%{_datadir}/appdata/%{_fontname}-serif-bengali.metainfo.xml

%package -n fonts-ttf-google-noto-serif-devanagari
Summary:	Serif Devanagari font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-devanagari = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-devanagari-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-devanagari
%common_desc
Noto font Serif Devanagari.

%files -n fonts-ttf-google-noto-serif-devanagari
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifDevanagari-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-devanagari.conf
%{_datadir}/appdata/%{_fontname}-serif-devanagari.metainfo.xml

%package -n fonts-ttf-google-noto-serif-gujarati
Summary:	Serif Gujarati font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-gujarati = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-gujarati-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-gujarati
%common_desc
Noto font Serif Gujarati.

%files -n fonts-ttf-google-noto-serif-gujarati
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifGujarati-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gujarati.conf
%{_datadir}/appdata/%{_fontname}-serif-gujarati.metainfo.xml

%package -n fonts-ttf-google-noto-serif-gurmukhi
Summary:	Serif Gurmukhi font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-gurmukhi = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-gurmukhi-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-gurmukhi
%common_desc
Noto font Serif Gurmukhi.

%files -n fonts-ttf-google-noto-serif-gurmukhi
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifGurmukhi-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gurmukhi.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gurmukhi.conf
%{_datadir}/appdata/%{_fontname}-serif-gurmukhi.metainfo.xml

%package -n fonts-ttf-google-noto-serif-kannada
Summary:	Serif Kannada font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-kannada = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-kannada-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-kannada
%common_desc
Noto font Serif Kannada.

%files -n fonts-ttf-google-noto-serif-kannada
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifKannada-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-kannada.conf
%{_datadir}/appdata/%{_fontname}-serif-kannada.metainfo.xml

%package -n fonts-ttf-google-noto-serif-malayalam
Summary:	Serif Malayalam font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-malayalam = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-malayalam-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-malayalam
%common_desc
Noto font Serif Malayalam.

%files -n fonts-ttf-google-noto-serif-malayalam
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifMalayalam-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-malayalam.conf
%{_datadir}/appdata/%{_fontname}-serif-malayalam.metainfo.xml

%package -n fonts-ttf-google-noto-serif-sinhala
Summary:	Serif Sinhala font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-sinhala = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-sinhala-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-sinhala
%common_desc
Noto font Serif Sinhala.

%files -n fonts-ttf-google-noto-serif-sinhala
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifSinhala-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-sinhala.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-sinhala.conf
%{_datadir}/appdata/%{_fontname}-serif-sinhala.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tamil
Summary:	Serif Tamil font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-tamil = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tamil-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tamil
%common_desc
Noto font Serif Tamil.

%files -n fonts-ttf-google-noto-serif-tamil
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifTamil-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil.conf
%{_datadir}/appdata/%{_fontname}-serif-tamil.metainfo.xml

%package -n fonts-ttf-google-noto-serif-telugu
Summary:	Serif Telugu font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-telugu = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-telugu-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-telugu
%common_desc
Noto font Serif Telugu.

%files -n fonts-ttf-google-noto-serif-telugu
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifTelugu-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-telugu.conf
%{_datadir}/appdata/%{_fontname}-serif-telugu.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tibetan
Summary:	Serif Tibetan font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-serif-tibetan = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tibetan-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tibetan
%common_desc
Noto font Serif Tibetan.

%files -n fonts-ttf-google-noto-serif-tibetan
%dir %_ttffontsdir/%_fontname
%_ttffontsdir/%_fontname/NotoSerifTibetan-*.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tibetan.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tibetan.conf
%{_datadir}/appdata/%{_fontname}-serif-tibetan.metainfo.xml

%package -n fonts-ttf-google-noto-sans-vf
Summary:	Sans variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-vf
%common_desc
Noto font Sans.

%files -n fonts-ttf-google-noto-sans-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSans-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-arabic-vf
Summary:	Sans Arabic variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-arabic-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-arabic-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-arabic-vf
%common_desc
Noto font Sans Arabic.

%files -n fonts-ttf-google-noto-sans-arabic-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansArabic-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-arabic-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-arabic-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-arabic-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-arabic-ui-vf
Summary:	Sans Arabic UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-arabic-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-arabic-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-arabic-ui-vf
%common_desc
Noto font Sans Arabic UI.

%files -n fonts-ttf-google-noto-sans-arabic-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansArabicUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-arabic-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-arabic-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-arabic-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-armenian-vf
Summary:	Sans Armenian variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-armenian-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-armenian-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-armenian-vf
%common_desc
Noto font Sans Armenian.

%files -n fonts-ttf-google-noto-sans-armenian-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansArmenian-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-armenian-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-armenian-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-armenian-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bengali-vf
Summary:	Sans Bengali variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-bengali-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bengali-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali-vf
%common_desc
Noto font Sans Bengali.

%files -n fonts-ttf-google-noto-sans-bengali-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansBengali-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-bengali-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-bengali-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-bengali-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-bengali-ui-vf
Summary:	Sans Bengali UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-bengali-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-bengali-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-bengali-ui-vf
%common_desc
Noto font Sans Bengali UI.

%files -n fonts-ttf-google-noto-sans-bengali-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansBengaliUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-bengali-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-bengali-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-bengali-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-canadian-aboriginal-vf
Summary:	Sans Canadian Aboriginal variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-canadian-aboriginal-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-canadian-aboriginal-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-canadian-aboriginal-vf
%common_desc
Noto font Sans Canadian Aboriginal.

%files -n fonts-ttf-google-noto-sans-canadian-aboriginal-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansCanadianAboriginal-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-canadian-aboriginal-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-canadian-aboriginal-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-canadian-aboriginal-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cham-vf
Summary:	Sans Cham variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-cham-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cham-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cham-vf
%common_desc
Noto font Sans Cham.

%files -n fonts-ttf-google-noto-sans-cham-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansCham-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cham-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cham-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-cham-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-cherokee-vf
Summary:	Sans Cherokee variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-cherokee-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-cherokee-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-cherokee-vf
%common_desc
Noto font Sans Cherokee.

%files -n fonts-ttf-google-noto-sans-cherokee-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansCherokee-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-cherokee-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-cherokee-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-cherokee-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-devanagari-vf
Summary:	Sans Devanagari variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-devanagari-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-devanagari-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari-vf
%common_desc
Noto font Sans Devanagari.

%files -n fonts-ttf-google-noto-sans-devanagari-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansDevanagari-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-devanagari-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-devanagari-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-devanagari-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-devanagari-ui-vf
Summary:	Sans Devanagari UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-devanagari-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-devanagari-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-devanagari-ui-vf
%common_desc
Noto font Sans Devanagari UI.

%files -n fonts-ttf-google-noto-sans-devanagari-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansDevanagariUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-devanagari-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-devanagari-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-devanagari-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-display-vf
Summary:	Sans Display variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-display-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-display-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-display-vf
%common_desc
Noto font Sans Display.

%files -n fonts-ttf-google-noto-sans-display-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansDisplay-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-display-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-display-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-display-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-ethiopic-vf
Summary:	Sans Ethiopic variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-ethiopic-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-ethiopic-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-ethiopic-vf
%common_desc
Noto font Sans Ethiopic.

%files -n fonts-ttf-google-noto-sans-ethiopic-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansEthiopic-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-ethiopic-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-ethiopic-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-ethiopic-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-georgian-vf
Summary:	Sans Georgian variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-georgian-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-georgian-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-georgian-vf
%common_desc
Noto font Sans Georgian.

%files -n fonts-ttf-google-noto-sans-georgian-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansGeorgian-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-georgian-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-georgian-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-georgian-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-hebrew-vf
Summary:	Sans Hebrew variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-hebrew-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-hebrew-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-hebrew-vf
%common_desc
Noto font Sans Hebrew.

%files -n fonts-ttf-google-noto-sans-hebrew-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansHebrew-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-hebrew-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-hebrew-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-hebrew-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kannada-vf
Summary:	Sans Kannada variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-kannada-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kannada-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada-vf
%common_desc
Noto font Sans Kannada.

%files -n fonts-ttf-google-noto-sans-kannada-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansKannada-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-kannada-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-kannada-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-kannada-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-kannada-ui-vf
Summary:	Sans Kannada UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-kannada-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-kannada-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-kannada-ui-vf
%common_desc
Noto font Sans Kannada UI.

%files -n fonts-ttf-google-noto-sans-kannada-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansKannadaUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-kannada-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-kannada-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-kannada-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khmer-vf
Summary:	Sans Khmer variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-khmer-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khmer-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer-vf
%common_desc
Noto font Sans Khmer.

%files -n fonts-ttf-google-noto-sans-khmer-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansKhmer-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-khmer-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-khmer-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-khmer-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-khmer-ui-vf
Summary:	Sans Khmer UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-khmer-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-khmer-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-khmer-ui-vf
%common_desc
Noto font Sans Khmer UI.

%files -n fonts-ttf-google-noto-sans-khmer-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansKhmerUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-khmer-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-khmer-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-khmer-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lao-vf
Summary:	Sans Lao variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-lao-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lao-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao-vf
%common_desc
Noto font Sans Lao.

%files -n fonts-ttf-google-noto-sans-lao-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansLao-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-lao-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-lao-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-lao-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-lao-ui-vf
Summary:	Sans Lao UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-lao-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-lao-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-lao-ui-vf
%common_desc
Noto font Sans Lao UI.

%files -n fonts-ttf-google-noto-sans-lao-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansLaoUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-lao-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-lao-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-lao-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-malayalam-vf
Summary:	Sans Malayalam variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-malayalam-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-malayalam-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam-vf
%common_desc
Noto font Sans Malayalam.

%files -n fonts-ttf-google-noto-sans-malayalam-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansMalayalam-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-malayalam-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-malayalam-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-malayalam-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-malayalam-ui-vf
Summary:	Sans Malayalam UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-malayalam-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-malayalam-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-malayalam-ui-vf
%common_desc
Noto font Sans Malayalam UI.

%files -n fonts-ttf-google-noto-sans-malayalam-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansMalayalamUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-malayalam-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-malayalam-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-malayalam-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-mono-vf
Summary:	Sans Mono variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-mono-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-mono-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-mono-vf
%common_desc
Noto font Sans Mono.

%files -n fonts-ttf-google-noto-sans-mono-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansMono-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-mono-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-mono-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-mono-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-myanmar-vf
Summary:	Sans Myanmar variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-myanmar-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-myanmar-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar-vf
%common_desc
Noto font Sans Myanmar.

%files -n fonts-ttf-google-noto-sans-myanmar-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansMyanmar-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-myanmar-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-myanmar-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-myanmar-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-myanmar-ui-vf
Summary:	Sans Myanmar UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-myanmar-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-myanmar-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-myanmar-ui-vf
%common_desc
Noto font Sans Myanmar UI.

%files -n fonts-ttf-google-noto-sans-myanmar-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansMyanmarUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-myanmar-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-myanmar-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-myanmar-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-sinhala-vf
Summary:	Sans Sinhala variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-sinhala-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-sinhala-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-sinhala-vf
%common_desc
Noto font Sans Sinhala.

%files -n fonts-ttf-google-noto-sans-sinhala-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansSinhala-*VF.*tf
%{_fontconfig_templatedir}/%{hprio}-%{fontconf}-sans-sinhala-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{hprio}-%{fontconf}-sans-sinhala-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-sinhala-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-symbols-vf
Summary:	Sans Symbols variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-symbols-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-symbols-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-symbols-vf
%common_desc
Noto font Sans Symbols.

%files -n fonts-ttf-google-noto-sans-symbols-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansSymbols-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-symbols-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-symbols-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-symbols-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tamil-vf
Summary:	Sans Tamil variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-tamil-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tamil-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil-vf
%common_desc
Noto font Sans Tamil.

%files -n fonts-ttf-google-noto-sans-tamil-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansTamil-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-tamil-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-tamil-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-tamil-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-tamil-ui-vf
Summary:	Sans Tamil UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-tamil-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-tamil-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-tamil-ui-vf
%common_desc
Noto font Sans Tamil UI.

%files -n fonts-ttf-google-noto-sans-tamil-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansTamilUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-tamil-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-tamil-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-tamil-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thaana-vf
Summary:	Sans Thaana variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	fonts-ttf-google-noto-sans-thaana-vf = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thaana-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thaana-vf
%common_desc
Noto font Sans Thaana.

%files -n fonts-ttf-google-noto-sans-thaana-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansThaana-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thaana-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thaana-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-thaana-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thai-vf
Summary:	Sans Thai variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-thai-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thai-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai-vf
%common_desc
Noto font Sans Thai.

%files -n fonts-ttf-google-noto-sans-thai-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansThai-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-sans-thai-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-sans-thai-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-thai-vf.metainfo.xml

%package -n fonts-ttf-google-noto-sans-thai-ui-vf
Summary:	Sans Thai UI variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-sans-thai-ui-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-sans-thai-ui-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-sans-thai-ui-vf
%common_desc
Noto font Sans Thai UI.

%files -n fonts-ttf-google-noto-sans-thai-ui-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSansThaiUI-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-sans-thai-ui-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-sans-thai-ui-vf.conf
%{_datadir}/appdata/%{_fontname}-sans-thai-ui-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-vf
Summary:	Serif variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-vf
%common_desc
Noto font Serif.

%files -n fonts-ttf-google-noto-serif-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerif-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-armenian-vf
Summary:	Serif Armenian variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-armenian-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-armenian-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-armenian-vf
%common_desc
Noto font Serif Armenian.

%files -n fonts-ttf-google-noto-serif-armenian-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifArmenian-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-armenian-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-armenian-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-armenian-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-display-vf
Summary:	Serif Display variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-display-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-display-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-display-vf
%common_desc
Noto font Serif Display.

%files -n fonts-ttf-google-noto-serif-display-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifDisplay-*VF.*tf
%{_fontconfig_templatedir}/%{lprio}-%{fontconf}-serif-display-vf.conf
%config(noreplace) %{_fontconfig_confdir}/%{lprio}-%{fontconf}-serif-display-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-display-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-ethiopic-vf
Summary:	Serif Ethiopic variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-ethiopic-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-ethiopic-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-ethiopic-vf
%common_desc
Noto font Serif Ethiopic.

%files -n fonts-ttf-google-noto-serif-ethiopic-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifEthiopic-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-ethiopic-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-ethiopic-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-ethiopic-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-georgian-vf
Summary:	Serif Georgian variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-georgian-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-georgian-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-georgian-vf
%common_desc
Noto font Serif Georgian.

%files -n fonts-ttf-google-noto-serif-georgian-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifGeorgian-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-georgian-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-georgian-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-georgian-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-gujarati-vf
Summary:	Serif Gujarati variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-gujarati-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-gujarati-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-gujarati-vf
%common_desc
Noto font Serif Gujarati.

%files -n fonts-ttf-google-noto-serif-gujarati-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifGujarati-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gujarati-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gujarati-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-gujarati-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-gurmukhi-vf
Summary:	Serif Gurmukhi variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-gurmukhi-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-gurmukhi-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-gurmukhi-vf
%common_desc
Noto font Serif Gurmukhi.

%files -n fonts-ttf-google-noto-serif-gurmukhi-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifGurmukhi-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-gurmukhi-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-gurmukhi-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-gurmukhi-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-hebrew-vf
Summary:	Serif Hebrew variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-hebrew-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-hebrew-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-hebrew-vf
%common_desc
Noto font Serif Hebrew.

%files -n fonts-ttf-google-noto-serif-hebrew-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifHebrew-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-hebrew-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-hebrew-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-hebrew-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-kannada-vf
Summary:	Serif Kannada variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-kannada-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-kannada-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-kannada-vf
%common_desc
Noto font Serif Kannada.

%files -n fonts-ttf-google-noto-serif-kannada-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifKannada-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-kannada-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-kannada-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-kannada-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-khmer-vf
Summary:	Serif Khmer variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-khmer-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-khmer-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-khmer-vf
%common_desc
Noto font Serif Khmer.

%files -n fonts-ttf-google-noto-serif-khmer-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifKhmer-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-khmer-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-khmer-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-khmer-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-lao-vf
Summary:	Serif Lao variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-lao-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-lao-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-lao-vf
%common_desc
Noto font Serif Lao.

%files -n fonts-ttf-google-noto-serif-lao-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifLao-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-lao-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-lao-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-lao-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-myanmar-vf
Summary:	Serif Myanmar variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-myanmar-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-myanmar-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-myanmar-vf
%common_desc
Noto font Serif Myanmar.

%files -n fonts-ttf-google-noto-serif-myanmar-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifMyanmar-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-myanmar-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-myanmar-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-myanmar-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-sinhala-vf
Summary:	Serif Sinhala variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-sinhala-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-sinhala-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-sinhala-vf
%common_desc
Noto font Serif Sinhala.

%files -n fonts-ttf-google-noto-serif-sinhala-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifSinhala-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-sinhala-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-sinhala-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-sinhala-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tamil-vf
Summary:	Serif Tamil variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-tamil-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tamil-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tamil-vf
%common_desc
Noto font Serif Tamil.

%files -n fonts-ttf-google-noto-serif-tamil-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifTamil-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-tamil-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tamil-slanted-vf
Summary:	Serif Tamil Slanted variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-tamil-slanted-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tamil-slanted-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tamil-slanted-vf
%common_desc
Noto font Serif Tamil Slanted.

%files -n fonts-ttf-google-noto-serif-tamil-slanted-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifTamilSlanted-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tamil-slanted-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tamil-slanted-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-tamil-slanted-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-thai-vf
Summary:	Serif Thai variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-thai-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-thai-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-thai-vf
%common_desc
Noto font Serif Thai.

%files -n fonts-ttf-google-noto-serif-thai-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifThai-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-thai-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-thai-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-thai-vf.metainfo.xml

%package -n fonts-ttf-google-noto-serif-tibetan-vf
Summary:	Serif Tibetan variable font
Group:		System/Fonts/True type
Requires:	fonts-ttf-%{_fontname}-common = %EVR
Conflicts:	%{_fontname}-serif-tibetan-vf-fonts = 20161022-alt1_4
Obsoletes:	%{_fontname}-serif-tibetan-vf-fonts = 20161022-alt1_4

%description -n fonts-ttf-google-noto-serif-tibetan-vf
%common_desc
Noto font Serif Tibetan.

%files -n fonts-ttf-google-noto-serif-tibetan-vf
%dir %_ttffontsdir/%_fontnamevf
%_ttffontsdir/%_fontnamevf/NotoSerifTibetan-*VF.*tf
%{_fontconfig_templatedir}/66-%{fontconf}-serif-tibetan-vf.conf
%config(noreplace) %{_fontconfig_confdir}/66-%{fontconf}-serif-tibetan-vf.conf
%{_datadir}/appdata/%{_fontname}-serif-tibetan-vf.metainfo.xml

%prep
%setup -q -n noto-fonts-%{commit}


%build

%install
%global fontname %{_fontname}
%global _fontdir  %_ttffontsdir/%{_fontname}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p unhinted/Noto*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p hinted/Noto*.ttf %{buildroot}%{_fontdir}
%global fontname %{_fontnamevf}
%global _fontdir  %_ttffontsdir/%{_fontnamevf}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p phaseIII_only/unhinted/variable-ttf/Noto*.ttf %{buildroot}%{_fontdir}



install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add appstream metadata
install -Dm 0644 -p %{SOURCE200} \
        %{buildroot}%{_datadir}/appdata/%{_fontname}.metainfo.xml

%define fcconfbuild(a:g:p:v)\
%define _pname %(echo %{*} | tr "A-Z " "a-z-")\
%define pname %{_pname}%{-v:-vf}\
%define fconf %{-p*}%{!-p:%{mprio}}-%{fontconf}-%{pname}.conf\
cat<<_EOL_>%{buildroot}%{_fontconfig_templatedir}/%{fconf}\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
<!DOCTYPE fontconfig SYSTEM \"fonts.dtd\">\
<fontconfig>\
  <alias>\
    <family>%{-g*}</family>\
    <prefer>\
      <family>Noto %{*}</family>\
    </prefer>\
  </alias>\
  <alias>\
    <family>Noto %{*}</family>\
    <default>\
      <family>%{-g*}</family>\
    </default>\
  </alias>\
</fontconfig>\
_EOL_

%fcconfbuild -g fantasy Music
%fcconfbuild -g sans-serif Sans Adlam
%fcconfbuild -g sans-serif Sans Adlam Unjoined
%fcconfbuild -g sans-serif Sans Anatolian Hieroglyphs
%fcconfbuild -g sans-serif Sans Arabic
%fcconfbuild -p %{lprio} -g sans-serif Sans Arabic UI
%fcconfbuild -g sans-serif Sans Avestan
%fcconfbuild -g sans-serif Sans Bassa Vah
%fcconfbuild -g sans-serif Sans Bhaiksuki
%fcconfbuild -g sans-serif Sans Brahmi
%fcconfbuild -g sans-serif Sans Carian
%fcconfbuild -g sans-serif Sans Caucasian Albanian
%fcconfbuild -g sans-serif Sans Chakma
%fcconfbuild -g sans-serif Sans Deseret
%fcconfbuild -p %{lprio} -g sans-serif Sans Display
%fcconfbuild -g sans-serif Sans Duployan
%fcconfbuild -g sans-serif Sans Egyptian Hieroglyphs
%fcconfbuild -g sans-serif Sans Elbasan
%fcconfbuild -g sans-serif Sans Glagolitic
%fcconfbuild -g sans-serif Sans Grantha
%fcconfbuild -g sans-serif Sans Hatran
%fcconfbuild -g sans-serif Sans Imperial Aramaic
%fcconfbuild -g sans-serif Sans Inscriptional Pahlavi
%fcconfbuild -g sans-serif Sans Inscriptional Parthian
%fcconfbuild -g sans-serif Sans Kaithi
%fcconfbuild -g sans-serif Sans Kayah Li
%fcconfbuild -g sans-serif Sans Kharoshthi
%fcconfbuild -g sans-serif Sans Khojki
%fcconfbuild -g sans-serif Sans Khudawadi
%fcconfbuild -g sans-serif Sans Linear A
%fcconfbuild -g sans-serif Sans Linear B
%fcconfbuild -g sans-serif Sans Lycian
%fcconfbuild -g sans-serif Sans Lydian
%fcconfbuild -g sans-serif Sans Mahajani
%fcconfbuild -g sans-serif Sans Mandaic
%fcconfbuild -g sans-serif Sans Manichaean
%fcconfbuild -g sans-serif Sans Marchen
%fcconfbuild -g sans-serif -p %{lprio} Sans Math
%fcconfbuild -g sans-serif Sans Mende Kikakui
%fcconfbuild -g sans-serif Sans Meroitic
%fcconfbuild -g sans-serif Sans Miao
%fcconfbuild -g sans-serif Sans Modi
%fcconfbuild -g monospace Sans Mono
%fcconfbuild -g sans-serif Sans Mro
%fcconfbuild -g sans-serif Sans Multani
%fcconfbuild -g sans-serif Sans Nabataean
%fcconfbuild -g sans-serif Sans Newa
%fcconfbuild -g sans-serif Sans Old Hungarian
%fcconfbuild -g sans-serif Sans Old Italic
%fcconfbuild -g sans-serif Sans Old North Arabian
%fcconfbuild -g sans-serif Sans Old Permic
%fcconfbuild -g sans-serif Sans Old Persian
%fcconfbuild -g sans-serif Sans Old South Arabian
%fcconfbuild -g sans-serif Sans Old Turkic
%fcconfbuild -g sans-serif Sans Osage
%fcconfbuild -g sans-serif Sans Osmanya
%fcconfbuild -g sans-serif Sans Pahawh Hmong
%fcconfbuild -g sans-serif Sans Palmyrene
%fcconfbuild -g sans-serif Sans Pau Cin Hau
%fcconfbuild -g sans-serif Sans Phags Pa
%fcconfbuild -g sans-serif Sans Phoenician
%fcconfbuild -g sans-serif Sans Psalter Pahlavi
%fcconfbuild -g sans-serif Sans Samaritan
%fcconfbuild -g sans-serif Sans Sharada
%fcconfbuild -p %{lprio} -g sans-serif Sans Sinhala UI
%fcconfbuild -g sans-serif Sans Sora Sompeng
%fcconfbuild -g sans-serif Sans Syloti Nagri
%fcconfbuild -g fantasy Sans Symbols
%fcconfbuild -g fantasy Sans Symbols2
%fcconfbuild -g sans-serif Sans Syriac
%fcconfbuild -g sans-serif Sans Tai Le
%fcconfbuild -g sans-serif Sans Tai Tham
%fcconfbuild -g sans-serif Sans Tai Viet
%fcconfbuild -g sans-serif Sans Takri
%fcconfbuild -g sans-serif Sans Tirhuta
%fcconfbuild -g sans-serif Sans Ugaritic
%fcconfbuild -g sans-serif Sans Warang Citi
%fcconfbuild -g sans-serif Sans Yi
%fcconfbuild -g sans-serif Sans
%fcconfbuild -g serif Serif Ahom
%fcconfbuild -p %{lprio} -g serif Serif Display
%fcconfbuild -g serif Serif Ethiopic
%fcconfbuild -g serif Serif Gurmukhi
%fcconfbuild -g serif Serif Hebrew
%fcconfbuild -g serif Serif Myanmar
%fcconfbuild -g serif Serif Sinhala
%fcconfbuild -g serif Serif Tamil Slanted
%fcconfbuild -g serif Serif Tibetan
%fcconfbuild -g serif Serif

%fcconfbuild -v -g sans-serif Sans
%fcconfbuild -v -g sans-serif Sans Arabic
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Arabic UI
%fcconfbuild -v -g sans-serif Sans Armenian
%fcconfbuild -v -g sans-serif Sans Bengali
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Bengali UI
%fcconfbuild -v -g sans-serif Sans Canadian Aboriginal
%fcconfbuild -v -g sans-serif Sans Cham
%fcconfbuild -v -g sans-serif Sans Cherokee
%fcconfbuild -v -g sans-serif Sans Devanagari
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Devanagari UI
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Display
%fcconfbuild -v -g sans-serif Sans Ethiopic
%fcconfbuild -v -g sans-serif Sans Georgian
%fcconfbuild -v -g sans-serif Sans Hebrew
%fcconfbuild -v -g sans-serif Sans Kannada
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Kannada UI
%fcconfbuild -v -g sans-serif Sans Khmer
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Khmer UI
%fcconfbuild -v -g sans-serif Sans Lao
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Lao UI
%fcconfbuild -v -g sans-serif Sans Malayalam
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Malayalam UI
%fcconfbuild -v -g monospace Sans Mono
%fcconfbuild -v -g sans-serif Sans Myanmar
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Myanmar UI
%fcconfbuild -v -g sans-serif -p %{hprio} Sans Sinhala
%fcconfbuild -v -g fantasy Sans Symbols
%fcconfbuild -v -g sans-serif Sans Tamil
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Tamil UI
%fcconfbuild -v -g sans-serif Sans Thaana
%fcconfbuild -v -g sans-serif Sans Thai
%fcconfbuild -v -g sans-serif -p %{lprio} Sans Thai UI
%fcconfbuild -v -g serif Serif
%fcconfbuild -v -g serif Serif Armenian
%fcconfbuild -v -g serif -p %{lprio} Serif Display
%fcconfbuild -v -g serif Serif Ethiopic
%fcconfbuild -v -g serif Serif Georgian
%fcconfbuild -v -g serif Serif Gujarati
%fcconfbuild -v -g serif Serif Gurmukhi
%fcconfbuild -v -g serif Serif Hebrew
%fcconfbuild -v -g serif Serif Kannada
%fcconfbuild -v -g serif Serif Khmer
%fcconfbuild -v -g serif Serif Lao
%fcconfbuild -v -g serif Serif Myanmar
%fcconfbuild -v -g serif Serif Sinhala
%fcconfbuild -v -g serif Serif Tamil
%fcconfbuild -v -g serif Serif Tamil Slanted
%fcconfbuild -v -g serif Serif Thai
%fcconfbuild -v -g serif Serif Tibetan

for f in \
        kufi-arabic music naskh-arabic naskh-arabic-ui \
        sans sans-adlam sans-adlam-unjoined sans-anatolian-hieroglyphs \
	sans-arabic sans-arabic-ui \
	sans-armenian sans-avestan sans-bamum sans-bassa-vah \
        sans-batak sans-bhaiksuki sans-bengali sans-bengali-ui sans-brahmi \
        sans-buginese sans-buhid sans-canadian-aboriginal sans-caucasian-albanian \
	sans-carian \
        sans-chakma sans-cham sans-cherokee sans-coptic sans-cuneiform \
        sans-cypriot sans-deseret sans-devanagari sans-devanagari-ui \
	sans-duployan \
        sans-egyptian-hieroglyphs sans-elbasan sans-ethiopic sans-georgian \
        sans-glagolitic sans-gothic sans-grantha sans-gujarati sans-gujarati-ui \
        sans-gurmukhi sans-gurmukhi-ui sans-hanunoo sans-hatran sans-hebrew \
        sans-imperial-aramaic sans-inscriptional-pahlavi \
        sans-inscriptional-parthian sans-javanese \
        sans-kaithi sans-kannada sans-kannada-ui sans-kayah-li \
        sans-kharoshthi sans-khmer sans-khmer-ui sans-khojki sans-khudawadi sans-lao \
        sans-lao-ui sans-lepcha sans-limbu sans-linear-a sans-linear-b sans-lisu \
        sans-lycian sans-lydian sans-mahajani sans-malayalam sans-malayalam-ui \
        sans-mandaic sans-manichaean sans-marchen sans-meetei-mayek sans-math \
	sans-mende-kikakui \
	sans-meroitic sans-miao sans-modi sans-mongolian sans-mro sans-multani \
	sans-myanmar \
        sans-myanmar-ui sans-nabataean sans-new-tai-lue sans-newa sans-nko sans-ogham \
        sans-ol-chiki sans-old-hungarian sans-old-italic sans-old-north-arabian \
	sans-old-permic sans-old-persian \
        sans-old-south-arabian sans-old-turkic sans-osage sans-osmanya \
        sans-pahawh-hmong sans-palmyrene sans-pau-cin-hau \
	sans-phags-pa sans-phoenician sans-psalter-pahlavi sans-rejang sans-runic \
        sans-samaritan sans-saurashtra sans-sharada sans-shavian sans-sinhala sans-sinhala-ui \
	sans-sora-sompeng \
        sans-sundanese sans-syloti-nagri sans-symbols sans-symbols2 sans-syriac sans-syriac-eastern \
        sans-syriac-estrangela sans-syriac-western sans-tagalog \
        sans-tagbanwa sans-takri sans-tai-le sans-tai-tham sans-tai-viet \
        sans-tamil sans-tamil-ui sans-telugu sans-telugu-ui \
        sans-thaana sans-thai sans-thai-ui sans-tifinagh sans-tirhuta \
        sans-ugaritic sans-display sans-vai sans-warang-citi sans-yi \
        serif serif-ahom serif-armenian serif-display serif-ethiopic serif-georgian \
	serif-gurmukhi \
	serif-hebrew serif-khmer serif-lao serif-myanmar serif-sinhala serif-thai \
        sans-oriya sans-oriya-ui sans-tibetan nastaliq-urdu sans-mono \
        serif-balinese serif-bengali serif-devanagari serif-gujarati serif-kannada \
        serif-malayalam serif-tamil serif-tamil-slanted serif-telugu serif-tibetan \
	sans-vf sans-arabic-vf sans-arabic-ui-vf sans-armenian-vf sans-bengali-vf \
	sans-bengali-ui-vf sans-canadian-aboriginal-vf sans-cham-vf sans-cherokee-vf \
	sans-devanagari-vf sans-devanagari-ui-vf sans-display-vf sans-ethiopic-vf \
	sans-georgian-vf sans-hebrew-vf sans-kannada-vf sans-kannada-ui-vf \
	sans-khmer-vf sans-khmer-ui-vf sans-lao-vf sans-lao-ui-vf sans-malayalam-vf \
	sans-malayalam-ui-vf sans-mono-vf sans-myanmar-vf sans-myanmar-ui-vf \
	sans-sinhala-vf sans-symbols-vf sans-tamil-vf sans-tamil-ui-vf \
	sans-thaana-vf sans-thai-vf sans-thai-ui-vf \
	serif-vf serif-armenian-vf serif-display-vf serif-ethiopic-vf serif-georgian-vf \
	serif-gujarati-vf serif-gurmukhi-vf serif-hebrew-vf serif-kannada-vf \
	serif-khmer-vf serif-lao-vf serif-myanmar-vf serif-sinhala-vf \
	serif-tamil-vf serif-tamil-slanted-vf serif-thai-vf serif-tibetan-vf \
        ; do
  fconf=$(basename -a %{_sourcedir}/*-%{fontconf}-$f.conf)
  ifconf=$(basename -a %{buildroot}%{_fontconfig_templatedir}/*-%{fontconf}-$f.conf)
  if [ "$(echo $fconf | wc -w)" -ne 1 -o "$(echo $ifconf | wc -w)" -ne 1 ]; then
     echo "Did not find unique \*-%{fontconf}-$f.conf file"
     exit 1
  fi
  if [ -f %{_sourcedir}/${fconf} ]; then
    install -m 0644 -p %{_sourcedir}/${fconf} \
          %{buildroot}%{_fontconfig_templatedir}/${fconf}
  else
    fconf=$ifconf
  fi
  ln -s %{_fontconfig_templatedir}/${fconf} \
        %{buildroot}%{_fontconfig_confdir}/${fconf}

  meta=%{_fontname}-$f.metainfo.xml
  echo '<?xml version="1.0" encoding="UTF-8"?>' > $meta
  echo '<!-- Copyright 2014 Parag Nemade <pnemade AT redhat DOT com> -->' >> $meta
  echo '<component type="font">' >> $meta
  echo "  <id>google-noto-$f</id>" >> $meta
  echo '  <metadata_license>CC-BY-3.0</metadata_license>' >> $meta
  echo '  <extends>google-noto</extends>' >> $meta
  echo '</component>' >> $meta

  install -Dm 0644 -p %{_fontname}-$f.metainfo.xml \
          %{buildroot}%{_datadir}/appdata/%{_fontname}-$f.metainfo.xml
done


%files -n fonts-ttf-google-noto-common
%doc --no-dereference LICENSE
%doc README.md FAQ.md
%{_datadir}/appdata/%{_fontname}.metainfo.xml


%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 20181223-alt1_1
- new version

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 20181130-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 20180905-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 20161022-alt2_7
- update to new release by fcimport

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

