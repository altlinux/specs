Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname fontawesome5-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname fontawesome5-fonts
Name:           fonts-otf-fontawesome5
Summary:        Support files for the FontAwesome 5 fonts
Version:        5.15.4
Release:        alt1_2
License:        MIT
URL:            https://fontawesome.com/
BuildArch:      noarch

%global _desc \
Font Awesome gives you scalable vector icons that can instantly be\
customized - size, color, drop shadow, and anything that can be done\
with the power of CSS.

%global fontlicense     OFL
%global fontlicenses    LICENSE.txt
%global fontdocs        CHANGELOG.md README* UPGRADING.md
%global fontorg         com.fontawesome

%global fontfamily1     FontAwesome5 Free
%global fontsummary1    Iconic font set
%global fonts1          otfs/*Free*
%global fontpkgheader1  \
Requires:       fonts-otf-fontawesome5 = %{version}

%global fontdescription1 %_desc\
\
The FontAwesome Free Fonts contain large numbers of icons packaged as\
font files.

%global fontfamily2     FontAwesome5 Brands
%global fontsummary2    Iconic font set
%global fonts2          otfs/*Brands*
%global fontpkgheader2  \
Requires:       fonts-otf-fontawesome5 = %{version}

%global fontdescription2 %_desc\
\
The FontAwesome Brand Fonts contain brand logos packaged as font files.

Source0:        https://github.com/FortAwesome/Font-Awesome/archive/%{version}/Font-Awesome-%{version}.tar.gz
Source1:        60-fontawesome5-free-fonts.conf
Source2:        60-fontawesome5-brands-fonts.conf
# Script to generate Source3
Source3:        trademarks.py
Source4:        README-Trademarks.txt

# Not for upstream.  This patch modifies the CSS to point to local OpenType font
# files, rather than to the eot, svg, ttf, woff, and woff2 web fonts, as
# required by Fedora's font packaging guidelines.
Patch0:         %{oldname}-opentype-css.patch

BuildRequires:  appstream libappstream
Source44: import.info

%description 
%_desc

This package contains CSS, SCSS and LESS style files for each of the
fonts in the FontAwesome family, as well as JSON and YAML metadata.

%package     -n fonts-otf-fontawesome5-free
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-fontawesome5-free
%{?fontdescription1}
%package     -n fonts-otf-fontawesome5-brands
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-otf-fontawesome5-brands
%{?fontdescription2}
%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-fontawesome5-free = %EVR
Requires:  fonts-otf-fontawesome5-brands = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%package web
Group: System/Fonts/True type
License:        CC-BY
Summary:        Iconic font set, javascript and SVG files

%description web 
%_desc

This package contains javascript and SVG files, which are typically used
on web pages.

%prep
%global fontconfs1      %{SOURCE1}
%global fontconfs2      %{SOURCE2}
%setup -q -n Font-Awesome-%{version}
%patch0 -p1

cp -p %{SOURCE4} .

%build
# fontbuild 1
fontnames=$(
  for font in 'otfs/Font Awesome 5 Free-Regular-400.otf' 'otfs/Font Awesome 5 Free-Solid-900.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'otfs/Font Awesome 5 Free-Regular-400.otf' 'otfs/Font Awesome 5 Free-Solid-900.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the fontawesome5-free-fonts appstream file"
cat > "com.fontawesome.fontawesome5-free-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>com.fontawesome.fontawesome5-free-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>FontAwesome5 Free</name>
  <summary><![CDATA[Iconic font set]]></summary>
  <description>
    <p><![CDATA[Font Awesome gives you scalable vector icons that can instantly be]]></p><p><![CDATA[customized - size, color, drop shadow, and anything that can be done]]></p><p><![CDATA[with the power of CSS.]]></p> The FontAwesome Free Fonts contain large numbers of icons packaged as font files.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://fontawesome.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'otfs/Font Awesome 5 Brands-Regular-400.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'otfs/Font Awesome 5 Brands-Regular-400.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the fontawesome5-brands-fonts appstream file"
cat > "com.fontawesome.fontawesome5-brands-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>com.fontawesome.fontawesome5-brands-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>FontAwesome5 Brands</name>
  <summary><![CDATA[Iconic font set]]></summary>
  <description>
    <p><![CDATA[Font Awesome gives you scalable vector icons that can instantly be]]></p><p><![CDATA[customized - size, color, drop shadow, and anything that can be done]]></p><p><![CDATA[with the power of CSS.]]></p> The FontAwesome Brand Fonts contain brand logos packaged as font files.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://fontawesome.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing fontawesome5-free-fonts
echo "" > "fontawesome5-free-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/fontawesome5/
echo "%%dir %_fontsdir/otf/fontawesome5" >> "fontawesome5-free-fonts1.list"
install -m 0644 -vp "otfs/Font Awesome 5 Free-Regular-400.otf" %buildroot%_fontsdir/otf/fontawesome5/
echo \"%_fontsdir/otf/fontawesome5//$(basename "otfs/Font Awesome 5 Free-Regular-400.otf")\" >> 'fontawesome5-free-fonts1.list'
install -m 0644 -vp "otfs/Font Awesome 5 Free-Solid-900.otf" %buildroot%_fontsdir/otf/fontawesome5/
echo \"%_fontsdir/otf/fontawesome5//$(basename "otfs/Font Awesome 5 Free-Solid-900.otf")\" >> 'fontawesome5-free-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "fontawesome5-free-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "fontawesome5-free-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'com.fontawesome.fontawesome5-free-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "fontawesome5-free-fonts1.list"
done

for fontdoc in 'CHANGELOG.md' 'README-Trademarks.txt' 'README.md' 'UPGRADING.md'; do
  echo %%doc "'${fontdoc}'" >> "fontawesome5-free-fonts1.list"
done

for fontlicense in 'LICENSE.txt'; do
  echo %%doc "'${fontlicense}'" >> "fontawesome5-free-fonts1.list"
done
echo Installing fontawesome5-brands-fonts
echo "" > "fontawesome5-brands-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/fontawesome5/
echo "%%dir %_fontsdir/otf/fontawesome5" >> "fontawesome5-brands-fonts2.list"
install -m 0644 -vp "otfs/Font Awesome 5 Brands-Regular-400.otf" %buildroot%_fontsdir/otf/fontawesome5/
echo \"%_fontsdir/otf/fontawesome5//$(basename "otfs/Font Awesome 5 Brands-Regular-400.otf")\" >> 'fontawesome5-brands-fonts2.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE2' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "fontawesome5-brands-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "fontawesome5-brands-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'com.fontawesome.fontawesome5-brands-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "fontawesome5-brands-fonts2.list"
done

for fontdoc in 'CHANGELOG.md' 'README-Trademarks.txt' 'README.md' 'UPGRADING.md'; do
  echo %%doc "'${fontdoc}'" >> "fontawesome5-brands-fonts2.list"
done

for fontlicense in 'LICENSE.txt'; do
  echo %%doc "'${fontlicense}'" >> "fontawesome5-brands-fonts2.list"
done

# Install the web files
mkdir -p %{buildroot}%{_datadir}/fontawesome5
cp -a css js less metadata scss sprites svgs %{buildroot}%{_datadir}/fontawesome5

# Fix up the generated metainfo; see bz 1943727
sed -e 's,OFL,OFL-1.1,' \
    -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\([^]]*\)\]\]>,\1,g' \
    -i %{buildroot}%{_metainfodir}/*.metainfo.xml

# Validate the metainfo
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/%{fontorg}.fontawesome5-free-fonts.metainfo.xml
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/%{fontorg}.fontawesome5-brands-fonts.metainfo.xml

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'fontawesome5-free-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'fontawesome5-free-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'fontawesome5-brands-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'fontawesome5-brands-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files
%dir %{_datadir}/fontawesome5/
%{_datadir}/fontawesome5/css/
%{_datadir}/fontawesome5/less/
%{_datadir}/fontawesome5/metadata/
%{_datadir}/fontawesome5/scss/

%files -n fonts-otf-fontawesome5-free -f fontawesome5-free-fonts1.list
%files -n fonts-otf-fontawesome5-brands -f fontawesome5-brands-fonts2.list

%files web
%doc CHANGELOG.md README* UPGRADING.md
%doc --no-dereference LICENSE.txt
%dir %{_datadir}/fontawesome5/
%{_datadir}/fontawesome5/js/
%{_datadir}/fontawesome5/sprites/
%{_datadir}/fontawesome5/svgs/

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 5.15.4-alt1_2
- update

