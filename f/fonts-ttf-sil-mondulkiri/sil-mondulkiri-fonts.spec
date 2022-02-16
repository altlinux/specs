Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-mondulkiri-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-mondulkiri-fonts
# SPDX-License-Identifier: MIT
Version: 7.100
Release: alt1_5
URL:     https://scripts.sil.org/Mondulkiri

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily0       Mondulkiri
%global fontsummary0      Khmer Mondulkiri, a Khmer script font family suited for very small print
%global fonts0            Mondulkiri*.ttf
%global fontdescription0  \
The Khmer Mondulkiri font family provides Unicode support for the Khmer script.\
It is very light and well suited for very small print.

%global fontfamily1       Busra
%global fontsummary1      Khmer Busra, a Khmer script font family suited for normal text
%global fonts1            Busra*.ttf
%global fontdescription1  \
The Khmer Busra font family provides Unicode support for the Khmer script. It\
is probably the best SIL font family for Khmer normal text. The regular font\
was formerly named a.'Khmer Mondulkiri Booka.' and the bold font was named a.'Khmer\
Mondulkiri SemiBolda.'.

%global archivename Mondulkiri-%{version}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-sil-mondulkiri-fonts.xml
Source11: 65-sil-busra-fonts.xml

Name:           fonts-ttf-sil-mondulkiri
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-sil-busra
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-sil-busra
%{?fontdescription1}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-sil-mondulkiri = %EVR
Requires:  fonts-ttf-sil-busra = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%setup -q -n %{archivename}
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in 'Mondulkiri-B.ttf' 'Mondulkiri-BI.ttf' 'Mondulkiri-I.ttf' 'Mondulkiri-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mondulkiri-B.ttf' 'Mondulkiri-BI.ttf' 'Mondulkiri-I.ttf' 'Mondulkiri-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-mondulkiri-fonts appstream file"
cat > "org.altlinux.sil-mondulkiri-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-mondulkiri-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Mondulkiri</name>
  <summary><![CDATA[Khmer Mondulkiri, a Khmer script font family suited for very small print]]></summary>
  <description>
    <p><![CDATA[The Khmer Mondulkiri font family provides Unicode support for the Khmer script.]]></p><p><![CDATA[It is very light and well suited for very small print.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'Busra-B.ttf' 'Busra-BI.ttf' 'Busra-I.ttf' 'Busra-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Busra-B.ttf' 'Busra-BI.ttf' 'Busra-I.ttf' 'Busra-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-fonts appstream file"
cat > "org.altlinux.sil-busra-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra</name>
  <summary><![CDATA[Khmer Busra, a Khmer script font family suited for normal text]]></summary>
  <description>
    <p><![CDATA[The Khmer Busra font family provides Unicode support for the Khmer script. It]]></p><p><![CDATA[is probably the best SIL font family for Khmer normal text. The regular font]]></p><p><![CDATA[was formerly named “Khmer Mondulkiri Book” and the bold font was named “Khmer]]></p><p><![CDATA[Mondulkiri SemiBold”.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-mondulkiri-fonts
echo "" > "sil-mondulkiri-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri" >> "sil-mondulkiri-fonts0.list"
install -m 0644 -vp "Mondulkiri-B.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Mondulkiri-B.ttf")\" >> 'sil-mondulkiri-fonts0.list'
install -m 0644 -vp "Mondulkiri-BI.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Mondulkiri-BI.ttf")\" >> 'sil-mondulkiri-fonts0.list'
install -m 0644 -vp "Mondulkiri-I.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Mondulkiri-I.ttf")\" >> 'sil-mondulkiri-fonts0.list'
install -m 0644 -vp "Mondulkiri-R.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Mondulkiri-R.ttf")\" >> 'sil-mondulkiri-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mondulkiri-B.ttf' 'Mondulkiri-BI.ttf' 'Mondulkiri-I.ttf' 'Mondulkiri-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-mondulkiri-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-mondulkiri-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-mondulkiri-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-mondulkiri-fonts0.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-mondulkiri-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-mondulkiri-fonts0.list"
done
echo Installing sil-busra-fonts
echo "" > "sil-busra-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri" >> "sil-busra-fonts1.list"
install -m 0644 -vp "Busra-B.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Busra-B.ttf")\" >> 'sil-busra-fonts1.list'
install -m 0644 -vp "Busra-BI.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Busra-BI.ttf")\" >> 'sil-busra-fonts1.list'
install -m 0644 -vp "Busra-I.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Busra-I.ttf")\" >> 'sil-busra-fonts1.list'
install -m 0644 -vp "Busra-R.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri/
echo \"%_fontsdir/ttf/sil-mondulkiri//$(basename "Busra-R.ttf")\" >> 'sil-busra-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Busra-B.ttf' 'Busra-BI.ttf' 'Busra-I.ttf' 'Busra-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-fonts1.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-mondulkiri-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-mondulkiri-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-mondulkiri -f sil-mondulkiri-fonts0.list
%files -n fonts-ttf-sil-busra -f sil-busra-fonts1.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*pdf

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 7.100-alt1_5
- new version

