Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname marcsabatella-campania-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name marcsabatella-campania-fonts
%define fontpkgname marcsabatella-campania-fonts
Version:        2.009
Release:        alt1_5
URL:            https://github.com/MarcSabatella/Campania

%global foundry           MarcSabatella
%global fontlicense       OFL
%global fontlicenses      LICENSE
%global fontdocs          README.md
%global fontfamily        Campania
%global fontsummary       Font for Roman numeral analysis (music theory)
%global fonts             *.otf
%global fontorg           com.github

%global fontdescription   \
This font is inspired by the work of Florian Kretlow and the impressive\
Figurato font he developed for figured bass, as well as the work of\
Ronald Caltabiano and his pioneering Sicilian Numerals font.  This\
version of Campania is not directly based on either of these, however.\
Instead, it uses the glyphs from Doulos and adds some relatively\
straightforward contextual substitutions and positioning rules to allow\
you to enter the most common symbols just by typing naturally.

Source0:        https://github.com/MarcSabatella/Campania/archive/%{version}/%{oldname}-%{version}.tar.gz
Source1:        65-marcsabatella-campania-fonts.conf

BuildRequires:  appstream libappstream
BuildRequires:  fontforge libfontforge python3-module-fontforge

Name:           fonts-otf-marcsabatella-campania
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs         %{SOURCE1}
%setup -q -n Campania-%{version}


%build
# fontbuild 
fontnames=$(
  for font in 'Campania.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Campania.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the marcsabatella-campania-fonts appstream file"
cat > "com.github.marcsabatella-campania-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>com.github.marcsabatella-campania-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>MarcSabatella Campania</name>
  <summary><![CDATA[Font for Roman numeral analysis (music theory)]]></summary>
  <description>
    <p><![CDATA[This font is inspired by the work of Florian Kretlow and the impressive]]></p><p><![CDATA[Figurato font he developed for figured bass, as well as the work of]]></p><p><![CDATA[Ronald Caltabiano and his pioneering Sicilian Numerals font.  This]]></p><p><![CDATA[version of Campania is not directly based on either of these, however.]]></p><p><![CDATA[Instead, it uses the glyphs from Doulos and adds some relatively]]></p><p><![CDATA[straightforward contextual substitutions and positioning rules to allow]]></p><p><![CDATA[you to enter the most common symbols just by typing naturally.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://github.com/MarcSabatella/Campania</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
fontforge -lang=ff -c 'Open($1); Generate($2)' Campania.sfd Campania.otf

%install
echo Installing marcsabatella-campania-fonts
echo "" > "marcsabatella-campania-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/marcsabatella-campania/
echo "%%dir %_fontsdir/otf/marcsabatella-campania" >> "marcsabatella-campania-fonts.list"
install -m 0644 -vp "Campania.otf" %buildroot%_fontsdir/otf/marcsabatella-campania/
echo \"%_fontsdir/otf/marcsabatella-campania//$(basename "Campania.otf")\" >> 'marcsabatella-campania-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "marcsabatella-campania-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "marcsabatella-campania-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'com.github.marcsabatella-campania-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "marcsabatella-campania-fonts.list"
done

for fontdoc in 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "marcsabatella-campania-fonts.list"
done

for fontlicense in 'LICENSE'; do
  echo %%doc "'${fontlicense}'" >> "marcsabatella-campania-fonts.list"
done
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{oldname}.metainfo.xml

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'marcsabatella-campania-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'marcsabatella-campania-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%files -n fonts-otf-marcsabatella-campania -f marcsabatella-campania-fonts.list

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 2.009-alt1_5
- new version

