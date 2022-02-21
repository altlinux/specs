Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-tagmukay-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-tagmukay-fonts
# SPDX-License-Identifier: MIT
Version: 2.000
Release: alt1_6

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Tagmukay
%global fontsummary       Tagmukay, a Shifinagh font that supports the Tawallammat dialect of Tamajaq
%global projectname       tagmukay
%global archivename       Tagmukay-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Tagmukay is a Shifinagh script font with support for the Tawallammat Tamajaq\
language. The script name is more commonly spelled Tifinagh, but Shifinagh is\
the preferred spelling in the region where Tawallammat Tamajaq is spoken.\
\
Tawallammat Tamajaq, when written in the Shifinagh script, follows the\
traditional a.'consonant onlya.' way of writing this ancient script. The Tagmukay\
font family has these consonants and also the logic needed to form the\
bi-consonant ligatures needed to distinguish between vocalic and non-vocalic\
consonant clusters.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-sil-tagmukay-fonts.xml

Name:           fonts-ttf-sil-tagmukay
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
%linuxtext *.txt documentation/*.txt
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'Tagmukay-Bold.ttf' 'Tagmukay-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Tagmukay-Bold.ttf' 'Tagmukay-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-tagmukay-fonts appstream file"
cat > "org.altlinux.sil-tagmukay-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-tagmukay-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Tagmukay</name>
  <summary><![CDATA[Tagmukay, a Shifinagh font that supports the Tawallammat dialect of Tamajaq]]></summary>
  <description>
    <p><![CDATA[Tagmukay is a Shifinagh script font with support for the Tawallammat Tamajaq]]></p><p><![CDATA[language. The script name is more commonly spelled Tifinagh, but Shifinagh is]]></p><p><![CDATA[the preferred spelling in the region where Tawallammat Tamajaq is spoken.]]></p> Tawallammat Tamajaq, when written in the Shifinagh script, follows the traditional “consonant only” way of writing this ancient script. The Tagmukay font family has these consonants and also the logic needed to form the bi-consonant ligatures needed to distinguish between vocalic and non-vocalic consonant clusters.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-tagmukay-fonts
echo "" > "sil-tagmukay-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-tagmukay/
echo "%%dir %_fontsdir/ttf/sil-tagmukay" >> "sil-tagmukay-fonts.list"
install -m 0644 -vp "Tagmukay-Bold.ttf" %buildroot%_fontsdir/ttf/sil-tagmukay/
echo \"%_fontsdir/ttf/sil-tagmukay//$(basename "Tagmukay-Bold.ttf")\" >> 'sil-tagmukay-fonts.list'
install -m 0644 -vp "Tagmukay-Regular.ttf" %buildroot%_fontsdir/ttf/sil-tagmukay/
echo \"%_fontsdir/ttf/sil-tagmukay//$(basename "Tagmukay-Regular.ttf")\" >> 'sil-tagmukay-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Tagmukay-Bold.ttf' 'Tagmukay-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-tagmukay-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-tagmukay-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-tagmukay-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-tagmukay-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt' 'documentation/Tagmukay-Glyphs.odt' 'documentation/Tagmukay-SmartFontFeatures.odt'; do
  echo %%doc "'${fontdoc}'" >> "sil-tagmukay-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-tagmukay-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-tagmukay-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-tagmukay-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-tagmukay -f sil-tagmukay-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.000-alt1_6
- new version

