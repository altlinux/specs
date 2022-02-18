Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname adobe-source-sans-pro-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname adobe-source-sans-pro-fonts
Version:        3.046
Release:        alt1_3
URL:            https://github.com/adobe-fonts/source-sans-pro/

%global foundry adobe
%global fontlicense OFL
%global fontlicenses LICENSE.md
%global fontdocs README.md
%global fontdocsex %{fontlicenses}

%global fontfamily Source Sans Pro
%global fontsummary A set of OpenType fonts designed for user interfaces
%global fonts OTF/*.otf
%global fontdescription Source Sans is a set of OpenType fonts that have been designed to work well in\
user interface (UI) environments, as well as in text setting for screen and\
print.

Source0:        https://github.com/adobe-fonts/source-sans-pro/}/releases/download/%{version}R/OTF-source-sans-%{version}R.zip
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10:       63-adobe-source-sans-pro-fonts.conf

Name:           fonts-otf-adobe-source-sans-pro
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}


%prep
%global fontconfs %{SOURCE10}
%setup -n %{oldname}-%{version} -q -c



%build
# fontbuild 
fontnames=$(
  for font in 'OTF/SourceSans3-Black.otf' 'OTF/SourceSans3-BlackIt.otf' 'OTF/SourceSans3-Bold.otf' 'OTF/SourceSans3-BoldIt.otf' 'OTF/SourceSans3-ExtraLight.otf' 'OTF/SourceSans3-ExtraLightIt.otf' 'OTF/SourceSans3-It.otf' 'OTF/SourceSans3-Light.otf' 'OTF/SourceSans3-LightIt.otf' 'OTF/SourceSans3-Regular.otf' 'OTF/SourceSans3-Semibold.otf' 'OTF/SourceSans3-SemiboldIt.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/SourceSans3-Black.otf' 'OTF/SourceSans3-BlackIt.otf' 'OTF/SourceSans3-Bold.otf' 'OTF/SourceSans3-BoldIt.otf' 'OTF/SourceSans3-ExtraLight.otf' 'OTF/SourceSans3-ExtraLightIt.otf' 'OTF/SourceSans3-It.otf' 'OTF/SourceSans3-Light.otf' 'OTF/SourceSans3-LightIt.otf' 'OTF/SourceSans3-Regular.otf' 'OTF/SourceSans3-Semibold.otf' 'OTF/SourceSans3-SemiboldIt.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adobe-source-sans-pro-fonts appstream file"
cat > "org.altlinux.adobe-source-sans-pro-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adobe-source-sans-pro-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>adobe Source Sans Pro</name>
  <summary><![CDATA[A set of OpenType fonts designed for user interfaces]]></summary>
  <description>
    <p><![CDATA[Source Sans is a set of OpenType fonts that have been designed to work well inuser interface (UI) environments, as well as in text setting for screen and]]></p><p><![CDATA[print.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://github.com/adobe-fonts/source-sans-pro/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM


%install
echo Installing adobe-source-sans-pro-fonts
echo "" > "adobe-source-sans-pro-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo "%%dir %_fontsdir/otf/adobe-source-sans-pro" >> "adobe-source-sans-pro-fonts.list"
install -m 0644 -vp "OTF/SourceSans3-Black.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-Black.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-BlackIt.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-BlackIt.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-Bold.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-Bold.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-BoldIt.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-BoldIt.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-ExtraLight.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-ExtraLight.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-ExtraLightIt.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-ExtraLightIt.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-It.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-It.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-Light.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-Light.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-LightIt.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-LightIt.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-Regular.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-Regular.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-Semibold.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-Semibold.otf")\" >> 'adobe-source-sans-pro-fonts.list'
install -m 0644 -vp "OTF/SourceSans3-SemiboldIt.otf" %buildroot%_fontsdir/otf/adobe-source-sans-pro/
echo \"%_fontsdir/otf/adobe-source-sans-pro//$(basename "OTF/SourceSans3-SemiboldIt.otf")\" >> 'adobe-source-sans-pro-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adobe-source-sans-pro-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adobe-source-sans-pro-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adobe-source-sans-pro-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adobe-source-sans-pro-fonts.list"
done


%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adobe-source-sans-pro-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adobe-source-sans-pro-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'


%files -n fonts-otf-adobe-source-sans-pro -f adobe-source-sans-pro-fonts.list


%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 3.046-alt1_3
- update to new release by fcimport

* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.006-alt1_1
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 2.045-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.020-alt1_1
- update to new release by fcimport

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.065-alt1_0
- new version 2.010roman-1.065-italic

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.034-alt1_2
- update to new release by fcimport

* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.034-alt1_1
- fc import

