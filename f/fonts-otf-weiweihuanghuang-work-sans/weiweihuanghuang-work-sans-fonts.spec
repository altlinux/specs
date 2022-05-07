Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname weiweihuanghuang-work-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname weiweihuanghuang-work-sans-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/weiweihuanghuang/Work-Sans
%global commit      dcd044c29b6f92f101a94777f744fa0f051da14b
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/weiweihuanghuang/Work-Sans
%global forgesource https://github.com/weiweihuanghuang/Work-Sans/archive/dcd044c29b6f92f101a94777f744fa0f051da14b/Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b.tar.gz
%global archivename Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b
%global archiveext tar.gz
%global archiveurl https://github.com/weiweihuanghuang/Work-Sans/archive/dcd044c29b6f92f101a94777f744fa0f051da14b/Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b.tar.gz
%global topdir Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b
%global extractdir Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b
%global repo Work-Sans
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit dcd044c29b6f92f101a94777f744fa0f051da14b
#global shortcommit %nil
#global branch %nil
%global version 2.07
#global date %nil
%global distprefix .gitdcd044c
# FedoraForgeMeta2ALT: end generated meta

Version: 2.07
Release: alt1_15
URL:     %{forgeurl}

%global foundry           weiweihuanghuang
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Work Sans
%global fontsummary       Work Sans, a font family in the early grotesque style
%global fonts             fonts/variable/*ttf fonts/static/OTF/*otf
%global fontdescription   \
Work Sans is a font family based loosely on early Grotesques a.. i.e. Stephenson\
Blake, Miller & Richard and Bauersche GieA.erei. The core of the fonts are\
optimized for on-screen medium-sized text usage,  but can still be used in\
print. The fonts at the extreme weights are designed more for display use.\
Overall, features are simplified and optimized for screen resolutions a.. for\
example, diacritic marks are larger than how they would be in print.

Source0:  %{forgesource}
Source10: 58-weiweihuanghuang-work-sans-fonts.xml

Name:           fonts-otf-weiweihuanghuang-work-sans
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%package doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n Work-Sans-dcd044c29b6f92f101a94777f744fa0f051da14b
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/variable/WorkSans-Italic-VF.ttf' 'fonts/variable/WorkSans-Roman-VF.ttf' 'fonts/static/OTF/WorkSans-Black.otf' 'fonts/static/OTF/WorkSans-BlackItalic.otf' 'fonts/static/OTF/WorkSans-Bold.otf' 'fonts/static/OTF/WorkSans-BoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraBold.otf' 'fonts/static/OTF/WorkSans-ExtraBoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraLight.otf' 'fonts/static/OTF/WorkSans-ExtraLightItalic.otf' 'fonts/static/OTF/WorkSans-Italic.otf' 'fonts/static/OTF/WorkSans-Light.otf' 'fonts/static/OTF/WorkSans-LightItalic.otf' 'fonts/static/OTF/WorkSans-Medium.otf' 'fonts/static/OTF/WorkSans-MediumItalic.otf' 'fonts/static/OTF/WorkSans-Regular.otf' 'fonts/static/OTF/WorkSans-SemiBold.otf' 'fonts/static/OTF/WorkSans-SemiBoldItalic.otf' 'fonts/static/OTF/WorkSans-Thin.otf' 'fonts/static/OTF/WorkSans-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/variable/WorkSans-Italic-VF.ttf' 'fonts/variable/WorkSans-Roman-VF.ttf' 'fonts/static/OTF/WorkSans-Black.otf' 'fonts/static/OTF/WorkSans-BlackItalic.otf' 'fonts/static/OTF/WorkSans-Bold.otf' 'fonts/static/OTF/WorkSans-BoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraBold.otf' 'fonts/static/OTF/WorkSans-ExtraBoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraLight.otf' 'fonts/static/OTF/WorkSans-ExtraLightItalic.otf' 'fonts/static/OTF/WorkSans-Italic.otf' 'fonts/static/OTF/WorkSans-Light.otf' 'fonts/static/OTF/WorkSans-LightItalic.otf' 'fonts/static/OTF/WorkSans-Medium.otf' 'fonts/static/OTF/WorkSans-MediumItalic.otf' 'fonts/static/OTF/WorkSans-Regular.otf' 'fonts/static/OTF/WorkSans-SemiBold.otf' 'fonts/static/OTF/WorkSans-SemiBoldItalic.otf' 'fonts/static/OTF/WorkSans-Thin.otf' 'fonts/static/OTF/WorkSans-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the weiweihuanghuang-work-sans-fonts appstream file"
cat > "org.altlinux.weiweihuanghuang-work-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.weiweihuanghuang-work-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>weiweihuanghuang Work Sans</name>
  <summary><![CDATA[Work Sans, a font family in the early grotesque style]]></summary>
  <description>
    <p><![CDATA[Work Sans is a font family based loosely on early Grotesques — i.e. Stephenson]]></p><p><![CDATA[Blake, Miller & Richard and Bauersche Gießerei. The core of the fonts are]]></p><p><![CDATA[optimized for on-screen medium-sized text usage,  but can still be used in]]></p><p><![CDATA[print. The fonts at the extreme weights are designed more for display use.]]></p><p><![CDATA[Overall, features are simplified and optimized for screen resolutions – for]]></p><p><![CDATA[example, diacritic marks are larger than how they would be in print.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing weiweihuanghuang-work-sans-fonts
echo "" > "weiweihuanghuang-work-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/weiweihuanghuang-work-sans/
echo "%%dir %_fontsdir/ttf/weiweihuanghuang-work-sans" >> "weiweihuanghuang-work-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo "%%dir %_fontsdir/otf/weiweihuanghuang-work-sans" >> "weiweihuanghuang-work-sans-fonts.list"
install -m 0644 -vp "fonts/variable/WorkSans-Italic-VF.ttf" %buildroot%_fontsdir/ttf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/ttf/weiweihuanghuang-work-sans/WorkSans-Italic-VF.ttf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/variable/WorkSans-Roman-VF.ttf" %buildroot%_fontsdir/ttf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/ttf/weiweihuanghuang-work-sans/WorkSans-Roman-VF.ttf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Black.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Black.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-BlackItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-BlackItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Bold.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Bold.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-BoldItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-BoldItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-ExtraBold.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-ExtraBold.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-ExtraBoldItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-ExtraLight.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-ExtraLight.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-ExtraLightItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Italic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Italic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Light.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Light.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-LightItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-LightItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Medium.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Medium.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-MediumItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-MediumItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Regular.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Regular.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-SemiBold.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-SemiBold.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-SemiBoldItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-Thin.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-Thin.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
install -m 0644 -vp "fonts/static/OTF/WorkSans-ThinItalic.otf" %buildroot%_fontsdir/otf/weiweihuanghuang-work-sans/
echo \"%_fontsdir/otf/weiweihuanghuang-work-sans/WorkSans-ThinItalic.otf\" >> 'weiweihuanghuang-work-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/variable/WorkSans-Italic-VF.ttf' 'fonts/variable/WorkSans-Roman-VF.ttf' 'fonts/static/OTF/WorkSans-Black.otf' 'fonts/static/OTF/WorkSans-BlackItalic.otf' 'fonts/static/OTF/WorkSans-Bold.otf' 'fonts/static/OTF/WorkSans-BoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraBold.otf' 'fonts/static/OTF/WorkSans-ExtraBoldItalic.otf' 'fonts/static/OTF/WorkSans-ExtraLight.otf' 'fonts/static/OTF/WorkSans-ExtraLightItalic.otf' 'fonts/static/OTF/WorkSans-Italic.otf' 'fonts/static/OTF/WorkSans-Light.otf' 'fonts/static/OTF/WorkSans-LightItalic.otf' 'fonts/static/OTF/WorkSans-Medium.otf' 'fonts/static/OTF/WorkSans-MediumItalic.otf' 'fonts/static/OTF/WorkSans-Regular.otf' 'fonts/static/OTF/WorkSans-SemiBold.otf' 'fonts/static/OTF/WorkSans-SemiBoldItalic.otf' 'fonts/static/OTF/WorkSans-Thin.otf' 'fonts/static/OTF/WorkSans-ThinItalic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "weiweihuanghuang-work-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "weiweihuanghuang-work-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.weiweihuanghuang-work-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "weiweihuanghuang-work-sans-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'BUILD.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "weiweihuanghuang-work-sans-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "weiweihuanghuang-work-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'weiweihuanghuang-work-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'weiweihuanghuang-work-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-weiweihuanghuang-work-sans -f weiweihuanghuang-work-sans-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.07-alt1_15
- update to new release by fcimport

* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.07-alt1_9
- new version

