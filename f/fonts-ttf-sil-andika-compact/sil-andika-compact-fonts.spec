Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-andika-compact-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-andika-compact-fonts
# SPDX-License-Identifier: MIT
Version: 5.000
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika Compact
%global fontsummary       SIL Andika Compact, a font family for literacy and beginning readers
%global projectname       andika
%global archivename       AndikaCompact-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Suggests: font(andika)\

%global fonts             *.ttf
%global fontdescription   \
Andika is a sans serif, Unicode-compliant font family designed especially for\
literacy use, taking into account the needs of beginning readers. The focus is\
on clear, easy-to-perceive letter-forms that will not be readily confused with\
one another.\
\
A sans serif font is preferred by some literacy personnel for teaching people\
to read. Its forms are simpler and less cluttered than those of most serif\
fonts. For years, literacy workers have had to make do with fonts that were\
not really suitable for beginning readers and writers. In some cases, literacy\
specialists have had to tediously assemble letters from a variety of fonts in\
order to get all of the characters they need for their particular language\
project, resulting in confusing and unattractive publications. Andika\
addresses those issues.\
\
The Andika Compact font family was derived from Andika using SIL TypeTuner,\
by setting the a.'Line spacinga.' feature to a.'Tighta.', and it cannot be TypeTuned\
again. It may exhibit some diacritics clipping on screen (but should print\
fine).

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 62-sil-andika-compact-fonts.xml

Name:           fonts-ttf-sil-andika-compact
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
  for font in 'AndikaCompact-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AndikaCompact-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-andika-compact-fonts appstream file"
cat > "org.altlinux.sil-andika-compact-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-andika-compact-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Andika Compact</name>
  <summary><![CDATA[SIL Andika Compact, a font family for literacy and beginning readers]]></summary>
  <description>
    <p><![CDATA[Andika is a sans serif, Unicode-compliant font family designed especially for]]></p><p><![CDATA[literacy use, taking into account the needs of beginning readers. The focus is]]></p><p><![CDATA[on clear, easy-to-perceive letter-forms that will not be readily confused with]]></p><p><![CDATA[one another.]]></p> A sans serif font is preferred by some literacy personnel for teaching people to read. Its forms are simpler and less cluttered than those of most serif fonts. For years, literacy workers have had to make do with fonts that were not really suitable for beginning readers and writers. In some cases, literacy specialists have had to tediously assemble letters from a variety of fonts in order to get all of the characters they need for their particular language project, resulting in confusing and unattractive publications. Andika addresses those issues. The Andika Compact font family was derived from Andika using SIL TypeTuner, by setting the “Line spacing” feature to “Tight”, and it cannot be TypeTuned again. It may exhibit some diacritics clipping on screen (but should print fine).
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-andika-compact-fonts
echo "" > "sil-andika-compact-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-andika-compact/
echo "%%dir %_fontsdir/ttf/sil-andika-compact" >> "sil-andika-compact-fonts.list"
install -m 0644 -vp "AndikaCompact-R.ttf" %buildroot%_fontsdir/ttf/sil-andika-compact/
echo \"%_fontsdir/ttf/sil-andika-compact//$(basename "AndikaCompact-R.ttf")\" >> 'sil-andika-compact-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'AndikaCompact-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-andika-compact-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-andika-compact-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-andika-compact-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-andika-compact-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-andika-compact-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-andika-compact-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-andika-compact-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-andika-compact-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-andika-compact -f sil-andika-compact-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 5.000-alt1_5
- new version

