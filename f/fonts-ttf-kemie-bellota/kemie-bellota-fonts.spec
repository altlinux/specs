Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname kemie-bellota-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname kemie-bellota-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/kemie/Bellota-Font/
Version:            4.1
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/kemie/Bellota-Font/
%global forgesource https://github.com/kemie/Bellota-Font//archive/4.1/Bellota-Font-4.1.tar.gz
%global archivename Bellota-Font-4.1
%global archiveext tar.gz
%global archiveurl https://github.com/kemie/Bellota-Font//archive/4.1/Bellota-Font-4.1.tar.gz
%global topdir Bellota-Font-4.1
%global extractdir Bellota-Font-4.1
%global repo Bellota-Font
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 4.1
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

Release: alt1_3
URL:     %{forgeurl}

%global foundry           kemie
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *TXT *md
%global fontdocsex        %{fontlicenses}

%global common_description \
The Bellota font families are ornamented, low contrast sans-serifs with text\
and swash alternates. Theya.'re just cute enough! They include stylistic\
alternates (for swash and non-ornamented characters) and ligatures available\
through OpenType features.

%global fontfamily0       Bellota
%global fontsummary0      An ornamented, cute, low contrast sans-serif font family
%global fonts0            ttf/*ttf
%global fontsex0          %{fonts1}
%global fontdescription0  \
%{common_description}\
\
Bellota, is the most exuberant variation published by the project.

%global fontfamily1       Bellota Text
%global fontsummary1      An ornamented, slightly demure, cute, low contrast sans-serif font family
%global fontpkgheader1    \
Requires: font(bellota)\

%global fonts1            ttf/BellotaText*ttf
%global fontdescription1  \
%{common_description}\
\
Bellota Text is slightly more demure than Bellota itself.

Source0:  %{forgesource}
Source10: 60-kemie-bellota-fonts.xml
Source11: 60-kemie-bellota-text-fonts.xml

Name:           fonts-ttf-kemie-bellota
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-kemie-bellota-text
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-kemie-bellota-text
%{?fontdescription1}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-kemie-bellota = %EVR
Requires:  fonts-ttf-kemie-bellota-text = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%setup -q -n Bellota-Font-4.1

%build
# fontbuild 0
fontnames=$(
  for font in 'ttf/Bellota-Bold.ttf' 'ttf/Bellota-BoldItalic.ttf' 'ttf/Bellota-Italic.ttf' 'ttf/Bellota-Light.ttf' 'ttf/Bellota-LightItalic.ttf' 'ttf/Bellota-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'ttf/Bellota-Bold.ttf' 'ttf/Bellota-BoldItalic.ttf' 'ttf/Bellota-Italic.ttf' 'ttf/Bellota-Light.ttf' 'ttf/Bellota-LightItalic.ttf' 'ttf/Bellota-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the kemie-bellota-fonts appstream file"
cat > "org.altlinux.kemie-bellota-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.kemie-bellota-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>kemie Bellota</name>
  <summary><![CDATA[An ornamented, cute, low contrast sans-serif font family]]></summary>
  <description>
    <p><![CDATA[The Bellota font families are ornamented, low contrast sans-serifs with text]]></p><p><![CDATA[and swash alternates. They’re just cute enough! They include stylistic]]></p><p><![CDATA[alternates (for swash and non-ornamented characters) and ligatures available]]></p><p><![CDATA[through OpenType features.]]></p> Bellota, is the most exuberant variation published by the project.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'ttf/BellotaText-Bold.ttf' 'ttf/BellotaText-BoldItalic.ttf' 'ttf/BellotaText-Italic.ttf' 'ttf/BellotaText-Light.ttf' 'ttf/BellotaText-LightItalic.ttf' 'ttf/BellotaText-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'ttf/BellotaText-Bold.ttf' 'ttf/BellotaText-BoldItalic.ttf' 'ttf/BellotaText-Italic.ttf' 'ttf/BellotaText-Light.ttf' 'ttf/BellotaText-LightItalic.ttf' 'ttf/BellotaText-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the kemie-bellota-text-fonts appstream file"
cat > "org.altlinux.kemie-bellota-text-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.kemie-bellota-text-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>kemie Bellota Text</name>
  <summary><![CDATA[An ornamented, slightly demure, cute, low contrast sans-serif font family]]></summary>
  <description>
    <p><![CDATA[The Bellota font families are ornamented, low contrast sans-serifs with text]]></p><p><![CDATA[and swash alternates. They’re just cute enough! They include stylistic]]></p><p><![CDATA[alternates (for swash and non-ornamented characters) and ligatures available]]></p><p><![CDATA[through OpenType features.]]></p> Bellota Text is slightly more demure than Bellota itself.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing kemie-bellota-fonts
echo "" > "kemie-bellota-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/kemie-bellota/
echo "%%dir %_fontsdir/ttf/kemie-bellota" >> "kemie-bellota-fonts0.list"
install -m 0644 -vp "ttf/Bellota-Bold.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-Bold.ttf")\" >> 'kemie-bellota-fonts0.list'
install -m 0644 -vp "ttf/Bellota-BoldItalic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-BoldItalic.ttf")\" >> 'kemie-bellota-fonts0.list'
install -m 0644 -vp "ttf/Bellota-Italic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-Italic.ttf")\" >> 'kemie-bellota-fonts0.list'
install -m 0644 -vp "ttf/Bellota-Light.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-Light.ttf")\" >> 'kemie-bellota-fonts0.list'
install -m 0644 -vp "ttf/Bellota-LightItalic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-LightItalic.ttf")\" >> 'kemie-bellota-fonts0.list'
install -m 0644 -vp "ttf/Bellota-Regular.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/Bellota-Regular.ttf")\" >> 'kemie-bellota-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'ttf/Bellota-Bold.ttf' 'ttf/Bellota-BoldItalic.ttf' 'ttf/Bellota-Italic.ttf' 'ttf/Bellota-Light.ttf' 'ttf/Bellota-LightItalic.ttf' 'ttf/Bellota-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "kemie-bellota-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "kemie-bellota-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.kemie-bellota-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "kemie-bellota-fonts0.list"
done

for fontdoc in 'authors.txt' 'contributors.txt' 'FONTLOG.TXT' 'readme.md'; do
  echo %%doc "'${fontdoc}'" >> "kemie-bellota-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "kemie-bellota-fonts0.list"
done
echo Installing kemie-bellota-text-fonts
echo "" > "kemie-bellota-text-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/kemie-bellota/
echo "%%dir %_fontsdir/ttf/kemie-bellota" >> "kemie-bellota-text-fonts1.list"
install -m 0644 -vp "ttf/BellotaText-Bold.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-Bold.ttf")\" >> 'kemie-bellota-text-fonts1.list'
install -m 0644 -vp "ttf/BellotaText-BoldItalic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-BoldItalic.ttf")\" >> 'kemie-bellota-text-fonts1.list'
install -m 0644 -vp "ttf/BellotaText-Italic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-Italic.ttf")\" >> 'kemie-bellota-text-fonts1.list'
install -m 0644 -vp "ttf/BellotaText-Light.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-Light.ttf")\" >> 'kemie-bellota-text-fonts1.list'
install -m 0644 -vp "ttf/BellotaText-LightItalic.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-LightItalic.ttf")\" >> 'kemie-bellota-text-fonts1.list'
install -m 0644 -vp "ttf/BellotaText-Regular.ttf" %buildroot%_fontsdir/ttf/kemie-bellota/
echo \"%_fontsdir/ttf/kemie-bellota//$(basename "ttf/BellotaText-Regular.ttf")\" >> 'kemie-bellota-text-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'ttf/BellotaText-Bold.ttf' 'ttf/BellotaText-BoldItalic.ttf' 'ttf/BellotaText-Italic.ttf' 'ttf/BellotaText-Light.ttf' 'ttf/BellotaText-LightItalic.ttf' 'ttf/BellotaText-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "kemie-bellota-text-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "kemie-bellota-text-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.kemie-bellota-text-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "kemie-bellota-text-fonts1.list"
done

for fontdoc in 'authors.txt' 'contributors.txt' 'FONTLOG.TXT' 'readme.md'; do
  echo %%doc "'${fontdoc}'" >> "kemie-bellota-text-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "kemie-bellota-text-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'kemie-bellota-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'kemie-bellota-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'kemie-bellota-text-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'kemie-bellota-text-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-kemie-bellota -f kemie-bellota-fonts0.list
%files -n fonts-ttf-kemie-bellota-text -f kemie-bellota-text-fonts1.list

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 4.1-alt1_3
- new version

