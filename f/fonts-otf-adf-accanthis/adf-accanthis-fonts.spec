Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname adf-accanthis-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname adf-accanthis-fonts
# SPDX-License-Identifier: MIT
Version: 1.8
Release: alt1_26
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPLv2+ with exceptions
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE.txt

%global common_description \
A Latin font family published by Hirwen Harendala.'s Arkandis Digital Foundry,\
Accanthis was inspired from the a.'Cloister Oldstylea.' font family found in the\
a.'American Specimen Book of Typefaces Suplementa.'. Its medium contrast is\
sufficient to be reader-friendly and deliver an elegant and refined experience.\
\
Accanthis is a modernized garaldic font family and is well suited to book\
typesetting and refined presentations.

%global fontfamily0       Accanthis
%global fontsummary0      ADF Accanthis, a modernized garaldic serif font family, a.'Galliarda.' alternative
%global fontpkgheader0    \
Obsoletes: adf-accanthis-fonts-common < %{version}-%{release}\

%global fonts0            OTF/AccanthisADFStd-*.otf
%global fontdescription0  \
%{common_description}\
\
This variant is intended to serve as alternative to the a.'Galliarda.' font family.

%global fontfamily2       Accanthis-2
%global fontsummary2      ADF Accanthis Na..2, a modernized garaldic serif, a.'Horley old stylea.' alternative
%global fonts2            OTF/AccanthisADFStdNo2-*.otf
%global fontdescription2  \
%{common_description}\
\
This variant is closer to the a.'Horley old stylea.' font family than the original\
version.

%global fontfamily3       Accanthis-3
%global fontsummary3      ADF Accanthis Na..3, a modernized garaldic serif font family
%global fonts3            OTF/AccanthisADFStdNo3-*.otf
%global fontdescription3  \
%{common_description}\
\
This variant remixes a slightly modified Accanthis a..2 with elements from the\
original Italic and changes to k, p, z and numbers.

%global archivename Accanthis-Std-20101124

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/Accanthis-Cat.pdf
Source10:  60-adf-accanthis-fonts.xml
Source12:  60-adf-accanthis-2-fonts.xml
Source13:  60-adf-accanthis-3-fonts.xml


Name:           fonts-otf-adf-accanthis
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-adf-accanthis-2
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-adf-accanthis-2
%{?fontdescription2}
%package     -n fonts-ttf-adf-accanthis-3
Group: System/Fonts/True type
Summary:        %{fontsummary3}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-ttf-adf-accanthis-3
%{?fontdescription3}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-adf-accanthis = %EVR
Requires:  fonts-ttf-adf-accanthis-2 = %EVR
Requires:  fonts-ttf-adf-accanthis-3 = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs2      %{SOURCE12}
%global fontconfngs3      %{SOURCE13}
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE.txt OTF/COPYING

