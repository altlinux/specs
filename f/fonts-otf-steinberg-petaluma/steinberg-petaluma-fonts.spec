Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname steinberg-petaluma-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname steinberg-petaluma-fonts
# The Scripts font has a different version from the other two
%global petalumaver       1.065
%global petalumascriptver 1.10

Version:        %{petalumaver}
URL:            https://www.smufl.org/fonts/

%global tag              petaluma-%{version}
%global date             20210127
%global forgeurl         https://github.com/steinbergmedia/petaluma

%global forgeurl https://github.com/steinbergmedia/petaluma
%global forgesource https://github.com/steinbergmedia/petaluma/archive/petaluma-%{petalumaver}/petaluma-petaluma-%{petalumaver}.tar.gz
%global archivename petaluma-petaluma-1.10
%global archiveext tar.gz
%global archiveurl https://github.com/steinbergmedia/petaluma/archive/petaluma-1.10/petaluma-petaluma-1.10.tar.gz
%global topdir petaluma-petaluma-1.10
%global extractdir petaluma-petaluma-1.10
%global repo petaluma
#global owner %nil
#global namespace %nil
%global scm git
%global tag petaluma-1.10
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 1.10
%global date 20210127
%global distprefix 20210127git1.10

Release:        alt1_2

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL
%global fontlicenses     redist/OFL*.txt
%global fontdocs         README.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description \
Petaluma is a Unicode typeface designed by Steinberg for its Dorico music\
notation and scoring application.  It is compliant with version 1.3 of\
the Standard Music Font Layout (SMuFL), a community-driven standard for\
how music symbols should be laid out in the Unicode Private Use Area\
(PUA) in the Basic Multilingual Plane (BMP) for compatibility between\
different scoring applications.

%global fontfamily0      Petaluma
%global fontsummary0     Petaluma music font
%global fonts0           redist/otf/Petaluma.otf
%global fontdescription0 %{common_description}\
\
This package contains the Petaluma font.  It is a Unicode typeface\
designed by Steinberg for its music notation and scoring application.

%global fontfamily1      PetalumaText
%global fontsummary1     Petaluma text font
%global fonts1           redist/otf/PetalumaText.otf
%global fontdescription1 %{common_description}\
\
This package contains the Petaluma Text font.  It is a Unicode typeface\
designed by Steinberg for its music notation and scoring application.

%global fontfamily2      PetalumaScript
%global fontsummary2     Petaluma script font
%global fonts2           redist/otf/PetalumaScript.otf
%global fontpkgheader2   \
Version:        %{petalumascriptver}\

%global fontdescription2 %{common_description}\
\
This package contains the Petaluma Script font.  It is a Unicode typeface\
designed by Steinberg for its music notation and scoring application.

Source0:        %{forgesource}
Source1:        65-steinberg-petaluma-fonts.conf
Source2:        65-steinberg-petalumatext-fonts.conf
Source3:        65-steinberg-petalumascript-fonts.conf

BuildRequires:  appstream libappstream

Name:           fonts-otf-steinberg-petaluma
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
%define _fontdir %_fontsdir/otf/steinberg-petaluma
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-otf-steinberg-petalumatext
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-steinberg-petalumatext
%{?fontdescription1}
%package     -n fonts-otf-steinberg-petalumascript
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-otf-steinberg-petalumascript
%{?fontdescription2}

# We cannot use %%fontmetapkg, because it doesn't know how to deal with a
# different version number for the Scripts font.
%package        all
Group: System/Fonts/True type
Summary:        All the font packages generated from %{oldname}
Version:        %{petalumaver}
Requires:       %{name} = %{petalumaver}-%{release}
Requires:       fonts-otf-steinberg-petalumatext = %{petalumaver}-%{release}
Requires:       fonts-otf-steinberg-petalumascript = %{petalumascriptver}-%{release}

%description    all
This meta-package installs all the font packages generated from the
%{oldname} source package.

%prep
%global fontconfs0       %{SOURCE1}
%global fontconfs1       %{SOURCE2}
%global fontconfs2       %{SOURCE3}
%setup -q -n petaluma-petaluma-%{petalumaver}

