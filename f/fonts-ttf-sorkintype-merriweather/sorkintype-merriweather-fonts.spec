Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sorkintype-merriweather-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sorkintype-merriweather-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather
%global commit      fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/SorkinType/Merriweather
%global forgesource https://github.com/SorkinType/Merriweather/archive/fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b/Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b.tar.gz
%global archivename Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
%global archiveext tar.gz
%global archiveurl https://github.com/SorkinType/Merriweather/archive/fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b/Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b.tar.gz
%global topdir Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
%global extractdir Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
%global repo Merriweather
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b
#global shortcommit %nil
#global branch %nil
%global version 2.008
#global date %nil
%global distprefix .gitfad21f9
# FedoraForgeMeta2ALT: end generated meta

Version: 2.008
Release: alt1_6
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather
%global fontsummary       Merriweather, a warm space-saving serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*ttf
%global fontsex           fonts/variable/*WO7*ttf fonts/ttfs/Merriweather35*ttf
%global fontdescription   \
Merriweather offers a Renaissance warmth while using proportions which are\
space-saving. It is suitable for editorial design, news and other kinds of\
space sensitive typography.\
\
Merriweather was designed to be a text face that is pleasant to read on\
screens. It features a very large x height, slightly condensed letter-forms, a\
mild diagonal stress, sturdy serifs and open forms

Source0:  %{forgesource}
Source10: 57-sorkintype-merriweather-fonts.xml

Name:           fonts-ttf-sorkintype-merriweather
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n Merriweather-fad21f97f3525af393d7a1d6c2995cbaf4b0cd7b

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/ttfs/Merriweather-Black.ttf' 'fonts/ttfs/Merriweather-BlackDisplay.ttf' 'fonts/ttfs/Merriweather-BlackDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BlackDisplayWide.ttf' 'fonts/ttfs/Merriweather-BlackHeading.ttf' 'fonts/ttfs/Merriweather-BlackHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BlackHeadingWide.ttf' 'fonts/ttfs/Merriweather-BlackItalic.ttf' 'fonts/ttfs/Merriweather-BlackNarrow.ttf' 'fonts/ttfs/Merriweather-BlackText.ttf' 'fonts/ttfs/Merriweather-BlackTextNarrow.ttf' 'fonts/ttfs/Merriweather-BlackTextWide.ttf' 'fonts/ttfs/Merriweather-BlackWide.ttf' 'fonts/ttfs/Merriweather-Bold.ttf' 'fonts/ttfs/Merriweather-BoldDisplay.ttf' 'fonts/ttfs/Merriweather-BoldDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BoldDisplayWide.ttf' 'fonts/ttfs/Merriweather-BoldHeading.ttf' 'fonts/ttfs/Merriweather-BoldHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BoldHeadingWide.ttf' 'fonts/ttfs/Merriweather-BoldItalic.ttf' 'fonts/ttfs/Merriweather-BoldNarrow.ttf' 'fonts/ttfs/Merriweather-BoldText.ttf' 'fonts/ttfs/Merriweather-BoldTextNarrow.ttf' 'fonts/ttfs/Merriweather-BoldTextWide.ttf' 'fonts/ttfs/Merriweather-BoldWide.ttf' 'fonts/ttfs/Merriweather-Italic.ttf' 'fonts/ttfs/Merriweather-Light.ttf' 'fonts/ttfs/Merriweather-LightDisplay.ttf' 'fonts/ttfs/Merriweather-LightDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-LightDisplayWide.ttf' 'fonts/ttfs/Merriweather-LightHeading.ttf' 'fonts/ttfs/Merriweather-LightHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-LightHeadingWide.ttf' 'fonts/ttfs/Merriweather-LightItalic.ttf' 'fonts/ttfs/Merriweather-LightNarrow.ttf' 'fonts/ttfs/Merriweather-LightText.ttf' 'fonts/ttfs/Merriweather-LightTextNarrow.ttf' 'fonts/ttfs/Merriweather-LightTextWide.ttf' 'fonts/ttfs/Merriweather-LightWide.ttf' 'fonts/ttfs/Merriweather-Regular.ttf' 'fonts/ttfs/Merriweather-RegularDisplay.ttf' 'fonts/ttfs/Merriweather-RegularDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-RegularDisplayWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-RegularHeadingWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadling.ttf' 'fonts/ttfs/Merriweather-RegularNarrow.ttf' 'fonts/ttfs/Merriweather-RegularText.ttf' 'fonts/ttfs/Merriweather-RegularTextNarrow.ttf' 'fonts/ttfs/Merriweather-RegularTextWide.ttf' 'fonts/ttfs/Merriweather-RegularWide.ttf' 'fonts/variable/Merriweather-Italic-VF.ttf' 'fonts/variable/Merriweather-Roman-VF.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/ttfs/Merriweather-Black.ttf' 'fonts/ttfs/Merriweather-BlackDisplay.ttf' 'fonts/ttfs/Merriweather-BlackDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BlackDisplayWide.ttf' 'fonts/ttfs/Merriweather-BlackHeading.ttf' 'fonts/ttfs/Merriweather-BlackHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BlackHeadingWide.ttf' 'fonts/ttfs/Merriweather-BlackItalic.ttf' 'fonts/ttfs/Merriweather-BlackNarrow.ttf' 'fonts/ttfs/Merriweather-BlackText.ttf' 'fonts/ttfs/Merriweather-BlackTextNarrow.ttf' 'fonts/ttfs/Merriweather-BlackTextWide.ttf' 'fonts/ttfs/Merriweather-BlackWide.ttf' 'fonts/ttfs/Merriweather-Bold.ttf' 'fonts/ttfs/Merriweather-BoldDisplay.ttf' 'fonts/ttfs/Merriweather-BoldDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BoldDisplayWide.ttf' 'fonts/ttfs/Merriweather-BoldHeading.ttf' 'fonts/ttfs/Merriweather-BoldHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BoldHeadingWide.ttf' 'fonts/ttfs/Merriweather-BoldItalic.ttf' 'fonts/ttfs/Merriweather-BoldNarrow.ttf' 'fonts/ttfs/Merriweather-BoldText.ttf' 'fonts/ttfs/Merriweather-BoldTextNarrow.ttf' 'fonts/ttfs/Merriweather-BoldTextWide.ttf' 'fonts/ttfs/Merriweather-BoldWide.ttf' 'fonts/ttfs/Merriweather-Italic.ttf' 'fonts/ttfs/Merriweather-Light.ttf' 'fonts/ttfs/Merriweather-LightDisplay.ttf' 'fonts/ttfs/Merriweather-LightDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-LightDisplayWide.ttf' 'fonts/ttfs/Merriweather-LightHeading.ttf' 'fonts/ttfs/Merriweather-LightHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-LightHeadingWide.ttf' 'fonts/ttfs/Merriweather-LightItalic.ttf' 'fonts/ttfs/Merriweather-LightNarrow.ttf' 'fonts/ttfs/Merriweather-LightText.ttf' 'fonts/ttfs/Merriweather-LightTextNarrow.ttf' 'fonts/ttfs/Merriweather-LightTextWide.ttf' 'fonts/ttfs/Merriweather-LightWide.ttf' 'fonts/ttfs/Merriweather-Regular.ttf' 'fonts/ttfs/Merriweather-RegularDisplay.ttf' 'fonts/ttfs/Merriweather-RegularDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-RegularDisplayWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-RegularHeadingWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadling.ttf' 'fonts/ttfs/Merriweather-RegularNarrow.ttf' 'fonts/ttfs/Merriweather-RegularText.ttf' 'fonts/ttfs/Merriweather-RegularTextNarrow.ttf' 'fonts/ttfs/Merriweather-RegularTextWide.ttf' 'fonts/ttfs/Merriweather-RegularWide.ttf' 'fonts/variable/Merriweather-Italic-VF.ttf' 'fonts/variable/Merriweather-Roman-VF.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sorkintype-merriweather-fonts appstream file"
cat > "org.altlinux.sorkintype-merriweather-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sorkintype-merriweather-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SorkinType Merriweather</name>
  <summary><![CDATA[Merriweather, a warm space-saving serif font family]]></summary>
  <description>
    <p><![CDATA[Merriweather offers a Renaissance warmth while using proportions which are]]></p><p><![CDATA[space-saving. It is suitable for editorial design, news and other kinds of]]></p><p><![CDATA[space sensitive typography.]]></p> Merriweather was designed to be a text face that is pleasant to read on screens. It features a very large x height, slightly condensed letter-forms, a mild diagonal stress, sturdy serifs and open forms
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sorkintype-merriweather-fonts
echo "" > "sorkintype-merriweather-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo "%%dir %_fontsdir/ttf/sorkintype-merriweather" >> "sorkintype-merriweather-fonts.list"
install -m 0644 -vp "fonts/ttfs/Merriweather-Black.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-Black.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackDisplay.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackDisplay.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackDisplayNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackDisplayNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackDisplayWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackDisplayWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackHeading.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackHeading.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackHeadingNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackHeadingNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackHeadingWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackHeadingWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackItalic.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackText.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackText.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackTextNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackTextNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackTextWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackTextWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BlackWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BlackWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-Bold.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-Bold.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldDisplay.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldDisplay.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldDisplayNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldDisplayNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldDisplayWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldDisplayWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldHeading.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldHeading.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldHeadingNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldHeadingNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldHeadingWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldHeadingWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldItalic.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldText.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldText.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldTextNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldTextNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldTextWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldTextWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-BoldWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-BoldWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-Italic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-Italic.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-Light.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-Light.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightDisplay.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightDisplay.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightDisplayNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightDisplayNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightDisplayWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightDisplayWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightHeading.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightHeading.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightHeadingNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightHeadingNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightHeadingWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightHeadingWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightItalic.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightText.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightText.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightTextNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightTextNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightTextWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightTextWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-LightWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-LightWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-Regular.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-Regular.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularDisplay.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularDisplay.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularDisplayNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularDisplayNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularDisplayWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularDisplayWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularHeadingNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularHeadingNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularHeadingWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularHeadingWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularHeadling.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularHeadling.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularText.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularText.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularTextNarrow.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularTextNarrow.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularTextWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularTextWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/ttfs/Merriweather-RegularWide.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/ttfs/Merriweather-RegularWide.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/variable/Merriweather-Italic-VF.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/variable/Merriweather-Italic-VF.ttf")\" >> 'sorkintype-merriweather-fonts.list'
install -m 0644 -vp "fonts/variable/Merriweather-Roman-VF.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather/
echo \"%_fontsdir/ttf/sorkintype-merriweather//$(basename "fonts/variable/Merriweather-Roman-VF.ttf")\" >> 'sorkintype-merriweather-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/ttfs/Merriweather-Black.ttf' 'fonts/ttfs/Merriweather-BlackDisplay.ttf' 'fonts/ttfs/Merriweather-BlackDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BlackDisplayWide.ttf' 'fonts/ttfs/Merriweather-BlackHeading.ttf' 'fonts/ttfs/Merriweather-BlackHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BlackHeadingWide.ttf' 'fonts/ttfs/Merriweather-BlackItalic.ttf' 'fonts/ttfs/Merriweather-BlackNarrow.ttf' 'fonts/ttfs/Merriweather-BlackText.ttf' 'fonts/ttfs/Merriweather-BlackTextNarrow.ttf' 'fonts/ttfs/Merriweather-BlackTextWide.ttf' 'fonts/ttfs/Merriweather-BlackWide.ttf' 'fonts/ttfs/Merriweather-Bold.ttf' 'fonts/ttfs/Merriweather-BoldDisplay.ttf' 'fonts/ttfs/Merriweather-BoldDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-BoldDisplayWide.ttf' 'fonts/ttfs/Merriweather-BoldHeading.ttf' 'fonts/ttfs/Merriweather-BoldHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-BoldHeadingWide.ttf' 'fonts/ttfs/Merriweather-BoldItalic.ttf' 'fonts/ttfs/Merriweather-BoldNarrow.ttf' 'fonts/ttfs/Merriweather-BoldText.ttf' 'fonts/ttfs/Merriweather-BoldTextNarrow.ttf' 'fonts/ttfs/Merriweather-BoldTextWide.ttf' 'fonts/ttfs/Merriweather-BoldWide.ttf' 'fonts/ttfs/Merriweather-Italic.ttf' 'fonts/ttfs/Merriweather-Light.ttf' 'fonts/ttfs/Merriweather-LightDisplay.ttf' 'fonts/ttfs/Merriweather-LightDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-LightDisplayWide.ttf' 'fonts/ttfs/Merriweather-LightHeading.ttf' 'fonts/ttfs/Merriweather-LightHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-LightHeadingWide.ttf' 'fonts/ttfs/Merriweather-LightItalic.ttf' 'fonts/ttfs/Merriweather-LightNarrow.ttf' 'fonts/ttfs/Merriweather-LightText.ttf' 'fonts/ttfs/Merriweather-LightTextNarrow.ttf' 'fonts/ttfs/Merriweather-LightTextWide.ttf' 'fonts/ttfs/Merriweather-LightWide.ttf' 'fonts/ttfs/Merriweather-Regular.ttf' 'fonts/ttfs/Merriweather-RegularDisplay.ttf' 'fonts/ttfs/Merriweather-RegularDisplayNarrow.ttf' 'fonts/ttfs/Merriweather-RegularDisplayWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadingNarrow.ttf' 'fonts/ttfs/Merriweather-RegularHeadingWide.ttf' 'fonts/ttfs/Merriweather-RegularHeadling.ttf' 'fonts/ttfs/Merriweather-RegularNarrow.ttf' 'fonts/ttfs/Merriweather-RegularText.ttf' 'fonts/ttfs/Merriweather-RegularTextNarrow.ttf' 'fonts/ttfs/Merriweather-RegularTextWide.ttf' 'fonts/ttfs/Merriweather-RegularWide.ttf' 'fonts/variable/Merriweather-Italic-VF.ttf' 'fonts/variable/Merriweather-Roman-VF.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sorkintype-merriweather-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sorkintype-merriweather-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sorkintype-merriweather-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sorkintype-merriweather-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'requirements.txt' 'TRADEMARKS.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "sorkintype-merriweather-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sorkintype-merriweather-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sorkintype-merriweather-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sorkintype-merriweather-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sorkintype-merriweather -f sorkintype-merriweather-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documents/*

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.008-alt1_6
- new version

