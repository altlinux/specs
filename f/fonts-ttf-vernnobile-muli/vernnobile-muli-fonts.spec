Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname vernnobile-muli-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname vernnobile-muli-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/MuliFont
%global commit      580b05e1f2ad319cd98a8de03fd2da7b36677954
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/googlefonts/MuliFont
%global forgesource https://github.com/googlefonts/MuliFont/archive/580b05e1f2ad319cd98a8de03fd2da7b36677954/MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954.tar.gz
%global archivename MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954
%global archiveext tar.gz
%global archiveurl https://github.com/googlefonts/MuliFont/archive/580b05e1f2ad319cd98a8de03fd2da7b36677954/MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954.tar.gz
%global topdir MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954
%global extractdir MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954
%global repo MuliFont
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 580b05e1f2ad319cd98a8de03fd2da7b36677954
#global shortcommit %nil
#global branch %nil
%global version 2.001
#global date %nil
%global distprefix .git580b05e
# FedoraForgeMeta2ALT: end generated meta

Version: 2.001
Release: alt1_6
URL:     %{forgeurl}

%global foundry           vernnobile
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Muli
%global fontsummary       Muli, a minimalist sans serif font family
%global fonts             fonts/*ttf
%global fontdescription   \
Muli is a minimalist sans serif font family, designed for both display and text\
typography.

Source0:  %{forgesource}
Source10: 60-vernnobile-muli-fonts.xml

Name:           fonts-ttf-vernnobile-muli
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
%setup -q -n MuliFont-580b05e1f2ad319cd98a8de03fd2da7b36677954

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/Muli-Black.ttf' 'fonts/Muli-BlackItalic.ttf' 'fonts/Muli-Bold.ttf' 'fonts/Muli-BoldItalic.ttf' 'fonts/Muli-ExtraBold.ttf' 'fonts/Muli-ExtraBoldItalic.ttf' 'fonts/Muli-ExtraLight.ttf' 'fonts/Muli-ExtraLightItalic.ttf' 'fonts/Muli-Italic.ttf' 'fonts/Muli-Light.ttf' 'fonts/Muli-LightItalic.ttf' 'fonts/Muli-Regular.ttf' 'fonts/Muli-SemiBold.ttf' 'fonts/Muli-SemiBoldItalic.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/Muli-Black.ttf' 'fonts/Muli-BlackItalic.ttf' 'fonts/Muli-Bold.ttf' 'fonts/Muli-BoldItalic.ttf' 'fonts/Muli-ExtraBold.ttf' 'fonts/Muli-ExtraBoldItalic.ttf' 'fonts/Muli-ExtraLight.ttf' 'fonts/Muli-ExtraLightItalic.ttf' 'fonts/Muli-Italic.ttf' 'fonts/Muli-Light.ttf' 'fonts/Muli-LightItalic.ttf' 'fonts/Muli-Regular.ttf' 'fonts/Muli-SemiBold.ttf' 'fonts/Muli-SemiBoldItalic.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the vernnobile-muli-fonts appstream file"
cat > "org.altlinux.vernnobile-muli-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.vernnobile-muli-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>vernnobile Muli</name>
  <summary><![CDATA[Muli, a minimalist sans serif font family]]></summary>
  <description>
    <p><![CDATA[Muli is a minimalist sans serif font family, designed for both display and text]]></p><p><![CDATA[typography.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing vernnobile-muli-fonts
echo "" > "vernnobile-muli-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/vernnobile-muli/
echo "%%dir %_fontsdir/ttf/vernnobile-muli" >> "vernnobile-muli-fonts.list"
install -m 0644 -vp "fonts/Muli-Black.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-Black.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-BlackItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-BlackItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-Bold.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-Bold.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-BoldItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-BoldItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-ExtraBold.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-ExtraBold.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-ExtraBoldItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-ExtraBoldItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-ExtraLight.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-ExtraLight.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-ExtraLightItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-ExtraLightItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-Italic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-Italic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-Light.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-Light.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-LightItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-LightItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-Regular.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-Regular.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-SemiBold.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-SemiBold.ttf")\" >> 'vernnobile-muli-fonts.list'
install -m 0644 -vp "fonts/Muli-SemiBoldItalic.ttf" %buildroot%_fontsdir/ttf/vernnobile-muli/
echo \"%_fontsdir/ttf/vernnobile-muli//$(basename "fonts/Muli-SemiBoldItalic.ttf")\" >> 'vernnobile-muli-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/Muli-Black.ttf' 'fonts/Muli-BlackItalic.ttf' 'fonts/Muli-Bold.ttf' 'fonts/Muli-BoldItalic.ttf' 'fonts/Muli-ExtraBold.ttf' 'fonts/Muli-ExtraBoldItalic.ttf' 'fonts/Muli-ExtraLight.ttf' 'fonts/Muli-ExtraLightItalic.ttf' 'fonts/Muli-Italic.ttf' 'fonts/Muli-Light.ttf' 'fonts/Muli-LightItalic.ttf' 'fonts/Muli-Regular.ttf' 'fonts/Muli-SemiBold.ttf' 'fonts/Muli-SemiBoldItalic.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "vernnobile-muli-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "vernnobile-muli-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.vernnobile-muli-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "vernnobile-muli-fonts.list"
done

for fontdoc in 'AUTHOR.txt' 'CONTRIBUTORS.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "vernnobile-muli-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "vernnobile-muli-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'vernnobile-muli-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'vernnobile-muli-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-vernnobile-muli -f vernnobile-muli-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 2.001-alt1_6
- new version

