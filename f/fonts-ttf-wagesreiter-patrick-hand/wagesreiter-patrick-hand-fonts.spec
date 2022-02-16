Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname wagesreiter-patrick-hand-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name wagesreiter-patrick-hand-fonts
%define fontpkgname wagesreiter-patrick-hand-fonts
# SPDX-License-Identifier: MIT
Version: 20200215
Release: alt1_5
URL:     https://fonts.google.com/specimen/Patrick+Hand

%global foundry           Wagesreiter
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.pb *.html

%global fontfamily        Patrick Hand
%global fontsummary       Patrick Hand, an handwriting font family
%global fonts             *ttf
%global fontdescription   \
Patrick Hand is a font family based on the designera.'s own handwriting. It is\
developed to bring an impressive and useful handwriting effect to your\
texts.\
\
It has all the basic Latin characters as well as most of the Latin extended\
ones. It also includes some fancy glyphs like heavy quotation marks and the\
floral heart! Ligatures, small caps and old style numbers are available as\
OpenType features.

Source0:  %{oldname}-%{version}.tar.xz
# Not available outside the huge Google fonts repository
Source1:  getfiles.sh
Source10: 60-wagesreiter-patrick-hand-fonts.xml

Name:           fonts-ttf-wagesreiter-patrick-hand
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
%setup -n %{oldname}-%{version} -q

%build
# fontbuild 
fontnames=$(
  for font in 'PatrickHand-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'PatrickHand-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the wagesreiter-patrick-hand-fonts appstream file"
cat > "org.altlinux.wagesreiter-patrick-hand-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.wagesreiter-patrick-hand-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Wagesreiter Patrick Hand</name>
  <summary><![CDATA[Patrick Hand, an handwriting font family]]></summary>
  <description>
    <p><![CDATA[Patrick Hand is a font family based on the designer’s own handwriting. It is]]></p><p><![CDATA[developed to bring an impressive and useful handwriting effect to your]]></p><p><![CDATA[texts.]]></p> It has all the basic Latin characters as well as most of the Latin extended ones. It also includes some fancy glyphs like heavy quotation marks and the floral heart! Ligatures, small caps and old style numbers are available as OpenType features.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://fonts.google.com/specimen/Patrick+Hand</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing wagesreiter-patrick-hand-fonts
echo "" > "wagesreiter-patrick-hand-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/wagesreiter-patrick-hand/
echo "%%dir %_fontsdir/ttf/wagesreiter-patrick-hand" >> "wagesreiter-patrick-hand-fonts.list"
install -m 0644 -vp "PatrickHand-Regular.ttf" %buildroot%_fontsdir/ttf/wagesreiter-patrick-hand/
echo \"%_fontsdir/ttf/wagesreiter-patrick-hand//$(basename "PatrickHand-Regular.ttf")\" >> 'wagesreiter-patrick-hand-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'PatrickHand-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "wagesreiter-patrick-hand-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "wagesreiter-patrick-hand-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.wagesreiter-patrick-hand-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "wagesreiter-patrick-hand-fonts.list"
done

for fontdoc in 'METADATA.pb' 'DESCRIPTION.en_us.html'; do
  echo %%doc "'${fontdoc}'" >> "wagesreiter-patrick-hand-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "wagesreiter-patrick-hand-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'wagesreiter-patrick-hand-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'wagesreiter-patrick-hand-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-wagesreiter-patrick-hand -f wagesreiter-patrick-hand-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 20200215-alt1_5
- new version

