Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-sophia-nubian-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-sophia-nubian-fonts
# SPDX-License-Identifier: MIT
Version: 1.0
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Sophia Nubian
%global fontsummary       Sophia Nubian, a font family for Nubian languages which use the Coptic script
%global projectname       sophianubian
%global archivename       SN%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Sophia Nubian is a sans serif font family based on SIL Sophia. Its primary\
purpose is to provide adequate representation for Nubian languages which use\
the Coptic script. Since Nubian languages do not use casing, uppercase\
characters are not included in this font. A basic set of Latin glyphs is also\
provided.

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-sil-sophia-nubian-fonts.xml

Name:           fonts-ttf-sil-sophia-nubian
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
  for font in 'SNB.ttf' 'SNBI.ttf' 'SNI.ttf' 'SNR.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'SNB.ttf' 'SNBI.ttf' 'SNI.ttf' 'SNR.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-sophia-nubian-fonts appstream file"
cat > "org.altlinux.sil-sophia-nubian-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-sophia-nubian-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Sophia Nubian</name>
  <summary><![CDATA[Sophia Nubian, a font family for Nubian languages which use the Coptic script]]></summary>
  <description>
    <p><![CDATA[Sophia Nubian is a sans serif font family based on SIL Sophia. Its primary]]></p><p><![CDATA[purpose is to provide adequate representation for Nubian languages which use]]></p><p><![CDATA[the Coptic script. Since Nubian languages do not use casing, uppercase]]></p><p><![CDATA[characters are not included in this font. A basic set of Latin glyphs is also]]></p><p><![CDATA[provided.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-sophia-nubian-fonts
echo "" > "sil-sophia-nubian-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-sophia-nubian/
echo "%%dir %_fontsdir/ttf/sil-sophia-nubian" >> "sil-sophia-nubian-fonts.list"
install -m 0644 -vp "SNB.ttf" %buildroot%_fontsdir/ttf/sil-sophia-nubian/
echo \"%_fontsdir/ttf/sil-sophia-nubian//$(basename "SNB.ttf")\" >> 'sil-sophia-nubian-fonts.list'
install -m 0644 -vp "SNBI.ttf" %buildroot%_fontsdir/ttf/sil-sophia-nubian/
echo \"%_fontsdir/ttf/sil-sophia-nubian//$(basename "SNBI.ttf")\" >> 'sil-sophia-nubian-fonts.list'
install -m 0644 -vp "SNI.ttf" %buildroot%_fontsdir/ttf/sil-sophia-nubian/
echo \"%_fontsdir/ttf/sil-sophia-nubian//$(basename "SNI.ttf")\" >> 'sil-sophia-nubian-fonts.list'
install -m 0644 -vp "SNR.ttf" %buildroot%_fontsdir/ttf/sil-sophia-nubian/
echo \"%_fontsdir/ttf/sil-sophia-nubian//$(basename "SNR.ttf")\" >> 'sil-sophia-nubian-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'SNB.ttf' 'SNBI.ttf' 'SNI.ttf' 'SNR.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-sophia-nubian-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-sophia-nubian-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-sophia-nubian-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-sophia-nubian-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'Readme.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-sophia-nubian-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-sophia-nubian-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-sophia-nubian-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-sophia-nubian-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-sophia-nubian -f sil-sophia-nubian-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt1_5
- new version

