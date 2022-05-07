Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname vernnobile-nunito-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname vernnobile-nunito-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/nunito
%global commit      6d8a4e1c00df8b361e59656eee7c2b458d663191
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/googlefonts/nunito
%global forgesource https://github.com/googlefonts/nunito/archive/6d8a4e1c00df8b361e59656eee7c2b458d663191/nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191.tar.gz
%global archivename nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191
%global archiveext tar.gz
%global archiveurl https://github.com/googlefonts/nunito/archive/6d8a4e1c00df8b361e59656eee7c2b458d663191/nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191.tar.gz
%global topdir nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191
%global extractdir nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191
%global repo nunito
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 6d8a4e1c00df8b361e59656eee7c2b458d663191
#global shortcommit %nil
#global branch %nil
%global version 3.504
#global date %nil
%global distprefix .git6d8a4e1
# FedoraForgeMeta2ALT: end generated meta

Version: 3.504
Release: alt1_12
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Nunito
%global fontsummary       Nunito, a sans serif font family with rounded terminals
%global fonts             fonts/TTF-unhinted/*otf
%global fontdescription   \
Nunito is a well balanced sans serif with rounded terminals. Nunito has been\
designed mainly to be used as a display font but is usable as a text font too.\
Nunito has been designed to be used freely across the internet by web browsers\
on desktop computers, laptops and mobile devices.

Source0:  %{forgesource}
Source10: 58-vernnobile-nunito-fonts.xml

Name:           fonts-otf-vernnobile-nunito
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
%setup -q -n nunito-6d8a4e1c00df8b361e59656eee7c2b458d663191

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/TTF-unhinted/Nunito-Black.otf' 'fonts/TTF-unhinted/Nunito-BlackItalic.otf' 'fonts/TTF-unhinted/Nunito-Bold.otf' 'fonts/TTF-unhinted/Nunito-BoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraBold.otf' 'fonts/TTF-unhinted/Nunito-ExtraBoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraLight.otf' 'fonts/TTF-unhinted/Nunito-ExtraLightItalic.otf' 'fonts/TTF-unhinted/Nunito-Italic.otf' 'fonts/TTF-unhinted/Nunito-Light.otf' 'fonts/TTF-unhinted/Nunito-LightItalic.otf' 'fonts/TTF-unhinted/Nunito-Regular.otf' 'fonts/TTF-unhinted/Nunito-SemiBold.otf' 'fonts/TTF-unhinted/Nunito-SemiBoldItalic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Italic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/TTF-unhinted/Nunito-Black.otf' 'fonts/TTF-unhinted/Nunito-BlackItalic.otf' 'fonts/TTF-unhinted/Nunito-Bold.otf' 'fonts/TTF-unhinted/Nunito-BoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraBold.otf' 'fonts/TTF-unhinted/Nunito-ExtraBoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraLight.otf' 'fonts/TTF-unhinted/Nunito-ExtraLightItalic.otf' 'fonts/TTF-unhinted/Nunito-Italic.otf' 'fonts/TTF-unhinted/Nunito-Light.otf' 'fonts/TTF-unhinted/Nunito-LightItalic.otf' 'fonts/TTF-unhinted/Nunito-Regular.otf' 'fonts/TTF-unhinted/Nunito-SemiBold.otf' 'fonts/TTF-unhinted/Nunito-SemiBoldItalic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Italic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the vernnobile-nunito-fonts appstream file"
cat > "org.altlinux.vernnobile-nunito-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.vernnobile-nunito-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>vernnobile Nunito</name>
  <summary><![CDATA[Nunito, a sans serif font family with rounded terminals]]></summary>
  <description>
    <p><![CDATA[Nunito is a well balanced sans serif with rounded terminals. Nunito has been]]></p><p><![CDATA[designed mainly to be used as a display font but is usable as a text font too.]]></p><p><![CDATA[Nunito has been designed to be used freely across the internet by web browsers]]></p><p><![CDATA[on desktop computers, laptops and mobile devices.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing vernnobile-nunito-fonts
echo "" > "vernnobile-nunito-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/vernnobile-nunito/
echo "%%dir %_fontsdir/otf/vernnobile-nunito" >> "vernnobile-nunito-fonts.list"
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-Black.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-Black.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-BlackItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-BlackItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-Bold.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-Bold.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-BoldItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-BoldItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-ExtraBold.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-ExtraBold.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-ExtraBoldItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-ExtraLight.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-ExtraLight.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-ExtraLightItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-Italic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-Italic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-Light.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-Light.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-LightItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-LightItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-Regular.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-Regular.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-SemiBold.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-SemiBold.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/Nunito-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/Nunito-SemiBoldItalic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/NunitoHeavy-Italic.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/NunitoHeavy-Italic.otf\" >> 'vernnobile-nunito-fonts.list'
install -m 0644 -vp "fonts/TTF-unhinted/NunitoHeavy-Regular.otf" %buildroot%_fontsdir/otf/vernnobile-nunito/
echo \"%_fontsdir/otf/vernnobile-nunito/NunitoHeavy-Regular.otf\" >> 'vernnobile-nunito-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/TTF-unhinted/Nunito-Black.otf' 'fonts/TTF-unhinted/Nunito-BlackItalic.otf' 'fonts/TTF-unhinted/Nunito-Bold.otf' 'fonts/TTF-unhinted/Nunito-BoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraBold.otf' 'fonts/TTF-unhinted/Nunito-ExtraBoldItalic.otf' 'fonts/TTF-unhinted/Nunito-ExtraLight.otf' 'fonts/TTF-unhinted/Nunito-ExtraLightItalic.otf' 'fonts/TTF-unhinted/Nunito-Italic.otf' 'fonts/TTF-unhinted/Nunito-Light.otf' 'fonts/TTF-unhinted/Nunito-LightItalic.otf' 'fonts/TTF-unhinted/Nunito-Regular.otf' 'fonts/TTF-unhinted/Nunito-SemiBold.otf' 'fonts/TTF-unhinted/Nunito-SemiBoldItalic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Italic.otf' 'fonts/TTF-unhinted/NunitoHeavy-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "vernnobile-nunito-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "vernnobile-nunito-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.vernnobile-nunito-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "vernnobile-nunito-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'DESCRIPTION.en_us.html' 'BUILD.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "vernnobile-nunito-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "vernnobile-nunito-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'vernnobile-nunito-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'vernnobile-nunito-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-vernnobile-nunito -f vernnobile-nunito-fonts.list

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 3.504-alt1_12
- update to new release by fcimport

* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 3.504-alt1_6
- new version

