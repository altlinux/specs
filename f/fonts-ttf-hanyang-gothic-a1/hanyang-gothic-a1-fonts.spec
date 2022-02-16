Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname hanyang-gothic-a1-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname hanyang-gothic-a1-fonts
%global git_date   20180313
%global git_commit 16680f8688ffcd467d2eb2146a9ce0343404581d
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:8}")

Version: 163840
Release: alt1_6.%{git_date}git%{git_commit_short}

URL: https://www.hanyang.co.kr/hygothic/

%global foundry  HanYang
%global fontlicense  OFL
%global fontlicenses  OFL.txt

%global fontfamily  Gothic A1
%global fontsummary  HanYang Gothic A1, an elegant Korean and Latin font

%global fontdescription  HanYang I&C Co's Gothic A1 is an elegant font for Korean and Latin text,\
available in 9 weights.

%global fonts  *.ttf


# Archive created by running the gothicA1-fetch.sh script (see Source99)
%global archivename HanYang-GothicA1-%{git_commit}
Source0: %{archivename}.zip

Source10: 60-hanyang-gothic-a1-fonts.xml

# A script to fetch the font files from Google Fonts repo on GitHub
Source99: gothicA1-fetch.sh


Name:           fonts-ttf-hanyang-gothic-a1
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}


%prep
%global fontconfs  %{SOURCE10}
%setup -q -n %{archivename}


%build
# fontbuild 
fontnames=$(
  for font in 'GothicA1-Black.ttf' 'GothicA1-Bold.ttf' 'GothicA1-ExtraBold.ttf' 'GothicA1-ExtraLight.ttf' 'GothicA1-Light.ttf' 'GothicA1-Medium.ttf' 'GothicA1-Regular.ttf' 'GothicA1-SemiBold.ttf' 'GothicA1-Thin.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GothicA1-Black.ttf' 'GothicA1-Bold.ttf' 'GothicA1-ExtraBold.ttf' 'GothicA1-ExtraLight.ttf' 'GothicA1-Light.ttf' 'GothicA1-Medium.ttf' 'GothicA1-Regular.ttf' 'GothicA1-SemiBold.ttf' 'GothicA1-Thin.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the hanyang-gothic-a1-fonts appstream file"
cat > "org.altlinux.hanyang-gothic-a1-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.hanyang-gothic-a1-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>HanYang Gothic A1</name>
  <summary><![CDATA[HanYang Gothic A1, an elegant Korean and Latin font]]></summary>
  <description>
    <p><![CDATA[HanYang I&C Co's Gothic A1 is an elegant font for Korean and Latin text,available in 9 weights.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.hanyang.co.kr/hygothic/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM


%install
echo Installing hanyang-gothic-a1-fonts
echo "" > "hanyang-gothic-a1-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo "%%dir %_fontsdir/ttf/hanyang-gothic-a1" >> "hanyang-gothic-a1-fonts.list"
install -m 0644 -vp "GothicA1-Black.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Black.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-Bold.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Bold.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-ExtraBold.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-ExtraBold.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-ExtraLight.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-ExtraLight.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-Light.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Light.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-Medium.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Medium.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-Regular.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Regular.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-SemiBold.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-SemiBold.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
install -m 0644 -vp "GothicA1-Thin.ttf" %buildroot%_fontsdir/ttf/hanyang-gothic-a1/
echo \"%_fontsdir/ttf/hanyang-gothic-a1//$(basename "GothicA1-Thin.ttf")\" >> 'hanyang-gothic-a1-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "hanyang-gothic-a1-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "hanyang-gothic-a1-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.hanyang-gothic-a1-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "hanyang-gothic-a1-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "hanyang-gothic-a1-fonts.list"
done


%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'hanyang-gothic-a1-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'hanyang-gothic-a1-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'


%files -n fonts-ttf-hanyang-gothic-a1 -f hanyang-gothic-a1-fonts.list


%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 163840-alt1_6.20180313git16680f86
- new version

