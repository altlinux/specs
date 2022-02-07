Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname google-droid-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname google-droid-fonts
# SPDX-License-Identifier: MIT
BuildArch: noarch

# No sane versionning upstream, use git clone timestamp
Version: 20200215
Release: alt1_12
License: ASL 2.0
URL:     https://android.googlesource.com/

%global source_name       google-droid-fonts

%global foundry           Google
%global fontlicenses      NOTICE
%global fontdocs          *.txt

%global common_description \
The Droid font family was designed in the fall of 2006 by Ascendera.'s Steve\
Matteson, as a commission from Google to create a set of system fonts for its\
Android platform. The goal was to provide optimal quality and comfort on a\
mobile handset when rendered in application menus, web browsers and for other\
screen text.\
\
The family was later extended in collaboration with other designers such as\
Pascal Zoghbi of 29ArabicLetters.

%global fontfamily1       Droid Sans
%global fontsummary1      Droid Sans, a humanist sans-serif font family
%global fontpkgheader1   \
Obsoletes: google-droid-kufi-fonts < %{version}-%{release}\
Requires: font(notosans)\

%global fonts1            DroidSans*ttf DroidKufi*ttf
%global fontsex1          DroidSansMono*ttf DroidSansFallback.ttf DroidSansHebrew.ttf
%global fontdescription1  \
%{common_description}\
\
Droid Sans is a humanist sans serif font family designed for user interfaces and electronic communication.\
\
The Arabic block was initially designed by Steve Matteson of Ascender under the\
Droid Kufi name, with consulting by Pascal Zoghbi of 29ArabicLetters to\
finalize the font family.

%global fontfamily2       Droid Sans Mono
%global fontsummary2      Droid Sans Mono, a humanist mono-space sans-serif font family
%global fontpkgheader2    \
Requires: font(notosansmono)\

%global fonts2            DroidSansMono*ttf
%global fontdescription2  \
%{common_description}\
\
Droid Sans Mono is a humanist mono-space sans serif font family designed for\
user interfaces and electronic communication.

%global fontfamily3       Droid Serif
%global fontsummary3      Droid Serif, a contemporary serif font family
%global fontpkgheader3    \
Requires: font(notoserif)\

%global fonts3            DroidSerif*ttf DroidNaskh*ttf
%global fontsex3          DroidNaskhUI-Regular.ttf DroidNaskh-Regular-Shift.ttf
%global fontdescription3  \
%{common_description}\
\
Droid Serif is a contemporary serif typeface family designed for comfortable\
reading on screen. Droid Serif is slightly condensed to maximize the amount of\
text displayed on small screens. Vertical stress and open forms contribute to\
its readability while its proportion and overall design complement its\
companion Droid Sans.\
\
The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the\
Droid Naskh name.

%global archivename google-droid-fonts-%{version}


Source0:  %{archivename}.tar.xz
# Brutal script used to pull sources from upstream git
# Needs at least 2 Gib of space in /var/tmp
Source1:  getdroid.sh
Source11: 66-google-droid-sans-fonts.xml
Source12: 60-google-droid-sans-mono-fonts.xml
Source13: 66-google-droid-serif-fonts.xml

Name:     fonts-ttf-google-droid
Summary:  A set of general-purpose font families released by Google as part of Android
Source44: import.info
%description
%common_description

%package     -n fonts-ttf-google-droid-sans
Group: System/Fonts/True type
Summary:        %{fontsummary1}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
Conflicts: fonts-ttf-droid < 1.01
%description -n fonts-ttf-google-droid-sans
%{?fontdescription1}
%package     -n fonts-ttf-google-droid-sans-mono
Group: System/Fonts/True type
Summary:        %{fontsummary2}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
Conflicts: fonts-ttf-droid < 1.01
%description -n fonts-ttf-google-droid-sans-mono
%{?fontdescription2}
%package     -n fonts-ttf-google-droid-serif
Group: System/Fonts/True type
Summary:        %{fontsummary3}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
Conflicts: fonts-ttf-droid < 1.01
%description -n fonts-ttf-google-droid-serif
%{?fontdescription3}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-google-droid-sans = %EVR
Requires:  fonts-ttf-google-droid-sans-mono = %EVR
Requires:  fonts-ttf-google-droid-serif = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fontconfngs1      %{SOURCE11}
%global fontconfngs2      %{SOURCE12}
%global fontconfngs3      %{SOURCE13}
%setup -q -n %{archivename}

