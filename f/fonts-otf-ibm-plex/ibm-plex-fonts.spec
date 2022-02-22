Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname ibm-plex-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ibm-plex-fonts
# SPDX-License-Identifier: MIT

Name:    fonts-otf-ibm-plex
Version: 6.0.0
Release: alt1_1
Summary: IBM Plex, the new IBM set of coordinated grotesque corporate fonts

License: OFL
URL:     https://www.ibm.com/plex/

BuildArch: noarch

%global foundry           IBM
%global fontlicense       OFL
%global fontlicenses      IBM-Plex-Sans/license.txt
#global fontdocs          *.md

%global common_description \
IBM wanted Plex to be a distinctive, yet timeless workhorse a.. an alternative to\
its previous corporate font family, a.'Helvetica Neuea.', for this new era. The\
Grotesque style was the perfect fit. Not only do Grotesque font families\
balance human and rational elements, the Grotesque style also came about during\
the Industrial Age, when IBM was born.\


%global fontfamily1       Plex Sans
%global fontsummary1      IBM Plex Sans, the new grotesque IBM corporate font family
%global fontpkgheader1    \
#Suggests: font(ibmplexsansmono)\
Obsoletes: ibm-plex-fonts-common          < %{version}-%{release}\
Obsoletes: ibm-plex-sans-arabic-fonts     < %{version}-%{release}\
Obsoletes: ibm-plex-sans-condensed-fonts  < %{version}-%{release}\
Obsoletes: ibm-plex-sans-devanagari-fonts < %{version}-%{release}\
Obsoletes: ibm-plex-sans-hebrew-fonts     < %{version}-%{release}\
Obsoletes: ibm-plex-sans-thai-fonts       < %{version}-%{release}\