%build
# fontbuild 0
fontnames=$(
  for font in 'OTF/AccanthisADFStd-Bold.otf' 'OTF/AccanthisADFStd-BoldItalic.otf' 'OTF/AccanthisADFStd-Italic.otf' 'OTF/AccanthisADFStd-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/AccanthisADFStd-Bold.otf' 'OTF/AccanthisADFStd-BoldItalic.otf' 'OTF/AccanthisADFStd-Italic.otf' 'OTF/AccanthisADFStd-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-accanthis-fonts appstream file"
cat > "org.altlinux.adf-accanthis-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-accanthis-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Accanthis</name>
  <summary><![CDATA[ADF Accanthis, a modernized garaldic serif font family, “Galliard” alternative]]></summary>
  <description>
    <p><![CDATA[A Latin font family published by Hirwen Harendal’s Arkandis Digital Foundry,]]></p><p><![CDATA[Accanthis was inspired from the “Cloister Oldstyle” font family found in the]]></p><p><![CDATA[“American Specimen Book of Typefaces Suplement”. Its medium contrast is]]></p><p><![CDATA[sufficient to be reader-friendly and deliver an elegant and refined experience.]]></p> Accanthis is a modernized garaldic font family and is well suited to book typesetting and refined presentations. This variant is intended to serve as alternative to the “Galliard” font
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://arkandis.tuxfamily.org/adffonts.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'OTF/AccanthisADFStdNo2-Bold.otf' 'OTF/AccanthisADFStdNo2-BoldItalic.otf' 'OTF/AccanthisADFStdNo2-Italic.otf' 'OTF/AccanthisADFStdNo2-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/AccanthisADFStdNo2-Bold.otf' 'OTF/AccanthisADFStdNo2-BoldItalic.otf' 'OTF/AccanthisADFStdNo2-Italic.otf' 'OTF/AccanthisADFStdNo2-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-accanthis-2-fonts appstream file"
cat > "org.altlinux.adf-accanthis-2-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-accanthis-2-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Accanthis-2</name>
  <summary><![CDATA[ADF Accanthis Nᵒ2, a modernized garaldic serif, “Horley old style” alternative]]></summary>
  <description>
    <p><![CDATA[A Latin font family published by Hirwen Harendal’s Arkandis Digital Foundry,]]></p><p><![CDATA[Accanthis was inspired from the “Cloister Oldstyle” font family found in the]]></p><p><![CDATA[“American Specimen Book of Typefaces Suplement”. Its medium contrast is]]></p><p><![CDATA[sufficient to be reader-friendly and deliver an elegant and refined experience.]]></p> Accanthis is a modernized garaldic font family and is well suited to book typesetting and refined presentations. This variant is closer to the “Horley old style” font family than the original
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://arkandis.tuxfamily.org/adffonts.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'OTF/AccanthisADFStdNo3-Bold.otf' 'OTF/AccanthisADFStdNo3-BoldItalic.otf' 'OTF/AccanthisADFStdNo3-Italic.otf' 'OTF/AccanthisADFStdNo3-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/AccanthisADFStdNo3-Bold.otf' 'OTF/AccanthisADFStdNo3-BoldItalic.otf' 'OTF/AccanthisADFStdNo3-Italic.otf' 'OTF/AccanthisADFStdNo3-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-accanthis-3-fonts appstream file"
cat > "org.altlinux.adf-accanthis-3-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-accanthis-3-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Accanthis-3</name>
  <summary><![CDATA[ADF Accanthis Nᵒ3, a modernized garaldic serif font family]]></summary>
  <description>
    <p><![CDATA[A Latin font family published by Hirwen Harendal’s Arkandis Digital Foundry,]]></p><p><![CDATA[Accanthis was inspired from the “Cloister Oldstyle” font family found in the]]></p><p><![CDATA[“American Specimen Book of Typefaces Suplement”. Its medium contrast is]]></p><p><![CDATA[sufficient to be reader-friendly and deliver an elegant and refined experience.]]></p> Accanthis is a modernized garaldic font family and is well suited to book typesetting and refined presentations. This variant remixes a slightly modified Accanthis №2 with elements from the
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://arkandis.tuxfamily.org/adffonts.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "adf-accanthis-fonts
echo "" > "adf-accanthis-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-accanthis/
echo "%%dir %_fontsdir/otf/adf-accanthis" >> "adf-accanthis-fonts0.list"
install -m 0644 -vp "OTF/AccanthisADFStd-Bold.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStd-Bold.otf")\" >> 'adf-accanthis-fonts0.list'
install -m 0644 -vp "OTF/AccanthisADFStd-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStd-BoldItalic.otf")\" >> 'adf-accanthis-fonts0.list'
install -m 0644 -vp "OTF/AccanthisADFStd-Italic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStd-Italic.otf")\" >> 'adf-accanthis-fonts0.list'
install -m 0644 -vp "OTF/AccanthisADFStd-Regular.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStd-Regular.otf")\" >> 'adf-accanthis-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'OTF/AccanthisADFStd-Bold.otf' 'OTF/AccanthisADFStd-BoldItalic.otf' 'OTF/AccanthisADFStd-Italic.otf' 'OTF/AccanthisADFStd-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-accanthis-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-accanthis-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-accanthis-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-accanthis-fonts0.list"
done

