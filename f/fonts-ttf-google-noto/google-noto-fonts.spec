%define oldname google-noto-fonts
%global fontname google-noto
%global fontconf 66-%{fontname}
%global common_desc \
Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported script. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all script available \
in Unicode.

Name:           fonts-ttf-google-noto
Version:        20130807
Release:        alt1_2
Summary:        Hinted and Unhinted open type fonts for Unicode scripts
Group:          System/Fonts/True type
License:        ASL 2.0
URL:            https://code.google.com/p/noto
Source0:        http://noto.googlecode.com/svn/trunk/packages/NotoFonts-hinted-2013-08-07.tgz
Source1:        http://noto.googlecode.com/svn/trunk/packages/NotoFonts-unhinted-2013-08-07.tgz
Source2:        %{fontconf}-sans.conf
Source3:        %{fontconf}-sans-armenian.conf
Source4:        %{fontconf}-sans-avestan.conf
Source5:        %{fontconf}-sans-bengali.conf
Source6:        %{fontconf}-sans-bengali-ui.conf
Source7:        %{fontconf}-sans-brahmi.conf
Source8:        %{fontconf}-sans-carian.conf
Source9:        %{fontconf}-sans-cherokee.conf
Source10:        %{fontconf}-sans-coptic.conf
Source11:        %{fontconf}-sans-deseret.conf
Source12:        %{fontconf}-sans-devanagari.conf
Source13:        %{fontconf}-sans-devanagari-ui.conf
Source14:        %{fontconf}-sans-egyptian-hieroglyphs.conf
Source15:        %{fontconf}-sans-ethiopic.conf
Source16:        %{fontconf}-sans-georgian.conf
Source17:        %{fontconf}-sans-glagolitic.conf
Source18:        %{fontconf}-sans-hebrew.conf
Source19:        %{fontconf}-sans-imperial-aramaic.conf
Source20:        %{fontconf}-sans-kaithi.conf
Source21:        %{fontconf}-sans-kannada.conf
Source22:        %{fontconf}-sans-kayah-li.conf
Source23:        %{fontconf}-sans-kharoshthi.conf
Source24:        %{fontconf}-sans-khmer.conf
Source25:        %{fontconf}-sans-khmer-ui.conf
Source26:        %{fontconf}-sans-lao.conf
Source27:        %{fontconf}-sans-lao-ui.conf
Source28:        %{fontconf}-sans-lisu.conf
Source29:        %{fontconf}-sans-lycian.conf
Source30:        %{fontconf}-sans-lydian.conf
Source31:        %{fontconf}-sans-malayalam.conf
Source32:        %{fontconf}-sans-malayalam-ui.conf
Source33:        %{fontconf}-sans-mandaic.conf
Source34:        %{fontconf}-sans-meeteimayek.conf
Source35:        %{fontconf}-sans-nko.conf
Source36:        %{fontconf}-sans-old-south-arabian.conf
Source37:        %{fontconf}-sans-old-turkic.conf
Source38:        %{fontconf}-sans-osmanya.conf
Source39:        %{fontconf}-sans-phoenician.conf
Source40:        %{fontconf}-sans-shavian.conf
Source41:        %{fontconf}-sans-symbols.conf
Source42:        %{fontconf}-sans-tagalog.conf
Source43:        %{fontconf}-sans-tai-tham.conf
Source44:        %{fontconf}-sans-tamil.conf
Source45:        %{fontconf}-sans-tamil-ui.conf
Source46:        %{fontconf}-sans-telugu.conf
Source47:        %{fontconf}-sans-thai.conf
Source48:        %{fontconf}-sans-thai-ui.conf
Source49:        %{fontconf}-sans-ugaritic.conf
Source50:        %{fontconf}-sans-ui.conf
Source51:        %{fontconf}-sans-vai.conf
Source52:        %{fontconf}-serif-armenian.conf
Source53:        %{fontconf}-serif.conf
Source54:        %{fontconf}-serif-georgian.conf
Source55:        %{fontconf}-serif-khmer.conf
Source56:        %{fontconf}-serif-lao.conf
Source57:        %{fontconf}-serif-thai.conf
Source58:        %{fontconf}-sans-kannada-ui.conf
Source59:        %{fontconf}-sans-telugu-ui.conf
Source60:        %{fontconf}-sans-gujarati.conf
Source61:        %{fontconf}-sans-gujarati-ui.conf
Source62:        %{fontconf}-sans-hanunno.conf
Source63:        %{fontconf}-sans-tai-viet.conf

BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Source64: import.info

%description
%common_desc


%package -n fonts-ttf-google-noto-sans
Group: System/Fonts/True type
Summary:        Free sans-serif font for Latin script

%description -n fonts-ttf-google-noto-sans
%common_desc
Hinted sans-serif fonts for Latin script.

%files -n fonts-ttf-google-noto-sans
%{_fontconfig_templatedir}/%{fontconf}-sans.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSans-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-armenian
Group: System/Fonts/True type
Summary:        Free sans-serif font for Armenian script

%description -n fonts-ttf-google-noto-sans-armenian
%common_desc
Hinted sans-serif fonts for Armenian script.

%files -n fonts-ttf-google-noto-sans-armenian
%{_fontconfig_templatedir}/%{fontconf}-sans-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-armenian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansArmenian-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-avestan
Group: System/Fonts/True type
Summary:        Free sans-serif font for Avestan script

%description -n fonts-ttf-google-noto-sans-avestan
%common_desc
Unhinted sans-serif fonts for Avestan script.

%files -n fonts-ttf-google-noto-sans-avestan
%{_fontconfig_templatedir}/%{fontconf}-sans-avestan.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-avestan.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansAvestan-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-bengali
Group: System/Fonts/True type
Summary:        Free sans-serif font for Bengali script

%description -n fonts-ttf-google-noto-sans-bengali
%common_desc
Unhinted sans-serif fonts for Bengali script.

%files -n fonts-ttf-google-noto-sans-bengali
%{_fontconfig_templatedir}/%{fontconf}-sans-bengali.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-bengali.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansBengali-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-bengali-ui
Group: System/Fonts/True type
Summary:        Free sans-serif UI font for Bengali script

%description -n fonts-ttf-google-noto-sans-bengali-ui
%common_desc
Unhinted sans-serif UI fonts for Bengali script.

%files -n fonts-ttf-google-noto-sans-bengali-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-bengali-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-bengali-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansBengaliUI-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-brahmi
Group: System/Fonts/True type
Summary:        Free sans-serif font for Brahmi script

%description -n fonts-ttf-google-noto-sans-brahmi
%common_desc
Unhinted sans-serif fonts for Brahmi script.

%files -n fonts-ttf-google-noto-sans-brahmi
%{_fontconfig_templatedir}/%{fontconf}-sans-brahmi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-brahmi.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansBrahmi-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-carian
Group: System/Fonts/True type
Summary:        Free sans-serif font for Carian script

%description -n fonts-ttf-google-noto-sans-carian
%common_desc
Unhinted sans-serif fonts for Carian script.

%files -n fonts-ttf-google-noto-sans-carian
%{_fontconfig_templatedir}/%{fontconf}-sans-carian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-carian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansCarian-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-cherokee
Group: System/Fonts/True type
Summary:        Free sans-serif font for Cherokee script

%description -n fonts-ttf-google-noto-sans-cherokee
%common_desc
Unhinted sans-serif fonts for Cherokee script.

%files -n fonts-ttf-google-noto-sans-cherokee
%{_fontconfig_templatedir}/%{fontconf}-sans-cherokee.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-cherokee.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansCherokee-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-coptic
Group: System/Fonts/True type
Summary:        Free sans-serif font for Coptic script

%description -n fonts-ttf-google-noto-sans-coptic
%common_desc
Unhinted sans-serif fonts for Coptic script.

%files -n fonts-ttf-google-noto-sans-coptic
%{_fontconfig_templatedir}/%{fontconf}-sans-coptic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-coptic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansCoptic-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-deseret
Group: System/Fonts/True type
Summary:        Free sans-serif font for Deseret script

%description -n fonts-ttf-google-noto-sans-deseret
%common_desc
Unhinted sans-serif fonts for Deseret script.

%files -n fonts-ttf-google-noto-sans-deseret
%{_fontconfig_templatedir}/%{fontconf}-sans-deseret.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-deseret.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansDeseret-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-devanagari
Group: System/Fonts/True type
Summary:        Free Devanagari script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-devanagari
%common_desc
Hinted sans-serif fonts for Devanagari script.

%files -n fonts-ttf-google-noto-sans-devanagari
%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-devanagari.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansDevanagari-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-devanagari-ui
Group: System/Fonts/True type
Summary:        Free Devanagari script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-devanagari-ui
%common_desc
Hinted sans-serif UI fonts for Devanagari script.

