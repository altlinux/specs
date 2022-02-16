Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname catharsis-cormorant-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname catharsis-cormorant-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/CatharsisFonts/Cormorant
%global commit      83d1fa9b582005f8f913d178fdbe98094698a6c4
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/CatharsisFonts/Cormorant
%global forgesource https://github.com/CatharsisFonts/Cormorant/archive/83d1fa9b582005f8f913d178fdbe98094698a6c4/Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4.tar.gz
%global archivename Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4
%global archiveext tar.gz
%global archiveurl https://github.com/CatharsisFonts/Cormorant/archive/83d1fa9b582005f8f913d178fdbe98094698a6c4/Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4.tar.gz
%global topdir Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4
%global extractdir Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4
%global repo Cormorant
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 83d1fa9b582005f8f913d178fdbe98094698a6c4
#global shortcommit %nil
#global branch %nil
%global version 3.602
#global date %nil
%global distprefix .git83d1fa9
# FedoraForgeMeta2ALT: end generated meta

Version: 3.602
Release: alt1_4
URL:     https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family

%global foundry           Catharsis Fonts
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global common_description \
Cormorant is an original design for an extravagant display serif font family\
inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.\
While traditional Garamond cuts make for exquisite reading at book sizes, they\
appear clumpy and inelegant at larger sizes. The design goal of Cormorant was\
to distill the aesthetic essence of Garamond, unfetter it from the limitations\
of metal printing, and allow it to bloom into its natural refined form at high\
definition.\
\
Cormorant is characterized by scandalously small counters, razor-sharp serifs,\
dangerously smooth curves, and flamboyantly tall accents. While many\
implementations of Garamond at small optical sizes already exist (including the\
open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely\
populated niche of display-size counterparts that exploit the high resolution\
of contemporary screens and print media to the fullest.\
\
Cormorant is made for large sizes; the larger, the better. However, it works\
well as a text face in high-resolution environments.\
\
Cormorant is a native 21st-century typeface making ample use of OpenType\
technology. Some OpenType features are applied automatically while you type,\
subtly improving the flow of the text. This includes kerning, standard\
ligatures, and contextual alternates. Other features are intended to be\
activated manually by the user, such as discretionary ligatures, stylistic\
alternates, small capitals, and alternate figure sets.

%global fontfamily0       Cormorant
%global fontsummary0      Cormorant, a display serif font family inspired by the Garamond heritage
%global fonts0            2.*OpenType*Files/*otf
%global fontsex0          2.*OpenType*Files/CormorantSC*.otf %{fonts1} %{fonts2} %{fonts3} %{fonts4}
%global fontdescription0  \
%{common_description}\


%global fontfamily1       Cormorant Garamond
%global fontsummary1      Cormorant Garamond, a variant with more traditional shapes
%global fontpkgheader1    \
Requires: font(cormorant)\

%global fonts1            2.*OpenType*Files/CormorantGaramond*.otf
%global fontdescription1  \
%{common_description}\
\
While Cormoranta.'s quality is most evident in titling and poster usage at the\
largest sizes, its Garamond genome renders it highly legible down to text sizes\
on high-resolution devices and in print. This is particularly true about the\
a.'Cormorant Garamonda.' cuts of the typeface.\
\
Cormorant Garamond offers larger counters and subtly more traditional Garamond\
shapes for a few key characters to achieve more reading comfort.

%global fontfamily2       Cormorant Infant
%global fontsummary2      Cormorant Infant, a gentle schoolbook-style variant
%global fontpkgheader2    \
Requires: font(cormorant)\

%global fonts2            2.*OpenType*Files/CormorantInfant*.otf
%global fontdescription2  \
%{common_description}\
\
In Cormorant Infant, the letters a.'a g ya.' and their derivatives are replaced\
by gentle schoolbook-style single-storey shapes.

%global fontfamily3       Cormorant Upright
%global fontpkgname3      catharsis-cormorant-upright-fonts
%global fontsummary3      Cormorant Upright, an un-slanted cursive variant
%global fontpkgheader3    \
Requires: font(cormorant)\

%global fonts3            2.*OpenType*Files/CormorantUpright*.otf
%global fontdescription3  \
%{common_description}\
\
Cormorant Upright is an un-slanted cursive of the main Cormorant font family.

%global fontfamily4       Cormorant Unicase
%global fontsummary4      Cormorant Unicase, a small-caps variant with some lowercase letter-forms
%global fontpkgheader4    \
Requires: font(cormorant)\

%global fonts4            2.*OpenType*Files/CormorantUnicase*.otf
%global fontdescription4  \
%{common_description}\
\
Cormorant Unicase, is a small-caps variant with some lowercase letter-forms for\
an eye-catching futuristic look.

Source0:  %{forgesource}
Source10: 57-catharsis-cormorant-fonts.xml
Source11: 57-catharsis-cormorant-garamond-fonts.xml
Source12: 58-catharsis-cormorant-infant-fonts.xml
Source13: 60-catharsis-cormorant-upright-fonts.xml
Source14: 60-catharsis-cormorant-unicase-fonts.xml

Name:           fonts-otf-catharsis-cormorant
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-otf-catharsis-cormorant-garamond
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-catharsis-cormorant-garamond
%{?fontdescription1}
%package     -n fonts-otf-catharsis-cormorant-infant
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-otf-catharsis-cormorant-infant
%{?fontdescription2}
%package     -n fonts-otf-catharsis-cormorant-upright
Group: System/Fonts/True type
Summary:        %{fontsummary3}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-otf-catharsis-cormorant-upright
%{?fontdescription3}
%package     -n fonts-otf-catharsis-cormorant-unicase
Group: System/Fonts/True type
Summary:        %{fontsummary4}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader4}
%description -n fonts-otf-catharsis-cormorant-unicase
%{?fontdescription4}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-catharsis-cormorant = %EVR
Requires:  fonts-otf-catharsis-cormorant-garamond = %EVR
Requires:  fonts-otf-catharsis-cormorant-infant = %EVR
Requires:  fonts-otf-catharsis-cormorant-upright = %EVR
Requires:  fonts-otf-catharsis-cormorant-unicase = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%global fontconfngs2      %{SOURCE12}
%global fontconfngs3      %{SOURCE13}
%global fontconfngs4      %{SOURCE14}
%setup -q -n Cormorant-83d1fa9b582005f8f913d178fdbe98094698a6c4
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in '2. OpenType Files/Cormorant-Bold.otf' '2. OpenType Files/Cormorant-BoldItalic.otf' '2. OpenType Files/Cormorant-Italic.otf' '2. OpenType Files/Cormorant-Light.otf' '2. OpenType Files/Cormorant-LightItalic.otf' '2. OpenType Files/Cormorant-Medium.otf' '2. OpenType Files/Cormorant-MediumItalic.otf' '2. OpenType Files/Cormorant-Regular.otf' '2. OpenType Files/Cormorant-SemiBold.otf' '2. OpenType Files/Cormorant-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '2. OpenType Files/Cormorant-Bold.otf' '2. OpenType Files/Cormorant-BoldItalic.otf' '2. OpenType Files/Cormorant-Italic.otf' '2. OpenType Files/Cormorant-Light.otf' '2. OpenType Files/Cormorant-LightItalic.otf' '2. OpenType Files/Cormorant-Medium.otf' '2. OpenType Files/Cormorant-MediumItalic.otf' '2. OpenType Files/Cormorant-Regular.otf' '2. OpenType Files/Cormorant-SemiBold.otf' '2. OpenType Files/Cormorant-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the catharsis-cormorant-fonts appstream file"
cat > "org.altlinux.catharsis-cormorant-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.catharsis-cormorant-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Catharsis Fonts Cormorant</name>
  <summary><![CDATA[Cormorant, a display serif font family inspired by the Garamond heritage]]></summary>
  <description>
    <p><![CDATA[Cormorant is an original design for an extravagant display serif font family]]></p><p><![CDATA[inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.]]></p><p><![CDATA[While traditional Garamond cuts make for exquisite reading at book sizes, they]]></p><p><![CDATA[appear clumpy and inelegant at larger sizes. The design goal of Cormorant was]]></p><p><![CDATA[to distill the aesthetic essence of Garamond, unfetter it from the limitations]]></p><p><![CDATA[of metal printing, and allow it to bloom into its natural refined form at high]]></p><p><![CDATA[definition.]]></p> Cormorant is characterized by scandalously small counters, razor-sharp serifs, dangerously smooth curves, and flamboyantly tall accents. While many implementations of Garamond at small optical sizes already exist (including the open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely populated niche of display-size counterparts that exploit the high resolution of contemporary screens and print media to the fullest. Cormorant is made for large sizes; the larger, the better. However, it works well as a text face in high-resolution environments. Cormorant is a native 21st-century typeface making ample use of OpenType technology. Some OpenType features are applied automatically while you type, subtly improving the flow of the text. This includes kerning, standard ligatures, and contextual alternates. Other features are intended to be activated manually by the user, such as discretionary ligatures, stylistic alternates, small capitals, and alternate figure sets.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in '2. OpenType Files/CormorantGaramond-Bold.otf' '2. OpenType Files/CormorantGaramond-BoldItalic.otf' '2. OpenType Files/CormorantGaramond-Italic.otf' '2. OpenType Files/CormorantGaramond-Light.otf' '2. OpenType Files/CormorantGaramond-LightItalic.otf' '2. OpenType Files/CormorantGaramond-Medium.otf' '2. OpenType Files/CormorantGaramond-MediumItalic.otf' '2. OpenType Files/CormorantGaramond-Regular.otf' '2. OpenType Files/CormorantGaramond-SemiBold.otf' '2. OpenType Files/CormorantGaramond-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '2. OpenType Files/CormorantGaramond-Bold.otf' '2. OpenType Files/CormorantGaramond-BoldItalic.otf' '2. OpenType Files/CormorantGaramond-Italic.otf' '2. OpenType Files/CormorantGaramond-Light.otf' '2. OpenType Files/CormorantGaramond-LightItalic.otf' '2. OpenType Files/CormorantGaramond-Medium.otf' '2. OpenType Files/CormorantGaramond-MediumItalic.otf' '2. OpenType Files/CormorantGaramond-Regular.otf' '2. OpenType Files/CormorantGaramond-SemiBold.otf' '2. OpenType Files/CormorantGaramond-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the catharsis-cormorant-garamond-fonts appstream file"
cat > "org.altlinux.catharsis-cormorant-garamond-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.catharsis-cormorant-garamond-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Catharsis Fonts Cormorant Garamond</name>
  <summary><![CDATA[Cormorant Garamond, a variant with more traditional shapes]]></summary>
  <description>
    <p><![CDATA[Cormorant is an original design for an extravagant display serif font family]]></p><p><![CDATA[inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.]]></p><p><![CDATA[While traditional Garamond cuts make for exquisite reading at book sizes, they]]></p><p><![CDATA[appear clumpy and inelegant at larger sizes. The design goal of Cormorant was]]></p><p><![CDATA[to distill the aesthetic essence of Garamond, unfetter it from the limitations]]></p><p><![CDATA[of metal printing, and allow it to bloom into its natural refined form at high]]></p><p><![CDATA[definition.]]></p> Cormorant is characterized by scandalously small counters, razor-sharp serifs, dangerously smooth curves, and flamboyantly tall accents. While many implementations of Garamond at small optical sizes already exist (including the open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely populated niche of display-size counterparts that exploit the high resolution of contemporary screens and print media to the fullest. Cormorant is made for large sizes; the larger, the better. However, it works well as a text face in high-resolution environments. Cormorant is a native 21st-century typeface making ample use of OpenType technology. Some OpenType features are applied automatically while you type, subtly improving the flow of the text. This includes kerning, standard ligatures, and contextual alternates. Other features are intended to be activated manually by the user, such as discretionary ligatures, stylistic alternates, small capitals, and alternate figure sets. While Cormorant’s quality is most evident in titling and poster usage at the largest sizes, its Garamond genome renders it highly legible down to text sizes on high-resolution devices and in print. This is particularly true about the “Cormorant Garamond” cuts of the typeface. Cormorant Garamond offers larger counters and subtly more traditional Garamond shapes for a few key characters to achieve more reading comfort.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in '2. OpenType Files/CormorantInfant-Bold.otf' '2. OpenType Files/CormorantInfant-BoldItalic.otf' '2. OpenType Files/CormorantInfant-Italic.otf' '2. OpenType Files/CormorantInfant-Light.otf' '2. OpenType Files/CormorantInfant-LightItalic.otf' '2. OpenType Files/CormorantInfant-Medium.otf' '2. OpenType Files/CormorantInfant-MediumItalic.otf' '2. OpenType Files/CormorantInfant-Regular.otf' '2. OpenType Files/CormorantInfant-SemiBold.otf' '2. OpenType Files/CormorantInfant-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '2. OpenType Files/CormorantInfant-Bold.otf' '2. OpenType Files/CormorantInfant-BoldItalic.otf' '2. OpenType Files/CormorantInfant-Italic.otf' '2. OpenType Files/CormorantInfant-Light.otf' '2. OpenType Files/CormorantInfant-LightItalic.otf' '2. OpenType Files/CormorantInfant-Medium.otf' '2. OpenType Files/CormorantInfant-MediumItalic.otf' '2. OpenType Files/CormorantInfant-Regular.otf' '2. OpenType Files/CormorantInfant-SemiBold.otf' '2. OpenType Files/CormorantInfant-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the catharsis-cormorant-infant-fonts appstream file"
cat > "org.altlinux.catharsis-cormorant-infant-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.catharsis-cormorant-infant-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Catharsis Fonts Cormorant Infant</name>
  <summary><![CDATA[Cormorant Infant, a gentle schoolbook-style variant]]></summary>
  <description>
    <p><![CDATA[Cormorant is an original design for an extravagant display serif font family]]></p><p><![CDATA[inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.]]></p><p><![CDATA[While traditional Garamond cuts make for exquisite reading at book sizes, they]]></p><p><![CDATA[appear clumpy and inelegant at larger sizes. The design goal of Cormorant was]]></p><p><![CDATA[to distill the aesthetic essence of Garamond, unfetter it from the limitations]]></p><p><![CDATA[of metal printing, and allow it to bloom into its natural refined form at high]]></p><p><![CDATA[definition.]]></p> Cormorant is characterized by scandalously small counters, razor-sharp serifs, dangerously smooth curves, and flamboyantly tall accents. While many implementations of Garamond at small optical sizes already exist (including the open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely populated niche of display-size counterparts that exploit the high resolution of contemporary screens and print media to the fullest. Cormorant is made for large sizes; the larger, the better. However, it works well as a text face in high-resolution environments. Cormorant is a native 21st-century typeface making ample use of OpenType technology. Some OpenType features are applied automatically while you type, subtly improving the flow of the text. This includes kerning, standard ligatures, and contextual alternates. Other features are intended to be activated manually by the user, such as discretionary ligatures, stylistic alternates, small capitals, and alternate figure sets. In Cormorant Infant, the letters “a g y” and their derivatives are replaced by gentle schoolbook-style single-storey shapes.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in '2. OpenType Files/CormorantUpright-Bold.otf' '2. OpenType Files/CormorantUpright-Light.otf' '2. OpenType Files/CormorantUpright-Medium.otf' '2. OpenType Files/CormorantUpright-Regular.otf' '2. OpenType Files/CormorantUpright-SemiBold.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '2. OpenType Files/CormorantUpright-Bold.otf' '2. OpenType Files/CormorantUpright-Light.otf' '2. OpenType Files/CormorantUpright-Medium.otf' '2. OpenType Files/CormorantUpright-Regular.otf' '2. OpenType Files/CormorantUpright-SemiBold.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the catharsis-cormorant-upright-fonts appstream file"
cat > "org.altlinux.catharsis-cormorant-upright-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.catharsis-cormorant-upright-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Catharsis Fonts Cormorant Upright</name>
  <summary><![CDATA[Cormorant Upright, an un-slanted cursive variant]]></summary>
  <description>
    <p><![CDATA[Cormorant is an original design for an extravagant display serif font family]]></p><p><![CDATA[inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.]]></p><p><![CDATA[While traditional Garamond cuts make for exquisite reading at book sizes, they]]></p><p><![CDATA[appear clumpy and inelegant at larger sizes. The design goal of Cormorant was]]></p><p><![CDATA[to distill the aesthetic essence of Garamond, unfetter it from the limitations]]></p><p><![CDATA[of metal printing, and allow it to bloom into its natural refined form at high]]></p><p><![CDATA[definition.]]></p> Cormorant is characterized by scandalously small counters, razor-sharp serifs, dangerously smooth curves, and flamboyantly tall accents. While many implementations of Garamond at small optical sizes already exist (including the open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely populated niche of display-size counterparts that exploit the high resolution of contemporary screens and print media to the fullest. Cormorant is made for large sizes; the larger, the better. However, it works well as a text face in high-resolution environments. Cormorant is a native 21st-century typeface making ample use of OpenType technology. Some OpenType features are applied automatically while you type, subtly improving the flow of the text. This includes kerning, standard ligatures, and contextual alternates. Other features are intended to be activated manually by the user, such as discretionary ligatures, stylistic alternates, small capitals, and alternate figure sets. Cormorant Upright is an un-slanted cursive of the main Cormorant font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 4
fontnames=$(
  for font in '2. OpenType Files/CormorantUnicase-Bold.otf' '2. OpenType Files/CormorantUnicase-Light.otf' '2. OpenType Files/CormorantUnicase-Medium.otf' '2. OpenType Files/CormorantUnicase-Regular.otf' '2. OpenType Files/CormorantUnicase-SemiBold.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '2. OpenType Files/CormorantUnicase-Bold.otf' '2. OpenType Files/CormorantUnicase-Light.otf' '2. OpenType Files/CormorantUnicase-Medium.otf' '2. OpenType Files/CormorantUnicase-Regular.otf' '2. OpenType Files/CormorantUnicase-SemiBold.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the catharsis-cormorant-unicase-fonts appstream file"
cat > "org.altlinux.catharsis-cormorant-unicase-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.catharsis-cormorant-unicase-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Catharsis Fonts Cormorant Unicase</name>
  <summary><![CDATA[Cormorant Unicase, a small-caps variant with some lowercase letter-forms]]></summary>
  <description>
    <p><![CDATA[Cormorant is an original design for an extravagant display serif font family]]></p><p><![CDATA[inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.]]></p><p><![CDATA[While traditional Garamond cuts make for exquisite reading at book sizes, they]]></p><p><![CDATA[appear clumpy and inelegant at larger sizes. The design goal of Cormorant was]]></p><p><![CDATA[to distill the aesthetic essence of Garamond, unfetter it from the limitations]]></p><p><![CDATA[of metal printing, and allow it to bloom into its natural refined form at high]]></p><p><![CDATA[definition.]]></p> Cormorant is characterized by scandalously small counters, razor-sharp serifs, dangerously smooth curves, and flamboyantly tall accents. While many implementations of Garamond at small optical sizes already exist (including the open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely populated niche of display-size counterparts that exploit the high resolution of contemporary screens and print media to the fullest. Cormorant is made for large sizes; the larger, the better. However, it works well as a text face in high-resolution environments. Cormorant is a native 21st-century typeface making ample use of OpenType technology. Some OpenType features are applied automatically while you type, subtly improving the flow of the text. This includes kerning, standard ligatures, and contextual alternates. Other features are intended to be activated manually by the user, such as discretionary ligatures, stylistic alternates, small capitals, and alternate figure sets. Cormorant Unicase, is a small-caps variant with some lowercase letter-forms for an eye-catching futuristic look.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing catharsis-cormorant-fonts
echo "" > "catharsis-cormorant-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/catharsis-cormorant/
echo "%%dir %_fontsdir/otf/catharsis-cormorant" >> "catharsis-cormorant-fonts0.list"
install -m 0644 -vp "2. OpenType Files/Cormorant-Bold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-Bold.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-BoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-BoldItalic.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-Italic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-Italic.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-Light.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-Light.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-LightItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-LightItalic.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-Medium.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-Medium.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-MediumItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-MediumItalic.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-Regular.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-Regular.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-SemiBold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-SemiBold.otf")\" >> 'catharsis-cormorant-fonts0.list'
install -m 0644 -vp "2. OpenType Files/Cormorant-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/Cormorant-SemiBoldItalic.otf")\" >> 'catharsis-cormorant-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f '2. OpenType Files/Cormorant-Bold.otf' '2. OpenType Files/Cormorant-BoldItalic.otf' '2. OpenType Files/Cormorant-Italic.otf' '2. OpenType Files/Cormorant-Light.otf' '2. OpenType Files/Cormorant-LightItalic.otf' '2. OpenType Files/Cormorant-Medium.otf' '2. OpenType Files/Cormorant-MediumItalic.otf' '2. OpenType Files/Cormorant-Regular.otf' '2. OpenType Files/Cormorant-SemiBold.otf' '2. OpenType Files/Cormorant-SemiBoldItalic.otf'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "catharsis-cormorant-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "catharsis-cormorant-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.catharsis-cormorant-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "catharsis-cormorant-fonts0.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "catharsis-cormorant-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "catharsis-cormorant-fonts0.list"
done
echo Installing catharsis-cormorant-garamond-fonts
echo "" > "catharsis-cormorant-garamond-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/catharsis-cormorant/
echo "%%dir %_fontsdir/otf/catharsis-cormorant" >> "catharsis-cormorant-garamond-fonts1.list"
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-Bold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-Bold.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-BoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-BoldItalic.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-Italic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-Italic.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-Light.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-Light.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-LightItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-LightItalic.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-Medium.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-Medium.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-MediumItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-MediumItalic.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-Regular.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-Regular.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-SemiBold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-SemiBold.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
install -m 0644 -vp "2. OpenType Files/CormorantGaramond-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantGaramond-SemiBoldItalic.otf")\" >> 'catharsis-cormorant-garamond-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f '2. OpenType Files/CormorantGaramond-Bold.otf' '2. OpenType Files/CormorantGaramond-BoldItalic.otf' '2. OpenType Files/CormorantGaramond-Italic.otf' '2. OpenType Files/CormorantGaramond-Light.otf' '2. OpenType Files/CormorantGaramond-LightItalic.otf' '2. OpenType Files/CormorantGaramond-Medium.otf' '2. OpenType Files/CormorantGaramond-MediumItalic.otf' '2. OpenType Files/CormorantGaramond-Regular.otf' '2. OpenType Files/CormorantGaramond-SemiBold.otf' '2. OpenType Files/CormorantGaramond-SemiBoldItalic.otf'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "catharsis-cormorant-garamond-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "catharsis-cormorant-garamond-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.catharsis-cormorant-garamond-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "catharsis-cormorant-garamond-fonts1.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "catharsis-cormorant-garamond-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "catharsis-cormorant-garamond-fonts1.list"
done
echo Installing catharsis-cormorant-infant-fonts
echo "" > "catharsis-cormorant-infant-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/catharsis-cormorant/
echo "%%dir %_fontsdir/otf/catharsis-cormorant" >> "catharsis-cormorant-infant-fonts2.list"
install -m 0644 -vp "2. OpenType Files/CormorantInfant-Bold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-Bold.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-BoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-BoldItalic.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-Italic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-Italic.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-Light.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-Light.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-LightItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-LightItalic.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-Medium.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-Medium.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-MediumItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-MediumItalic.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-Regular.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-Regular.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-SemiBold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-SemiBold.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
install -m 0644 -vp "2. OpenType Files/CormorantInfant-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantInfant-SemiBoldItalic.otf")\" >> 'catharsis-cormorant-infant-fonts2.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE12'; do
      gen-fontconf -x "${fontconfng}" -w -f '2. OpenType Files/CormorantInfant-Bold.otf' '2. OpenType Files/CormorantInfant-BoldItalic.otf' '2. OpenType Files/CormorantInfant-Italic.otf' '2. OpenType Files/CormorantInfant-Light.otf' '2. OpenType Files/CormorantInfant-LightItalic.otf' '2. OpenType Files/CormorantInfant-Medium.otf' '2. OpenType Files/CormorantInfant-MediumItalic.otf' '2. OpenType Files/CormorantInfant-Regular.otf' '2. OpenType Files/CormorantInfant-SemiBold.otf' '2. OpenType Files/CormorantInfant-SemiBoldItalic.otf'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "catharsis-cormorant-infant-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "catharsis-cormorant-infant-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.catharsis-cormorant-infant-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "catharsis-cormorant-infant-fonts2.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "catharsis-cormorant-infant-fonts2.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "catharsis-cormorant-infant-fonts2.list"
done
echo Installing catharsis-cormorant-upright-fonts
echo "" > "catharsis-cormorant-upright-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/catharsis-cormorant/
echo "%%dir %_fontsdir/otf/catharsis-cormorant" >> "catharsis-cormorant-upright-fonts3.list"
install -m 0644 -vp "2. OpenType Files/CormorantUpright-Bold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUpright-Bold.otf")\" >> 'catharsis-cormorant-upright-fonts3.list'
install -m 0644 -vp "2. OpenType Files/CormorantUpright-Light.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUpright-Light.otf")\" >> 'catharsis-cormorant-upright-fonts3.list'
install -m 0644 -vp "2. OpenType Files/CormorantUpright-Medium.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUpright-Medium.otf")\" >> 'catharsis-cormorant-upright-fonts3.list'
install -m 0644 -vp "2. OpenType Files/CormorantUpright-Regular.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUpright-Regular.otf")\" >> 'catharsis-cormorant-upright-fonts3.list'
install -m 0644 -vp "2. OpenType Files/CormorantUpright-SemiBold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUpright-SemiBold.otf")\" >> 'catharsis-cormorant-upright-fonts3.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE13'; do
      gen-fontconf -x "${fontconfng}" -w -f '2. OpenType Files/CormorantUpright-Bold.otf' '2. OpenType Files/CormorantUpright-Light.otf' '2. OpenType Files/CormorantUpright-Medium.otf' '2. OpenType Files/CormorantUpright-Regular.otf' '2. OpenType Files/CormorantUpright-SemiBold.otf'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "catharsis-cormorant-upright-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "catharsis-cormorant-upright-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.catharsis-cormorant-upright-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "catharsis-cormorant-upright-fonts3.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "catharsis-cormorant-upright-fonts3.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "catharsis-cormorant-upright-fonts3.list"
done
echo Installing catharsis-cormorant-unicase-fonts
echo "" > "catharsis-cormorant-unicase-fonts4.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/catharsis-cormorant/
echo "%%dir %_fontsdir/otf/catharsis-cormorant" >> "catharsis-cormorant-unicase-fonts4.list"
install -m 0644 -vp "2. OpenType Files/CormorantUnicase-Bold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUnicase-Bold.otf")\" >> 'catharsis-cormorant-unicase-fonts4.list'
install -m 0644 -vp "2. OpenType Files/CormorantUnicase-Light.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUnicase-Light.otf")\" >> 'catharsis-cormorant-unicase-fonts4.list'
install -m 0644 -vp "2. OpenType Files/CormorantUnicase-Medium.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUnicase-Medium.otf")\" >> 'catharsis-cormorant-unicase-fonts4.list'
install -m 0644 -vp "2. OpenType Files/CormorantUnicase-Regular.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUnicase-Regular.otf")\" >> 'catharsis-cormorant-unicase-fonts4.list'
install -m 0644 -vp "2. OpenType Files/CormorantUnicase-SemiBold.otf" %buildroot%_fontsdir/otf/catharsis-cormorant/
echo \"%_fontsdir/otf/catharsis-cormorant//$(basename "2. OpenType Files/CormorantUnicase-SemiBold.otf")\" >> 'catharsis-cormorant-unicase-fonts4.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE14'; do
      gen-fontconf -x "${fontconfng}" -w -f '2. OpenType Files/CormorantUnicase-Bold.otf' '2. OpenType Files/CormorantUnicase-Light.otf' '2. OpenType Files/CormorantUnicase-Medium.otf' '2. OpenType Files/CormorantUnicase-Regular.otf' '2. OpenType Files/CormorantUnicase-SemiBold.otf'
    done
  )
  while IFS= read -r line; do
    [[ -n $line ]] && newfontconfs+=("$line")
  done <<< ${lines}

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in  "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "catharsis-cormorant-unicase-fonts4.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "catharsis-cormorant-unicase-fonts4.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.catharsis-cormorant-unicase-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "catharsis-cormorant-unicase-fonts4.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "catharsis-cormorant-unicase-fonts4.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "catharsis-cormorant-unicase-fonts4.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'catharsis-cormorant-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'catharsis-cormorant-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'catharsis-cormorant-garamond-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'catharsis-cormorant-garamond-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'catharsis-cormorant-infant-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'catharsis-cormorant-infant-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'catharsis-cormorant-upright-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'catharsis-cormorant-upright-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 4
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'catharsis-cormorant-unicase-fonts4.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'catharsis-cormorant-unicase-fonts4.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-catharsis-cormorant -f catharsis-cormorant-fonts0.list
%files -n fonts-otf-catharsis-cormorant-garamond -f catharsis-cormorant-garamond-fonts1.list
%files -n fonts-otf-catharsis-cormorant-infant -f catharsis-cormorant-infant-fonts2.list
%files -n fonts-otf-catharsis-cormorant-upright -f catharsis-cormorant-upright-fonts3.list
%files -n fonts-otf-catharsis-cormorant-unicase -f catharsis-cormorant-unicase-fonts4.list

%files doc
%doc --no-dereference OFL.txt
%doc 5.*Specimens*Test*Files/*pdf

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 3.602-alt1_4
- new version