%build
# fontbuild 1
fontnames=$(
  for font in 'DroidSans-Bold.ttf' 'DroidSans.ttf' 'DroidSansArmenian.ttf' 'DroidSansDevanagari-Regular.ttf' 'DroidSansEthiopic-Bold.ttf' 'DroidSansEthiopic-Regular.ttf' 'DroidSansFallbackFull.ttf' 'DroidSansGeorgian.ttf' 'DroidSansHebrew-Bold.ttf' 'DroidSansHebrew-Regular.ttf' 'DroidSansJapanese.ttf' 'DroidSansTamil-Bold.ttf' 'DroidSansTamil-Regular.ttf' 'DroidSansThai.ttf' 'DroidKufi-Bold.ttf' 'DroidKufi-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'DroidSans-Bold.ttf' 'DroidSans.ttf' 'DroidSansArmenian.ttf' 'DroidSansDevanagari-Regular.ttf' 'DroidSansEthiopic-Bold.ttf' 'DroidSansEthiopic-Regular.ttf' 'DroidSansFallbackFull.ttf' 'DroidSansGeorgian.ttf' 'DroidSansHebrew-Bold.ttf' 'DroidSansHebrew-Regular.ttf' 'DroidSansJapanese.ttf' 'DroidSansTamil-Bold.ttf' 'DroidSansTamil-Regular.ttf' 'DroidSansThai.ttf' 'DroidKufi-Bold.ttf' 'DroidKufi-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-droid-sans-fonts appstream file"
cat > "org.altlinux.google-droid-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-droid-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>Google Droid Sans</name>
  <summary><![CDATA[Droid Sans, a humanist sans-serif font family]]></summary>
  <description>
    <p><![CDATA[The Droid font family was designed in the fall of 2006 by Ascender’s Steve]]></p><p><![CDATA[Matteson, as a commission from Google to create a set of system fonts for its]]></p><p><![CDATA[Android platform. The goal was to provide optimal quality and comfort on a]]></p><p><![CDATA[mobile handset when rendered in application menus, web browsers and for other]]></p><p><![CDATA[screen text.]]></p> The family was later extended in collaboration with other designers such as Pascal Zoghbi of 29ArabicLetters. Droid Sans is a humanist sans serif font family designed for user interfaces and electronic communication. The Arabic block was initially designed by Steve Matteson of Ascender under the Droid Kufi name, with consulting by Pascal Zoghbi of 29ArabicLetters to
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://android.googlesource.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'DroidSansMono.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'DroidSansMono.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-droid-sans-mono-fonts appstream file"
cat > "org.altlinux.google-droid-sans-mono-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-droid-sans-mono-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>Google Droid Sans Mono</name>
  <summary><![CDATA[Droid Sans Mono, a humanist mono-space sans-serif font family]]></summary>
  <description>
    <p><![CDATA[The Droid font family was designed in the fall of 2006 by Ascender’s Steve]]></p><p><![CDATA[Matteson, as a commission from Google to create a set of system fonts for its]]></p><p><![CDATA[Android platform. The goal was to provide optimal quality and comfort on a]]></p><p><![CDATA[mobile handset when rendered in application menus, web browsers and for other]]></p><p><![CDATA[screen text.]]></p> The family was later extended in collaboration with other designers such as Pascal Zoghbi of 29ArabicLetters. Droid Sans Mono is a humanist mono-space sans serif font family designed for
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://android.googlesource.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'DroidSerif-Bold.ttf' 'DroidSerif-BoldItalic.ttf' 'DroidSerif-Italic.ttf' 'DroidSerif-Regular.ttf' 'DroidNaskh-Bold.ttf' 'DroidNaskh-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'DroidSerif-Bold.ttf' 'DroidSerif-BoldItalic.ttf' 'DroidSerif-Italic.ttf' 'DroidSerif-Regular.ttf' 'DroidNaskh-Bold.ttf' 'DroidNaskh-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-droid-serif-fonts appstream file"
cat > "org.altlinux.google-droid-serif-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-droid-serif-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>Google Droid Serif</name>
  <summary><![CDATA[Droid Serif, a contemporary serif font family]]></summary>
  <description>
    <p><![CDATA[The Droid font family was designed in the fall of 2006 by Ascender’s Steve]]></p><p><![CDATA[Matteson, as a commission from Google to create a set of system fonts for its]]></p><p><![CDATA[Android platform. The goal was to provide optimal quality and comfort on a]]></p><p><![CDATA[mobile handset when rendered in application menus, web browsers and for other]]></p><p><![CDATA[screen text.]]></p> The family was later extended in collaboration with other designers such as Pascal Zoghbi of 29ArabicLetters. Droid Serif is a contemporary serif typeface family designed for comfortable reading on screen. Droid Serif is slightly condensed to maximize the amount of text displayed on small screens. Vertical stress and open forms contribute to its readability while its proportion and overall design complement its companion Droid Sans. The Arabic block was designed by Pascal Zoghbi of 29ArabicLetters under the
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://android.googlesource.com/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing google-droid-sans-fonts
echo "" > "google-droid-sans-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-droid/
echo "%%dir %_fontsdir/ttf/google-droid" >> "google-droid-sans-fonts1.list"
install -m 0644 -vp "DroidSans-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSans-Bold.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSans.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSans.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansArmenian.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansArmenian.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansDevanagari-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansDevanagari-Regular.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansEthiopic-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansEthiopic-Bold.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansEthiopic-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansEthiopic-Regular.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansFallbackFull.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansFallbackFull.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansGeorgian.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansGeorgian.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansHebrew-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansHebrew-Bold.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansHebrew-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansHebrew-Regular.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansJapanese.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansJapanese.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansTamil-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansTamil-Bold.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansTamil-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansTamil-Regular.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidSansThai.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansThai.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidKufi-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidKufi-Bold.ttf")\" >> 'google-droid-sans-fonts1.list'
install -m 0644 -vp "DroidKufi-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidKufi-Regular.ttf")\" >> 'google-droid-sans-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'DroidSans-Bold.ttf' 'DroidSans.ttf' 'DroidSansArmenian.ttf' 'DroidSansDevanagari-Regular.ttf' 'DroidSansEthiopic-Bold.ttf' 'DroidSansEthiopic-Regular.ttf' 'DroidSansFallbackFull.ttf' 'DroidSansGeorgian.ttf' 'DroidSansHebrew-Bold.ttf' 'DroidSansHebrew-Regular.ttf' 'DroidSansJapanese.ttf' 'DroidSansTamil-Bold.ttf' 'DroidSansTamil-Regular.ttf' 'DroidSansThai.ttf' 'DroidKufi-Bold.ttf' 'DroidKufi-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "google-droid-sans-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "google-droid-sans-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-droid-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-droid-sans-fonts1.list"
done

