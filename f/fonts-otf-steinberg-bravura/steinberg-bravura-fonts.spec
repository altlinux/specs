Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname steinberg-bravura-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname steinberg-bravura-fonts
Version:        1.392
URL:            https://www.smufl.org/fonts/

%global tag         bravura-%{version}
%global date        20210209
%global forgeurl    https://github.com/steinbergmedia/bravura

# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/steinbergmedia/bravura
%global forgesource https://github.com/steinbergmedia/bravura/archive/bravura-1.392/bravura-bravura-1.392.tar.gz
%global archivename bravura-bravura-1.392
%global archiveext tar.gz
%global archiveurl https://github.com/steinbergmedia/bravura/archive/bravura-1.392/bravura-bravura-1.392.tar.gz
%global topdir bravura-bravura-1.392
%global extractdir bravura-bravura-1.392
%global repo bravura
#global owner %nil
#global namespace %nil
%global scm git
%global tag bravura-1.392
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 1.392
%global date 20210209
%global distprefix 20210209git1.392
# FedoraForgeMeta2ALT: end generated meta

Release:        alt1_2

%global foundry          steinberg
%global fontorg          org.smufl
%global fontlicense      OFL
%global fontlicenses     LICENSE.txt
%global fontdocs         README.md redist/bravura-text.md redist/FONTLOG.txt
%global fontdocsex       %{fontlicenses}

%global common_description \
Bravura is an OpenType music font developed for Steinberg's Dorico music\
notation and composition software.  It is also the reference font for\
Standard Music Font Layout (SMuFL), which provides a standard way of\
mapping the thousands of musical symbols required by conventional music\
notation into the Private Use Area in Unicode's Basic Multilingual Plane\
for a single (format-independent) font.

%global fontfamily0      Bravura
%global fontsummary0     Bravura music font
%global fonts0           redist/otf/Bravura.otf
%global fontdescription0 %{common_description}\
\
This package contains the Bravura font family.  It is a Unicode typeface\
designed by Steinberg for its music notation and scoring application.\


# This can be removed when F36 reaches EOL
%global fontpkgheader0 \
Obsoletes:      steinberg-bravura-fonts-common < 1.360\
Provides:       steinberg-bravura-fonts-common = %{version}-%{release}\


%global fontfamily1      BravuraText
%global fontsummary1     Bravura text font
%global fonts1           redist/otf/BravuraText.otf
%global fontdescription1 %{common_description}\
\
This package contains the Bravura Text font family.  It is a Unicode\
typeface designed by Steinberg for its music notation and scoring\
application.\


# This can be removed when F36 reaches EOL
%global fontpkgheader1 \
Obsoletes:      steinberg-bravura-text-fonts < 1.360\
Provides:       steinberg-bravura-text-fonts = %{version}-%{release}\


Source0:        %{forgesource}
Source1:        65-steinberg-bravura-fonts.conf
Source2:        65-steinberg-bravuratext-fonts.conf

BuildRequires:  appstream libappstream

Name:           fonts-otf-steinberg-bravura
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-otf-steinberg-bravuratext
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-steinberg-bravuratext
%{?fontdescription1}
%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-steinberg-bravura = %EVR
Requires:  fonts-otf-steinberg-bravuratext = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fontconfs0       %{SOURCE1}
%global fontconfs1       %{SOURCE2}
%define _fontdir %_fontsdir/otf/steinberg-bravura
%setup -q -n bravura-bravura-1.392
 
