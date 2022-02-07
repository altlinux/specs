Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname jomolhari-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname jomolhari-fonts
Version:        0.003
Release:        alt3_35

URL: https://fonts.google.com/specimen/Jomolhari

%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jomolhari
%global fontsummary       Jomolhari a Bhutanese style font for Tibetan and Dzongkha
%global archivename       jomolhari-alpha003c
%global fonts             *.ttf
%global fontdescription   \
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and\
Tibetan text. It is based on Bhutanese manuscript examples, supports the\
Unicode and the Chinese encoding for Tibetan.\
The font supports the standard combinations used in most texts.

Source0: http://chris.fynn.googlepages.com/%{archivename}.zip
Source1:        65-0-jomolhari-fonts.conf

Name:           fonts-ttf-jomolhari
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs         %{SOURCE1}
%setup -n %{oldname}-%{version} -q -c
%linuxtext FONTLOG.txt OFL-FAQ.txt OFL.txt

%build
# fontbuild 
fontnames=$(
  for font in 'Jomolhari-alpha3c-0605331.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Jomolhari-alpha3c-0605331.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the jomolhari-fonts appstream file"
cat > "org.altlinux.jomolhari-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.jomolhari-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Jomolhari</name>
  <summary><![CDATA[Jomolhari a Bhutanese style font for Tibetan and Dzongkha]]></summary>
  <description>
    <p><![CDATA[Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and]]></p><p><![CDATA[Tibetan text. It is based on Bhutanese manuscript examples, supports the]]></p><p><![CDATA[Unicode and the Chinese encoding for Tibetan.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://fonts.google.com/specimen/Jomolhari</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "jomolhari-fonts
echo "" > "jomolhari-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/jomolhari/
echo "%%dir %_fontsdir/ttf/jomolhari" >> "jomolhari-fonts.list"
install -m 0644 -vp "Jomolhari-alpha3c-0605331.ttf" %buildroot%_fontsdir/ttf/jomolhari/
echo \"%_fontsdir/ttf/jomolhari//$(basename "Jomolhari-alpha3c-0605331.ttf")\" >> 'jomolhari-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "jomolhari-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "jomolhari-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.jomolhari-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "jomolhari-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "jomolhari-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "jomolhari-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'jomolhari-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'jomolhari-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-jomolhari -f jomolhari-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 0.003-alt3_35
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_23
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_16
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_15
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_12
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3_11
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_11
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2_10
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1_10
- initial release by fcimport

