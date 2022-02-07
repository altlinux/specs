Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname julietaula-montserrat-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname julietaula-montserrat-fonts
%define autorelease 2

# Override versioning to sync with upstream
Epoch:    1
Version:  7.222
Release:  alt1_2
URL:      https://github.com/JulietaUla/Montserrat

%global         foundry         julietaula
%global         fontlicense     OFL
%global         fontlicenses    OFL.txt
%global         fontdocs        README.md AUTHORS.txt CONTRIBUTORS.txt DESCRIPTION.en_us.html
%global         fontdocsex      %{fontlicenses}

%global common_description \
A typeface inspired by signs around the Montserrat area \
of Buenos Aires, Argentina.

%global fontfamily0       Montserrat
%global fontsummary0      Base version of the Montserrat area inspired typeface
%global fontpkgheader0    \
Obsoletes: julietaula-montserrat-fonts-common < %{version}-%{release}\

%global fonts0            fonts/otf/Montserrat-*.otf
%global fontdescription  \
%{common_description}\
\
This package provide the base fonts.


%global fontfamily1       Montserrat Alternates
%global fontsummary1      A Montserrat area inspired typeface family alternate version
%global fonts1            fonts/otf/MontserratAlternates-*.otf
%global fontdescription1  \
%{common_description}\
\
This package provide an alternate version of the fonts.

Source0:  https://github.com/JulietaUla/Montserrat}/archive/v%{version}.tar.gz#/Montserrat-%{version}.tar.gz
Source10: 61-julietaula-montserrat-fonts.conf
Source11: 61-julietaula-montserrat-alternates-fonts.conf

Name:           fonts-otf-julietaula-montserrat
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription}
%package     -n fonts-otf-julietaula-montserrat-alternates
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-julietaula-montserrat-alternates
%{?fontdescription1}

%prep
%global fontconfs0        %{SOURCE10}
%global fontconfs1        %{SOURCE11}
%setup -q -n Montserrat-%{version}


%build
# fontbuild 0
fontnames=$(
  for font in 'fonts/otf/Montserrat-Black.otf' 'fonts/otf/Montserrat-BlackItalic.otf' 'fonts/otf/Montserrat-Bold.otf' 'fonts/otf/Montserrat-BoldItalic.otf' 'fonts/otf/Montserrat-ExtraBold.otf' 'fonts/otf/Montserrat-ExtraBoldItalic.otf' 'fonts/otf/Montserrat-ExtraLight.otf' 'fonts/otf/Montserrat-ExtraLightItalic.otf' 'fonts/otf/Montserrat-Italic.otf' 'fonts/otf/Montserrat-Light.otf' 'fonts/otf/Montserrat-LightItalic.otf' 'fonts/otf/Montserrat-Medium.otf' 'fonts/otf/Montserrat-MediumItalic.otf' 'fonts/otf/Montserrat-Regular.otf' 'fonts/otf/Montserrat-SemiBold.otf' 'fonts/otf/Montserrat-SemiBoldItalic.otf' 'fonts/otf/Montserrat-Thin.otf' 'fonts/otf/Montserrat-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Montserrat-Black.otf' 'fonts/otf/Montserrat-BlackItalic.otf' 'fonts/otf/Montserrat-Bold.otf' 'fonts/otf/Montserrat-BoldItalic.otf' 'fonts/otf/Montserrat-ExtraBold.otf' 'fonts/otf/Montserrat-ExtraBoldItalic.otf' 'fonts/otf/Montserrat-ExtraLight.otf' 'fonts/otf/Montserrat-ExtraLightItalic.otf' 'fonts/otf/Montserrat-Italic.otf' 'fonts/otf/Montserrat-Light.otf' 'fonts/otf/Montserrat-LightItalic.otf' 'fonts/otf/Montserrat-Medium.otf' 'fonts/otf/Montserrat-MediumItalic.otf' 'fonts/otf/Montserrat-Regular.otf' 'fonts/otf/Montserrat-SemiBold.otf' 'fonts/otf/Montserrat-SemiBoldItalic.otf' 'fonts/otf/Montserrat-Thin.otf' 'fonts/otf/Montserrat-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the julietaula-montserrat-fonts appstream file"
cat > "org.altlinux.julietaula-montserrat-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.julietaula-montserrat-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>julietaula Montserrat</name>
  <summary><![CDATA[Base version of the Montserrat area inspired typeface]]></summary>
  <description>
    <p><![CDATA[A typeface inspired by signs around the Montserrat area]]></p><p><![CDATA[of Buenos Aires, Argentina.]]></p> This package provide the base fonts.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://github.com/JulietaUla/Montserrat</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'fonts/otf/MontserratAlternates-Black.otf' 'fonts/otf/MontserratAlternates-BlackItalic.otf' 'fonts/otf/MontserratAlternates-Bold.otf' 'fonts/otf/MontserratAlternates-BoldItalic.otf' 'fonts/otf/MontserratAlternates-ExtraBold.otf' 'fonts/otf/MontserratAlternates-ExtraBoldItalic.otf' 'fonts/otf/MontserratAlternates-ExtraLight.otf' 'fonts/otf/MontserratAlternates-ExtraLightItalic.otf' 'fonts/otf/MontserratAlternates-Italic.otf' 'fonts/otf/MontserratAlternates-Light.otf' 'fonts/otf/MontserratAlternates-LightItalic.otf' 'fonts/otf/MontserratAlternates-Medium.otf' 'fonts/otf/MontserratAlternates-MediumItalic.otf' 'fonts/otf/MontserratAlternates-Regular.otf' 'fonts/otf/MontserratAlternates-SemiBold.otf' 'fonts/otf/MontserratAlternates-SemiBoldItalic.otf' 'fonts/otf/MontserratAlternates-Thin.otf' 'fonts/otf/MontserratAlternates-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/MontserratAlternates-Black.otf' 'fonts/otf/MontserratAlternates-BlackItalic.otf' 'fonts/otf/MontserratAlternates-Bold.otf' 'fonts/otf/MontserratAlternates-BoldItalic.otf' 'fonts/otf/MontserratAlternates-ExtraBold.otf' 'fonts/otf/MontserratAlternates-ExtraBoldItalic.otf' 'fonts/otf/MontserratAlternates-ExtraLight.otf' 'fonts/otf/MontserratAlternates-ExtraLightItalic.otf' 'fonts/otf/MontserratAlternates-Italic.otf' 'fonts/otf/MontserratAlternates-Light.otf' 'fonts/otf/MontserratAlternates-LightItalic.otf' 'fonts/otf/MontserratAlternates-Medium.otf' 'fonts/otf/MontserratAlternates-MediumItalic.otf' 'fonts/otf/MontserratAlternates-Regular.otf' 'fonts/otf/MontserratAlternates-SemiBold.otf' 'fonts/otf/MontserratAlternates-SemiBoldItalic.otf' 'fonts/otf/MontserratAlternates-Thin.otf' 'fonts/otf/MontserratAlternates-ThinItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the julietaula-montserrat-alternates-fonts appstream file"
cat > "org.altlinux.julietaula-montserrat-alternates-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.julietaula-montserrat-alternates-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>julietaula Montserrat Alternates</name>
  <summary><![CDATA[A Montserrat area inspired typeface family alternate version]]></summary>
  <description>
    <p><![CDATA[A typeface inspired by signs around the Montserrat area]]></p><p><![CDATA[of Buenos Aires, Argentina.]]></p> This package provide an alternate version of the fonts.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://github.com/JulietaUla/Montserrat</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing julietaula-montserrat-fonts
echo "" > "julietaula-montserrat-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/julietaula-montserrat/
echo "%%dir %_fontsdir/otf/julietaula-montserrat" >> "julietaula-montserrat-fonts0.list"
install -m 0644 -vp "fonts/otf/Montserrat-Black.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Black.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-BlackItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-BlackItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Bold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Bold.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-BoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-BoldItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-ExtraBold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-ExtraBold.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-ExtraBoldItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-ExtraLight.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-ExtraLight.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-ExtraLightItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Italic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Italic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Light.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Light.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-LightItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-LightItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Medium.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Medium.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-MediumItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-MediumItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Regular.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Regular.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-SemiBold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-SemiBold.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-SemiBoldItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-Thin.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-Thin.otf")\" >> 'julietaula-montserrat-fonts0.list'
install -m 0644 -vp "fonts/otf/Montserrat-ThinItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/Montserrat-ThinItalic.otf")\" >> 'julietaula-montserrat-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "julietaula-montserrat-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "julietaula-montserrat-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.julietaula-montserrat-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "julietaula-montserrat-fonts0.list"
done