%files -n fonts-ttf-google-noto-sans-devanagari-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-devanagari-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansDevanagariUI-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-ethiopic
Group: System/Fonts/True type
Summary:        Free Ethiopic script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-ethiopic
%common_desc
Hinted sans-serif fonts for Ethiopic script.

%files -n fonts-ttf-google-noto-sans-ethiopic
%{_fontconfig_templatedir}/%{fontconf}-sans-ethiopic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-ethiopic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansEthiopic-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
Group: System/Fonts/True type
Summary:        Free sans-serif font for Egyptian Hieroglyphs script

%description -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%common_desc
Unhinted sans-serif fonts for Egyptian Hieroglyphs script.

%files -n fonts-ttf-google-noto-sans-egyptian-hieroglyphs
%{_fontconfig_templatedir}/%{fontconf}-sans-egyptian-hieroglyphs.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-egyptian-hieroglyphs.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansEgyptianHieroglyphs-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-georgian
Group: System/Fonts/True type
Summary:        Free Georgian script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-georgian
%common_desc
Hinted sans-serif fonts for Georgian script.

%files -n fonts-ttf-google-noto-sans-georgian
%{_fontconfig_templatedir}/%{fontconf}-sans-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-georgian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansGeorgian-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-glagolitic
Group: System/Fonts/True type
Summary:        Free sans-serif font for Glagolitic script

%description -n fonts-ttf-google-noto-sans-glagolitic
%common_desc
Unhinted sans-serif fonts for Glagolitic script.

%files -n fonts-ttf-google-noto-sans-glagolitic
%{_fontconfig_templatedir}/%{fontconf}-sans-glagolitic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-glagolitic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansGlagolitic-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-hebrew
Group: System/Fonts/True type
Summary:        Free Hebrew script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-hebrew
%common_desc
Hinted sans-serif fonts for Hebrew script.

%files -n fonts-ttf-google-noto-sans-hebrew
%{_fontconfig_templatedir}/%{fontconf}-sans-hebrew.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-hebrew.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansHebrew-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-imperial-aramaic
Group: System/Fonts/True type
Summary:        Free sans-serif font for Imperial Aramaic script

%description -n fonts-ttf-google-noto-sans-imperial-aramaic
%common_desc
Unhinted sans-serif fonts for Imperial Aramaic script.

%files -n fonts-ttf-google-noto-sans-imperial-aramaic
%{_fontconfig_templatedir}/%{fontconf}-sans-imperial-aramaic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-imperial-aramaic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansImperialAramaic-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-kaithi
Group: System/Fonts/True type
Summary:        Free sans-serif font for Kaithi script

%description -n fonts-ttf-google-noto-sans-kaithi
%common_desc
Unhinted sans-serif fonts for Kaithi script.

%files -n fonts-ttf-google-noto-sans-kaithi
%{_fontconfig_templatedir}/%{fontconf}-sans-kaithi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-kaithi.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKaithi-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-kannada
Group: System/Fonts/True type
Summary:        Free sans-serif font for Kannada script

%description -n fonts-ttf-google-noto-sans-kannada
%common_desc
Unhinted sans-serif fonts for Kannada script.

%files -n fonts-ttf-google-noto-sans-kannada
%{_fontconfig_templatedir}/%{fontconf}-sans-kannada.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-kannada.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKannada-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-kayah-li
Group: System/Fonts/True type
Summary:        Free sans-serif font for Kayah Li script

%description -n fonts-ttf-google-noto-sans-kayah-li
%common_desc
Unhinted sans-serif fonts for Kayah Li script.

%files -n fonts-ttf-google-noto-sans-kayah-li
%{_fontconfig_templatedir}/%{fontconf}-sans-kayah-li.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-kayah-li.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKayahLi-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-kharoshthi
Group: System/Fonts/True type
Summary:        Free sans-serif font for Kharoshthi script

%description -n fonts-ttf-google-noto-sans-kharoshthi
%common_desc
Unhinted sans-serif fonts for Kharoshthi script.

%files -n fonts-ttf-google-noto-sans-kharoshthi
%{_fontconfig_templatedir}/%{fontconf}-sans-kharoshthi.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-kharoshthi.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKharoshthi-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-khmer
Group: System/Fonts/True type
Summary:        Free Khmer script sans-serif font

