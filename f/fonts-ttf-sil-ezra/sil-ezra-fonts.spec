Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-ezra-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-ezra-fonts
# SPDX-License-Identifier: MIT
Version: 2.51
Release: alt1_4
URL:     https://scripts.sil.org/ezrasil_home

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      Licenses.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description \
The Ezra SIL font families are fashioned after the square letter forms of the\
typography of the Biblia Hebraica Stuttgartensia (BHS), a beautiful Old\
Testament volume familiar to Biblical Hebrew scholars.\
\
The different font families are available to provide two different styles of\
cantillation marks. They were developed together, but there are some\
differences in how they display markings. This was done intentionally.

%global fontfamily0       Ezra SIL
%global fontsummary0      Ezra SIL, an Hebrew font family
%global fonts0            *.ttf
%global fontsex0          *SR.ttf
%global fontdescription0  \
%{common_description}\
\
The Ezra SIL font family is supposed to render text identically to the printed BHS.

%global fontfamily1       Ezra SIL SR
%global fontsummary1      Ezra SIL SR, an Hebrew font family
%global fonts1            *SR.ttf
%global fontdescription1  \
%{common_description}\
\
The Ezra SIL SR font has a different style of cantillation marks which may be\
more familiar to users working with other editions.


%global archivename EzraSIL251

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-sil-ezra-fonts.xml
Source11: 65-sil-ezra-sr-fonts.xml

Name:           fonts-ttf-sil-ezra
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-sil-ezra-sr
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-sil-ezra-sr
%{?fontdescription1}

%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in 'SILEOT.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'SILEOT.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-ezra-fonts appstream file"
cat > "org.altlinux.sil-ezra-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-ezra-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Ezra SIL</name>
  <summary><![CDATA[Ezra SIL, an Hebrew font family]]></summary>
  <description>
    <p><![CDATA[The Ezra SIL font families are fashioned after the square letter forms of the]]></p><p><![CDATA[typography of the Biblia Hebraica Stuttgartensia (BHS), a beautiful Old]]></p><p><![CDATA[Testament volume familiar to Biblical Hebrew scholars.]]></p> The different font families are available to provide two different styles of cantillation marks. They were developed together, but there are some differences in how they display markings. This was done intentionally. The Ezra SIL font family is supposed to render text identically to the printed BHS.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/ezrasil_home</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'SILEOTSR.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'SILEOTSR.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-ezra-sr-fonts appstream file"
cat > "org.altlinux.sil-ezra-sr-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-ezra-sr-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Ezra SIL SR</name>
  <summary><![CDATA[Ezra SIL SR, an Hebrew font family]]></summary>
  <description>
    <p><![CDATA[The Ezra SIL font families are fashioned after the square letter forms of the]]></p><p><![CDATA[typography of the Biblia Hebraica Stuttgartensia (BHS), a beautiful Old]]></p><p><![CDATA[Testament volume familiar to Biblical Hebrew scholars.]]></p> The different font families are available to provide two different styles of cantillation marks. They were developed together, but there are some differences in how they display markings. This was done intentionally. The Ezra SIL SR font has a different style of cantillation marks which may be more familiar to users working with other editions.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/ezrasil_home</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-ezra-fonts
echo "" > "sil-ezra-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-ezra/
echo "%%dir %_fontsdir/ttf/sil-ezra" >> "sil-ezra-fonts0.list"
install -m 0644 -vp "SILEOT.ttf" %buildroot%_fontsdir/ttf/sil-ezra/
echo \"%_fontsdir/ttf/sil-ezra//$(basename "SILEOT.ttf")\" >> 'sil-ezra-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'SILEOT.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-ezra-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-ezra-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-ezra-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-ezra-fonts0.list"
done

for fontdoc in 'Filelist.txt' 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-ezra-fonts0.list"
done

for fontlicense in 'Licenses.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-ezra-fonts0.list"
done
echo Installing sil-ezra-sr-fonts
echo "" > "sil-ezra-sr-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-ezra/
echo "%%dir %_fontsdir/ttf/sil-ezra" >> "sil-ezra-sr-fonts1.list"
install -m 0644 -vp "SILEOTSR.ttf" %buildroot%_fontsdir/ttf/sil-ezra/
echo \"%_fontsdir/ttf/sil-ezra//$(basename "SILEOTSR.ttf")\" >> 'sil-ezra-sr-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'SILEOTSR.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-ezra-sr-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-ezra-sr-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-ezra-sr-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-ezra-sr-fonts1.list"
done

for fontdoc in 'Filelist.txt' 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-ezra-sr-fonts1.list"
done

for fontlicense in 'Licenses.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-ezra-sr-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-ezra-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-ezra-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-ezra-sr-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-ezra-sr-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-ezra -f sil-ezra-fonts0.list
%files -n fonts-ttf-sil-ezra-sr -f sil-ezra-sr-fonts1.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.51-alt1_4
- new version