for fontdoc in 'README.md' 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'DESCRIPTION.en_us.html'; do
  echo %%doc "'${fontdoc}'" >> "julietaula-montserrat-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "julietaula-montserrat-fonts0.list"
done
echo Installing julietaula-montserrat-alternates-fonts
echo "" > "julietaula-montserrat-alternates-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/julietaula-montserrat/
echo "%%dir %_fontsdir/otf/julietaula-montserrat" >> "julietaula-montserrat-alternates-fonts1.list"
install -m 0644 -vp "fonts/otf/MontserratAlternates-Black.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Black.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-BlackItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-BlackItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Bold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Bold.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-BoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-BoldItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-ExtraBold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-ExtraBold.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-ExtraBoldItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-ExtraLight.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-ExtraLight.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-ExtraLightItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Italic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Italic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Light.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Light.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-LightItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-LightItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Medium.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Medium.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-MediumItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-MediumItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Regular.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Regular.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-SemiBold.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-SemiBold.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-SemiBoldItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-Thin.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-Thin.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
install -m 0644 -vp "fonts/otf/MontserratAlternates-ThinItalic.otf" %buildroot%_fontsdir/otf/julietaula-montserrat/
echo \"%_fontsdir/otf/julietaula-montserrat//$(basename "fonts/otf/MontserratAlternates-ThinItalic.otf")\" >> 'julietaula-montserrat-alternates-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE11' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "julietaula-montserrat-alternates-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "julietaula-montserrat-alternates-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.julietaula-montserrat-alternates-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "julietaula-montserrat-alternates-fonts1.list"
done

for fontdoc in 'README.md' 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'DESCRIPTION.en_us.html'; do
  echo %%doc "'${fontdoc}'" >> "julietaula-montserrat-alternates-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "julietaula-montserrat-alternates-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'julietaula-montserrat-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'julietaula-montserrat-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'julietaula-montserrat-alternates-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'julietaula-montserrat-alternates-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-julietaula-montserrat -f julietaula-montserrat-fonts0.list
%files -n fonts-otf-julietaula-montserrat-alternates -f julietaula-montserrat-alternates-fonts1.list

%changelog
* Tue Feb 08 2022 Igor Vlasenko <viy@altlinux.org> 1:7.222-alt1_2
- update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1:7.210-alt1_1
- update to new release by fcimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_5
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_2
- update to new release by fcimport

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:7.200-alt1_1
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.002-alt1_3
- new version

