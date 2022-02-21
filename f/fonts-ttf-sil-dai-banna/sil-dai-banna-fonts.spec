Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-dai-banna-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-dai-banna-fonts
# SPDX-License-Identifier: MIT
Version: 2.200
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dai Banna SIL
%global fontsummary       Dai Banna SIL, a font family for rendering New Tai Lue (Xishuangbanna Dai)
%global projectname       daibanna
%global archivename       DaiBanna-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Dai Banna includes a complete set of New Tai Lue (Xishuangbanna Dai)\
consonants, vowels, tones, and digits, along with punctuation and other useful\
symbols. A basic set of Latin glyphs, including Arabic numerals, is also\
provided.\
\
The New Tai Lue script is used by approximately 300a..000 people who speak the\
Xishuangbanna Dai language in Yunnan, China.a.. It is a simplification of the Tai\
Tham (Old Tai Lue) script as used for this language for hundreds of years.\
\
The Dai News Department of Xishuangbanna Daily provided valuable advice during\
the development of this font family. Xishuangbanna Daily, established in 1957,\
is the largest newspaper company in Yunnan, China that publishes in the New Tai\
Lue script.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 65-sil-dai-banna-fonts.xml

Name:           fonts-ttf-sil-dai-banna
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
%setup -q -n dai-banna-%{version}
%linuxtext *.txt doc/*.txt

%build
# fontbuild 
fontnames=$(
  for font in 'DBSILBB.ttf' 'DBSILBC.ttf' 'DBSILBO.ttf' 'DBSILBR.ttf' 'DBSILLB.ttf' 'DBSILLC.ttf' 'DBSILLO.ttf' 'DBSILLR.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'DBSILBB.ttf' 'DBSILBC.ttf' 'DBSILBO.ttf' 'DBSILBR.ttf' 'DBSILLB.ttf' 'DBSILLC.ttf' 'DBSILLO.ttf' 'DBSILLR.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-dai-banna-fonts appstream file"
cat > "org.altlinux.sil-dai-banna-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-dai-banna-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Dai Banna SIL</name>
  <summary><![CDATA[Dai Banna SIL, a font family for rendering New Tai Lue (Xishuangbanna Dai)]]></summary>
  <description>
    <p><![CDATA[Dai Banna includes a complete set of New Tai Lue (Xishuangbanna Dai)]]></p><p><![CDATA[consonants, vowels, tones, and digits, along with punctuation and other useful]]></p><p><![CDATA[symbols. A basic set of Latin glyphs, including Arabic numerals, is also]]></p><p><![CDATA[provided.]]></p> The New Tai Lue script is used by approximately 300 000 people who speak the Xishuangbanna Dai language in Yunnan, China.  It is a simplification of the Tai Tham (Old Tai Lue) script as used for this language for hundreds of years. The Dai News Department of Xishuangbanna Daily provided valuable advice during the development of this font family. Xishuangbanna Daily, established in 1957, is the largest newspaper company in Yunnan, China that publishes in the New Tai Lue script.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-dai-banna-fonts
echo "" > "sil-dai-banna-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-dai-banna/
echo "%%dir %_fontsdir/ttf/sil-dai-banna" >> "sil-dai-banna-fonts.list"
install -m 0644 -vp "DBSILBB.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILBB.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILBC.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILBC.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILBO.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILBO.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILBR.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILBR.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILLB.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILLB.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILLC.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILLC.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILLO.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILLO.ttf")\" >> 'sil-dai-banna-fonts.list'
install -m 0644 -vp "DBSILLR.ttf" %buildroot%_fontsdir/ttf/sil-dai-banna/
echo \"%_fontsdir/ttf/sil-dai-banna//$(basename "DBSILLR.ttf")\" >> 'sil-dai-banna-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'DBSILBB.ttf' 'DBSILBC.ttf' 'DBSILBO.ttf' 'DBSILBR.ttf' 'DBSILLB.ttf' 'DBSILLC.ttf' 'DBSILLO.ttf' 'DBSILLR.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-dai-banna-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-dai-banna-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-dai-banna-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-dai-banna-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-dai-banna-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-dai-banna-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-dai-banna-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-dai-banna-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-dai-banna -f sil-dai-banna-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc doc/*.pdf doc/*.txt

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.200-alt1_5
- new version

