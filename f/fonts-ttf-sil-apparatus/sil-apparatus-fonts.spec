Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-apparatus-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-apparatus-fonts
# SPDX-License-Identifier: MIT
Version: 1.0
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Apparatus SIL
%global fontsummary       Apparatus SIL, a font family for rendering Greek & Hebrew biblical texts
%global archivename       ApparatusSIL
%global projectname       %{archivename}
URL:                      https://scripts.sil.org/ApparatusSIL
%global fonts             *.ttf *.TTF
%global fontdescription   \
The Apparatus SIL font family was designed to provide most of the symbols\
needed to reproduce the textual apparatus found in major editions of Greek &\
Hebrew biblical texts. It is based on SIL Charis, a font family designed for\
optimum clarity and compactness when printed at small point sizes. This assures\
that both Charis SIL and Apparatus SIL can be used together in documents with a\
consistency of style.\
\
Most lines of text in the apparatus can be reproduced by combining the Greek\
and Hebrew fonts, transliteration (using a font such as Charis SIL), and the\
Apparatus SIL font.

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=AppSIL%{version}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 60-sil-apparatus-fonts.xml

Name:           fonts-ttf-sil-apparatus
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
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'AppSILR.ttf' 'AppSILB.TTF' 'AppSILBI.TTF' 'AppSILI.TTF'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AppSILR.ttf' 'AppSILB.TTF' 'AppSILBI.TTF' 'AppSILI.TTF'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-apparatus-fonts appstream file"
cat > "org.altlinux.sil-apparatus-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-apparatus-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Apparatus SIL</name>
  <summary><![CDATA[Apparatus SIL, a font family for rendering Greek & Hebrew biblical texts]]></summary>
  <description>
    <p><![CDATA[The Apparatus SIL font family was designed to provide most of the symbols]]></p><p><![CDATA[needed to reproduce the textual apparatus found in major editions of Greek &]]></p><p><![CDATA[Hebrew biblical texts. It is based on SIL Charis, a font family designed for]]></p><p><![CDATA[optimum clarity and compactness when printed at small point sizes. This assures]]></p><p><![CDATA[that both Charis SIL and Apparatus SIL can be used together in documents with a]]></p><p><![CDATA[consistency of style.]]></p> Most lines of text in the apparatus can be reproduced by combining the Greek and Hebrew fonts, transliteration (using a font such as Charis SIL), and the Apparatus SIL font.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/ApparatusSIL</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-apparatus-fonts
echo "" > "sil-apparatus-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-apparatus/
echo "%%dir %_fontsdir/ttf/sil-apparatus" >> "sil-apparatus-fonts.list"
install -m 0644 -vp "AppSILR.ttf" %buildroot%_fontsdir/ttf/sil-apparatus/
echo \"%_fontsdir/ttf/sil-apparatus//$(basename "AppSILR.ttf")\" >> 'sil-apparatus-fonts.list'
install -m 0644 -vp "AppSILB.TTF" %buildroot%_fontsdir/ttf/sil-apparatus/
echo \"%_fontsdir/ttf/sil-apparatus//$(basename "AppSILB.TTF")\" >> 'sil-apparatus-fonts.list'
install -m 0644 -vp "AppSILBI.TTF" %buildroot%_fontsdir/ttf/sil-apparatus/
echo \"%_fontsdir/ttf/sil-apparatus//$(basename "AppSILBI.TTF")\" >> 'sil-apparatus-fonts.list'
install -m 0644 -vp "AppSILI.TTF" %buildroot%_fontsdir/ttf/sil-apparatus/
echo \"%_fontsdir/ttf/sil-apparatus//$(basename "AppSILI.TTF")\" >> 'sil-apparatus-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'AppSILR.ttf' 'AppSILB.TTF' 'AppSILBI.TTF' 'AppSILI.TTF'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-apparatus-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-apparatus-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-apparatus-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-apparatus-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-apparatus-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-apparatus-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-apparatus-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-apparatus-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-apparatus -f sil-apparatus-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt1_5
- new version