for fontdoc in 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "google-droid-sans-fonts1.list"
done

for fontlicense in 'NOTICE'; do
  echo %%doc "'${fontlicense}'" >> "google-droid-sans-fonts1.list"
done
echo Installing google-droid-sans-mono-fonts
echo "" > "google-droid-sans-mono-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-droid/
echo "%%dir %_fontsdir/ttf/google-droid" >> "google-droid-sans-mono-fonts2.list"
install -m 0644 -vp "DroidSansMono.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSansMono.ttf")\" >> 'google-droid-sans-mono-fonts2.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE12'; do
      gen-fontconf -x "${fontconfng}" -w -f 'DroidSansMono.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "google-droid-sans-mono-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "google-droid-sans-mono-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-droid-sans-mono-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-droid-sans-mono-fonts2.list"
done

for fontdoc in 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "google-droid-sans-mono-fonts2.list"
done

for fontlicense in 'NOTICE'; do
  echo %%doc "'${fontlicense}'" >> "google-droid-sans-mono-fonts2.list"
done
echo Installing google-droid-serif-fonts
echo "" > "google-droid-serif-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-droid/
echo "%%dir %_fontsdir/ttf/google-droid" >> "google-droid-serif-fonts3.list"
install -m 0644 -vp "DroidSerif-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSerif-Bold.ttf")\" >> 'google-droid-serif-fonts3.list'
install -m 0644 -vp "DroidSerif-BoldItalic.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSerif-BoldItalic.ttf")\" >> 'google-droid-serif-fonts3.list'
install -m 0644 -vp "DroidSerif-Italic.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSerif-Italic.ttf")\" >> 'google-droid-serif-fonts3.list'
install -m 0644 -vp "DroidSerif-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidSerif-Regular.ttf")\" >> 'google-droid-serif-fonts3.list'
install -m 0644 -vp "DroidNaskh-Bold.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidNaskh-Bold.ttf")\" >> 'google-droid-serif-fonts3.list'
install -m 0644 -vp "DroidNaskh-Regular.ttf" %buildroot%_fontsdir/ttf/google-droid/
echo \"%_fontsdir/ttf/google-droid//$(basename "DroidNaskh-Regular.ttf")\" >> 'google-droid-serif-fonts3.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE13'; do
      gen-fontconf -x "${fontconfng}" -w -f 'DroidSerif-Bold.ttf' 'DroidSerif-BoldItalic.ttf' 'DroidSerif-Italic.ttf' 'DroidSerif-Regular.ttf' 'DroidNaskh-Bold.ttf' 'DroidNaskh-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "google-droid-serif-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "google-droid-serif-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-droid-serif-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-droid-serif-fonts3.list"
done

for fontdoc in 'README.txt'; do
  echo %%doc "'${fontdoc}'" >> "google-droid-serif-fonts3.list"
done

for fontlicense in 'NOTICE'; do
  echo %%doc "'${fontlicense}'" >> "google-droid-serif-fonts3.list"
done

%check
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-droid-sans-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-droid-sans-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-droid-sans-mono-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-droid-sans-mono-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-droid-serif-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-droid-serif-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-google-droid-sans -f google-droid-sans-fonts1.list
%files -n fonts-ttf-google-droid-sans-mono -f google-droid-sans-mono-fonts2.list
%files -n fonts-ttf-google-droid-serif -f google-droid-serif-fonts3.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20200215-alt1_12
- update

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 20120715-alt3_12
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt3_8
- update to new release by fcimport

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt3_7
- added conflict to fonts-ttf-droid

* Fri Jun 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt2_7
- added obsoletes on fonts-ttf-droid

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_4
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 20120715-alt1_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_3
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 20100409-alt1_2
- initial release by fcimport