%global fonts1            IBM-Plex-Sans/*.otf IBM-Plex-Sans-Condensed/*.otf IBM-Plex-Sans-Arabic/*.otf IBM-Plex-Sans-Hebrew/*.otf IBM-Plex-Sans-Thai/*.otf IBM-Plex-Sans-Devanagari/*.otf
%global fontdescription1  \
%{common_description}\
This package provides the grotesque sans-serif variable-width IBM Plex Sans,\
the main font family of the Plex set.

%global fontfamily2       Plex Mono
%global fontsummary2      IBM Plex Mono, the monospace grotesque coding font family of the Plex set
%global fonts2            IBM-Plex-Mono/*.otf
%global fontdescription2  \
%{common_description}\
This package provides the grotesque sans-serif fixed-width IBM Plex Mono, a\
little something for developers, because monospace does not need to be monotone.

%global fontfamily3       Plex Serif
%global fontsummary3      IBM Plex Serif, the hybrid grotesque serif font family of the Plex set
%global fonts3            IBM-Plex-Serif/*.otf
%global fontdescription3  \
%{common_description}\
This package provides the hybrid grotesque serif variable-width IBM Plex Serif,\
combining the best of Plex, Bodoni, and Janson into a contemporary serif.

%global fontfamily4       Plex Sans Thai Looped
%global fontsummary4      IBM Plex Sans Thai Looped, a formal variant of IBM Plex Sans for Thai
%global fontpkgheader4    \
Requires: fonts-otf-ibm-plex-sans\

%global fonts4            IBM-Plex-Sans-Thai-Looped/*.otf
%global fontdescription4  \
%{common_description}\
This package provides a more formal and traditional form of Thai for the\
grotesque sans-serif variable-width IBM Plex Sans, that includes loops.

Source0:  https://github.com/IBM/plex/releases/download/v%{version}/OpenType.zip#/%{oldname}-%{version}.zip
Source11: 58-ibm-plex-sans-fonts.xml
Source12: 58-ibm-plex-mono-fonts.xml
Source13: 58-ibm-plex-serif-fonts.xml
Source14: 59-ibm-plex-sans-thai-looped-fonts.xml
Source44: import.info

%description
%{common_description}

%package     -n fonts-otf-ibm-plex-sans
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-ibm-plex-sans
%{?fontdescription1}
%package     -n fonts-otf-ibm-plex-mono
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-otf-ibm-plex-mono
%{?fontdescription2}
%package     -n fonts-otf-ibm-plex-serif
Group: System/Fonts/True type
Summary:        %{fontsummary3}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-otf-ibm-plex-serif
%{?fontdescription3}
%package     -n fonts-otf-ibm-plex-sans-thai-looped
Group: System/Fonts/True type
Summary:        %{fontsummary4}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader4}
%description -n fonts-otf-ibm-plex-sans-thai-looped
%{?fontdescription4}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-ibm-plex-sans = %EVR
Requires:  fonts-otf-ibm-plex-mono = %EVR
Requires:  fonts-otf-ibm-plex-serif = %EVR
Requires:  fonts-otf-ibm-plex-sans-thai-looped = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fontconfs1        %{SOURCE11}
%global fontconfs2        %{SOURCE12}
%global fontconfs3        %{SOURCE13}
%global fontconfs4        %{SOURCE14}
%setup -n OpenType

%build
# fontbuild 1
fontnames=$(
  for font in 'IBM-Plex-Sans/IBMPlexSans-Bold.otf' 'IBM-Plex-Sans/IBMPlexSans-BoldItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-ExtraLight.otf' 'IBM-Plex-Sans/IBMPlexSans-ExtraLightItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Italic.otf' 'IBM-Plex-Sans/IBMPlexSans-Light.otf' 'IBM-Plex-Sans/IBMPlexSans-LightItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Medium.otf' 'IBM-Plex-Sans/IBMPlexSans-MediumItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Regular.otf' 'IBM-Plex-Sans/IBMPlexSans-SemiBold.otf' 'IBM-Plex-Sans/IBMPlexSans-SemiBoldItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Text.otf' 'IBM-Plex-Sans/IBMPlexSans-TextItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Thin.otf' 'IBM-Plex-Sans/IBMPlexSans-ThinItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Bold.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-BoldItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLight.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLightItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Italic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Light.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-LightItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Medium.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-MediumItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Regular.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBold.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBoldItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Text.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-TextItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Thin.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ThinItalic.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Bold.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-ExtraLight.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Light.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Medium.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Regular.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-SemiBold.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Text.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Thin.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Bold.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-ExtraLight.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Light.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Medium.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Regular.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-SemiBold.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Text.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Thin.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Bold.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-ExtraLight.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Light.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Medium.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Regular.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-SemiBold.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Text.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Thin.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Bold.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-ExtraLight.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Light.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Medium.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Regular.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-SemiBold.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Text.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Thin.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'IBM-Plex-Sans/IBMPlexSans-Bold.otf' 'IBM-Plex-Sans/IBMPlexSans-BoldItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-ExtraLight.otf' 'IBM-Plex-Sans/IBMPlexSans-ExtraLightItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Italic.otf' 'IBM-Plex-Sans/IBMPlexSans-Light.otf' 'IBM-Plex-Sans/IBMPlexSans-LightItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Medium.otf' 'IBM-Plex-Sans/IBMPlexSans-MediumItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Regular.otf' 'IBM-Plex-Sans/IBMPlexSans-SemiBold.otf' 'IBM-Plex-Sans/IBMPlexSans-SemiBoldItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Text.otf' 'IBM-Plex-Sans/IBMPlexSans-TextItalic.otf' 'IBM-Plex-Sans/IBMPlexSans-Thin.otf' 'IBM-Plex-Sans/IBMPlexSans-ThinItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Bold.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-BoldItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLight.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLightItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Italic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Light.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-LightItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Medium.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-MediumItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Regular.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBold.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBoldItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Text.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-TextItalic.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Thin.otf' 'IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ThinItalic.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Bold.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-ExtraLight.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Light.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Medium.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Regular.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-SemiBold.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Text.otf' 'IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Thin.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Bold.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-ExtraLight.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Light.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Medium.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Regular.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-SemiBold.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Text.otf' 'IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Thin.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Bold.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-ExtraLight.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Light.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Medium.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Regular.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-SemiBold.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Text.otf' 'IBM-Plex-Sans-Thai/IBMPlexSansThai-Thin.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Bold.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-ExtraLight.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Light.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Medium.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Regular.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-SemiBold.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Text.otf' 'IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Thin.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ibm-plex-sans-fonts appstream file"
cat > "org.altlinux.ibm-plex-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ibm-plex-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>IBM Plex Sans</name>
  <summary><![CDATA[IBM Plex Sans, the new grotesque IBM corporate font family]]></summary>
  <description>
    <p><![CDATA[IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to]]></p><p><![CDATA[its previous corporate font family, “Helvetica Neue”, for this new era. The]]></p><p><![CDATA[Grotesque style was the perfect fit. Not only do Grotesque font families]]></p><p><![CDATA[balance human and rational elements, the Grotesque style also came about during]]></p><p><![CDATA[the Industrial Age, when IBM was born.]]></p> This package provides the grotesque sans-serif variable-width IBM Plex Sans, the main font family of the Plex set.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.ibm.com/plex/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'IBM-Plex-Mono/IBMPlexMono-Bold.otf' 'IBM-Plex-Mono/IBMPlexMono-BoldItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-ExtraLight.otf' 'IBM-Plex-Mono/IBMPlexMono-ExtraLightItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Italic.otf' 'IBM-Plex-Mono/IBMPlexMono-Light.otf' 'IBM-Plex-Mono/IBMPlexMono-LightItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Medium.otf' 'IBM-Plex-Mono/IBMPlexMono-MediumItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Regular.otf' 'IBM-Plex-Mono/IBMPlexMono-SemiBold.otf' 'IBM-Plex-Mono/IBMPlexMono-SemiBoldItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Text.otf' 'IBM-Plex-Mono/IBMPlexMono-TextItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Thin.otf' 'IBM-Plex-Mono/IBMPlexMono-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'IBM-Plex-Mono/IBMPlexMono-Bold.otf' 'IBM-Plex-Mono/IBMPlexMono-BoldItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-ExtraLight.otf' 'IBM-Plex-Mono/IBMPlexMono-ExtraLightItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Italic.otf' 'IBM-Plex-Mono/IBMPlexMono-Light.otf' 'IBM-Plex-Mono/IBMPlexMono-LightItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Medium.otf' 'IBM-Plex-Mono/IBMPlexMono-MediumItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Regular.otf' 'IBM-Plex-Mono/IBMPlexMono-SemiBold.otf' 'IBM-Plex-Mono/IBMPlexMono-SemiBoldItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Text.otf' 'IBM-Plex-Mono/IBMPlexMono-TextItalic.otf' 'IBM-Plex-Mono/IBMPlexMono-Thin.otf' 'IBM-Plex-Mono/IBMPlexMono-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ibm-plex-mono-fonts appstream file"
cat > "org.altlinux.ibm-plex-mono-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ibm-plex-mono-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>IBM Plex Mono</name>
  <summary><![CDATA[IBM Plex Mono, the monospace grotesque coding font family of the Plex set]]></summary>
  <description>
    <p><![CDATA[IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to]]></p><p><![CDATA[its previous corporate font family, “Helvetica Neue”, for this new era. The]]></p><p><![CDATA[Grotesque style was the perfect fit. Not only do Grotesque font families]]></p><p><![CDATA[balance human and rational elements, the Grotesque style also came about during]]></p><p><![CDATA[the Industrial Age, when IBM was born.]]></p> This package provides the grotesque sans-serif fixed-width IBM Plex Mono, a little something for developers, because monospace does not need to be monotone.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.ibm.com/plex/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'IBM-Plex-Serif/IBMPlexSerif-Bold.otf' 'IBM-Plex-Serif/IBMPlexSerif-BoldItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-ExtraLight.otf' 'IBM-Plex-Serif/IBMPlexSerif-ExtraLightItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Italic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Light.otf' 'IBM-Plex-Serif/IBMPlexSerif-LightItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Medium.otf' 'IBM-Plex-Serif/IBMPlexSerif-MediumItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Regular.otf' 'IBM-Plex-Serif/IBMPlexSerif-SemiBold.otf' 'IBM-Plex-Serif/IBMPlexSerif-SemiBoldItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Text.otf' 'IBM-Plex-Serif/IBMPlexSerif-TextItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Thin.otf' 'IBM-Plex-Serif/IBMPlexSerif-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'IBM-Plex-Serif/IBMPlexSerif-Bold.otf' 'IBM-Plex-Serif/IBMPlexSerif-BoldItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-ExtraLight.otf' 'IBM-Plex-Serif/IBMPlexSerif-ExtraLightItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Italic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Light.otf' 'IBM-Plex-Serif/IBMPlexSerif-LightItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Medium.otf' 'IBM-Plex-Serif/IBMPlexSerif-MediumItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Regular.otf' 'IBM-Plex-Serif/IBMPlexSerif-SemiBold.otf' 'IBM-Plex-Serif/IBMPlexSerif-SemiBoldItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Text.otf' 'IBM-Plex-Serif/IBMPlexSerif-TextItalic.otf' 'IBM-Plex-Serif/IBMPlexSerif-Thin.otf' 'IBM-Plex-Serif/IBMPlexSerif-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ibm-plex-serif-fonts appstream file"
cat > "org.altlinux.ibm-plex-serif-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ibm-plex-serif-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>IBM Plex Serif</name>
  <summary><![CDATA[IBM Plex Serif, the hybrid grotesque serif font family of the Plex set]]></summary>
  <description>
    <p><![CDATA[IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to]]></p><p><![CDATA[its previous corporate font family, “Helvetica Neue”, for this new era. The]]></p><p><![CDATA[Grotesque style was the perfect fit. Not only do Grotesque font families]]></p><p><![CDATA[balance human and rational elements, the Grotesque style also came about during]]></p><p><![CDATA[the Industrial Age, when IBM was born.]]></p> This package provides the hybrid grotesque serif variable-width IBM Plex Serif, combining the best of Plex, Bodoni, and Janson into a contemporary serif.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.ibm.com/plex/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 4
fontnames=$(
  for font in 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Bold.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-ExtraLight.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Light.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Medium.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Regular.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-SemiBold.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Text.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Thin.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Bold.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-ExtraLight.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Light.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Medium.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Regular.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-SemiBold.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Text.otf' 'IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Thin.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ibm-plex-sans-thai-looped-fonts appstream file"
cat > "org.altlinux.ibm-plex-sans-thai-looped-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ibm-plex-sans-thai-looped-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>IBM Plex Sans Thai Looped</name>
  <summary><![CDATA[IBM Plex Sans Thai Looped, a formal variant of IBM Plex Sans for Thai]]></summary>
  <description>
    <p><![CDATA[IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to]]></p><p><![CDATA[its previous corporate font family, “Helvetica Neue”, for this new era. The]]></p><p><![CDATA[Grotesque style was the perfect fit. Not only do Grotesque font families]]></p><p><![CDATA[balance human and rational elements, the Grotesque style also came about during]]></p><p><![CDATA[the Industrial Age, when IBM was born.]]></p> This package provides a more formal and traditional form of Thai for the grotesque sans-serif variable-width IBM Plex Sans, that includes loops.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.ibm.com/plex/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ibm-plex-sans-fonts
echo "" > "ibm-plex-sans-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ibm-plex/
echo "%%dir %_fontsdir/otf/ibm-plex" >> "ibm-plex-sans-fonts1.list"
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-BoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-BoldItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-ExtraLightItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Italic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Italic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-LightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-LightItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-MediumItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-MediumItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-SemiBoldItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-TextItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-TextItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans/IBMPlexSans-ThinItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans/IBMPlexSans-ThinItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-BoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-BoldItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ExtraLightItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Italic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Italic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-LightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-LightItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-MediumItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-MediumItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-SemiBoldItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-TextItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-TextItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ThinItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Condensed/IBMPlexSansCondensed-ThinItalic.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Arabic/IBMPlexSansArabic-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Hebrew/IBMPlexSansHebrew-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai/IBMPlexSansThai-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai/IBMPlexSansThai-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Bold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-ExtraLight.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Light.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Medium.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Regular.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-SemiBold.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Text.otf")\" >> 'ibm-plex-sans-fonts1.list'
install -m 0644 -vp "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Devanagari/IBMPlexSansDevanagari-Thin.otf")\" >> 'ibm-plex-sans-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE11' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ibm-plex-sans-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ibm-plex-sans-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ibm-plex-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ibm-plex-sans-fonts1.list"
done

for fontlicense in 'IBM-Plex-Sans/license.txt'; do
  echo %%doc "'${fontlicense}'" >> "ibm-plex-sans-fonts1.list"
done
echo Installing ibm-plex-mono-fonts
echo "" > "ibm-plex-mono-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ibm-plex/
echo "%%dir %_fontsdir/otf/ibm-plex" >> "ibm-plex-mono-fonts2.list"
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Bold.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-BoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-BoldItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-ExtraLight.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-ExtraLightItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Italic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Italic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Light.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-LightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-LightItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Medium.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-MediumItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-MediumItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Regular.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-SemiBold.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-SemiBoldItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Text.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-TextItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-TextItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-Thin.otf")\" >> 'ibm-plex-mono-fonts2.list'
install -m 0644 -vp "IBM-Plex-Mono/IBMPlexMono-ThinItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Mono/IBMPlexMono-ThinItalic.otf")\" >> 'ibm-plex-mono-fonts2.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE12' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ibm-plex-mono-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ibm-plex-mono-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ibm-plex-mono-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ibm-plex-mono-fonts2.list"
done

for fontlicense in 'IBM-Plex-Sans/license.txt'; do
  echo %%doc "'${fontlicense}'" >> "ibm-plex-mono-fonts2.list"
done
echo Installing ibm-plex-serif-fonts
echo "" > "ibm-plex-serif-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ibm-plex/
echo "%%dir %_fontsdir/otf/ibm-plex" >> "ibm-plex-serif-fonts3.list"
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Bold.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-BoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-BoldItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-ExtraLight.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-ExtraLightItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Italic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Italic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Light.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-LightItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-LightItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Medium.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-MediumItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-MediumItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Regular.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-SemiBold.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-SemiBoldItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Text.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-TextItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-TextItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-Thin.otf")\" >> 'ibm-plex-serif-fonts3.list'
install -m 0644 -vp "IBM-Plex-Serif/IBMPlexSerif-ThinItalic.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Serif/IBMPlexSerif-ThinItalic.otf")\" >> 'ibm-plex-serif-fonts3.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE13' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ibm-plex-serif-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ibm-plex-serif-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ibm-plex-serif-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ibm-plex-serif-fonts3.list"
done

for fontlicense in 'IBM-Plex-Sans/license.txt'; do
  echo %%doc "'${fontlicense}'" >> "ibm-plex-serif-fonts3.list"
done
echo Installing ibm-plex-sans-thai-looped-fonts
echo "" > "ibm-plex-sans-thai-looped-fonts4.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ibm-plex/
echo "%%dir %_fontsdir/otf/ibm-plex" >> "ibm-plex-sans-thai-looped-fonts4.list"
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Bold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Bold.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-ExtraLight.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-ExtraLight.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Light.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Light.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Medium.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Medium.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Regular.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Regular.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-SemiBold.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-SemiBold.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Text.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Text.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
install -m 0644 -vp "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Thin.otf" %buildroot%_fontsdir/otf/ibm-plex/
echo \"%_fontsdir/otf/ibm-plex//$(basename "IBM-Plex-Sans-Thai-Looped/IBMPlexSansThaiLooped-Thin.otf")\" >> 'ibm-plex-sans-thai-looped-fonts4.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE14' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ibm-plex-sans-thai-looped-fonts4.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ibm-plex-sans-thai-looped-fonts4.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ibm-plex-sans-thai-looped-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ibm-plex-sans-thai-looped-fonts4.list"
done

for fontlicense in 'IBM-Plex-Sans/license.txt'; do
  echo %%doc "'${fontlicense}'" >> "ibm-plex-sans-thai-looped-fonts4.list"
done

%check
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ibm-plex-sans-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ibm-plex-sans-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ibm-plex-mono-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ibm-plex-mono-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ibm-plex-serif-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ibm-plex-serif-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 4
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ibm-plex-sans-thai-looped-fonts4.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ibm-plex-sans-thai-looped-fonts4.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ibm-plex-sans -f ibm-plex-sans-fonts1.list
%files -n fonts-otf-ibm-plex-mono -f ibm-plex-mono-fonts2.list
%files -n fonts-otf-ibm-plex-serif -f ibm-plex-serif-fonts3.list
%files -n fonts-otf-ibm-plex-sans-thai-looped -f ibm-plex-sans-thai-looped-fonts4.list

%changelog
* Tue Feb 22 2022 Igor Vlasenko <viy@altlinux.org> 6.0.0-alt1_1
- new version

