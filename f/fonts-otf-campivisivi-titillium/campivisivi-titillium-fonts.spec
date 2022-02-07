Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname campivisivi-titillium-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname campivisivi-titillium-fonts
Version: 20120913
Release: alt1_24
URL: http://www.campivisivi.net/titillium/

%global foundry           Campivisivi
%global fontlicense       OFL
%global fontlicenses      OFL-titillium.txt
%global fontdocs          OFL-FAQ.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Titillium
%global fontsummary       Sans-serif typeface from the Master of Visual Design Campi Visivi
%global fonts             *.otf
%global fontdescription   \
Sans-serif typeface from the Master of Visual Design Campi Visivi.

Source0: http://www.campivisivi.net/titillium/download/Titillium_roman_upright_italic_2_0_OT.zip
Source1: 61-campivisivi-titillium-fonts.conf

Name:           fonts-otf-campivisivi-titillium
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
%setup -q -n "Titillium_roman_upright_italic_2_0_OT"
%linuxtext OFL-titillium.txt OFL-FAQ.txt

%build
# fontbuild 
fontnames=$(
  for font in 'Titillium-Black.otf' 'Titillium-Bold.otf' 'Titillium-BoldItalic.otf' 'Titillium-BoldUpright.otf' 'Titillium-Light.otf' 'Titillium-LightItalic.otf' 'Titillium-LightUpright.otf' 'Titillium-Regular.otf' 'Titillium-RegularItalic.otf' 'Titillium-RegularUpright.otf' 'Titillium-Semibold.otf' 'Titillium-SemiboldItalic.otf' 'Titillium-SemiboldUpright.otf' 'Titillium-Thin.otf' 'Titillium-ThinItalic.otf' 'Titillium-ThinUpright.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Titillium-Black.otf' 'Titillium-Bold.otf' 'Titillium-BoldItalic.otf' 'Titillium-BoldUpright.otf' 'Titillium-Light.otf' 'Titillium-LightItalic.otf' 'Titillium-LightUpright.otf' 'Titillium-Regular.otf' 'Titillium-RegularItalic.otf' 'Titillium-RegularUpright.otf' 'Titillium-Semibold.otf' 'Titillium-SemiboldItalic.otf' 'Titillium-SemiboldUpright.otf' 'Titillium-Thin.otf' 'Titillium-ThinItalic.otf' 'Titillium-ThinUpright.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the campivisivi-titillium-fonts appstream file"
cat > "org.altlinux.campivisivi-titillium-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.campivisivi-titillium-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Campivisivi Titillium</name>
  <summary><![CDATA[Sans-serif typeface from the Master of Visual Design Campi Visivi]]></summary>
  <description>
    
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.campivisivi.net/titillium/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "campivisivi-titillium-fonts
echo "" > "campivisivi-titillium-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/campivisivi-titillium/
echo "%%dir %_fontsdir/otf/campivisivi-titillium" >> "campivisivi-titillium-fonts.list"
install -m 0644 -vp "Titillium-Black.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Black.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-Bold.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Bold.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-BoldItalic.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-BoldItalic.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-BoldUpright.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-BoldUpright.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-Light.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Light.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-LightItalic.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-LightItalic.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-LightUpright.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-LightUpright.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-Regular.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Regular.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-RegularItalic.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-RegularItalic.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-RegularUpright.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-RegularUpright.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-Semibold.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Semibold.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-SemiboldItalic.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-SemiboldItalic.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-SemiboldUpright.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-SemiboldUpright.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-Thin.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-Thin.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-ThinItalic.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-ThinItalic.otf")\" >> 'campivisivi-titillium-fonts.list'
install -m 0644 -vp "Titillium-ThinUpright.otf" %buildroot%_fontsdir/otf/campivisivi-titillium/
echo \"%_fontsdir/otf/campivisivi-titillium//$(basename "Titillium-ThinUpright.otf")\" >> 'campivisivi-titillium-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "campivisivi-titillium-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "campivisivi-titillium-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.campivisivi-titillium-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "campivisivi-titillium-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "campivisivi-titillium-fonts.list"
done

for fontlicense in 'OFL-titillium.txt'; do
  echo %%doc "'${fontlicense}'" >> "campivisivi-titillium-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'campivisivi-titillium-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'campivisivi-titillium-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-campivisivi-titillium -f campivisivi-titillium-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20120913-alt1_24
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_5
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 20120913-alt1_4
- converted for ALT Linux by srpmconvert tools