%description -n fonts-ttf-google-noto-sans-khmer
%common_desc
Hinted sans-serif fonts for Khmer script.

%files -n fonts-ttf-google-noto-sans-khmer
%{_fontconfig_templatedir}/%{fontconf}-sans-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-khmer.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKhmer-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-khmer-ui
Group: System/Fonts/True type
Summary:        Free Khmer script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-khmer-ui
%common_desc
Hinted sans-serif UI fonts for Khmer script.

%files -n fonts-ttf-google-noto-sans-khmer-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-khmer-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-khmer-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKhmerUI-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-lao
Group: System/Fonts/True type
Summary:        Free Lao script sans-serif font

%description -n fonts-ttf-google-noto-sans-lao
%common_desc
Hinted sans-serif fonts for Lao script.

%files -n fonts-ttf-google-noto-sans-lao
%{_fontconfig_templatedir}/%{fontconf}-sans-lao.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-lao.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansLao-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-lao-ui
Group: System/Fonts/True type
Summary:        Free Lao script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-lao-ui
%common_desc
Hinted sans-serif UI fonts for Lao script.

%files -n fonts-ttf-google-noto-sans-lao-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-lao-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-lao-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansLaoUI-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-lisu
Group: System/Fonts/True type
Summary:        Free Lisu script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-lisu
%common_desc
Unhinted sans-serif UI fonts for Lisu script.

%files -n fonts-ttf-google-noto-sans-lisu
%{_fontconfig_templatedir}/%{fontconf}-sans-lisu.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-lisu.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansLisu-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-lycian
Group: System/Fonts/True type
Summary:        Free Lycian script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-lycian
%common_desc
Unhinted sans-serif UI fonts for Lycian script.

%files -n fonts-ttf-google-noto-sans-lycian
%{_fontconfig_templatedir}/%{fontconf}-sans-lycian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-lycian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansLycian-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-lydian
Group: System/Fonts/True type
Summary:        Free Lydian script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-lydian
%common_desc
Unhinted sans-serif UI fonts for Lydian script.

%files -n fonts-ttf-google-noto-sans-lydian
%{_fontconfig_templatedir}/%{fontconf}-sans-lydian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-lydian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansLydian-*.ttf
%doc LICENSE



%package -n fonts-ttf-google-noto-sans-malayalam
Group: System/Fonts/True type
Summary:        Free Malayalam script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-malayalam
%common_desc
Unhinted sans-serif fonts for Malayalam script.

%files -n fonts-ttf-google-noto-sans-malayalam
%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-malayalam.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansMalayalam*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-malayalam-ui
Group: System/Fonts/True type
Summary:        Free Malayalam script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-malayalam-ui
%common_desc
Unhinted sans-serif UI fonts for Malayalam script.

%files -n fonts-ttf-google-noto-sans-malayalam-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-malayalam-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansMalayalamUI*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-mandaic
Group: System/Fonts/True type
Summary:        Free Mandaic script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-mandaic
%common_desc
Unhinted sans-serif fonts for Mandaic script.

%files -n fonts-ttf-google-noto-sans-mandaic
%{_fontconfig_templatedir}/%{fontconf}-sans-mandaic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-mandaic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansMandaic*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-meeteimayek
Group: System/Fonts/True type
Summary:        Free Meetei Mayek script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-meeteimayek
%common_desc
Unhinted sans-serif fonts for Meetei Mayek script.

%files -n fonts-ttf-google-noto-sans-meeteimayek
%{_fontconfig_templatedir}/%{fontconf}-sans-meeteimayek.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-meeteimayek.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansMeeteiMayek*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-nko
Group: System/Fonts/True type
Summary:        Free NKo script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-nko
%common_desc
Unhinted sans-serif fonts for NKo script.

%files -n fonts-ttf-google-noto-sans-nko
%{_fontconfig_templatedir}/%{fontconf}-sans-nko.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-nko.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansNKo*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-old-south-arabian
Group: System/Fonts/True type
Summary:        Free Old South Arabian script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-old-south-arabian
%common_desc
Unhinted sans-serif fonts for Old South Arabian script.

%files -n fonts-ttf-google-noto-sans-old-south-arabian
%{_fontconfig_templatedir}/%{fontconf}-sans-old-south-arabian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-old-south-arabian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansOldSouthArabian*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-old-turkic
Group: System/Fonts/True type
Summary:        Free Old Turkic script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-old-turkic
%common_desc
Unhinted sans-serif fonts for Old Turkic script.

