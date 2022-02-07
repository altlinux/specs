Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ecolier-court-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ecolier-court-fonts
# SPDX-License-Identifier: MIT
Version: 20070702
Release: alt3_33
# This used to be published here, copies are all over the web now
#URL:     http://perso.orange.fr/jm.douteau/page_ecolier.htm

%global fontlicense       OFL
%global fontlicenses      lisez_moi.txt
%global fontdocs          README-Fedora.txt

%global common_description \
The A.colier court font families were created by Jean-Marie Douteau to mimic the\
traditional cursive writing French children are taught in school.\
\
He kindly released two of them under the OFL, which are redistributed in this\
package.

%global fontfamily0       Ecolier Court
%global fontsummary0      A.colier Court, a schoolchildren cursive Latin font family
%global fontpkgheader0    \
Obsoletes: ecolier-court-fonts-common < %{version}-%{release}\

%global fontdescription0  \
%{common_description}

%global fontfamily1       Ecolier Lignes Court
%global fontsummary1      A.colier Lignes Court, a schoolchildren cursive Latin font family with lines
%global fontpkgheader1    \
Obsoletes: ecolier-court-lignes-fonts < %{version}-%{release}\


%global fontdescription1  \
%{common_description}\
\
The A. lignes A. (lines) A.colier Court font variant includes the Seyes lining\
commonly used on schoolchildren notepads.

Source0:  lisez_moi.txt
Source1:  README-Fedora.txt
Source10: ec_cour.ttf
Source11: ecl_cour.ttf
Source20: 61-ecolier-court-fonts.xml
Source21: 61-ecolier-lignes-court-fonts.xml

Name:           fonts-ttf-ecolier-court
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
Url: http://perso.orange.fr/jm.douteau/page_ecolier.htm
%description
%{?fontdescription0}
%package     -n fonts-ttf-ecolier-court-lignes
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-ecolier-court-lignes
%{?fontdescription1}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-ecolier-court = %EVR
Requires:  fonts-ttf-ecolier-court-lignes = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fonts0            %{SOURCE10}
%global fontconfngs0      %{SOURCE20}
%global fonts1            %{SOURCE11}
%global fontconfngs1      %{SOURCE21}
%setup -n %{oldname}-%{version} -q -c -T
install -m 0644 -p %{SOURCE0} %{SOURCE1} .
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in '%SOURCE10'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '%SOURCE10'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ecolier-court-fonts appstream file"
cat > "org.altlinux.ecolier-court-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ecolier-court-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Ecolier Court</name>
  <summary><![CDATA[Écolier Court, a schoolchildren cursive Latin font family]]></summary>
  <description>
    <p><![CDATA[The Écolier court font families were created by Jean-Marie Douteau to mimic the]]></p><p><![CDATA[traditional cursive writing French children are taught in school.]]></p> He kindly released two of them under the OFL, which are redistributed in this
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://perso.orange.fr/jm.douteau/page_ecolier.htm</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in '%SOURCE11'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in '%SOURCE11'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ecolier-lignes-court-fonts appstream file"
cat > "org.altlinux.ecolier-lignes-court-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ecolier-lignes-court-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Ecolier Lignes Court</name>
  <summary><![CDATA[Écolier Lignes Court, a schoolchildren cursive Latin font family with lines]]></summary>
  <description>
    <p><![CDATA[The Écolier court font families were created by Jean-Marie Douteau to mimic the]]></p><p><![CDATA[traditional cursive writing French children are taught in school.]]></p> He kindly released two of them under the OFL, which are redistributed in this package. The « lignes » (lines) Écolier Court font variant includes the Seyes lining
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://perso.orange.fr/jm.douteau/page_ecolier.htm</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ecolier-court-fonts
echo "" > "ecolier-court-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/ecolier-court/
echo "%%dir %_fontsdir/ttf/ecolier-court" >> "ecolier-court-fonts0.list"
install -m 0644 -vp "%SOURCE10" %buildroot%_fontsdir/ttf/ecolier-court/
echo \"%_fontsdir/ttf/ecolier-court//$(basename "%SOURCE10")\" >> 'ecolier-court-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE20'; do
      gen-fontconf -x "${fontconfng}" -w -f '%SOURCE10'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ecolier-court-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ecolier-court-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ecolier-court-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ecolier-court-fonts0.list"
done

for fontdoc in 'README-Fedora.txt'; do
  echo %%doc "'${fontdoc}'" >> "ecolier-court-fonts0.list"
done

for fontlicense in 'lisez_moi.txt'; do
  echo %%doc "'${fontlicense}'" >> "ecolier-court-fonts0.list"
done
echo Installing ecolier-lignes-court-fonts
echo "" > "ecolier-lignes-court-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/ecolier-court/
echo "%%dir %_fontsdir/ttf/ecolier-court" >> "ecolier-lignes-court-fonts1.list"
install -m 0644 -vp "%SOURCE11" %buildroot%_fontsdir/ttf/ecolier-court/
echo \"%_fontsdir/ttf/ecolier-court//$(basename "%SOURCE11")\" >> 'ecolier-lignes-court-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE21'; do
      gen-fontconf -x "${fontconfng}" -w -f '%SOURCE11'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ecolier-lignes-court-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ecolier-lignes-court-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ecolier-lignes-court-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ecolier-lignes-court-fonts1.list"
done

for fontdoc in 'README-Fedora.txt'; do
  echo %%doc "'${fontdoc}'" >> "ecolier-lignes-court-fonts1.list"
done

for fontlicense in 'lisez_moi.txt'; do
  echo %%doc "'${fontlicense}'" >> "ecolier-lignes-court-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ecolier-court-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ecolier-court-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ecolier-lignes-court-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ecolier-lignes-court-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-ecolier-court -f ecolier-court-fonts0.list
%files -n fonts-ttf-ecolier-court-lignes -f ecolier-lignes-court-fonts1.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20070702-alt3_33
- update

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_23
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_20
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_15
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070702-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070702-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070702-alt2_13
- rebuild with new rpm-build-fonts

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20070702-alt1_13
- initial release by fcimport