%build
# fontbuild 0
fontnames=$(
  for font in 'redist/otf/Bravura.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'redist/otf/Bravura.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the steinberg-bravura-fonts appstream file"
cat > "org.smufl.steinberg-bravura-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.smufl.steinberg-bravura-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>steinberg Bravura</name>
  <summary><![CDATA[Bravura music font]]></summary>
  <description>
    <p><![CDATA[Bravura is an OpenType music font developed for Steinberg's Dorico music]]></p><p><![CDATA[notation and composition software.  It is also the reference font for]]></p><p><![CDATA[Standard Music Font Layout (SMuFL), which provides a standard way of]]></p><p><![CDATA[mapping the thousands of musical symbols required by conventional music]]></p><p><![CDATA[notation into the Private Use Area in Unicode's Basic Multilingual Plane]]></p><p><![CDATA[for a single (format-independent) font.]]></p> This package contains the Bravura font family.  It is a Unicode typeface designed by Steinberg for its music notation and scoring application.
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
  for font in 'redist/otf/BravuraText.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'redist/otf/BravuraText.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the steinberg-bravuratext-fonts appstream file"
cat > "org.smufl.steinberg-bravuratext-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.smufl.steinberg-bravuratext-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>steinberg BravuraText</name>
  <summary><![CDATA[Bravura text font]]></summary>
  <description>
    <p><![CDATA[Bravura is an OpenType music font developed for Steinberg's Dorico music]]></p><p><![CDATA[notation and composition software.  It is also the reference font for]]></p><p><![CDATA[Standard Music Font Layout (SMuFL), which provides a standard way of]]></p><p><![CDATA[mapping the thousands of musical symbols required by conventional music]]></p><p><![CDATA[notation into the Private Use Area in Unicode's Basic Multilingual Plane]]></p><p><![CDATA[for a single (format-independent) font.]]></p> This package contains the Bravura Text font family.  It is a Unicode typeface designed by Steinberg for its music notation and scoring application.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.smufl.org/fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing steinberg-bravura-fonts
echo "" > "steinberg-bravura-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/steinberg-bravura/
echo "%%dir %_fontsdir/otf/steinberg-bravura" >> "steinberg-bravura-fonts0.list"
install -m 0644 -vp "redist/otf/Bravura.otf" %buildroot%_fontsdir/otf/steinberg-bravura/
echo \"%_fontsdir/otf/steinberg-bravura//$(basename "redist/otf/Bravura.otf")\" >> 'steinberg-bravura-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "steinberg-bravura-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "steinberg-bravura-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.smufl.steinberg-bravura-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "steinberg-bravura-fonts0.list"
done

for fontdoc in 'README.md' 'redist/bravura-text.md' 'redist/FONTLOG.txt'; do
  echo %%doc "'${fontdoc}'" >> "steinberg-bravura-fonts0.list"
done

for fontlicense in 'LICENSE.txt'; do
  echo %%doc "'${fontlicense}'" >> "steinberg-bravura-fonts0.list"
done
echo Installing steinberg-bravuratext-fonts
echo "" > "steinberg-bravuratext-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/steinberg-bravura/
echo "%%dir %_fontsdir/otf/steinberg-bravura" >> "steinberg-bravuratext-fonts1.list"
install -m 0644 -vp "redist/otf/BravuraText.otf" %buildroot%_fontsdir/otf/steinberg-bravura/
echo \"%_fontsdir/otf/steinberg-bravura//$(basename "redist/otf/BravuraText.otf")\" >> 'steinberg-bravuratext-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE2' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "steinberg-bravuratext-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "steinberg-bravuratext-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.smufl.steinberg-bravuratext-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "steinberg-bravuratext-fonts1.list"
done

for fontdoc in 'README.md' 'redist/bravura-text.md' 'redist/FONTLOG.txt'; do
  echo %%doc "'${fontdoc}'" >> "steinberg-bravuratext-fonts1.list"
done

for fontlicense in 'LICENSE.txt'; do
  echo %%doc "'${fontlicense}'" >> "steinberg-bravuratext-fonts1.list"
done
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{oldname}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,OFL,OFL-1.1-RFN,' \
    -e 's,updatecontact,update_contact,g' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

# Install the SMuFL metadata
install -m 0644 -p redist/bravura_metadata.json \
        %{buildroot}%{_fontdir}/metadata.json

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'steinberg-bravura-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'steinberg-bravura-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'steinberg-bravuratext-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'steinberg-bravuratext-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files -n fonts-otf-steinberg-bravura -f steinberg-bravura-fonts0.list
%_fontsdir/*/steinberg-bravura/metadata.json

%files -n fonts-otf-steinberg-bravuratext -f steinberg-bravuratext-fonts1.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 1.392-alt1_2
- update