%files -n fonts-ttf-google-noto-sans-old-turkic
%{_fontconfig_templatedir}/%{fontconf}-sans-old-turkic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-old-turkic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansOldTurkic*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-osmanya
Group: System/Fonts/True type
Summary:        Free Osmanya script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-osmanya
%common_desc
Unhinted sans-serif fonts for Osmanya script.

%files -n fonts-ttf-google-noto-sans-osmanya
%{_fontconfig_templatedir}/%{fontconf}-sans-osmanya.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-osmanya.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansOsmanya*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-phoenician
Group: System/Fonts/True type
Summary:        Free Phoenician script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-phoenician
%common_desc
Unhinted sans-serif fonts for Phoenician script.

%files -n fonts-ttf-google-noto-sans-phoenician
%{_fontconfig_templatedir}/%{fontconf}-sans-phoenician.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-phoenician.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansPhoenician*.ttf
%doc LICENSE



%package -n fonts-ttf-google-noto-sans-shavian
Group: System/Fonts/True type
Summary:        Free Shavian script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-shavian
%common_desc
Unhinted sans-serif fonts for Shavian script.

%files -n fonts-ttf-google-noto-sans-shavian
%{_fontconfig_templatedir}/%{fontconf}-sans-shavian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-shavian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansShavian*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-symbols
Group: System/Fonts/True type
Summary:        Free Symbols script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-symbols
%common_desc
Unhinted sans-serif fonts for Symbols script.

%files -n fonts-ttf-google-noto-sans-symbols
%{_fontconfig_templatedir}/%{fontconf}-sans-symbols.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-symbols.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansSymbols*.ttf
%doc LICENSE



%package -n fonts-ttf-google-noto-sans-tagalog
Group: System/Fonts/True type
Summary:        Free tagalog script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-tagalog
%common_desc
Unhinted sans-serif fonts for tagalog script.

%files -n fonts-ttf-google-noto-sans-tagalog
%{_fontconfig_templatedir}/%{fontconf}-sans-tagalog.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-tagalog.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTagalog*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-tai-tham
Group: System/Fonts/True type
Summary:        Free Tai Tham script sans-serif fonts

%description -n fonts-ttf-google-noto-sans-tai-tham
%common_desc
Unhinted sans-serif fonts for Tai Tham script.

%files -n fonts-ttf-google-noto-sans-tai-tham
%{_fontconfig_templatedir}/%{fontconf}-sans-tai-tham.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-tai-tham.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTaiTham*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-tamil
Group: System/Fonts/True type
Summary:        Free Tamil script sans-serif font

%description -n fonts-ttf-google-noto-sans-tamil
%common_desc
Hinted sans-serif fonts for Tamil script.

%files -n fonts-ttf-google-noto-sans-tamil
%{_fontconfig_templatedir}/%{fontconf}-sans-tamil.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-tamil.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTamil-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-tamil-ui
Group: System/Fonts/True type
Summary:        Free Tamil script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-tamil-ui
%common_desc
Hinted sans-serif UI fonts for Tamil script.

%files -n fonts-ttf-google-noto-sans-tamil-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-tamil-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-tamil-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTamilUI-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-telugu
Group: System/Fonts/True type
Summary:        Free Telugu script sans-serif font

%description -n fonts-ttf-google-noto-sans-telugu
%common_desc
Unhinted sans-serif fonts for Telugu script.

%files -n fonts-ttf-google-noto-sans-telugu
%{_fontconfig_templatedir}/%{fontconf}-sans-telugu.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-telugu.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTelugu-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-thai
Group: System/Fonts/True type
Summary:        Free Thai script sans-serif font

%description -n fonts-ttf-google-noto-sans-thai
%common_desc
Hinted sans-serif fonts for Thai script.

%files -n fonts-ttf-google-noto-sans-thai
%{_fontconfig_templatedir}/%{fontconf}-sans-thai.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-thai.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansThai-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-thai-ui
Group: System/Fonts/True type
Summary:        Free Thai script sans-serif fonts for UI

%description -n fonts-ttf-google-noto-sans-thai-ui
%common_desc
Hinted sans-serif UI fonts for Thai script.

%files -n fonts-ttf-google-noto-sans-thai-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-thai-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-thai-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansThaiUI-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-ugaritic
Group: System/Fonts/True type
Summary:        Free Ugaritic script sans-serif font

