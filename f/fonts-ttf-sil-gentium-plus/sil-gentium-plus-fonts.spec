Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-gentium-plus-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-gentium-plus-fonts
# SPDX-License-Identifier: MIT
Version: 5.000
Release: alt1_9

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gentium Plus
%global fontsummary       Gentium Plus, a Latin/Greek/Cyrillic font family
%global projectname       gentium
%global archivename       GentiumPlus-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Suggests: font(gentiumbasic)\

%global fonts             *.ttf
%global fontdescription   \
Gentium is a font family designed to enable the diverse ethnic groups around\
the world who use the Latin, Cyrillic and Greek scripts to produce readable,\
high-quality publications.\
\
Gentium was a winner of the TDC2003 Type Design Competition and was exhibited\
as part of the bukva:raz! exhibit at the UN Headquarters Main Lobby, 17 Jan a..\
13 Feb, 2002.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 60-sil-gentium-plus-fonts.xml

Name:           fonts-ttf-sil-gentium-plus
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

%build
# fontbuild 
fontnames=$(
  for font in 'GentiumPlus-I.ttf' 'GentiumPlus-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GentiumPlus-I.ttf' 'GentiumPlus-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-gentium-plus-fonts appstream file"
cat > "org.altlinux.sil-gentium-plus-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-gentium-plus-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Gentium Plus</name>
  <summary><![CDATA[Gentium Plus, a Latin/Greek/Cyrillic font family]]></summary>
  <description>
    <p><![CDATA[Gentium is a font family designed to enable the diverse ethnic groups around]]></p><p><![CDATA[the world who use the Latin, Cyrillic and Greek scripts to produce readable,]]></p><p><![CDATA[high-quality publications.]]></p> Gentium was a winner of the TDC2003 Type Design Competition and was exhibited as part of the bukva:raz! exhibit at the UN Headquarters Main Lobby, 17 Jan – 13 Feb, 2002.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-gentium-plus-fonts
echo "" > "sil-gentium-plus-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-gentium-plus/
echo "%%dir %_fontsdir/ttf/sil-gentium-plus" >> "sil-gentium-plus-fonts.list"
install -m 0644 -vp "GentiumPlus-I.ttf" %buildroot%_fontsdir/ttf/sil-gentium-plus/
echo \"%_fontsdir/ttf/sil-gentium-plus//$(basename "GentiumPlus-I.ttf")\" >> 'sil-gentium-plus-fonts.list'
install -m 0644 -vp "GentiumPlus-R.ttf" %buildroot%_fontsdir/ttf/sil-gentium-plus/
echo \"%_fontsdir/ttf/sil-gentium-plus//$(basename "GentiumPlus-R.ttf")\" >> 'sil-gentium-plus-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GentiumPlus-I.ttf' 'GentiumPlus-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-gentium-plus-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-gentium-plus-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-gentium-plus-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-gentium-plus-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'GENTIUM-FAQ.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt' 'documentation/GentiumPlus-features.odt'; do
  echo %%doc "'${fontdoc}'" >> "sil-gentium-plus-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-gentium-plus-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-gentium-plus-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-gentium-plus-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-gentium-plus -f sil-gentium-plus-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 5.000-alt1_9
- new version

