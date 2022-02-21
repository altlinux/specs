Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-andika-new-basic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-andika-new-basic-fonts
# SPDX-License-Identifier: MIT
Version: 5.500
Release: alt1_4

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika New Basic
%global fontsummary       SIL Andika New Basic, a font family for literacy and beginning readers
%global projectname       andika
%global archivename       AndikaNewBasic-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Suggests: font(andika)\

%global fonts             *.ttf
%global fontdescription   \
Andika New Basic is a limited-character-set (no extended IPA or Cyrillic)\
version of Andika that includes regular, bold, italic and bold-italic faces.\
\
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
addresses those issues.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 60-sil-andika-new-basic-fonts.xml

Name:           fonts-ttf-sil-andika-new-basic
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
  for font in 'AndikaNewBasic-B.ttf' 'AndikaNewBasic-BI.ttf' 'AndikaNewBasic-I.ttf' 'AndikaNewBasic-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AndikaNewBasic-B.ttf' 'AndikaNewBasic-BI.ttf' 'AndikaNewBasic-I.ttf' 'AndikaNewBasic-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-andika-new-basic-fonts appstream file"
cat > "org.altlinux.sil-andika-new-basic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-andika-new-basic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Andika New Basic</name>
  <summary><![CDATA[SIL Andika New Basic, a font family for literacy and beginning readers]]></summary>
  <description>
    <p><![CDATA[Andika New Basic is a limited-character-set (no extended IPA or Cyrillic)]]></p><p><![CDATA[version of Andika that includes regular, bold, italic and bold-italic faces.]]></p> Andika is a sans serif, Unicode-compliant font family designed especially for literacy use, taking into account the needs of beginning readers. The focus is on clear, easy-to-perceive letter-forms that will not be readily confused with one another. A sans serif font is preferred by some literacy personnel for teaching people to read. Its forms are simpler and less cluttered than those of most serif fonts. For years, literacy workers have had to make do with fonts that were not really suitable for beginning readers and writers. In some cases, literacy specialists have had to tediously assemble letters from a variety of fonts in order to get all of the characters they need for their particular language project, resulting in confusing and unattractive publications. Andika addresses those issues.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-andika-new-basic-fonts
echo "" > "sil-andika-new-basic-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-andika-new-basic/
echo "%%dir %_fontsdir/ttf/sil-andika-new-basic" >> "sil-andika-new-basic-fonts.list"
install -m 0644 -vp "AndikaNewBasic-B.ttf" %buildroot%_fontsdir/ttf/sil-andika-new-basic/
echo \"%_fontsdir/ttf/sil-andika-new-basic//$(basename "AndikaNewBasic-B.ttf")\" >> 'sil-andika-new-basic-fonts.list'
install -m 0644 -vp "AndikaNewBasic-BI.ttf" %buildroot%_fontsdir/ttf/sil-andika-new-basic/
echo \"%_fontsdir/ttf/sil-andika-new-basic//$(basename "AndikaNewBasic-BI.ttf")\" >> 'sil-andika-new-basic-fonts.list'
install -m 0644 -vp "AndikaNewBasic-I.ttf" %buildroot%_fontsdir/ttf/sil-andika-new-basic/
echo \"%_fontsdir/ttf/sil-andika-new-basic//$(basename "AndikaNewBasic-I.ttf")\" >> 'sil-andika-new-basic-fonts.list'
install -m 0644 -vp "AndikaNewBasic-R.ttf" %buildroot%_fontsdir/ttf/sil-andika-new-basic/
echo \"%_fontsdir/ttf/sil-andika-new-basic//$(basename "AndikaNewBasic-R.ttf")\" >> 'sil-andika-new-basic-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'AndikaNewBasic-B.ttf' 'AndikaNewBasic-BI.ttf' 'AndikaNewBasic-I.ttf' 'AndikaNewBasic-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-andika-new-basic-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-andika-new-basic-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-andika-new-basic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-andika-new-basic-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-andika-new-basic-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-andika-new-basic-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-andika-new-basic-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-andika-new-basic-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-andika-new-basic -f sil-andika-new-basic-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 5.500-alt1_4
- new version

