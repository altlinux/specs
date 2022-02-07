Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-charis-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-charis-fonts
# SPDX-License-Identifier: MIT
Version: 6.001
Release: alt1_1

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Charis SIL
%global fontsummary       Charis SIL, a font family similar to Bitstream Charter
%global projectname       charis
%global archivename       CharisSIL-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
Charis SIL provides glyphs for a wide range of Latin and Cyrillic characters.\
Charis is similar to Bitstream Charter, one of the first fonts designed\
specifically for laser printers. It is highly readable and holds up well in\
less-than-ideal reproduction environments. It also has a full set of styles\
a.. regular, italic, bold, bold italic a.. and so is more useful in general\
publishing than Doulos SIL. Charis is a serif proportionally spaced font\
optimized for readability in long printed documents.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 60-sil-charis-fonts.xml

Name:           fonts-ttf-sil-charis
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
Provides: fonts-ttf-charis = %version-%release
Obsoletes: fonts-ttf-charis <= 4.104-alt1

%description
%{?fontdescription}

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n %{archivename}
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'CharisSIL-Bold.ttf' 'CharisSIL-BoldItalic.ttf' 'CharisSIL-Italic.ttf' 'CharisSIL-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'CharisSIL-Bold.ttf' 'CharisSIL-BoldItalic.ttf' 'CharisSIL-Italic.ttf' 'CharisSIL-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-charis-fonts appstream file"
cat > "org.altlinux.sil-charis-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-charis-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Charis SIL</name>
  <summary><![CDATA[Charis SIL, a font family similar to Bitstream Charter]]></summary>
  <description>
    <p><![CDATA[Charis SIL provides glyphs for a wide range of Latin and Cyrillic characters.]]></p><p><![CDATA[Charis is similar to Bitstream Charter, one of the first fonts designed]]></p><p><![CDATA[specifically for laser printers. It is highly readable and holds up well in]]></p><p><![CDATA[less-than-ideal reproduction environments. It also has a full set of styles]]></p><p><![CDATA[— regular, italic, bold, bold italic — and so is more useful in general]]></p><p><![CDATA[publishing than Doulos SIL. Charis is a serif proportionally spaced font]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "sil-charis-fonts
echo "" > "sil-charis-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-charis/
echo "%%dir %_fontsdir/ttf/sil-charis" >> "sil-charis-fonts.list"
install -m 0644 -vp "CharisSIL-Bold.ttf" %buildroot%_fontsdir/ttf/sil-charis/
echo \"%_fontsdir/ttf/sil-charis//$(basename "CharisSIL-Bold.ttf")\" >> 'sil-charis-fonts.list'
install -m 0644 -vp "CharisSIL-BoldItalic.ttf" %buildroot%_fontsdir/ttf/sil-charis/
echo \"%_fontsdir/ttf/sil-charis//$(basename "CharisSIL-BoldItalic.ttf")\" >> 'sil-charis-fonts.list'
install -m 0644 -vp "CharisSIL-Italic.ttf" %buildroot%_fontsdir/ttf/sil-charis/
echo \"%_fontsdir/ttf/sil-charis//$(basename "CharisSIL-Italic.ttf")\" >> 'sil-charis-fonts.list'
install -m 0644 -vp "CharisSIL-Regular.ttf" %buildroot%_fontsdir/ttf/sil-charis/
echo \"%_fontsdir/ttf/sil-charis//$(basename "CharisSIL-Regular.ttf")\" >> 'sil-charis-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'CharisSIL-Bold.ttf' 'CharisSIL-BoldItalic.ttf' 'CharisSIL-Italic.ttf' 'CharisSIL-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-charis-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-charis-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-charis-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-charis-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-charis-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-charis-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-charis-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-charis-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-charis -f sil-charis-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 6.001-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 5.000-alt1_5
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.000-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.114-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.106-alt5_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.106-alt5_6
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.106-alt5_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.106-alt4_5
- update to new release by fcimport

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 4.106-alt4_4
- really added provides/obsoletes for short names

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 4.106-alt3_4
- added provides/obsoletes for short names

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.106-alt2_4
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 4.106-alt1_4
- initial release by fcimport

