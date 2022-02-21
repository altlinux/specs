Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-annapurna-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-annapurna-fonts
# SPDX-License-Identifier: MIT
Version: 1.204
Release: alt1_6

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Annapurna SIL
%global fontsummary       Annapurna SIL, a Devanagari font family
%global projectname       annapurna
%global projectname       annapurna
%global archivename       AnnapurnaSIL-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Annapurna SIL is a Unicode-based font family with broad support for writing\
systems that use the Devanagari script. Inspired by traditional calligraphic\
forms, the design is intended to be highly readable, reasonably compact, and\
visually attractive.\
\
The Devanagari script is used to write over 170 languages in South Asia.\
Annapurna SIL supports a full range of these writing systems.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-sil-annapurna-fonts.xml

Name:           fonts-ttf-sil-annapurna
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
%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt
chmod 644 %{fontdocs} %{fontlicenses} documentation/*

%build
# fontbuild 
fontnames=$(
  for font in 'AnnapurnaSIL-Bold.ttf' 'AnnapurnaSIL-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AnnapurnaSIL-Bold.ttf' 'AnnapurnaSIL-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-annapurna-fonts appstream file"
cat > "org.altlinux.sil-annapurna-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-annapurna-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Annapurna SIL</name>
  <summary><![CDATA[Annapurna SIL, a Devanagari font family]]></summary>
  <description>
    <p><![CDATA[Annapurna SIL is a Unicode-based font family with broad support for writing]]></p><p><![CDATA[systems that use the Devanagari script. Inspired by traditional calligraphic]]></p><p><![CDATA[forms, the design is intended to be highly readable, reasonably compact, and]]></p><p><![CDATA[visually attractive.]]></p> The Devanagari script is used to write over 170 languages in South Asia. Annapurna SIL supports a full range of these writing systems.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-annapurna-fonts
echo "" > "sil-annapurna-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-annapurna/
echo "%%dir %_fontsdir/ttf/sil-annapurna" >> "sil-annapurna-fonts.list"
install -m 0644 -vp "AnnapurnaSIL-Bold.ttf" %buildroot%_fontsdir/ttf/sil-annapurna/
echo \"%_fontsdir/ttf/sil-annapurna//$(basename "AnnapurnaSIL-Bold.ttf")\" >> 'sil-annapurna-fonts.list'
install -m 0644 -vp "AnnapurnaSIL-Regular.ttf" %buildroot%_fontsdir/ttf/sil-annapurna/
echo \"%_fontsdir/ttf/sil-annapurna//$(basename "AnnapurnaSIL-Regular.ttf")\" >> 'sil-annapurna-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'AnnapurnaSIL-Bold.ttf' 'AnnapurnaSIL-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-annapurna-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-annapurna-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-annapurna-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-annapurna-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt' 'documentation/AnnapurnaSIL-GraphiteFeatures.odt'; do
  echo %%doc "'${fontdoc}'" >> "sil-annapurna-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-annapurna-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-annapurna-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-annapurna-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-annapurna -f sil-annapurna-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*.pdf

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.204-alt1_6
- new version

