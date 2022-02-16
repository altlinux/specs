Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname vernnobile-oswald-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname vernnobile-oswald-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/OswaldFont
%global commit      5a5fff234687674f8531a8537455e626b08b3321
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/googlefonts/OswaldFont
%global forgesource https://github.com/googlefonts/OswaldFont/archive/5a5fff234687674f8531a8537455e626b08b3321/OswaldFont-5a5fff234687674f8531a8537455e626b08b3321.tar.gz
%global archivename OswaldFont-5a5fff234687674f8531a8537455e626b08b3321
%global archiveext tar.gz
%global archiveurl https://github.com/googlefonts/OswaldFont/archive/5a5fff234687674f8531a8537455e626b08b3321/OswaldFont-5a5fff234687674f8531a8537455e626b08b3321.tar.gz
%global topdir OswaldFont-5a5fff234687674f8531a8537455e626b08b3321
%global extractdir OswaldFont-5a5fff234687674f8531a8537455e626b08b3321
%global repo OswaldFont
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 5a5fff234687674f8531a8537455e626b08b3321
#global shortcommit %nil
#global branch %nil
%global version 4.101
#global date %nil
%global distprefix .git5a5fff2
# FedoraForgeMeta2ALT: end generated meta

Version: 4.101
Release: alt1_8
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Oswald
%global fontsummary       Oswald, a reworked Gothic style font family
%global fonts             fonts/otf/*otf
%global fontdescription   \
Oswald is a reworking of the classic Gothic typeface style historically\
represented by designs such as a.'Alternate Gothica.'. The characters of Oswald\
have been re-drawn and reformed to better fit the pixel grid of standard\
digital screens. Oswald is designed to be used freely across the internet by\
web browsers on desktop computers, laptops and mobile devices.

Source0:  %{forgesource}
Source10: 60-vernnobile-oswald-fonts.xml

Name:           fonts-otf-vernnobile-oswald
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
%setup -q -n OswaldFont-5a5fff234687674f8531a8537455e626b08b3321
%linuxtext %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/Oswald-Bold.otf' 'fonts/otf/Oswald-ExtraLight.otf' 'fonts/otf/Oswald-Light.otf' 'fonts/otf/Oswald-Medium.otf' 'fonts/otf/Oswald-Regular.otf' 'fonts/otf/Oswald-SemiBold.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Oswald-Bold.otf' 'fonts/otf/Oswald-ExtraLight.otf' 'fonts/otf/Oswald-Light.otf' 'fonts/otf/Oswald-Medium.otf' 'fonts/otf/Oswald-Regular.otf' 'fonts/otf/Oswald-SemiBold.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the vernnobile-oswald-fonts appstream file"
cat > "org.altlinux.vernnobile-oswald-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.vernnobile-oswald-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>vernnobile Oswald</name>
  <summary><![CDATA[Oswald, a reworked Gothic style font family]]></summary>
  <description>
    <p><![CDATA[Oswald is a reworking of the classic Gothic typeface style historically]]></p><p><![CDATA[represented by designs such as “Alternate Gothic”. The characters of Oswald]]></p><p><![CDATA[have been re-drawn and reformed to better fit the pixel grid of standard]]></p><p><![CDATA[digital screens. Oswald is designed to be used freely across the internet by]]></p><p><![CDATA[web browsers on desktop computers, laptops and mobile devices.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing vernnobile-oswald-fonts
echo "" > "vernnobile-oswald-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/vernnobile-oswald/
echo "%%dir %_fontsdir/otf/vernnobile-oswald" >> "vernnobile-oswald-fonts.list"
install -m 0644 -vp "fonts/otf/Oswald-Bold.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-Bold.otf")\" >> 'vernnobile-oswald-fonts.list'
install -m 0644 -vp "fonts/otf/Oswald-ExtraLight.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-ExtraLight.otf")\" >> 'vernnobile-oswald-fonts.list'
install -m 0644 -vp "fonts/otf/Oswald-Light.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-Light.otf")\" >> 'vernnobile-oswald-fonts.list'
install -m 0644 -vp "fonts/otf/Oswald-Medium.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-Medium.otf")\" >> 'vernnobile-oswald-fonts.list'
install -m 0644 -vp "fonts/otf/Oswald-Regular.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-Regular.otf")\" >> 'vernnobile-oswald-fonts.list'
install -m 0644 -vp "fonts/otf/Oswald-SemiBold.otf" %buildroot%_fontsdir/otf/vernnobile-oswald/
echo \"%_fontsdir/otf/vernnobile-oswald//$(basename "fonts/otf/Oswald-SemiBold.otf")\" >> 'vernnobile-oswald-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/Oswald-Bold.otf' 'fonts/otf/Oswald-ExtraLight.otf' 'fonts/otf/Oswald-Light.otf' 'fonts/otf/Oswald-Medium.otf' 'fonts/otf/Oswald-Regular.otf' 'fonts/otf/Oswald-SemiBold.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "vernnobile-oswald-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "vernnobile-oswald-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.vernnobile-oswald-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "vernnobile-oswald-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'FONTLOG.txt' 'DESCRIPTION.en_us.html' 'DESCRIPTION.en_us_for_Heavy.html' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "vernnobile-oswald-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "vernnobile-oswald-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'vernnobile-oswald-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'vernnobile-oswald-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-vernnobile-oswald -f vernnobile-oswald-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 4.101-alt1_8
- new version

