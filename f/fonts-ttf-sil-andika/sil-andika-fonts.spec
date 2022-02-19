Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-andika-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-andika-fonts
# SPDX-License-Identifier: MIT
Version: 5.000
Release: alt1_5

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Andika
%global fontsummary       SIL Andika, a font family for literacy and beginning readers
%global projectname       andika
%global archivename       Andika-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Suggests: font(andikanewbasic)\

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
addresses those issues.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 61-sil-andika-fonts.xml

Name:           fonts-ttf-sil-andika
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
  for font in 'Andika-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Andika-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-andika-fonts appstream file"
cat > "org.altlinux.sil-andika-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-andika-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Andika</name>
  <summary><![CDATA[SIL Andika, a font family for literacy and beginning readers]]></summary>
  <description>
    <p><![CDATA[Andika is a sans serif, Unicode-compliant font family designed especially for]]></p><p><![CDATA[literacy use, taking into account the needs of beginning readers. The focus is]]></p><p><![CDATA[on clear, easy-to-perceive letter-forms that will not be readily confused with]]></p><p><![CDATA[one another.]]></p> A sans serif font is preferred by some literacy personnel for teaching people to read. Its forms are simpler and less cluttered than those of most serif fonts. For years, literacy workers have had to make do with fonts that were not really suitable for beginning readers and writers. In some cases, literacy specialists have had to tediously assemble letters from a variety of fonts in order to get all of the characters they need for their particular language project, resulting in confusing and unattractive publications. Andika addresses those issues.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-andika-fonts
echo "" > "sil-andika-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-andika/
echo "%%dir %_fontsdir/ttf/sil-andika" >> "sil-andika-fonts.list"
install -m 0644 -vp "Andika-R.ttf" %buildroot%_fontsdir/ttf/sil-andika/
echo \"%_fontsdir/ttf/sil-andika//$(basename "Andika-R.ttf")\" >> 'sil-andika-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Andika-R.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-andika-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-andika-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-andika-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-andika-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-andika-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-andika-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-andika-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-andika-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-andika -f sil-andika-fonts.list

%changelog
* Sat Feb 19 2022 Igor Vlasenko <viy@altlinux.org> 5.000-alt1_5
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_18
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_14
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_10
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_9
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8
- initial release by fcimport