%description -n fonts-ttf-google-noto-sans-ugaritic
%common_desc
Unhinted sans-serif fonts for Ugaritic script.

%files -n fonts-ttf-google-noto-sans-ugaritic
%{_fontconfig_templatedir}/%{fontconf}-sans-ugaritic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-ugaritic.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansUgaritic-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-ui
Group: System/Fonts/True type
Summary:        Free sans-serif Latin script fonts for UI

%description -n fonts-ttf-google-noto-sans-ui
%common_desc
Hinted sans-serif UI fonts for Latin script.

%files -n fonts-ttf-google-noto-sans-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansUI-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-vai
Group: System/Fonts/True type
Summary:        Free Vai script sans-serif font

%description -n fonts-ttf-google-noto-sans-vai
%common_desc
Unhinted sans-serif fonts for Vai script.

%files -n fonts-ttf-google-noto-sans-vai
%{_fontconfig_templatedir}/%{fontconf}-sans-vai.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-vai.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansVai-*.ttf
%doc LICENSE



%package -n fonts-ttf-google-noto-serif-armenian
Group: System/Fonts/True type
Summary:        Free Armenian script serif fonts

%description -n fonts-ttf-google-noto-serif-armenian
%common_desc
Hinted serif fonts for Armenian script.

%files -n fonts-ttf-google-noto-serif-armenian
%{_fontconfig_templatedir}/%{fontconf}-serif-armenian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-armenian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerifArmenian*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-serif
Group: System/Fonts/True type
Summary:        Free Latin script serif fonts

%description -n fonts-ttf-google-noto-serif
%common_desc
Hinted serif fonts for Latin script.

%files -n fonts-ttf-google-noto-serif
%{_fontconfig_templatedir}/%{fontconf}-serif.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerif-**.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-serif-georgian
Group: System/Fonts/True type
Summary:        Free Georgian script serif fonts

%description -n fonts-ttf-google-noto-serif-georgian
%common_desc
Hinted serif fonts for Georgian script.

%files -n fonts-ttf-google-noto-serif-georgian
%{_fontconfig_templatedir}/%{fontconf}-serif-georgian.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-georgian.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerifGeorgian*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-serif-khmer
Group: System/Fonts/True type
Summary:        Free Khmer script serif font

%description -n fonts-ttf-google-noto-serif-khmer
%common_desc
Hinted serif fonts for Khmer script.

%files -n fonts-ttf-google-noto-serif-khmer
%{_fontconfig_templatedir}/%{fontconf}-serif-khmer.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-khmer.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerifKhmer-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-serif-lao
Group: System/Fonts/True type
Summary:        Free Lao script serif fonts

%description -n fonts-ttf-google-noto-serif-lao
%common_desc
Hinted serif fonts for Lao script.

%files -n fonts-ttf-google-noto-serif-lao
%{_fontconfig_templatedir}/%{fontconf}-serif-lao.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-lao.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerifLao*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-serif-thai
Group: System/Fonts/True type
Summary:        Free Thai script serif fonts

%description -n fonts-ttf-google-noto-serif-thai
%common_desc
Hinted serif fonts for Thai script.

%files -n fonts-ttf-google-noto-serif-thai
%{_fontconfig_templatedir}/%{fontconf}-serif-thai.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-serif-thai.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSerifThai*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-kannada-ui
Group: System/Fonts/True type
Summary:        Free Unhinted Kannada script sans fonts

%description -n fonts-ttf-google-noto-sans-kannada-ui
%common_desc
Unhinted sanserif UI fonts for Kannada script.

%files -n fonts-ttf-google-noto-sans-kannada-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-kannada-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-kannada-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansKannadaUI*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-telugu-ui
Group: System/Fonts/True type
Summary:        Free Unhinted Telugu script sans fonts

%description -n fonts-ttf-google-noto-sans-telugu-ui
%common_desc
Unhinted sanserif UI fonts for Telugu script.

%files -n fonts-ttf-google-noto-sans-telugu-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-telugu-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-telugu-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTeluguUI*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-gujarati
Group: System/Fonts/True type
Summary:        Free Unhinted Gujarati script sans fonts

%description -n fonts-ttf-google-noto-sans-gujarati
%common_desc
Unhinted sanserif fonts for Gujarati script.

%files -n fonts-ttf-google-noto-sans-gujarati
%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-gujarati.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansGujarati-*.ttf
%doc LICENSE

