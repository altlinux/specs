Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ht-alegreya-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ht-alegreya-sans-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya-Sans
Version: 2.008
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/huertatipografica/Alegreya-Sans
%global forgesource https://github.com/huertatipografica/Alegreya-Sans/archive/2.008/Alegreya-Sans-2.008.tar.gz
%global archivename Alegreya-Sans-2.008
%global archiveext tar.gz
%global archiveurl https://github.com/huertatipografica/Alegreya-Sans/archive/2.008/Alegreya-Sans-2.008.tar.gz
%global topdir Alegreya-Sans-2.008
%global extractdir Alegreya-Sans-2.008
%global repo Alegreya-Sans
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 2.008
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

Release: alt1_7
URL:     https://www.huertatipografica.com/en/fonts/alegreya-sans-ht

%global foundry           HT
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya Sans
%global fontsummary       Alegreya Sans, a humanist sans serif font family with a calligraphic feeling
%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontdescription   \
Alegreya Sans is a humanist sans serif font family with a calligraphic feeling\
that conveys a dynamic and varied rhythm. This gives a pleasant feeling to\
readers of long texts.\
\
The family follows humanist proportions and principles, just like the serif\
version of the family, Alegreya. It achieves a playful and harmonious paragraph\
through elements carefully designed in an atmosphere of diversity.


Source0:  %{forgesource}
Source10: 58-ht-alegreya-sans-fonts.xml

Name:           fonts-otf-ht-alegreya-sans
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n Alegreya-Sans-2.008
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/AlegreyaSans-Black.otf' 'fonts/otf/AlegreyaSans-BlackItalic.otf' 'fonts/otf/AlegreyaSans-Bold.otf' 'fonts/otf/AlegreyaSans-BoldItalic.otf' 'fonts/otf/AlegreyaSans-ExtraBold.otf' 'fonts/otf/AlegreyaSans-ExtraBoldItalic.otf' 'fonts/otf/AlegreyaSans-Italic.otf' 'fonts/otf/AlegreyaSans-Light.otf' 'fonts/otf/AlegreyaSans-LightItalic.otf' 'fonts/otf/AlegreyaSans-Medium.otf' 'fonts/otf/AlegreyaSans-MediumItalic.otf' 'fonts/otf/AlegreyaSans-Regular.otf' 'fonts/otf/AlegreyaSans-Thin.otf' 'fonts/otf/AlegreyaSans-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/AlegreyaSans-Black.otf' 'fonts/otf/AlegreyaSans-BlackItalic.otf' 'fonts/otf/AlegreyaSans-Bold.otf' 'fonts/otf/AlegreyaSans-BoldItalic.otf' 'fonts/otf/AlegreyaSans-ExtraBold.otf' 'fonts/otf/AlegreyaSans-ExtraBoldItalic.otf' 'fonts/otf/AlegreyaSans-Italic.otf' 'fonts/otf/AlegreyaSans-Light.otf' 'fonts/otf/AlegreyaSans-LightItalic.otf' 'fonts/otf/AlegreyaSans-Medium.otf' 'fonts/otf/AlegreyaSans-MediumItalic.otf' 'fonts/otf/AlegreyaSans-Regular.otf' 'fonts/otf/AlegreyaSans-Thin.otf' 'fonts/otf/AlegreyaSans-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ht-alegreya-sans-fonts appstream file"
cat > "org.altlinux.ht-alegreya-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ht-alegreya-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>HT Alegreya Sans</name>
  <summary><![CDATA[Alegreya Sans, a humanist sans serif font family with a calligraphic feeling]]></summary>
  <description>
    <p><![CDATA[Alegreya Sans is a humanist sans serif font family with a calligraphic feeling]]></p><p><![CDATA[that conveys a dynamic and varied rhythm. This gives a pleasant feeling to]]></p><p><![CDATA[readers of long texts.]]></p> The family follows humanist proportions and principles, just like the serif version of the family, Alegreya. It achieves a playful and harmonious paragraph through elements carefully designed in an atmosphere of diversity.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.huertatipografica.com/en/fonts/alegreya-sans-ht</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ht-alegreya-sans-fonts
echo "" > "ht-alegreya-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo "%%dir %_fontsdir/otf/ht-alegreya-sans" >> "ht-alegreya-sans-fonts.list"
install -m 0644 -vp "fonts/otf/AlegreyaSans-Black.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Black.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-BlackItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-BlackItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Bold.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Bold.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-BoldItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-BoldItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-ExtraBold.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-ExtraBold.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-ExtraBoldItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Italic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Italic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Light.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Light.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-LightItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-LightItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Medium.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Medium.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-MediumItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-MediumItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Regular.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Regular.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-Thin.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-Thin.otf")\" >> 'ht-alegreya-sans-fonts.list'
install -m 0644 -vp "fonts/otf/AlegreyaSans-ThinItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya-sans/
echo \"%_fontsdir/otf/ht-alegreya-sans//$(basename "fonts/otf/AlegreyaSans-ThinItalic.otf")\" >> 'ht-alegreya-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/AlegreyaSans-Black.otf' 'fonts/otf/AlegreyaSans-BlackItalic.otf' 'fonts/otf/AlegreyaSans-Bold.otf' 'fonts/otf/AlegreyaSans-BoldItalic.otf' 'fonts/otf/AlegreyaSans-ExtraBold.otf' 'fonts/otf/AlegreyaSans-ExtraBoldItalic.otf' 'fonts/otf/AlegreyaSans-Italic.otf' 'fonts/otf/AlegreyaSans-Light.otf' 'fonts/otf/AlegreyaSans-LightItalic.otf' 'fonts/otf/AlegreyaSans-Medium.otf' 'fonts/otf/AlegreyaSans-MediumItalic.otf' 'fonts/otf/AlegreyaSans-Regular.otf' 'fonts/otf/AlegreyaSans-Thin.otf' 'fonts/otf/AlegreyaSans-ThinItalic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ht-alegreya-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ht-alegreya-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ht-alegreya-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ht-alegreya-sans-fonts.list"
done

for fontdoc in 'CONTRIBUTORS.txt' 'LICENSE.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "ht-alegreya-sans-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "ht-alegreya-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ht-alegreya-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ht-alegreya-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ht-alegreya-sans -f ht-alegreya-sans-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.008-alt1_7
- new version

