Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ndiscover-exo-2-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ndiscover-exo-2-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/NDISCOVER/Exo-2.0
%global commit      55728cfe5c9f0c121428467019f880fb6709f8d8
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/NDISCOVER/Exo-2.0
%global forgesource https://github.com/NDISCOVER/Exo-2.0/archive/55728cfe5c9f0c121428467019f880fb6709f8d8/Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8.tar.gz
%global archivename Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8
%global archiveext tar.gz
%global archiveurl https://github.com/NDISCOVER/Exo-2.0/archive/55728cfe5c9f0c121428467019f880fb6709f8d8/Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8.tar.gz
%global topdir Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8
%global extractdir Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8
%global repo Exo-2.0
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 55728cfe5c9f0c121428467019f880fb6709f8d8
#global shortcommit %nil
#global branch %nil
%global version 1.100
#global date %nil
%global distprefix .git55728cf
# FedoraForgeMeta2ALT: end generated meta

Version: 1.100
Release: alt1_3
URL:     %{forgeurl}

%global foundry           NDISCOVER
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Exo 2
%global fontsummary       Exo 2, a contemporary geometric sans serif font family
%global fonts             fonts/otf/*otf fonts/vf/*ttf
%global fontdescription   \
Exo 2 is a complete redrawing of Exo, a contemporary geometric sans serif\
font family that tries to convey a technological/futuristic feeling while keeping\
an elegant design. Exo is a very versatile font, so it has 9 weights (the\
maximum on the web) and each with a true italic version. Exo 2 has a more\
organic look that will perform much better at small text sizes and in long\
texts.

Source0:  %{forgesource}
Source10: 60-ndiscover-exo-2-fonts.xml

Name:           fonts-otf-ndiscover-exo-2
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
%setup -q -n Exo-2.0-55728cfe5c9f0c121428467019f880fb6709f8d8

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/Exo2-Black.otf' 'fonts/otf/Exo2-Bold.otf' 'fonts/otf/Exo2-ExtraBold.otf' 'fonts/otf/Exo2-ExtraLight.otf' 'fonts/otf/Exo2-Light.otf' 'fonts/otf/Exo2-Medium.otf' 'fonts/otf/Exo2-Regular.otf' 'fonts/otf/Exo2-SemiBold.otf' 'fonts/otf/Exo2-Thin.otf' 'fonts/vf/Exo2-Italic[wght].ttf' 'fonts/vf/Exo2[wght].ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Exo2-Black.otf' 'fonts/otf/Exo2-Bold.otf' 'fonts/otf/Exo2-ExtraBold.otf' 'fonts/otf/Exo2-ExtraLight.otf' 'fonts/otf/Exo2-Light.otf' 'fonts/otf/Exo2-Medium.otf' 'fonts/otf/Exo2-Regular.otf' 'fonts/otf/Exo2-SemiBold.otf' 'fonts/otf/Exo2-Thin.otf' 'fonts/vf/Exo2-Italic[wght].ttf' 'fonts/vf/Exo2[wght].ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ndiscover-exo-2-fonts appstream file"
cat > "org.altlinux.ndiscover-exo-2-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ndiscover-exo-2-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>NDISCOVER Exo 2</name>
  <summary><![CDATA[Exo 2, a contemporary geometric sans serif font family]]></summary>
  <description>
    <p><![CDATA[Exo 2 is a complete redrawing of Exo, a contemporary geometric sans serif]]></p><p><![CDATA[font family that tries to convey a technological/futuristic feeling while keeping]]></p><p><![CDATA[an elegant design. Exo is a very versatile font, so it has 9 weights (the]]></p><p><![CDATA[maximum on the web) and each with a true italic version. Exo 2 has a more]]></p><p><![CDATA[organic look that will perform much better at small text sizes and in long]]></p><p><![CDATA[texts.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ndiscover-exo-2-fonts
echo "" > "ndiscover-exo-2-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo "%%dir %_fontsdir/otf/ndiscover-exo-2" >> "ndiscover-exo-2-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/ndiscover-exo-2/
echo "%%dir %_fontsdir/ttf/ndiscover-exo-2" >> "ndiscover-exo-2-fonts.list"
install -m 0644 -vp "fonts/otf/Exo2-Black.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Black.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-Bold.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Bold.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-ExtraBold.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-ExtraBold.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-ExtraLight.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-ExtraLight.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-Light.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Light.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-Medium.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Medium.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-Regular.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Regular.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-SemiBold.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-SemiBold.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 -vp "fonts/otf/Exo2-Thin.otf" %buildroot%_fontsdir/otf/ndiscover-exo-2/
echo \"%_fontsdir/otf/ndiscover-exo-2//$(basename "fonts/otf/Exo2-Thin.otf")\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 "fonts/vf/Exo2-Italic[wght].ttf" %buildroot%_fontsdir/ttf/ndiscover-exo-2/Exo2-Italic_wght.ttf
echo \"%_fontsdir/ttf/ndiscover-exo-2/Exo2-Italic_wght.ttf\" >> 'ndiscover-exo-2-fonts.list'
install -m 0644 "fonts/vf/Exo2[wght].ttf" %buildroot%_fontsdir/ttf/ndiscover-exo-2/Exo2_wght.ttf
echo \"%_fontsdir/ttf/ndiscover-exo-2/Exo2_wght.ttf\" >> 'ndiscover-exo-2-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/Exo2-Black.otf' 'fonts/otf/Exo2-Bold.otf' 'fonts/otf/Exo2-ExtraBold.otf' 'fonts/otf/Exo2-ExtraLight.otf' 'fonts/otf/Exo2-Light.otf' 'fonts/otf/Exo2-Medium.otf' 'fonts/otf/Exo2-Regular.otf' 'fonts/otf/Exo2-SemiBold.otf' 'fonts/otf/Exo2-Thin.otf' 'fonts/vf/Exo2-Italic[wght].ttf' 'fonts/vf/Exo2[wght].ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ndiscover-exo-2-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ndiscover-exo-2-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ndiscover-exo-2-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ndiscover-exo-2-fonts.list"
done

for fontdoc in 'requirements.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "ndiscover-exo-2-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "ndiscover-exo-2-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ndiscover-exo-2-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ndiscover-exo-2-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ndiscover-exo-2 -f ndiscover-exo-2-fonts.list

%changelog
* Tue Feb 22 2022 Igor Vlasenko <viy@altlinux.org> 1.100-alt1_3
- new version

