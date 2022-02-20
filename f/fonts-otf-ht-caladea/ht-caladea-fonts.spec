Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ht-caladea-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ht-caladea-fonts
%global forgeurl https://github.com/huertatipografica/Caladea
%global commit 336a529cfad3d103d6527752686f8331d13e820a
Epoch: 1
Version: 1.001
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/huertatipografica/Caladea
%global forgesource https://github.com/huertatipografica/Caladea/archive/336a529cfad3d103d6527752686f8331d13e820a/Caladea-336a529cfad3d103d6527752686f8331d13e820a.tar.gz
%global archivename Caladea-336a529cfad3d103d6527752686f8331d13e820a
%global archiveext tar.gz
%global archiveurl https://github.com/huertatipografica/Caladea/archive/336a529cfad3d103d6527752686f8331d13e820a/Caladea-336a529cfad3d103d6527752686f8331d13e820a.tar.gz
%global topdir Caladea-336a529cfad3d103d6527752686f8331d13e820a
%global extractdir Caladea-336a529cfad3d103d6527752686f8331d13e820a
%global repo Caladea
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 336a529cfad3d103d6527752686f8331d13e820a
#global shortcommit %nil
#global branch %nil
%global version 1.001
#global date %nil
%global distprefix .git336a529
# FedoraForgeMeta2ALT: end generated meta

Release:  alt1_6
URL:     https://github.com/huertatipografica/Caladea

%global foundry           HT
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Caladea
%global fontsummary       Caladea, a serif font family metric-compatible with Cambria font family
%global fontpkgheader     \
Obsoletes:      google-crosextra-caladea-fonts < 1.002-0.15.20130214\
Provides:       google-crosextra-caladea-fonts = 1:%{version}-%{release}\

%global fonts             fonts/otf/*otf
%global fontdescription   \
Caladea is a free modern, friendly serif font family based on Cambo\
(https://fonts.google.com/specimen/Cambo) Designed by Carolina Giovagnoli\
and AndrA.s Torresi for Huerta TipogrA.fica in 2012.\
\
Cambo is a modern Latin typeface inspired by the contrast, style and ornaments\
of Khmer typefaces and writing styles. Its main objective is to be used to\
write Latin texts in a Khmer context, but it is also an elegant choice for all\
kinds of texts.\
\
Caladea is metric-compatible with Cambria font.

Source0:  %{forgesource}
Source1:  30-0-ht-caladea-fonts.conf
Source2:  62-ht-caladea-fonts.conf

Name:           fonts-otf-ht-caladea
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs         %{SOURCE1} %{SOURCE2}
%setup -q -n Caladea-336a529cfad3d103d6527752686f8331d13e820a
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/Caladea-Bold.otf' 'fonts/otf/Caladea-BoldItalic.otf' 'fonts/otf/Caladea-Italic.otf' 'fonts/otf/Caladea-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Caladea-Bold.otf' 'fonts/otf/Caladea-BoldItalic.otf' 'fonts/otf/Caladea-Italic.otf' 'fonts/otf/Caladea-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ht-caladea-fonts appstream file"
cat > "org.altlinux.ht-caladea-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ht-caladea-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>HT Caladea</name>
  <summary><![CDATA[Caladea, a serif font family metric-compatible with Cambria font family]]></summary>
  <description>
    <p><![CDATA[Caladea is a free modern, friendly serif font family based on Cambo]]></p><p><![CDATA[(https://fonts.google.com/specimen/Cambo) Designed by Carolina Giovagnoli]]></p><p><![CDATA[and Andrés Torresi for Huerta Tipográfica in 2012.]]></p> Cambo is a modern Latin typeface inspired by the contrast, style and ornaments of Khmer typefaces and writing styles. Its main objective is to be used to write Latin texts in a Khmer context, but it is also an elegant choice for all kinds of texts. Caladea is metric-compatible with Cambria font.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://github.com/huertatipografica/Caladea</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ht-caladea-fonts
echo "" > "ht-caladea-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ht-caladea/
echo "%%dir %_fontsdir/otf/ht-caladea" >> "ht-caladea-fonts.list"
install -m 0644 -vp "fonts/otf/Caladea-Bold.otf" %buildroot%_fontsdir/otf/ht-caladea/
echo \"%_fontsdir/otf/ht-caladea//$(basename "fonts/otf/Caladea-Bold.otf")\" >> 'ht-caladea-fonts.list'
install -m 0644 -vp "fonts/otf/Caladea-BoldItalic.otf" %buildroot%_fontsdir/otf/ht-caladea/
echo \"%_fontsdir/otf/ht-caladea//$(basename "fonts/otf/Caladea-BoldItalic.otf")\" >> 'ht-caladea-fonts.list'
install -m 0644 -vp "fonts/otf/Caladea-Italic.otf" %buildroot%_fontsdir/otf/ht-caladea/
echo \"%_fontsdir/otf/ht-caladea//$(basename "fonts/otf/Caladea-Italic.otf")\" >> 'ht-caladea-fonts.list'
install -m 0644 -vp "fonts/otf/Caladea-Regular.otf" %buildroot%_fontsdir/otf/ht-caladea/
echo \"%_fontsdir/otf/ht-caladea//$(basename "fonts/otf/Caladea-Regular.otf")\" >> 'ht-caladea-fonts.list'

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ht-caladea-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ht-caladea-fonts.list"
done

for fontdoc in 'AUTHOR.txt' 'CONTRIBUTORS.txt' 'requirements.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "ht-caladea-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "ht-caladea-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ht-caladea-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ht-caladea-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ht-caladea -f ht-caladea-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1:1.001-alt1_6
- new version

