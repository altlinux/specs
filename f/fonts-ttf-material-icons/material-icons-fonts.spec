Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname material-icons-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname material-icons-fonts
Version:        4.0.0
Release:        alt1_6
URL:            https://google.github.io/material-design-icons/

%global fontlicense     ASL 2.0
%global fontlicenses    LICENSE
%global fontdocs        README.md
%global fontfamily      Material Icons
%global fontsummary     Google material design system icons
%global fonts           font/*.otf font/*.ttf
%global fontorg         com.google

%global fontdescription \
Material design icons is the official icon set from Google.  The icons\
are designed under the material design guidelines.

Source0:        https://github.com/google/material-design-icons/archive/%{version}/material-design-icons-%{version}.tar.gz
Source1:        65-material-icons-fonts.conf

BuildRequires:  appstream libappstream

Name:           fonts-ttf-material-icons
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs       %{SOURCE1}
%setup -q -n material-design-icons-%{version}


%build
# fontbuild 
fontnames=$(
  for font in 'font/MaterialIconsOutlined-Regular.otf' 'font/MaterialIconsRound-Regular.otf' 'font/MaterialIconsSharp-Regular.otf' 'font/MaterialIconsTwoTone-Regular.otf' 'font/MaterialIcons-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'font/MaterialIconsOutlined-Regular.otf' 'font/MaterialIconsRound-Regular.otf' 'font/MaterialIconsSharp-Regular.otf' 'font/MaterialIconsTwoTone-Regular.otf' 'font/MaterialIcons-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the material-icons-fonts appstream file"
cat > "com.google.material-icons-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>com.google.material-icons-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>Material Icons</name>
  <summary><![CDATA[Google material design system icons]]></summary>
  <description>
    <p><![CDATA[Material design icons is the official icon set from Google.  The icons]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://google.github.io/material-design-icons/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "material-icons-fonts
echo "" > "material-icons-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/material-icons/
echo "%%dir %_fontsdir/otf/material-icons" >> "material-icons-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/material-icons/
echo "%%dir %_fontsdir/ttf/material-icons" >> "material-icons-fonts.list"
install -m 0644 -vp "font/MaterialIconsOutlined-Regular.otf" %buildroot%_fontsdir/otf/material-icons/
echo \"%_fontsdir/otf/material-icons//$(basename "font/MaterialIconsOutlined-Regular.otf")\" >> 'material-icons-fonts.list'
install -m 0644 -vp "font/MaterialIconsRound-Regular.otf" %buildroot%_fontsdir/otf/material-icons/
echo \"%_fontsdir/otf/material-icons//$(basename "font/MaterialIconsRound-Regular.otf")\" >> 'material-icons-fonts.list'
install -m 0644 -vp "font/MaterialIconsSharp-Regular.otf" %buildroot%_fontsdir/otf/material-icons/
echo \"%_fontsdir/otf/material-icons//$(basename "font/MaterialIconsSharp-Regular.otf")\" >> 'material-icons-fonts.list'
install -m 0644 -vp "font/MaterialIconsTwoTone-Regular.otf" %buildroot%_fontsdir/otf/material-icons/
echo \"%_fontsdir/otf/material-icons//$(basename "font/MaterialIconsTwoTone-Regular.otf")\" >> 'material-icons-fonts.list'
install -m 0644 -vp "font/MaterialIcons-Regular.ttf" %buildroot%_fontsdir/ttf/material-icons/
echo \"%_fontsdir/ttf/material-icons//$(basename "font/MaterialIcons-Regular.ttf")\" >> 'material-icons-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "material-icons-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "material-icons-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'com.google.material-icons-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "material-icons-fonts.list"
done

for fontdoc in 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "material-icons-fonts.list"
done

for fontlicense in 'LICENSE'; do
  echo %%doc "'${fontlicense}'" >> "material-icons-fonts.list"
done
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{oldname}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,ASL 2\.0,Apache-2.0,' \
    -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\(.*\)\]\]>,\1,' \
    -e 's,<font></font>,<font>Material Icons Outlined Regular</font>\n    <font>Material Icons Round Regular</font>\n    <font>Material Icons Sharp Regular</font>\n    <font>Material Icons Two Tone Regular</font>,' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'material-icons-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'material-icons-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files -n fonts-ttf-material-icons -f material-icons-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_6
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_0
- new version