%build
# fontbuild 0
fontnames=$(
  for font in 'redist/otf/Petaluma.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'redist/otf/Petaluma.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the steinberg-petaluma-fonts appstream file"
cat > "org.smufl.steinberg-petaluma-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.smufl.steinberg-petaluma-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>steinberg Petaluma</name>
  <summary><![CDATA[Petaluma music font]]></summary>
  <description>
    <p><![CDATA[Petaluma is a Unicode typeface designed by Steinberg for its Dorico music]]></p><p><![CDATA[notation and scoring application.  It is compliant with version 1.3 of]]></p><p><![CDATA[the Standard Music Font Layout (SMuFL), a community-driven standard for]]></p><p><![CDATA[how music symbols should be laid out in the Unicode Private Use Area]]></p><p><![CDATA[(PUA) in the Basic Multilingual Plane (BMP) for compatibility between]]></p><p><![CDATA[different scoring applications.]]></p> This package contains the Petaluma font.  It is a Unicode typeface designed by Steinberg for its music notation and scoring application.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.smufl.org/fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'redist/otf/PetalumaText.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'redist/otf/PetalumaText.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the steinberg-petalumatext-fonts appstream file"
cat > "org.smufl.steinberg-petalumatext-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.smufl.steinberg-petalumatext-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>steinberg PetalumaText</name>
  <summary><![CDATA[Petaluma text font]]></summary>
  <description>
    <p><![CDATA[Petaluma is a Unicode typeface designed by Steinberg for its Dorico music]]></p><p><![CDATA[notation and scoring application.  It is compliant with version 1.3 of]]></p><p><![CDATA[the Standard Music Font Layout (SMuFL), a community-driven standard for]]></p><p><![CDATA[how music symbols should be laid out in the Unicode Private Use Area]]></p><p><![CDATA[(PUA) in the Basic Multilingual Plane (BMP) for compatibility between]]></p><p><![CDATA[different scoring applications.]]></p> This package contains the Petaluma Text font.  It is a Unicode typeface designed by Steinberg for its music notation and scoring application.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.smufl.org/fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'redist/otf/PetalumaScript.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'redist/otf/PetalumaScript.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the steinberg-petalumascript-fonts appstream file"
cat > "org.smufl.steinberg-petalumascript-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.smufl.steinberg-petalumascript-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>steinberg PetalumaScript</name>
  <summary><![CDATA[Petaluma script font]]></summary>
  <description>
    <p><![CDATA[Petaluma is a Unicode typeface designed by Steinberg for its Dorico music]]></p><p><![CDATA[notation and scoring application.  It is compliant with version 1.3 of]]></p><p><![CDATA[the Standard Music Font Layout (SMuFL), a community-driven standard for]]></p><p><![CDATA[how music symbols should be laid out in the Unicode Private Use Area]]></p><p><![CDATA[(PUA) in the Basic Multilingual Plane (BMP) for compatibility between]]></p><p><![CDATA[different scoring applications.]]></p> This package contains the Petaluma Script font.  It is a Unicode typeface designed by Steinberg for its music notation and scoring application.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.smufl.org/fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing steinberg-petaluma-fonts
echo "" > "steinberg-petaluma-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/steinberg-petaluma/
echo "%%dir %_fontsdir/otf/steinberg-petaluma" >> "steinberg-petaluma-fonts0.list"
install -m 0644 -vp "redist/otf/Petaluma.otf" %buildroot%_fontsdir/otf/steinberg-petaluma/
echo \"%_fontsdir/otf/steinberg-petaluma//$(basename "redist/otf/Petaluma.otf")\" >> 'steinberg-petaluma-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "steinberg-petaluma-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "steinberg-petaluma-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.smufl.steinberg-petaluma-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "steinberg-petaluma-fonts0.list"
done

for fontdoc in 'README.md' 'redist/FONTLOG.txt'; do
  echo %%doc "'${fontdoc}'" >> "steinberg-petaluma-fonts0.list"
done

for fontlicense in 'redist/OFL-FAQ.txt' 'redist/OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "steinberg-petaluma-fonts0.list"
done
echo Installing steinberg-petalumatext-fonts
echo "" > "steinberg-petalumatext-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/steinberg-petaluma/
echo "%%dir %_fontsdir/otf/steinberg-petaluma" >> "steinberg-petalumatext-fonts1.list"
install -m 0644 -vp "redist/otf/PetalumaText.otf" %buildroot%_fontsdir/otf/steinberg-petaluma/
echo \"%_fontsdir/otf/steinberg-petaluma//$(basename "redist/otf/PetalumaText.otf")\" >> 'steinberg-petalumatext-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE2' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "steinberg-petalumatext-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "steinberg-petalumatext-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.smufl.steinberg-petalumatext-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "steinberg-petalumatext-fonts1.list"
done

for fontdoc in 'README.md' 'redist/FONTLOG.txt'; do
  echo %%doc "'${fontdoc}'" >> "steinberg-petalumatext-fonts1.list"
done

for fontlicense in 'redist/OFL-FAQ.txt' 'redist/OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "steinberg-petalumatext-fonts1.list"
done
echo Installing steinberg-petalumascript-fonts
echo "" > "steinberg-petalumascript-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/steinberg-petaluma/
echo "%%dir %_fontsdir/otf/steinberg-petaluma" >> "steinberg-petalumascript-fonts2.list"
install -m 0644 -vp "redist/otf/PetalumaScript.otf" %buildroot%_fontsdir/otf/steinberg-petaluma/
echo \"%_fontsdir/otf/steinberg-petaluma//$(basename "redist/otf/PetalumaScript.otf")\" >> 'steinberg-petalumascript-fonts2.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE3' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "steinberg-petalumascript-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "steinberg-petalumascript-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.smufl.steinberg-petalumascript-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "steinberg-petalumascript-fonts2.list"
done

for fontdoc in 'README.md' 'redist/FONTLOG.txt'; do
  echo %%doc "'${fontdoc}'" >> "steinberg-petalumascript-fonts2.list"
done

for fontlicense in 'redist/OFL-FAQ.txt' 'redist/OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "steinberg-petalumascript-fonts2.list"
done
metainfo="%{buildroot}%{_metainfodir}/%{fontorg}.%{oldname}.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.steinberg-petalumascript-fonts.metainfo.xml \
%{buildroot}%{_metainfodir}/%{fontorg}.steinberg-petalumatext-fonts.metainfo.xml"

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,OFL,OFL-1.1-RFN,' \
    -e 's,updatecontact,update_contact,g' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

# Install the SMuFL metadata
install -m 0644 -p redist/petaluma_metadata.json \
        %{buildroot}%{_fontdir}/metadata.json

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'steinberg-petaluma-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'steinberg-petaluma-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'steinberg-petalumatext-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'steinberg-petalumatext-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'steinberg-petalumascript-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'steinberg-petalumascript-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files -n fonts-otf-steinberg-petaluma -f steinberg-petaluma-fonts0.list
%{_fontdir}/metadata.json

%files -n fonts-otf-steinberg-petalumatext -f steinberg-petalumatext-fonts1.list

%files -n fonts-otf-steinberg-petalumascript -f steinberg-petalumascript-fonts2.list

%files          all

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 1.065-alt1_2
- update

