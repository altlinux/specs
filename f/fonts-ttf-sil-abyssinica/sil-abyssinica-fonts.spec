Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-abyssinica-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-abyssinica-fonts
Version:        1.200
Release:        alt2_23

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Abyssinica SIL
%global fontsummary       SIL Abyssinica fonts
%global projectname       AbyssinicaSIL
%global archivename       AbyssinicaSIL%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fonts             *.ttf
%global fontdescription   \
SIL Abyssinica is a Unicode typeface family containing glyphs for the\
Ethiopic script.\
\
The Ethiopic script is used for writing many of the languages of Ethiopia and\
Eritrea. Abyssinica SIL supports all Ethiopic characters which are in Unicode\
including the Unicode 4.1 extensions. Some languages of Ethiopia are not yet\
able to be fully represented in Unicode and, where necessary, we have included\
non-Unicode characters in the Private Use Area (see Private-use (PUA)\
characters supported by Abyssinica SIL).\
\
Abyssinica SIL is based on Ethiopic calligraphic traditions. This release is\
a regular typeface, with no bold or italic version available or planned.


# download from http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=AbyssinicaSIL1.200.zip&filename=AbyssinicaSIL1.200.zip
Source0:        %{archivename}.zip
Source1:        66-sil-abyssinica-fonts.conf

Name:           fonts-ttf-sil-abyssinica
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
%setup -q -n %{projectname}-%{version}
%linuxtext FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt documentation/DOCUMENTATION.txt

%build
# fontbuild 
fontnames=$(
  for font in 'AbyssinicaSIL-R.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AbyssinicaSIL-R.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-abyssinica-fonts appstream file"
cat > "org.altlinux.sil-abyssinica-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-abyssinica-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Abyssinica SIL</name>
  <summary><![CDATA[SIL Abyssinica fonts]]></summary>
  <description>
    <p><![CDATA[SIL Abyssinica is a Unicode typeface family containing glyphs for the]]></p><p><![CDATA[Ethiopic script.]]></p> The Ethiopic script is used for writing many of the languages of Ethiopia and Eritrea. Abyssinica SIL supports all Ethiopic characters which are in Unicode including the Unicode 4.1 extensions. Some languages of Ethiopia are not yet able to be fully represented in Unicode and, where necessary, we have included non-Unicode characters in the Private Use Area (see Private-use (PUA) characters supported by Abyssinica SIL). Abyssinica SIL is based on Ethiopic calligraphic traditions. This release is
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "sil-abyssinica-fonts
echo "" > "sil-abyssinica-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-abyssinica/
echo "%%dir %_fontsdir/ttf/sil-abyssinica" >> "sil-abyssinica-fonts.list"
install -m 0644 -vp "AbyssinicaSIL-R.ttf" %buildroot%_fontsdir/ttf/sil-abyssinica/
echo \"%_fontsdir/ttf/sil-abyssinica//$(basename "AbyssinicaSIL-R.ttf")\" >> 'sil-abyssinica-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-abyssinica-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-abyssinica-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-abyssinica-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-abyssinica-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-abyssinica-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-abyssinica-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-abyssinica-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-abyssinica-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-abyssinica -f sil-abyssinica-fonts.list


%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.200-alt2_23
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_12
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_5
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.200-alt2_2
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.200-alt1_2
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_11
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_10
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- bugfix release by fcimport

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_10
- initial release by fcimport

