Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname sil-awami-nastaliq-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-awami-nastaliq-fonts
# SPDX-License-Identifier: MIT
Version: 2.000
Release: alt1_4

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt documentation/*.txt documentation/*.odt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Awami Nastaliq
%global fontsummary       Awami Nastaliq, a Nastaliq-style Arabic script font family
%global projectname       awami
%global archivename       AwamiNastaliq-%{version}
URL:                      https://software.sil.org/%{projectname}/
%global fontpkgheader     \
#Recommends: font(charissil)\

%global fonts             *.ttf
%global fontdescription   \
Awami Nastaliq is a Nastaliq-style Arabic script font family supporting a wide\
variety of languages of southwest Asia, including but not limited to Urdu. This\
font is aimed at minority language support. This makes it unique among Nastaliq\
fonts.\
\
Nastaliq, based on a centuries-old calligraphic tradition, is considered one of\
the most beautiful scripts on the planet. Nastaliq has been called a.'the bride\
of calligraphya.' but its complexity also makes it one of the most difficult\
scripts to render using a computer font. Its right-to-left direction, vertical\
nature, and context-specific shaping provide a challenge to any font rendering\
engine and make it much more difficult to render than the flat (Naskh) Arabic\
script that it is based on. As a result, font developers have long struggled to\
produce a font with the correct shaping but at the same time avoid overlapping\
of dots and diacritics. In order to account for the seemingly infinite\
variations, the Graphite rendering engine has been extended just to handle\
these complexities properly.

Source0:  https://github.com/silnrsi/font-%{projectname}/releases/download/v%{version}/%{archivename}.tar.xz
Source10: 65-sil-awami-nastaliq-fonts.xml

Name:           fonts-ttf-sil-awami-nastaliq
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
  for font in 'AwamiNastaliq-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'AwamiNastaliq-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-awami-nastaliq-fonts appstream file"
cat > "org.altlinux.sil-awami-nastaliq-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-awami-nastaliq-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Awami Nastaliq</name>
  <summary><![CDATA[Awami Nastaliq, a Nastaliq-style Arabic script font family]]></summary>
  <description>
    <p><![CDATA[Awami Nastaliq is a Nastaliq-style Arabic script font family supporting a wide]]></p><p><![CDATA[variety of languages of southwest Asia, including but not limited to Urdu. This]]></p><p><![CDATA[font is aimed at minority language support. This makes it unique among Nastaliq]]></p><p><![CDATA[fonts.]]></p> Nastaliq, based on a centuries-old calligraphic tradition, is considered one of the most beautiful scripts on the planet. Nastaliq has been called “the bride of calligraphy” but its complexity also makes it one of the most difficult scripts to render using a computer font. Its right-to-left direction, vertical nature, and context-specific shaping provide a challenge to any font rendering engine and make it much more difficult to render than the flat (Naskh) Arabic script that it is based on. As a result, font developers have long struggled to produce a font with the correct shaping but at the same time avoid overlapping of dots and diacritics. In order to account for the seemingly infinite variations, the Graphite rendering engine has been extended just to handle these complexities properly.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/%{projectname}/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-awami-nastaliq-fonts
echo "" > "sil-awami-nastaliq-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-awami-nastaliq/
echo "%%dir %_fontsdir/ttf/sil-awami-nastaliq" >> "sil-awami-nastaliq-fonts.list"
install -m 0644 -vp "AwamiNastaliq-Regular.ttf" %buildroot%_fontsdir/ttf/sil-awami-nastaliq/
echo \"%_fontsdir/ttf/sil-awami-nastaliq//$(basename "AwamiNastaliq-Regular.ttf")\" >> 'sil-awami-nastaliq-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'AwamiNastaliq-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-awami-nastaliq-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-awami-nastaliq-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-awami-nastaliq-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-awami-nastaliq-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'README.txt' 'documentation/DOCUMENTATION.txt' 'documentation/AwamiNastaliq-Features.odt' 'documentation/AwamiNastaliq-TypeSample.odt'; do
  echo %%doc "'${fontdoc}'" >> "sil-awami-nastaliq-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-awami-nastaliq-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-awami-nastaliq-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-awami-nastaliq-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-awami-nastaliq -f sil-awami-nastaliq-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.000-alt1_4
- new version

