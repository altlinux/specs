Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname uswds-public-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname uswds-public-sans-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/uswds/public-sans/
Version:            1.008
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/uswds/public-sans/
%global forgesource https://github.com/uswds/public-sans//archive/1.008/public-sans-1.008.tar.gz
%global archivename public-sans-1.008
%global archiveext tar.gz
%global archiveurl https://github.com/uswds/public-sans//archive/1.008/public-sans-1.008.tar.gz
%global topdir public-sans-1.008
%global extractdir public-sans-1.008
%global repo public-sans
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 1.008
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

Release: alt1_5
URL:     https://public-sans.digital.gov/

%global foundry           USWDS
%global fontlicense       OFL
%global fontlicenses      LICENSE.md
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Public Sans
%global fontsummary       A strong, neutral, principles-driven, sans-serif Latin font family
%global fonts             binaries/otf/*otf binaries/variable/*ttf
%global fontdescription   \
Public Sans is a fork of the Libre Franklin font family. Libre Franklin is a\
reinterpretation and expansion of the 1912 Morris Fuller Bentona.'s classic.\
Public Sans has many similarities with its parent, but diverges enough in its\
particulars that its effect is distinct.\
\
Overall, Public Sans differs from Libre Franklin in its focus on long form\
reading and neutral UI applicability. It takes inspiration from geometric sans\
faces of the 20th century, as well as the original Franklins of the 19th,\
resulting in something of a mongrel face that retains its American origin.\
\
Public Sans is designed to work well with Apple and Google system fonts as the\
base in its font stack. Ita.'s designed to have metrics most similar to SF Pro\
Text (the Apple system font) and to fall somewhere between SF Pro Text and\
Roboto (the Google system font) in its overall size and appearance.

Source0:  %{forgesource}
Source10: 58-uswds-public-sans-fonts.xml

Name:           fonts-otf-uswds-public-sans
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n public-sans-1.008
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'binaries/otf/PublicSans-Black.otf' 'binaries/otf/PublicSans-BlackItalic.otf' 'binaries/otf/PublicSans-Bold.otf' 'binaries/otf/PublicSans-BoldItalic.otf' 'binaries/otf/PublicSans-ExtraBold.otf' 'binaries/otf/PublicSans-ExtraBoldItalic.otf' 'binaries/otf/PublicSans-ExtraLight.otf' 'binaries/otf/PublicSans-ExtraLightItalic.otf' 'binaries/otf/PublicSans-Italic.otf' 'binaries/otf/PublicSans-Light.otf' 'binaries/otf/PublicSans-LightItalic.otf' 'binaries/otf/PublicSans-Medium.otf' 'binaries/otf/PublicSans-MediumItalic.otf' 'binaries/otf/PublicSans-Regular.otf' 'binaries/otf/PublicSans-SemiBold.otf' 'binaries/otf/PublicSans-SemiBoldItalic.otf' 'binaries/otf/PublicSans-Thin.otf' 'binaries/otf/PublicSans-ThinItalic.otf' 'binaries/variable/Public-Sans-Italic-VF.ttf' 'binaries/variable/Public-Sans-Roman-VF.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'binaries/otf/PublicSans-Black.otf' 'binaries/otf/PublicSans-BlackItalic.otf' 'binaries/otf/PublicSans-Bold.otf' 'binaries/otf/PublicSans-BoldItalic.otf' 'binaries/otf/PublicSans-ExtraBold.otf' 'binaries/otf/PublicSans-ExtraBoldItalic.otf' 'binaries/otf/PublicSans-ExtraLight.otf' 'binaries/otf/PublicSans-ExtraLightItalic.otf' 'binaries/otf/PublicSans-Italic.otf' 'binaries/otf/PublicSans-Light.otf' 'binaries/otf/PublicSans-LightItalic.otf' 'binaries/otf/PublicSans-Medium.otf' 'binaries/otf/PublicSans-MediumItalic.otf' 'binaries/otf/PublicSans-Regular.otf' 'binaries/otf/PublicSans-SemiBold.otf' 'binaries/otf/PublicSans-SemiBoldItalic.otf' 'binaries/otf/PublicSans-Thin.otf' 'binaries/otf/PublicSans-ThinItalic.otf' 'binaries/variable/Public-Sans-Italic-VF.ttf' 'binaries/variable/Public-Sans-Roman-VF.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the uswds-public-sans-fonts appstream file"
cat > "org.altlinux.uswds-public-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.uswds-public-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>USWDS Public Sans</name>
  <summary><![CDATA[A strong, neutral, principles-driven, sans-serif Latin font family]]></summary>
  <description>
    <p><![CDATA[Public Sans is a fork of the Libre Franklin font family. Libre Franklin is a]]></p><p><![CDATA[reinterpretation and expansion of the 1912 Morris Fuller Benton’s classic.]]></p><p><![CDATA[Public Sans has many similarities with its parent, but diverges enough in its]]></p><p><![CDATA[particulars that its effect is distinct.]]></p> Overall, Public Sans differs from Libre Franklin in its focus on long form reading and neutral UI applicability. It takes inspiration from geometric sans faces of the 20th century, as well as the original Franklins of the 19th, resulting in something of a mongrel face that retains its American origin. Public Sans is designed to work well with Apple and Google system fonts as the base in its font stack. It’s designed to have metrics most similar to SF Pro Text (the Apple system font) and to fall somewhere between SF Pro Text and Roboto (the Google system font) in its overall size and appearance.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://public-sans.digital.gov/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing uswds-public-sans-fonts
echo "" > "uswds-public-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/uswds-public-sans/
echo "%%dir %_fontsdir/otf/uswds-public-sans" >> "uswds-public-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/uswds-public-sans/
echo "%%dir %_fontsdir/ttf/uswds-public-sans" >> "uswds-public-sans-fonts.list"
install -m 0644 -vp "binaries/otf/PublicSans-Black.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Black.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-BlackItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-BlackItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Bold.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Bold.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-BoldItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-BoldItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-ExtraBold.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-ExtraBold.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-ExtraBoldItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-ExtraLight.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-ExtraLight.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-ExtraLightItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Italic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Italic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Light.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Light.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-LightItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-LightItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Medium.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Medium.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-MediumItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-MediumItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Regular.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Regular.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-SemiBold.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-SemiBold.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-SemiBoldItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-Thin.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-Thin.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/otf/PublicSans-ThinItalic.otf" %buildroot%_fontsdir/otf/uswds-public-sans/
echo \"%_fontsdir/otf/uswds-public-sans//$(basename "binaries/otf/PublicSans-ThinItalic.otf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/variable/Public-Sans-Italic-VF.ttf" %buildroot%_fontsdir/ttf/uswds-public-sans/
echo \"%_fontsdir/ttf/uswds-public-sans//$(basename "binaries/variable/Public-Sans-Italic-VF.ttf")\" >> 'uswds-public-sans-fonts.list'
install -m 0644 -vp "binaries/variable/Public-Sans-Roman-VF.ttf" %buildroot%_fontsdir/ttf/uswds-public-sans/
echo \"%_fontsdir/ttf/uswds-public-sans//$(basename "binaries/variable/Public-Sans-Roman-VF.ttf")\" >> 'uswds-public-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'binaries/otf/PublicSans-Black.otf' 'binaries/otf/PublicSans-BlackItalic.otf' 'binaries/otf/PublicSans-Bold.otf' 'binaries/otf/PublicSans-BoldItalic.otf' 'binaries/otf/PublicSans-ExtraBold.otf' 'binaries/otf/PublicSans-ExtraBoldItalic.otf' 'binaries/otf/PublicSans-ExtraLight.otf' 'binaries/otf/PublicSans-ExtraLightItalic.otf' 'binaries/otf/PublicSans-Italic.otf' 'binaries/otf/PublicSans-Light.otf' 'binaries/otf/PublicSans-LightItalic.otf' 'binaries/otf/PublicSans-Medium.otf' 'binaries/otf/PublicSans-MediumItalic.otf' 'binaries/otf/PublicSans-Regular.otf' 'binaries/otf/PublicSans-SemiBold.otf' 'binaries/otf/PublicSans-SemiBoldItalic.otf' 'binaries/otf/PublicSans-Thin.otf' 'binaries/otf/PublicSans-ThinItalic.otf' 'binaries/variable/Public-Sans-Italic-VF.ttf' 'binaries/variable/Public-Sans-Roman-VF.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "uswds-public-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "uswds-public-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.uswds-public-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "uswds-public-sans-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'CONTRIBUTING.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "uswds-public-sans-fonts.list"
done

for fontlicense in 'LICENSE.md'; do
  echo %%doc "'${fontlicense}'" >> "uswds-public-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'uswds-public-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'uswds-public-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-uswds-public-sans -f uswds-public-sans-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.008-alt1_5
- new version

