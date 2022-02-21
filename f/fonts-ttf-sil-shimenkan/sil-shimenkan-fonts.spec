Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-shimenkan-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-shimenkan-fonts
# SPDX-License-Identifier: MIT
Version: 1.000
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Shimenkan
%global fontsummary       Shimenkan, a Miao (Pollard) script font family
%global projectname       shimenkan
%global archivename       Shimenkan-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Recommends: font(sourcesanspro)\

%global fonts             *.ttf
%global fontdescription   \
The Shimenkan font family supports the broad variety of writing systems that\
use the Miao (Pollard) script. It leverages OpenType features to provide the\
correct alternates and positioning for each language. Therefore, making use of\
this font requires good OpenType support in applications.\
\
The Latin glyphs are based on the OFL-licensed Source Sans Pro fonts. The Miao\
glyphs are designed to harmonize with the Latin, but remain true to the unique\
characteristics of Miao writing systems. The project is inspired by, but not\
based on, the Miao Unicode project.\
\
Languages that use the Miao script have different positioning and glyphs\
shaping conventions. Accessing the correct alternates and positioning for a\
given language requires application support for the corresponding OpenType\
feature.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-sil-shimenkan-fonts.xml

Name:           fonts-ttf-sil-shimenkan
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
%setup -q -n %{archivename}
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'Shimenkan-Bold.ttf' 'Shimenkan-Regular.ttf' 'ShimenkanBook-Bold.ttf' 'ShimenkanBook-Regular.ttf' 'ShimenkanExtraLight-Bold.ttf' 'ShimenkanExtraLight-Regular.ttf' 'ShimenkanLight-Bold.ttf' 'ShimenkanLight-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Shimenkan-Bold.ttf' 'Shimenkan-Regular.ttf' 'ShimenkanBook-Bold.ttf' 'ShimenkanBook-Regular.ttf' 'ShimenkanExtraLight-Bold.ttf' 'ShimenkanExtraLight-Regular.ttf' 'ShimenkanLight-Bold.ttf' 'ShimenkanLight-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-shimenkan-fonts appstream file"
cat > "org.altlinux.sil-shimenkan-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-shimenkan-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Shimenkan</name>
  <summary><![CDATA[Shimenkan, a Miao (Pollard) script font family]]></summary>
  <description>
    <p><![CDATA[The Shimenkan font family supports the broad variety of writing systems that]]></p><p><![CDATA[use the Miao (Pollard) script. It leverages OpenType features to provide the]]></p><p><![CDATA[correct alternates and positioning for each language. Therefore, making use of]]></p><p><![CDATA[this font requires good OpenType support in applications.]]></p> The Latin glyphs are based on the OFL-licensed Source Sans Pro fonts. The Miao glyphs are designed to harmonize with the Latin, but remain true to the unique characteristics of Miao writing systems. The project is inspired by, but not based on, the Miao Unicode project. Languages that use the Miao script have different positioning and glyphs shaping conventions. Accessing the correct alternates and positioning for a given language requires application support for the corresponding OpenType feature.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-shimenkan-fonts
echo "" > "sil-shimenkan-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-shimenkan/
echo "%%dir %_fontsdir/ttf/sil-shimenkan" >> "sil-shimenkan-fonts.list"
install -m 0644 -vp "Shimenkan-Bold.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "Shimenkan-Bold.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "Shimenkan-Regular.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "Shimenkan-Regular.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanBook-Bold.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanBook-Bold.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanBook-Regular.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanBook-Regular.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanExtraLight-Bold.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanExtraLight-Bold.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanExtraLight-Regular.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanExtraLight-Regular.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanLight-Bold.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanLight-Bold.ttf")\" >> 'sil-shimenkan-fonts.list'
install -m 0644 -vp "ShimenkanLight-Regular.ttf" %buildroot%_fontsdir/ttf/sil-shimenkan/
echo \"%_fontsdir/ttf/sil-shimenkan//$(basename "ShimenkanLight-Regular.ttf")\" >> 'sil-shimenkan-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Shimenkan-Bold.ttf' 'Shimenkan-Regular.ttf' 'ShimenkanBook-Bold.ttf' 'ShimenkanBook-Regular.ttf' 'ShimenkanExtraLight-Bold.ttf' 'ShimenkanExtraLight-Regular.ttf' 'ShimenkanLight-Bold.ttf' 'ShimenkanLight-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-shimenkan-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-shimenkan-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-shimenkan-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-shimenkan-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-shimenkan-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-shimenkan-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-shimenkan-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-shimenkan-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-shimenkan -f sil-shimenkan-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.000-alt1_5
- new version

