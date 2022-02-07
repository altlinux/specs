Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname kurdit-unikurd-web-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname kurdit-unikurd-web-fonts
Version:       20020502
Release:       alt3_29
# Below is only working Source URL
URL:           http://www.kurditgroup.org/node/1337

%global foundry           kurdit
%global fontlicense       GPLv3
%global fontlicenses      gpl.txt

%global fontfamily        Unikurd Web
%global fontsummary       A widely used Kurdish font for Arabic-like scripts and Latin
%global archivename       unikurdweb_0
%global fonts             *.ttf
%global fontdescription   \
A widely used Kurdish font which supports various Arabic-like scripts\
(Arabic, Kurdish, Persian) and also Latin.

Source0:       https://www.kurditgroup.org/sites/default/files/%{archivename}.zip
Source1:       65-kurdit-unikurd-web-fonts.conf

Name:           fonts-ttf-kurdit-unikurd-web
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
%setup -q -c -n %{archivename}


%build
# fontbuild 
fontnames=$(
  for font in 'Unikuweb.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Unikuweb.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the kurdit-unikurd-web-fonts appstream file"
cat > "org.altlinux.kurdit-unikurd-web-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.kurdit-unikurd-web-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv3</project_license>
  <name>kurdit Unikurd Web</name>
  <summary><![CDATA[A widely used Kurdish font for Arabic-like scripts and Latin]]></summary>
  <description>
    <p><![CDATA[A widely used Kurdish font which supports various Arabic-like scripts]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.kurditgroup.org/node/1337</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "kurdit-unikurd-web-fonts
echo "" > "kurdit-unikurd-web-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/kurdit-unikurd-web/
echo "%%dir %_fontsdir/ttf/kurdit-unikurd-web" >> "kurdit-unikurd-web-fonts.list"
install -m 0644 -vp "Unikuweb.ttf" %buildroot%_fontsdir/ttf/kurdit-unikurd-web/
echo \"%_fontsdir/ttf/kurdit-unikurd-web//$(basename "Unikuweb.ttf")\" >> 'kurdit-unikurd-web-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "kurdit-unikurd-web-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "kurdit-unikurd-web-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.kurdit-unikurd-web-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "kurdit-unikurd-web-fonts.list"
done

for fontlicense in 'gpl.txt'; do
  echo %%doc "'${fontlicense}'" >> "kurdit-unikurd-web-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'kurdit-unikurd-web-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'kurdit-unikurd-web-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-kurdit-unikurd-web -f kurdit-unikurd-web-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20020502-alt3_29
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_20
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_9
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20020502-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20020502-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20020502-alt2_6
- rebuild with new rpm-build-fonts

* Sun Aug 07 2011 Igor Vlasenko <viy@altlinux.ru> 20020502-alt1_6
- initial release by fcimport