for fontdoc in 'NOTICE.txt'; do
  echo %%doc "'${fontdoc}'" >> "adf-accanthis-fonts0.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-accanthis-fonts0.list"
done
echo "Installing "adf-accanthis-2-fonts
echo "" > "adf-accanthis-2-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-accanthis/
echo "%%dir %_fontsdir/otf/adf-accanthis" >> "adf-accanthis-2-fonts2.list"
install -m 0644 -vp "OTF/AccanthisADFStdNo2-Bold.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo2-Bold.otf")\" >> 'adf-accanthis-2-fonts2.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo2-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo2-BoldItalic.otf")\" >> 'adf-accanthis-2-fonts2.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo2-Italic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo2-Italic.otf")\" >> 'adf-accanthis-2-fonts2.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo2-Regular.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo2-Regular.otf")\" >> 'adf-accanthis-2-fonts2.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE12'; do
      gen-fontconf -x "${fontconfng}" -w -f 'OTF/AccanthisADFStdNo2-Bold.otf' 'OTF/AccanthisADFStdNo2-BoldItalic.otf' 'OTF/AccanthisADFStdNo2-Italic.otf' 'OTF/AccanthisADFStdNo2-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-accanthis-2-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-accanthis-2-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-accanthis-2-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-accanthis-2-fonts2.list"
done

for fontdoc in 'NOTICE.txt'; do
  echo %%doc "'${fontdoc}'" >> "adf-accanthis-2-fonts2.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-accanthis-2-fonts2.list"
done
echo "Installing "adf-accanthis-3-fonts
echo "" > "adf-accanthis-3-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-accanthis/
echo "%%dir %_fontsdir/otf/adf-accanthis" >> "adf-accanthis-3-fonts3.list"
install -m 0644 -vp "OTF/AccanthisADFStdNo3-Bold.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo3-Bold.otf")\" >> 'adf-accanthis-3-fonts3.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo3-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo3-BoldItalic.otf")\" >> 'adf-accanthis-3-fonts3.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo3-Italic.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo3-Italic.otf")\" >> 'adf-accanthis-3-fonts3.list'
install -m 0644 -vp "OTF/AccanthisADFStdNo3-Regular.otf" %buildroot%_fontsdir/otf/adf-accanthis/
echo \"%_fontsdir/otf/adf-accanthis//$(basename "OTF/AccanthisADFStdNo3-Regular.otf")\" >> 'adf-accanthis-3-fonts3.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE13'; do
      gen-fontconf -x "${fontconfng}" -w -f 'OTF/AccanthisADFStdNo3-Bold.otf' 'OTF/AccanthisADFStdNo3-BoldItalic.otf' 'OTF/AccanthisADFStdNo3-Italic.otf' 'OTF/AccanthisADFStdNo3-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-accanthis-3-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-accanthis-3-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-accanthis-3-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-accanthis-3-fonts3.list"
done

for fontdoc in 'NOTICE.txt'; do
  echo %%doc "'${fontdoc}'" >> "adf-accanthis-3-fonts3.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-accanthis-3-fonts3.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-accanthis-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-accanthis-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-accanthis-2-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-accanthis-2-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-accanthis-3-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-accanthis-3-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-adf-accanthis -f adf-accanthis-fonts0.list
%files -n fonts-ttf-adf-accanthis-2 -f adf-accanthis-2-fonts2.list
%files -n fonts-ttf-adf-accanthis-3 -f adf-accanthis-3-fonts3.list

%files doc
%doc --no-dereference OTF/COPYING
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_26
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_10
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_3
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_5
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5
- initial release by fcimport

