Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname aajohan-comfortaa-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name aajohan-comfortaa-fonts
%define fontpkgname aajohan-comfortaa-fonts
Version:        3.101
Release:        alt1_4
URL:            https://www.deviantart.com/aajohan

%global foundry           Aajohan
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt DESCRIPTION.en_us.html README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Comfortaa
%global fontsummary       Modern style true type font
%global fonts             fonts/OTF/*.otf fonts/TTF/*.ttf
%global fontdescription   \
Comfortaa is a sans-serif font comfortable in every aspect with\
Bold, Regular, and Thin variants.\
It has very good European language coverage and decent Cyrillic coverage.

Source0:        https://github.com/googlefonts/comfortaa/archive/%{version}%{?prerelease}/%{oldname}-%{version}%{?prerelease}.tar.gz
Source1:        61-aajohan-comfortaa-fonts.conf

Name:           fonts-ttf-aajohan-comfortaa
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
%setup -q -n comfortaa-%{version}

chmod 644 AUTHORS.txt CONTRIBUTORS.txt
%linuxtext FONTLOG.txt OFL.txt

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/OTF/Comfortaa-Bold.otf' 'fonts/OTF/Comfortaa-Light.otf' 'fonts/OTF/Comfortaa-Regular.otf' 'fonts/TTF/Comfortaa-Bold.ttf' 'fonts/TTF/Comfortaa-Light.ttf' 'fonts/TTF/Comfortaa-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/OTF/Comfortaa-Bold.otf' 'fonts/OTF/Comfortaa-Light.otf' 'fonts/OTF/Comfortaa-Regular.otf' 'fonts/TTF/Comfortaa-Bold.ttf' 'fonts/TTF/Comfortaa-Light.ttf' 'fonts/TTF/Comfortaa-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the aajohan-comfortaa-fonts appstream file"
cat > "org.altlinux.aajohan-comfortaa-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.aajohan-comfortaa-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Aajohan Comfortaa</name>
  <summary><![CDATA[Modern style true type font]]></summary>
  <description>
    <p><![CDATA[Comfortaa is a sans-serif font comfortable in every aspect with]]></p><p><![CDATA[Bold, Regular, and Thin variants.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.deviantart.com/aajohan</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "aajohan-comfortaa-fonts
echo "" > "aajohan-comfortaa-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/aajohan-comfortaa/
echo "%%dir %_fontsdir/otf/aajohan-comfortaa" >> "aajohan-comfortaa-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/aajohan-comfortaa/
echo "%%dir %_fontsdir/ttf/aajohan-comfortaa" >> "aajohan-comfortaa-fonts.list"
install -m 0644 -vp "fonts/OTF/Comfortaa-Bold.otf" %buildroot%_fontsdir/otf/aajohan-comfortaa/
echo \"%_fontsdir/otf/aajohan-comfortaa//$(basename "fonts/OTF/Comfortaa-Bold.otf")\" >> 'aajohan-comfortaa-fonts.list'
install -m 0644 -vp "fonts/OTF/Comfortaa-Light.otf" %buildroot%_fontsdir/otf/aajohan-comfortaa/
echo \"%_fontsdir/otf/aajohan-comfortaa//$(basename "fonts/OTF/Comfortaa-Light.otf")\" >> 'aajohan-comfortaa-fonts.list'
install -m 0644 -vp "fonts/OTF/Comfortaa-Regular.otf" %buildroot%_fontsdir/otf/aajohan-comfortaa/
echo \"%_fontsdir/otf/aajohan-comfortaa//$(basename "fonts/OTF/Comfortaa-Regular.otf")\" >> 'aajohan-comfortaa-fonts.list'
install -m 0644 -vp "fonts/TTF/Comfortaa-Bold.ttf" %buildroot%_fontsdir/ttf/aajohan-comfortaa/
echo \"%_fontsdir/ttf/aajohan-comfortaa//$(basename "fonts/TTF/Comfortaa-Bold.ttf")\" >> 'aajohan-comfortaa-fonts.list'
install -m 0644 -vp "fonts/TTF/Comfortaa-Light.ttf" %buildroot%_fontsdir/ttf/aajohan-comfortaa/
echo \"%_fontsdir/ttf/aajohan-comfortaa//$(basename "fonts/TTF/Comfortaa-Light.ttf")\" >> 'aajohan-comfortaa-fonts.list'
install -m 0644 -vp "fonts/TTF/Comfortaa-Regular.ttf" %buildroot%_fontsdir/ttf/aajohan-comfortaa/
echo \"%_fontsdir/ttf/aajohan-comfortaa//$(basename "fonts/TTF/Comfortaa-Regular.ttf")\" >> 'aajohan-comfortaa-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "aajohan-comfortaa-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "aajohan-comfortaa-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.aajohan-comfortaa-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "aajohan-comfortaa-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'FONTLOG.txt' 'DESCRIPTION.en_us.html' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "aajohan-comfortaa-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "aajohan-comfortaa-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'aajohan-comfortaa-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'aajohan-comfortaa-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-aajohan-comfortaa -f aajohan-comfortaa-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 3.101-alt1_4
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 3.101-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 3.001-alt1_1
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_4
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.003-alt1_2
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 2.003-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.002-alt2_6
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.002-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_2
- initial release by fcimport

