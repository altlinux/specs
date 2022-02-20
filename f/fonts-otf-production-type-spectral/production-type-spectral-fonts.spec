Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname production-type-spectral-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname production-type-spectral-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/productiontype/Spectral
%global commit      748733e3761fc7985ca9c473996ed121954debf8
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/productiontype/Spectral
%global forgesource https://github.com/productiontype/Spectral/archive/748733e3761fc7985ca9c473996ed121954debf8/Spectral-748733e3761fc7985ca9c473996ed121954debf8.tar.gz
%global archivename Spectral-748733e3761fc7985ca9c473996ed121954debf8
%global archiveext tar.gz
%global archiveurl https://github.com/productiontype/Spectral/archive/748733e3761fc7985ca9c473996ed121954debf8/Spectral-748733e3761fc7985ca9c473996ed121954debf8.tar.gz
%global topdir Spectral-748733e3761fc7985ca9c473996ed121954debf8
%global extractdir Spectral-748733e3761fc7985ca9c473996ed121954debf8
%global repo Spectral
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 748733e3761fc7985ca9c473996ed121954debf8
#global shortcommit %nil
#global branch %nil
%global version 2.003
#global date %nil
%global distprefix .git748733e
# FedoraForgeMeta2ALT: end generated meta

Version: 2.003
Release: alt1_6
URL:     %{forgeurl}

%global foundry           Production Type
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Spectral
%global fontsummary       Spectral, an efficient and versatile serif font family
%global fonts             fonts/desktop_otf/*otf
%global fontdescription   \
Spectral is a versatile serif font family available in seven weights of roman\
and italic, with small caps. Spectral offers an efficient, beautiful design\
thata.'s intended primarily for text-rich, screen-first environments and\
long-form reading.

Source0:  %{forgesource}
Source10: 57-production-type-spectral-fonts.xml

Name:           fonts-otf-production-type-spectral
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
%setup -q -n Spectral-748733e3761fc7985ca9c473996ed121954debf8

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/desktop_otf/Spectral-Bold.otf' 'fonts/desktop_otf/Spectral-BoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraBold.otf' 'fonts/desktop_otf/Spectral-ExtraBoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraLight.otf' 'fonts/desktop_otf/Spectral-ExtraLightItalic.otf' 'fonts/desktop_otf/spectral-italic.otf' 'fonts/desktop_otf/Spectral-Light.otf' 'fonts/desktop_otf/Spectral-LightItalic.otf' 'fonts/desktop_otf/Spectral-Medium.otf' 'fonts/desktop_otf/Spectral-MediumItalic.otf' 'fonts/desktop_otf/Spectral-Regular.otf' 'fonts/desktop_otf/Spectral-SemiBold.otf' 'fonts/desktop_otf/Spectral-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/desktop_otf/Spectral-Bold.otf' 'fonts/desktop_otf/Spectral-BoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraBold.otf' 'fonts/desktop_otf/Spectral-ExtraBoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraLight.otf' 'fonts/desktop_otf/Spectral-ExtraLightItalic.otf' 'fonts/desktop_otf/spectral-italic.otf' 'fonts/desktop_otf/Spectral-Light.otf' 'fonts/desktop_otf/Spectral-LightItalic.otf' 'fonts/desktop_otf/Spectral-Medium.otf' 'fonts/desktop_otf/Spectral-MediumItalic.otf' 'fonts/desktop_otf/Spectral-Regular.otf' 'fonts/desktop_otf/Spectral-SemiBold.otf' 'fonts/desktop_otf/Spectral-SemiBoldItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the production-type-spectral-fonts appstream file"
cat > "org.altlinux.production-type-spectral-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.production-type-spectral-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Production Type Spectral</name>
  <summary><![CDATA[Spectral, an efficient and versatile serif font family]]></summary>
  <description>
    <p><![CDATA[Spectral is a versatile serif font family available in seven weights of roman]]></p><p><![CDATA[and italic, with small caps. Spectral offers an efficient, beautiful design]]></p><p><![CDATA[that’s intended primarily for text-rich, screen-first environments and]]></p><p><![CDATA[long-form reading.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing production-type-spectral-fonts
echo "" > "production-type-spectral-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/production-type-spectral/
echo "%%dir %_fontsdir/otf/production-type-spectral" >> "production-type-spectral-fonts.list"
install -m 0644 -vp "fonts/desktop_otf/Spectral-Bold.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-Bold.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-BoldItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-BoldItalic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-ExtraBold.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-ExtraBold.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-ExtraBoldItalic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-ExtraLight.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-ExtraLight.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-ExtraLightItalic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/spectral-italic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/spectral-italic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-Light.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-Light.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-LightItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-LightItalic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-Medium.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-Medium.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-MediumItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-MediumItalic.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-Regular.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-Regular.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-SemiBold.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-SemiBold.otf")\" >> 'production-type-spectral-fonts.list'
install -m 0644 -vp "fonts/desktop_otf/Spectral-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/production-type-spectral/
echo \"%_fontsdir/otf/production-type-spectral//$(basename "fonts/desktop_otf/Spectral-SemiBoldItalic.otf")\" >> 'production-type-spectral-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/desktop_otf/Spectral-Bold.otf' 'fonts/desktop_otf/Spectral-BoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraBold.otf' 'fonts/desktop_otf/Spectral-ExtraBoldItalic.otf' 'fonts/desktop_otf/Spectral-ExtraLight.otf' 'fonts/desktop_otf/Spectral-ExtraLightItalic.otf' 'fonts/desktop_otf/spectral-italic.otf' 'fonts/desktop_otf/Spectral-Light.otf' 'fonts/desktop_otf/Spectral-LightItalic.otf' 'fonts/desktop_otf/Spectral-Medium.otf' 'fonts/desktop_otf/Spectral-MediumItalic.otf' 'fonts/desktop_otf/Spectral-Regular.otf' 'fonts/desktop_otf/Spectral-SemiBold.otf' 'fonts/desktop_otf/Spectral-SemiBoldItalic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "production-type-spectral-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "production-type-spectral-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.production-type-spectral-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "production-type-spectral-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'contributors.txt' 'ofl.txt' 'README.md' 'trademarks.md'; do
  echo %%doc "'${fontdoc}'" >> "production-type-spectral-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'production-type-spectral-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'production-type-spectral-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-production-type-spectral -f production-type-spectral-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.003-alt1_6
- new version

