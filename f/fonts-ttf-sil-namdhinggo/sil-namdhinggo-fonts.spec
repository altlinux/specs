Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-namdhinggo-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-namdhinggo-fonts
# SPDX-License-Identifier: MIT
Version: 1.004
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Namdhinggo SIL
%global fontsummary       Namdhinggo SIL, a font family for the Limbu writing system of Nepal
%global projectname       namdhinggo
%global archivename       NamdhinggoSIL-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Namdhinggo provides glyphs for all Limbu characters and some Latin.\
\
The Limbu, or Kirat Sirijonga, script is used by around 400A.000 people in Nepal\
and India. This Unicode-encoded font has been designed to support literacy and\
materials development in the Limbu language.\
\
According to traditional histories the Limbu script was developed by King\
Sirijonga in the 9th Century. It then fell out of use before being reintroduced\
in the 18th century by Teongsi Sirijonga (1704-1741) whom many felt to be the\
reincarnation of the first Sirijonga. The modern Sirijonga was apparently\
martyred in 1741 for the sake of this script by lamas in Sikkim. The script was\
named a.'Sirijongaa.' in his honor by the Limbu scholar Iman Singh Chemjong.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 66-sil-namdhinggo-fonts.xml

Name:           fonts-ttf-sil-namdhinggo
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
%setup -q -n NamdhinggoSIL
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'NamdhinggoSIL-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'NamdhinggoSIL-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-namdhinggo-fonts appstream file"
cat > "org.altlinux.sil-namdhinggo-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-namdhinggo-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Namdhinggo SIL</name>
  <summary><![CDATA[Namdhinggo SIL, a font family for the Limbu writing system of Nepal]]></summary>
  <description>
    <p><![CDATA[Namdhinggo provides glyphs for all Limbu characters and some Latin.]]></p> The Limbu, or Kirat Sirijonga, script is used by around 400 000 people in Nepal and India. This Unicode-encoded font has been designed to support literacy and materials development in the Limbu language. According to traditional histories the Limbu script was developed by King Sirijonga in the 9th Century. It then fell out of use before being reintroduced in the 18th century by Teongsi Sirijonga (1704-1741) whom many felt to be the reincarnation of the first Sirijonga. The modern Sirijonga was apparently martyred in 1741 for the sake of this script by lamas in Sikkim. The script was named ‘Sirijonga’ in his honor by the Limbu scholar Iman Singh Chemjong.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-namdhinggo-fonts
echo "" > "sil-namdhinggo-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-namdhinggo/
echo "%%dir %_fontsdir/ttf/sil-namdhinggo" >> "sil-namdhinggo-fonts.list"
install -m 0644 -vp "NamdhinggoSIL-R.ttf" %buildroot%_fontsdir/ttf/sil-namdhinggo/
echo \"%_fontsdir/ttf/sil-namdhinggo//$(basename "NamdhinggoSIL-R.ttf")\" >> 'sil-namdhinggo-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'NamdhinggoSIL-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-namdhinggo-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-namdhinggo-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-namdhinggo-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-namdhinggo-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-namdhinggo-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-namdhinggo-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-namdhinggo-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-namdhinggo-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-namdhinggo -f sil-namdhinggo-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.004-alt1_5
- new version

