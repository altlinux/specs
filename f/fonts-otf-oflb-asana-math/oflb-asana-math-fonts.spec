Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname oflb-asana-math-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname oflb-asana-math-fonts
Version:        0.954
Release:        alt1_16
## Note that upstream is dead and there is no download link available at this minute
## so please don't report FTBFS bugs for this package.
URL:            http://www.ctan.org/tex-archive/fonts/Asana-Math/

%global foundry           oflb
%global fontlicense       OFL
%global fontlicenses      License.txt
%global fontdocs          *.txt README.license
%global fontdocsex        %{fontlicenses}

%global fontfamily        Asana Math
%global fontsummary       An OpenType font with a MATH table
%global fonts             Asana-Math.otf
%global fontdescription   \
An OpenType font with a MATH table that can be used with XeTeX to typeset math\
content.

Source0:        http://mirrors.ctan.org/fonts/Asana-Math/Asana-Math.otf
Source1:        63-oflb-asana-math-fonts.conf
Source2:        README.license
#license text extracted from font file
Source3:        License.txt

Name:           fonts-otf-oflb-asana-math
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
%setup -n %{oldname}-%{version} -q -c -T
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
# fontbuild 
fontnames=$(
  for font in 'Asana-Math.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Asana-Math.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the oflb-asana-math-fonts appstream file"
cat > "org.altlinux.oflb-asana-math-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.oflb-asana-math-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>oflb Asana Math</name>
  <summary><![CDATA[An OpenType font with a MATH table]]></summary>
  <description>
    <p><![CDATA[An OpenType font with a MATH table that can be used with XeTeX to typeset math]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.ctan.org/tex-archive/fonts/Asana-Math/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "oflb-asana-math-fonts
echo "" > "oflb-asana-math-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/oflb-asana-math/
echo "%%dir %_fontsdir/otf/oflb-asana-math" >> "oflb-asana-math-fonts.list"
install -m 0644 -vp "Asana-Math.otf" %buildroot%_fontsdir/otf/oflb-asana-math/
echo \"%_fontsdir/otf/oflb-asana-math//$(basename "Asana-Math.otf")\" >> 'oflb-asana-math-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "oflb-asana-math-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "oflb-asana-math-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.oflb-asana-math-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "oflb-asana-math-fonts.list"
done

for fontdoc in 'README.license'; do
  echo %%doc "'${fontdoc}'" >> "oflb-asana-math-fonts.list"
done

for fontlicense in 'License.txt'; do
  echo %%doc "'${fontlicense}'" >> "oflb-asana-math-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'oflb-asana-math-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'oflb-asana-math-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-oflb-asana-math -f oflb-asana-math-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 0.954-alt1_16
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.954-alt1_5
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.952-alt1_2
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.930-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.930-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.930-alt2_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.930-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.930-alt1_2
- update to new release by fcimport

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.930-alt1_1
- update to new release by fcimport

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.914-alt1_9
- initial release by fcimport

