Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname madan-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname madan-fonts
BuildRequires: fontforge libfontforge python3-module-fontforge

Version: 2.000
Release: alt3_32
URL: http://madanpuraskar.org/

%global fontlicense       GPL+
%global fontlicenses      license.txt

%global fontfamily        Madan
%global fontsummary       Font for Nepali language
%global fonts             madan.ttf
%global fontdescription   \
This package provides the Madan font for Nepali made by the\
Madan Puraskar Pustakalaya project.

# Found new following working Source URL. Use wget to download this archive
Source0: http://ltk.org.np/downloads/fonts.zip
Source1: 65-0-madan-fonts.conf
# Extract from font info
Source2: license.txt
Source3: sfd2ttf.pe
# Below files will make sure "fc-scan madan.ttf |grep lang:" will show ne
Source4: madan.py
Source5: madan_u0970_glyph.svg

Name:           fonts-ttf-madan
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

cp -p %{SOURCE2} %{SOURCE3} \
      %{SOURCE4} %{SOURCE5} .

%linuxtext license.txt

chmod 755 sfd2ttf.pe madan.py 
./madan.py madan.ttf madan_u0970_glyph.svg
./sfd2ttf.pe madan.sfd

%build
# fontbuild 
fontnames=$(
  for font in 'madan.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'madan.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the madan-fonts appstream file"
cat > "org.altlinux.madan-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.madan-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPL+</project_license>
  <name>Madan</name>
  <summary><![CDATA[Font for Nepali language]]></summary>
  <description>
    <p><![CDATA[This package provides the Madan font for Nepali made by the]]></p><p><![CDATA[Madan Puraskar Pustakalaya project.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://madanpuraskar.org/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing madan-fonts
echo "" > "madan-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/madan/
echo "%%dir %_fontsdir/ttf/madan" >> "madan-fonts.list"
install -m 0644 -vp "madan.ttf" %buildroot%_fontsdir/ttf/madan/
echo \"%_fontsdir/ttf/madan//$(basename "madan.ttf")\" >> 'madan-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "madan-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "madan-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.madan-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "madan-fonts.list"
done

for fontlicense in 'license.txt'; do
  echo %%doc "'${fontlicense}'" >> "madan-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'madan-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'madan-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-madan -f madan-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 2.000-alt3_32
- update

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_19
- update to new release by fcimport

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_16
- fixed build

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_14
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_10
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_9
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_6
- update to new release by fcimport

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt2_4
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_4
- initial release by fcimport