%package -n fonts-ttf-google-noto-sans-gujarati-ui
Group: System/Fonts/True type
Summary:        Free Unhinted Gujarati script sans UI fonts

%description -n fonts-ttf-google-noto-sans-gujarati-ui
%common_desc
Unhinted sanserif UI fonts for Gujarati script.

%files -n fonts-ttf-google-noto-sans-gujarati-ui
%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati-ui.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-gujarati-ui.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansGujaratiUI*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-hanunno
Group: System/Fonts/True type
Summary:        Free Unhinted Hanunno script sans fonts

%description -n fonts-ttf-google-noto-sans-hanunno
%common_desc
Unhinted sanserif fonts for Hanunno script.

%files -n fonts-ttf-google-noto-sans-hanunno
%{_fontconfig_templatedir}/%{fontconf}-sans-hanunno.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-hanunno.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansHanunoo-*.ttf
%doc LICENSE


%package -n fonts-ttf-google-noto-sans-tai-viet
Group: System/Fonts/True type
Summary:        Free Unhinted Tai Viet script sans fonts

%description -n fonts-ttf-google-noto-sans-tai-viet
%common_desc
Unhinted sanserif fonts for Tai Viet script.

%files -n fonts-ttf-google-noto-sans-tai-viet
%{_fontconfig_templatedir}/%{fontconf}-sans-tai-viet.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-sans-tai-viet.conf
%{_fontbasedir}/*/%{_fontstem}/NotoSansTaiViet*.ttf
%doc LICENSE

%prep
%setup -n %{oldname}-%{version} -q -c
%setup -n %{oldname}-%{version} -c -q -a 1
cp -p fonts/individual/hinted/*.ttf .
rm -rf fonts/individual/unhinted/*Khmer* fonts/individual/unhinted/*Lao* fonts/individual/unhinted/*Hebrew*
cp -p fonts/individual/unhinted/*.ttf .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-armenian.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-avestan.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-bengali.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-bengali-ui.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-brahmi.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-carian.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-cherokee.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-coptic.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-deseret.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari-ui.conf
install -m 0644 -p %{SOURCE14} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-egyptian-hieroglyphs.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ethiopic.conf
install -m 0644 -p %{SOURCE16} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-georgian.conf
install -m 0644 -p %{SOURCE17} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-glagolitic.conf
install -m 0644 -p %{SOURCE18} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-hebrew.conf
install -m 0644 -p %{SOURCE19} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-imperial-aramaic.conf
install -m 0644 -p %{SOURCE20} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kaithi.conf
install -m 0644 -p %{SOURCE21} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kannada.conf
install -m 0644 -p %{SOURCE22} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kayah-li.conf
install -m 0644 -p %{SOURCE23} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kharoshthi.conf
install -m 0644 -p %{SOURCE24} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-khmer.conf
install -m 0644 -p %{SOURCE25} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-khmer-ui.conf
install -m 0644 -p %{SOURCE26} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lao.conf
install -m 0644 -p %{SOURCE27} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lao-ui.conf
install -m 0644 -p %{SOURCE28} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lisu.conf
install -m 0644 -p %{SOURCE29} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lycian.conf
install -m 0644 -p %{SOURCE30} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lydian.conf
install -m 0644 -p %{SOURCE31} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam.conf
install -m 0644 -p %{SOURCE32} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam-ui.conf
install -m 0644 -p %{SOURCE33} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-mandaic.conf
install -m 0644 -p %{SOURCE34} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-meeteimayek.conf
install -m 0644 -p %{SOURCE35} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-nko.conf
install -m 0644 -p %{SOURCE36} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-old-south-arabian.conf
install -m 0644 -p %{SOURCE37} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-old-turkic.conf
install -m 0644 -p %{SOURCE38} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-osmanya.conf
install -m 0644 -p %{SOURCE39} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-phoenician.conf
install -m 0644 -p %{SOURCE40} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-shavian.conf
install -m 0644 -p %{SOURCE41} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-symbols.conf
install -m 0644 -p %{SOURCE42} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tagalog.conf
install -m 0644 -p %{SOURCE43} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tai-tham.conf
install -m 0644 -p %{SOURCE44} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tamil.conf
install -m 0644 -p %{SOURCE45} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tamil-ui.conf
install -m 0644 -p %{SOURCE46} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-telugu.conf
install -m 0644 -p %{SOURCE47} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai.conf
install -m 0644 -p %{SOURCE48} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai-ui.conf
install -m 0644 -p %{SOURCE49} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ugaritic.conf
install -m 0644 -p %{SOURCE50} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ui.conf
install -m 0644 -p %{SOURCE51} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-vai.conf
install -m 0644 -p %{SOURCE52} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-armenian.conf
install -m 0644 -p %{SOURCE53} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE54} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-georgian.conf
install -m 0644 -p %{SOURCE55} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-khmer.conf
install -m 0644 -p %{SOURCE56} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-lao.conf
install -m 0644 -p %{SOURCE57} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-thai.conf
install -m 0644 -p %{SOURCE58} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kannada-ui.conf
install -m 0644 -p %{SOURCE59} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-telugu-ui.conf
install -m 0644 -p %{SOURCE60} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati.conf
install -m 0644 -p %{SOURCE61} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati-ui.conf
install -m 0644 -p %{SOURCE62} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-hanunno.conf
install -m 0644 -p %{SOURCE63} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tai-viet.conf


for fconf in %{fontconf}-sans.conf \
             %{fontconf}-sans-armenian.conf \
             %{fontconf}-sans-avestan.conf \
             %{fontconf}-sans-bengali.conf \
             %{fontconf}-sans-bengali-ui.conf \
             %{fontconf}-sans-brahmi.conf \
             %{fontconf}-sans-carian.conf \
             %{fontconf}-sans-cherokee.conf \
             %{fontconf}-sans-coptic.conf \
             %{fontconf}-sans-deseret.conf \
             %{fontconf}-sans-devanagari.conf \
             %{fontconf}-sans-devanagari-ui.conf \
             %{fontconf}-sans-egyptian-hieroglyphs.conf \
             %{fontconf}-sans-ethiopic.conf \
             %{fontconf}-sans-georgian.conf \
             %{fontconf}-sans-glagolitic.conf \
             %{fontconf}-sans-hebrew.conf \
             %{fontconf}-sans-imperial-aramaic.conf \
             %{fontconf}-sans-kaithi.conf \
             %{fontconf}-sans-kannada.conf \
             %{fontconf}-sans-kayah-li.conf \
             %{fontconf}-sans-kharoshthi.conf \
             %{fontconf}-sans-khmer.conf \
             %{fontconf}-sans-khmer-ui.conf \
             %{fontconf}-sans-lao.conf \
             %{fontconf}-sans-lao-ui.conf \
             %{fontconf}-sans-lisu.conf \
             %{fontconf}-sans-lycian.conf \
             %{fontconf}-sans-lydian.conf \
             %{fontconf}-sans-malayalam.conf \
             %{fontconf}-sans-malayalam-ui.conf \
             %{fontconf}-sans-mandaic.conf \
             %{fontconf}-sans-meeteimayek.conf \
             %{fontconf}-sans-nko.conf \
             %{fontconf}-sans-old-south-arabian.conf \
             %{fontconf}-sans-old-turkic.conf \
             %{fontconf}-sans-osmanya.conf \
             %{fontconf}-sans-phoenician.conf \
             %{fontconf}-sans-shavian.conf \
             %{fontconf}-sans-symbols.conf \
             %{fontconf}-sans-tagalog.conf \
             %{fontconf}-sans-tai-tham.conf \
             %{fontconf}-sans-tamil.conf \
             %{fontconf}-sans-tamil-ui.conf \
             %{fontconf}-sans-telugu.conf \
             %{fontconf}-sans-thai.conf \
             %{fontconf}-sans-thai-ui.conf \
             %{fontconf}-sans-ugaritic.conf \
             %{fontconf}-sans-ui.conf \
             %{fontconf}-sans-vai.conf \
             %{fontconf}-serif-armenian.conf \
             %{fontconf}-serif.conf \
             %{fontconf}-serif-georgian.conf \
             %{fontconf}-serif-khmer.conf \
             %{fontconf}-serif-lao.conf \
             %{fontconf}-sans-kannada-ui.conf \
             %{fontconf}-sans-telugu-ui.conf \
             %{fontconf}-serif-thai.conf \
             %{fontconf}-sans-gujarati.conf \
             %{fontconf}-sans-gujarati-ui.conf \
             %{fontconf}-sans-hanunno.conf \
             %{fontconf}-sans-tai-viet.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 20130807-alt1_2
- converted for ALT Linux by srpmconvert tools

