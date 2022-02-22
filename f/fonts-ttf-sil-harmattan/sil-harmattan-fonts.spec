Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-harmattan-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-harmattan-fonts
# SPDX-License-Identifier: MIT
Version: 1.001
Release: alt1_4

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Harmattan
%global fontsummary       Harmattan, a Warsh-style Arabic script font family
%global projectname       harmattan
%global archivename       Harmattan-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
# We blacklist the Andika subset in Harmattan, to use the latest full version\
Requires: font(andikanewbasic)\

%global fonts             *.ttf
%global fontdescription   \
Harmattan, named after the trade winds that blow during the dry season in West\
Africa, is designed in a Warsh style to suit the needs of languages using the\
Arabic script in West Africa.\
\
Because the font style is specifically intended for West Africa, the character\
set for this font is aimed at West African languages. Thus, Asia-specific\
glyphs are not included.

Source0:  https://software.sil.org/downloads/r/%{projectname}/%{archivename}.zip
Source10: 65-sil-harmattan-fonts.xml

Name:           fonts-ttf-sil-harmattan
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
%setup -q -n %{archivename}
%linuxtext *.txt documentation/*.txt

%build
# fontbuild 
fontnames=$(
  for font in 'Harmattan-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Harmattan-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-harmattan-fonts appstream file"
cat > "org.altlinux.sil-harmattan-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-harmattan-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Harmattan</name>
  <summary><![CDATA[Harmattan, a Warsh-style Arabic script font family]]></summary>
  <description>
    <p><![CDATA[Harmattan, named after the trade winds that blow during the dry season in West]]></p><p><![CDATA[Africa, is designed in a Warsh style to suit the needs of languages using the]]></p><p><![CDATA[Arabic script in West Africa.]]></p> Because the font style is specifically intended for West Africa, the character set for this font is aimed at West African languages. Thus, Asia-specific glyphs are not included.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-harmattan-fonts
echo "" > "sil-harmattan-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-harmattan/
echo "%%dir %_fontsdir/ttf/sil-harmattan" >> "sil-harmattan-fonts.list"
install -m 0644 -vp "Harmattan-Regular.ttf" %buildroot%_fontsdir/ttf/sil-harmattan/
echo \"%_fontsdir/ttf/sil-harmattan//$(basename "Harmattan-Regular.ttf")\" >> 'sil-harmattan-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Harmattan-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-harmattan-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-harmattan-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-harmattan-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-harmattan-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt' 'documentation/Harmattan-features.odt'; do
  echo %%doc "'${fontdoc}'" >> "sil-harmattan-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-harmattan-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-harmattan-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-harmattan-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-harmattan -f sil-harmattan-fonts.list

%changelog
* Tue Feb 22 2022 Igor Vlasenko <viy@altlinux.org> 1.001-alt1_4
- new version

