Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname google-rubik-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname google-rubik-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/rubik
%global commit      2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/googlefonts/rubik
%global forgesource https://github.com/googlefonts/rubik/archive/2e360a2044e6d1d4e3a6ddd992144a9a0b5446af/rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af.tar.gz
%global archivename rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
%global archiveext tar.gz
%global archiveurl https://github.com/googlefonts/rubik/archive/2e360a2044e6d1d4e3a6ddd992144a9a0b5446af/rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af.tar.gz
%global topdir rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
%global extractdir rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
%global repo rubik
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
#global shortcommit %nil
#global branch %nil
%global version 2.100
#global date %nil
%global distprefix .git2e360a2
# FedoraForgeMeta2ALT: end generated meta

Version: 2.100
Release: alt1_6
URL:     %{forgeurl}

%global foundry           google
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Rubik
%global fontsummary       Rubik, a sans serif font family with slightly rounded corners
%global fonts             fonts/ttf/*ttf fonts/variable*fonts/*ttf
%global fontdescription   \
Rubik is a sans serif font family with slightly rounded corners designed by\
Philipp Hubert and Sebastian Fischer at Hubert & Fischer as part of the Chrome\
Cube Lab project.

Source0:  %{forgesource}
Source10: 58-google-rubik-fonts.xml

Name:           fonts-ttf-google-rubik
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
%setup -q -n rubik-2e360a2044e6d1d4e3a6ddd992144a9a0b5446af
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/ttf/Rubik-Black.ttf' 'fonts/ttf/Rubik-BlackItalic.ttf' 'fonts/ttf/Rubik-Bold.ttf' 'fonts/ttf/Rubik-BoldItalic.ttf' 'fonts/ttf/Rubik-Italic.ttf' 'fonts/ttf/Rubik-Light.ttf' 'fonts/ttf/Rubik-LightItalic.ttf' 'fonts/ttf/Rubik-Medium.ttf' 'fonts/ttf/Rubik-MediumItalic.ttf' 'fonts/ttf/Rubik-Regular.ttf' 'fonts/variable fonts/RubikGX.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/ttf/Rubik-Black.ttf' 'fonts/ttf/Rubik-BlackItalic.ttf' 'fonts/ttf/Rubik-Bold.ttf' 'fonts/ttf/Rubik-BoldItalic.ttf' 'fonts/ttf/Rubik-Italic.ttf' 'fonts/ttf/Rubik-Light.ttf' 'fonts/ttf/Rubik-LightItalic.ttf' 'fonts/ttf/Rubik-Medium.ttf' 'fonts/ttf/Rubik-MediumItalic.ttf' 'fonts/ttf/Rubik-Regular.ttf' 'fonts/variable fonts/RubikGX.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-rubik-fonts appstream file"
cat > "org.altlinux.google-rubik-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-rubik-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>google Rubik</name>
  <summary><![CDATA[Rubik, a sans serif font family with slightly rounded corners]]></summary>
  <description>
    <p><![CDATA[Rubik is a sans serif font family with slightly rounded corners designed by]]></p><p><![CDATA[Philipp Hubert and Sebastian Fischer at Hubert & Fischer as part of the Chrome]]></p><p><![CDATA[Cube Lab project.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing google-rubik-fonts
echo "" > "google-rubik-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-rubik/
echo "%%dir %_fontsdir/ttf/google-rubik" >> "google-rubik-fonts.list"
install -m 0644 -vp "fonts/ttf/Rubik-Black.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Black.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-BlackItalic.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-BlackItalic.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-Bold.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Bold.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-BoldItalic.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-BoldItalic.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-Italic.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Italic.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-Light.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Light.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-LightItalic.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-LightItalic.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-Medium.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Medium.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-MediumItalic.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-MediumItalic.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/ttf/Rubik-Regular.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/ttf/Rubik-Regular.ttf")\" >> 'google-rubik-fonts.list'
install -m 0644 -vp "fonts/variable fonts/RubikGX.ttf" %buildroot%_fontsdir/ttf/google-rubik/
echo \"%_fontsdir/ttf/google-rubik//$(basename "fonts/variable fonts/RubikGX.ttf")\" >> 'google-rubik-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/ttf/Rubik-Black.ttf' 'fonts/ttf/Rubik-BlackItalic.ttf' 'fonts/ttf/Rubik-Bold.ttf' 'fonts/ttf/Rubik-BoldItalic.ttf' 'fonts/ttf/Rubik-Italic.ttf' 'fonts/ttf/Rubik-Light.ttf' 'fonts/ttf/Rubik-LightItalic.ttf' 'fonts/ttf/Rubik-Medium.ttf' 'fonts/ttf/Rubik-MediumItalic.ttf' 'fonts/ttf/Rubik-Regular.ttf' 'fonts/variable fonts/RubikGX.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "google-rubik-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "google-rubik-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-rubik-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-rubik-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "google-rubik-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "google-rubik-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-rubik-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-rubik-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-google-rubik -f google-rubik-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 2.100-alt1_6
- new version

