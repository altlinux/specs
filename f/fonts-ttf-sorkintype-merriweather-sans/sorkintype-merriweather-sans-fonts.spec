Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sorkintype-merriweather-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sorkintype-merriweather-sans-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/SorkinType/Merriweather-Sans
%global commit      f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/SorkinType/Merriweather-Sans
%global forgesource https://github.com/SorkinType/Merriweather-Sans/archive/f36d6e1eb17fd4eead50c320fc8313f5353c9f5f/Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f.tar.gz
%global archivename Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%global archiveext tar.gz
%global archiveurl https://github.com/SorkinType/Merriweather-Sans/archive/f36d6e1eb17fd4eead50c320fc8313f5353c9f5f/Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f.tar.gz
%global topdir Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%global extractdir Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
%global repo Merriweather-Sans
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit f36d6e1eb17fd4eead50c320fc8313f5353c9f5f
#global shortcommit %nil
#global branch %nil
%global version 1.008
#global date %nil
%global distprefix .gitf36d6e1
# FedoraForgeMeta2ALT: end generated meta

Version: 1.008
Release: alt1_6
URL:     %{forgeurl}

%global foundry           SorkinType
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Merriweather Sans
%global fontsummary       Merriweather Sans, a low-contrast semi-condensed sans-serif font family
%global fonts             fonts/ttfs/*ttf fonts/variable/*.ttf
%global fontdescription   \
Merriweather Sans is a low-contrast semi-condensed sans-serif font family\
designed to be readable at very small sizes. Merriweather Sans is traditional\
in feeling despite the modern shapes it has adopted for screens. It is a\
companion to the serif font family Merriweather.

Source0:  %{forgesource}
Source10: 57-sorkintype-merriweather-sans-fonts.xml

Name:           fonts-ttf-sorkintype-merriweather-sans
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
%setup -q -n Merriweather-Sans-f36d6e1eb17fd4eead50c320fc8313f5353c9f5f

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/ttfs/MerriweatherSans-Black.ttf' 'fonts/ttfs/MerriweatherSans-Bold.ttf' 'fonts/ttfs/MerriweatherSans-BoldItalic.ttf' 'fonts/ttfs/MerriweatherSans-Italic.ttf' 'fonts/ttfs/MerriweatherSans-Light.ttf' 'fonts/ttfs/MerriweatherSans-LightItalic.ttf' 'fonts/ttfs/MerriweatherSans-Regular.ttf' 'fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf' 'fonts/variable/MerriweatherSans-Italic-VF.ttf' 'fonts/variable/MerriweatherSans-Roman-VF.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/ttfs/MerriweatherSans-Black.ttf' 'fonts/ttfs/MerriweatherSans-Bold.ttf' 'fonts/ttfs/MerriweatherSans-BoldItalic.ttf' 'fonts/ttfs/MerriweatherSans-Italic.ttf' 'fonts/ttfs/MerriweatherSans-Light.ttf' 'fonts/ttfs/MerriweatherSans-LightItalic.ttf' 'fonts/ttfs/MerriweatherSans-Regular.ttf' 'fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf' 'fonts/variable/MerriweatherSans-Italic-VF.ttf' 'fonts/variable/MerriweatherSans-Roman-VF.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sorkintype-merriweather-sans-fonts appstream file"
cat > "org.altlinux.sorkintype-merriweather-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sorkintype-merriweather-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SorkinType Merriweather Sans</name>
  <summary><![CDATA[Merriweather Sans, a low-contrast semi-condensed sans-serif font family]]></summary>
  <description>
    <p><![CDATA[Merriweather Sans is a low-contrast semi-condensed sans-serif font family]]></p><p><![CDATA[designed to be readable at very small sizes. Merriweather Sans is traditional]]></p><p><![CDATA[in feeling despite the modern shapes it has adopted for screens. It is a]]></p><p><![CDATA[companion to the serif font family Merriweather.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sorkintype-merriweather-sans-fonts
echo "" > "sorkintype-merriweather-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo "%%dir %_fontsdir/ttf/sorkintype-merriweather-sans" >> "sorkintype-merriweather-sans-fonts.list"
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-Black.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-Black.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-Bold.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-Bold.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-BoldItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-BoldItalic.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-Italic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-Italic.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-Light.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-Light.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-LightItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-LightItalic.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-Regular.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-Regular.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/variable/MerriweatherSans-Italic-VF.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/variable/MerriweatherSans-Italic-VF.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
install -m 0644 -vp "fonts/variable/MerriweatherSans-Roman-VF.ttf" %buildroot%_fontsdir/ttf/sorkintype-merriweather-sans/
echo \"%_fontsdir/ttf/sorkintype-merriweather-sans//$(basename "fonts/variable/MerriweatherSans-Roman-VF.ttf")\" >> 'sorkintype-merriweather-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/ttfs/MerriweatherSans-Black.ttf' 'fonts/ttfs/MerriweatherSans-Bold.ttf' 'fonts/ttfs/MerriweatherSans-BoldItalic.ttf' 'fonts/ttfs/MerriweatherSans-Italic.ttf' 'fonts/ttfs/MerriweatherSans-Light.ttf' 'fonts/ttfs/MerriweatherSans-LightItalic.ttf' 'fonts/ttfs/MerriweatherSans-Regular.ttf' 'fonts/ttfs/MerriweatherSans-UltraBoldItalic.ttf' 'fonts/variable/MerriweatherSans-Italic-VF.ttf' 'fonts/variable/MerriweatherSans-Roman-VF.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sorkintype-merriweather-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sorkintype-merriweather-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sorkintype-merriweather-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sorkintype-merriweather-sans-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'requirements.txt' 'TRADEMARKS.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "sorkintype-merriweather-sans-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sorkintype-merriweather-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sorkintype-merriweather-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sorkintype-merriweather-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sorkintype-merriweather-sans -f sorkintype-merriweather-sans-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.008-alt1_6
- new version

