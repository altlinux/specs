Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname intel-clear-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname intel-clear-sans-fonts
# SPDX-License-Identifier: MIT
Version: 1.00
Release: alt1_6
%global  projectname clear-sans
URL:     https://01.org/%{projectname}

%global foundry           Intel
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE-2.0.txt

%global fontfamily        Clear Sans
%global fontsummary       Clear Sans, a versatile font family for screen, print, and Web
%global fonts             TTF/*.ttf
%global fontdescription  \
Clear Sans has been recognized as a versatile font for screen, print, and Web.\
Its minimized, unambiguous characters and slightly narrow proportions, make it\
ideal for UI design.\
\
Clear Sans was designed with on-screen legibility in mind. It strikes a balance\
between contemporary, professional, and stylish expression and thoroughly\
functional purpose. It has a sophisticated and elegant personality at all\
sizes, and its thoughtful design becomes even more evident at the thin weight.

Source0:  https://01.org/sites/default/files/downloads/%{projectname}/clearsans-%{version}.zip
Source10: 60-intel-clear-sans-fonts.xml

Name:           fonts-ttf-intel-clear-sans
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
%setup -n %{oldname}-%{version} -q -c

%build
# fontbuild 
fontnames=$(
  for font in 'TTF/ClearSans-Bold.ttf' 'TTF/ClearSans-BoldItalic.ttf' 'TTF/ClearSans-Italic.ttf' 'TTF/ClearSans-Light.ttf' 'TTF/ClearSans-Medium.ttf' 'TTF/ClearSans-MediumItalic.ttf' 'TTF/ClearSans-Regular.ttf' 'TTF/ClearSans-Thin.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'TTF/ClearSans-Bold.ttf' 'TTF/ClearSans-BoldItalic.ttf' 'TTF/ClearSans-Italic.ttf' 'TTF/ClearSans-Light.ttf' 'TTF/ClearSans-Medium.ttf' 'TTF/ClearSans-MediumItalic.ttf' 'TTF/ClearSans-Regular.ttf' 'TTF/ClearSans-Thin.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the intel-clear-sans-fonts appstream file"
cat > "org.altlinux.intel-clear-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.intel-clear-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>Intel Clear Sans</name>
  <summary><![CDATA[Clear Sans, a versatile font family for screen, print, and Web]]></summary>
  <description>
    <p><![CDATA[Clear Sans has been recognized as a versatile font for screen, print, and Web.]]></p><p><![CDATA[Its minimized, unambiguous characters and slightly narrow proportions, make it]]></p><p><![CDATA[ideal for UI design.]]></p> Clear Sans was designed with on-screen legibility in mind. It strikes a balance between contemporary, professional, and stylish expression and thoroughly functional purpose. It has a sophisticated and elegant personality at all sizes, and its thoughtful design becomes even more evident at the thin weight.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://01.org/%{projectname}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing intel-clear-sans-fonts
echo "" > "intel-clear-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/intel-clear-sans/
echo "%%dir %_fontsdir/ttf/intel-clear-sans" >> "intel-clear-sans-fonts.list"
install -m 0644 -vp "TTF/ClearSans-Bold.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Bold.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-BoldItalic.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-BoldItalic.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-Italic.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Italic.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-Light.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Light.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-Medium.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Medium.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-MediumItalic.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-MediumItalic.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-Regular.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Regular.ttf")\" >> 'intel-clear-sans-fonts.list'
install -m 0644 -vp "TTF/ClearSans-Thin.ttf" %buildroot%_fontsdir/ttf/intel-clear-sans/
echo \"%_fontsdir/ttf/intel-clear-sans//$(basename "TTF/ClearSans-Thin.ttf")\" >> 'intel-clear-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'TTF/ClearSans-Bold.ttf' 'TTF/ClearSans-BoldItalic.ttf' 'TTF/ClearSans-Italic.ttf' 'TTF/ClearSans-Light.ttf' 'TTF/ClearSans-Medium.ttf' 'TTF/ClearSans-MediumItalic.ttf' 'TTF/ClearSans-Regular.ttf' 'TTF/ClearSans-Thin.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "intel-clear-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "intel-clear-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.intel-clear-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "intel-clear-sans-fonts.list"
done

for fontlicense in 'LICENSE-2.0.txt'; do
  echo %%doc "'${fontlicense}'" >> "intel-clear-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'intel-clear-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'intel-clear-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-intel-clear-sans -f intel-clear-sans-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 1.00-alt1_6
- new version

