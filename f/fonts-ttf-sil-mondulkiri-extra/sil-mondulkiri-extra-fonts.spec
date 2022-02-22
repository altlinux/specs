Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-mondulkiri-extra-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-mondulkiri-extra-fonts
# SPDX-License-Identifier: MIT
BuildArch: noarch

Version: 5.300
Release: alt1_6
License: OFL
URL:     https://scripts.sil.org/Mondulkiri

%global foundry           SIL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description  The Mondulkiri font families provide\
Unicode support for the Khmer script. a.'Mondulkiria.' and a.'Ratanakiria.' are the\
names of two provinces in north-eastern Cambodia, Busra and Oureang are names\
of places in Mondulkiri province.

%global fontfamily1       Ratanakiri
%global fontsummary1      Khmer Ratanakiri, a Khmer Mool title font family
%global fonts1            RataV53.ttf
%global fontdescription1  \
%{common_description}\
\
Khmer Ratanakiri is a Mool (or Muol or Muul) font family which is frequently\
used for headings and signs. At this point of time most ligatures have not yet\
been implemented. Some coengs of independent vowels and other features used\
only infrequently in normal Khmer text are currently still implemented in a\
different character style. This font does not support more than one\
belowa..coeng, i.e. words like a..a..a..a..a..a.'a..a.. cannot be written in it.

%global fontfamily2       Oureang
%global fontsummary2      Khmer Oureang, a very bold Khmer title font family
%global fontpkgheader2    \
#Suggests: font(khmermondulkiri)\

%global fonts2            Mo9V55.ttf
%global fontdescription2  \
%{common_description}\
\
Khmer Oureang is a very bold Khmer script font family, useful for headings. It\
was formerly named a.'Khmer Mondulkiri ultraa.'.

%global fontfamily3       Busra MOE
%global fontsummary3      Khmer Busra MOE, a special Khmer Busra variant
%global fontpkgheader3    \
#Suggests: font(khmerbusra)\

%global fonts3            Mo5V56MO.ttf
%global fontdescription3  \
%{common_description}\
\
Khmer Busra MOE drops a belowa..vowel in a cluster containing a coenga..Ro.

%global fontfamily4       Busra dict
%global fontsummary4      Khmer Busra dict, a special Khmer Busra variant
%global fontpkgheader4    \
#Suggests: font(khmerbusra)\

%global fonts4            Mo5V56dc.ttf
%global fontdescription4  \
%{common_description}\
\
Khmer Busra dict has alternative shapes for four of the Khmer letters as they\
are found in some dictionaries.

%global fontfamily5       Busra high
%global fontsummary5      Khmer Busra high, a special Khmer Busra variant
%global fontpkgheader5    \
#Suggests: font(khmerbusra)\

%global fonts5            Mo5V56hi.ttf
%global fontdescription5  \
%{common_description}\
\
Khmer Busra high has a higher line height in order to accommodate some rare\
Khmer words on screen.

%global fontfamily6       Busra Bunong
%global fontsummary6      Khmer Busra Bunong, a special Khmer Busra variant
%global fontpkgheader6    \
#Suggests: font(khmerbusra)\

%global fonts6            Mo5V56Bu.ttf
%global fontdescription6  \
%{common_description}\
\
Khmer Busra Bunong has a lower line height. Some coengs or vowels under coengs\
may not display on screen or touch the top character of the next line. If any\
parts are clipped on the screen they should, however, be visible in print. It\
will provide more lines of text on a given page.

%global fontfamily7       Busra xspace
%global fontsummary7      Khmer Busra xspace, a special Khmer Busra variant
%global fontpkgheader7    \
#Suggests: font(khmerbusra)\

%global fonts7            Mo5V56xs.ttf
%global fontdescription7 \
%{common_description}\
\
Khmer Busra xspace makes a number of otherwise invisible or not easily visible\
characters visible. However, many word processors and editors take charge of\
some or all of these characters and do not display them in the way they are\
provided in the font.

%global fontfamily8       Busra diagnostic
%global fontsummary8      Khmer Busra diagnostic, a special Khmer Busra variant
%global fontpkgheader8    \
#Suggests: font(khmerbusra)\

%global fonts8            Mo5V56di.ttf
%global fontdescription8  \
%{common_description}\
\
Khmer Busra diagnostic does the same as Khmer Busra xspace, but also adds\
dotted circles before coengs if they follow a vowel as well as in between\
multiple abovea..symbols. Both of these character sequences are permitted in\
Windows, but the former is often a missa..spelling and the latter is also usually\
unintended and a missa..spelling as well as not being permitted in other\
operating systems. In this way the font helps to spot common typos.

%global fontfamily9       Busra dot
%global fontsummary9      Khmer Busra dot, a special Khmer Busra variant
%global fontpkgheader9    \
#Suggests: font(khmerbusra)\

%global fonts9            Mo5V56do.ttf
%global fontdescription9 \
%{common_description}\
\
This font does something that a Unicode font should not do and that is it does\
not show the a.'correcta.' symbol for one particular Unicode code-point. It shows a\
dotted circle in the place where a a.. should be shown. It may be used for\
didactic purposes.

%global archivename Mondulkiri-%{version}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}&filename=%{archivename}.zip#/%{archivename}.zip
Source11: 66-sil-ratanakiri-fonts.xml
Source12: 66-sil-oureang-fonts.xml
Source13: 66-sil-busra-moe-fonts.xml
Source14: 66-sil-busra-dict-fonts.xml
Source15: 66-sil-busra-high-fonts.xml
Source16: 66-sil-busra-bunong-fonts.xml
Source17: 66-sil-busra-xspace-fonts.xml
Source18: 66-sil-busra-diagnostic-fonts.xml
Source19: 66-sil-busra-dot-fonts.xml

Name:     fonts-ttf-sil-mondulkiri-extra
Summary:  Extra Khmer script font families from the SIL Mondulkiri project
Source44: import.info
%description
%common_description

%package     -n fonts-ttf-sil-ratanakiri
Group: System/Fonts/True type
Summary:        %{fontsummary1}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-sil-ratanakiri
%{?fontdescription1}
%package     -n fonts-ttf-sil-oureang
Group: System/Fonts/True type
Summary:        %{fontsummary2}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-sil-oureang
%{?fontdescription2}
%package     -n fonts-ttf-sil-busra-moe
Group: System/Fonts/True type
Summary:        %{fontsummary3}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-ttf-sil-busra-moe
%{?fontdescription3}
%package     -n fonts-ttf-sil-busra-dict
Group: System/Fonts/True type
Summary:        %{fontsummary4}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader4}
%description -n fonts-ttf-sil-busra-dict
%{?fontdescription4}
%package     -n fonts-ttf-sil-busra-high
Group: System/Fonts/True type
Summary:        %{fontsummary5}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader5}
%description -n fonts-ttf-sil-busra-high
%{?fontdescription5}
%package     -n fonts-ttf-sil-busra-bunong
Group: System/Fonts/True type
Summary:        %{fontsummary6}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader6}
%description -n fonts-ttf-sil-busra-bunong
%{?fontdescription6}
%package     -n fonts-ttf-sil-busra-xspace
Group: System/Fonts/True type
Summary:        %{fontsummary7}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader7}
%description -n fonts-ttf-sil-busra-xspace
%{?fontdescription7}
%package     -n sil-busra-diagnostic
Group: System/Fonts/True type
Summary:        %{fontsummary8}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader8}
%description -n sil-busra-diagnostic
%{?fontdescription8}
%package     -n fonts-ttf-sil-busra-dot
Group: System/Fonts/True type
Summary:        %{fontsummary9}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader9}
%description -n fonts-ttf-sil-busra-dot
%{?fontdescription9}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-sil-ratanakiri = %EVR
Requires:  fonts-ttf-sil-oureang = %EVR
Requires:  fonts-ttf-sil-busra-moe = %EVR
Requires:  fonts-ttf-sil-busra-dict = %EVR
Requires:  fonts-ttf-sil-busra-high = %EVR
Requires:  fonts-ttf-sil-busra-bunong = %EVR
Requires:  fonts-ttf-sil-busra-xspace = %EVR
Requires:  sil-busra-diagnostic = %EVR
Requires:  fonts-ttf-sil-busra-dot = %EVR
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
%global fontconfngs1      %{SOURCE11}
%global fontconfngs2      %{SOURCE12}
%global fontconfngs3      %{SOURCE13}
%global fontconfngs4      %{SOURCE14}
%global fontconfngs5      %{SOURCE15}
%global fontconfngs6      %{SOURCE16}
%global fontconfngs7      %{SOURCE17}
%global fontconfngs8      %{SOURCE18}
%global fontconfngs9      %{SOURCE19}
%setup -q -n %{archivename}
%linuxtext *.txt

%build
# fontbuild 1
fontnames=$(
  for font in 'RataV53.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'RataV53.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-ratanakiri-fonts appstream file"
cat > "org.altlinux.sil-ratanakiri-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-ratanakiri-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Ratanakiri</name>
  <summary><![CDATA[Khmer Ratanakiri, a Khmer Mool title font family]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Ratanakiri is a Mool (or Muol or Muul) font family which is frequently used for headings and signs. At this point of time most ligatures have not yet been implemented. Some coengs of independent vowels and other features used only infrequently in normal Khmer text are currently still implemented in a different character style. This font does not support more than one below‐coeng, i.e. words like លក្ស្មណៈ cannot be written in it.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'Mo9V55.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo9V55.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-oureang-fonts appstream file"
cat > "org.altlinux.sil-oureang-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-oureang-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Oureang</name>
  <summary><![CDATA[Khmer Oureang, a very bold Khmer title font family]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Oureang is a very bold Khmer script font family, useful for headings. It was formerly named “Khmer Mondulkiri ultra”.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'Mo5V56MO.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56MO.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-moe-fonts appstream file"
cat > "org.altlinux.sil-busra-moe-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-moe-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra MOE</name>
  <summary><![CDATA[Khmer Busra MOE, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra MOE drops a below‐vowel in a cluster containing a coeng‐Ro.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 4
fontnames=$(
  for font in 'Mo5V56dc.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56dc.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-dict-fonts appstream file"
cat > "org.altlinux.sil-busra-dict-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-dict-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra dict</name>
  <summary><![CDATA[Khmer Busra dict, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra dict has alternative shapes for four of the Khmer letters as they are found in some dictionaries.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 5
fontnames=$(
  for font in 'Mo5V56hi.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56hi.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-high-fonts appstream file"
cat > "org.altlinux.sil-busra-high-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-high-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra high</name>
  <summary><![CDATA[Khmer Busra high, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra high has a higher line height in order to accommodate some rare Khmer words on screen.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 6
fontnames=$(
  for font in 'Mo5V56Bu.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56Bu.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-bunong-fonts appstream file"
cat > "org.altlinux.sil-busra-bunong-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-bunong-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra Bunong</name>
  <summary><![CDATA[Khmer Busra Bunong, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra Bunong has a lower line height. Some coengs or vowels under coengs may not display on screen or touch the top character of the next line. If any parts are clipped on the screen they should, however, be visible in print. It will provide more lines of text on a given page.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 7
fontnames=$(
  for font in 'Mo5V56xs.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56xs.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-xspace-fonts appstream file"
cat > "org.altlinux.sil-busra-xspace-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-xspace-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra xspace</name>
  <summary><![CDATA[Khmer Busra xspace, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra xspace makes a number of otherwise invisible or not easily visible characters visible. However, many word processors and editors take charge of some or all of these characters and do not display them in the way they are provided in the font.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 8
fontnames=$(
  for font in 'Mo5V56di.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56di.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-diagnostic-fonts appstream file"
cat > "org.altlinux.sil-busra-diagnostic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-diagnostic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra diagnostic</name>
  <summary><![CDATA[Khmer Busra diagnostic, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> Khmer Busra diagnostic does the same as Khmer Busra xspace, but also adds dotted circles before coengs if they follow a vowel as well as in between multiple above‐symbols. Both of these character sequences are permitted in Windows, but the former is often a miss‐spelling and the latter is also usually unintended and a miss‐spelling as well as not being permitted in other operating systems. In this way the font helps to spot common typos.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 9
fontnames=$(
  for font in 'Mo5V56do.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Mo5V56do.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-busra-dot-fonts appstream file"
cat > "org.altlinux.sil-busra-dot-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-busra-dot-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Busra dot</name>
  <summary><![CDATA[Khmer Busra dot, a special Khmer Busra variant]]></summary>
  <description>
    <p><![CDATA[The Mondulkiri font families provideUnicode support for the Khmer script. “Mondulkiri” and “Ratanakiri” are the]]></p><p><![CDATA[names of two provinces in north-eastern Cambodia, Busra and Oureang are names]]></p><p><![CDATA[of places in Mondulkiri province.]]></p> This font does something that a Unicode font should not do and that is it does not show the “correct” symbol for one particular Unicode code-point. It shows a dotted circle in the place where a ក should be shown. It may be used for didactic purposes.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://scripts.sil.org/Mondulkiri</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing sil-ratanakiri-fonts
echo "" > "sil-ratanakiri-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-ratanakiri-fonts1.list"
install -m 0644 -vp "RataV53.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "RataV53.ttf")\" >> 'sil-ratanakiri-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'RataV53.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-ratanakiri-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-ratanakiri-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-ratanakiri-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-ratanakiri-fonts1.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-ratanakiri-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-ratanakiri-fonts1.list"
done
echo Installing sil-oureang-fonts
echo "" > "sil-oureang-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-oureang-fonts2.list"
install -m 0644 -vp "Mo9V55.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo9V55.ttf")\" >> 'sil-oureang-fonts2.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE12'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo9V55.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-oureang-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-oureang-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-oureang-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-oureang-fonts2.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-oureang-fonts2.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-oureang-fonts2.list"
done
echo Installing sil-busra-moe-fonts
echo "" > "sil-busra-moe-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-moe-fonts3.list"
install -m 0644 -vp "Mo5V56MO.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56MO.ttf")\" >> 'sil-busra-moe-fonts3.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE13'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56MO.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-moe-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-moe-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-moe-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-moe-fonts3.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-moe-fonts3.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-moe-fonts3.list"
done
echo Installing sil-busra-dict-fonts
echo "" > "sil-busra-dict-fonts4.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-dict-fonts4.list"
install -m 0644 -vp "Mo5V56dc.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56dc.ttf")\" >> 'sil-busra-dict-fonts4.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE14'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56dc.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-dict-fonts4.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-dict-fonts4.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-dict-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-dict-fonts4.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-dict-fonts4.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-dict-fonts4.list"
done
echo Installing sil-busra-high-fonts
echo "" > "sil-busra-high-fonts5.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-high-fonts5.list"
install -m 0644 -vp "Mo5V56hi.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56hi.ttf")\" >> 'sil-busra-high-fonts5.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE15'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56hi.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-high-fonts5.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-high-fonts5.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-high-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-high-fonts5.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-high-fonts5.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-high-fonts5.list"
done
echo Installing sil-busra-bunong-fonts
echo "" > "sil-busra-bunong-fonts6.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-bunong-fonts6.list"
install -m 0644 -vp "Mo5V56Bu.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56Bu.ttf")\" >> 'sil-busra-bunong-fonts6.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE16'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56Bu.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-bunong-fonts6.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-bunong-fonts6.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-bunong-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-bunong-fonts6.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-bunong-fonts6.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-bunong-fonts6.list"
done
echo Installing sil-busra-xspace-fonts
echo "" > "sil-busra-xspace-fonts7.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-xspace-fonts7.list"
install -m 0644 -vp "Mo5V56xs.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56xs.ttf")\" >> 'sil-busra-xspace-fonts7.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE17'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56xs.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-xspace-fonts7.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-xspace-fonts7.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-xspace-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-xspace-fonts7.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-xspace-fonts7.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-xspace-fonts7.list"
done
echo Installing sil-busra-diagnostic-fonts
echo "" > "sil-busra-diagnostic-fonts8.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-diagnostic-fonts8.list"
install -m 0644 -vp "Mo5V56di.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56di.ttf")\" >> 'sil-busra-diagnostic-fonts8.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE18'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56di.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-diagnostic-fonts8.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-diagnostic-fonts8.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-diagnostic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-diagnostic-fonts8.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-diagnostic-fonts8.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-diagnostic-fonts8.list"
done
echo Installing sil-busra-dot-fonts
echo "" > "sil-busra-dot-fonts9.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo "%%dir %_fontsdir/ttf/sil-mondulkiri-extra" >> "sil-busra-dot-fonts9.list"
install -m 0644 -vp "Mo5V56do.ttf" %buildroot%_fontsdir/ttf/sil-mondulkiri-extra/
echo \"%_fontsdir/ttf/sil-mondulkiri-extra//$(basename "Mo5V56do.ttf")\" >> 'sil-busra-dot-fonts9.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE19'; do
      gen-fontconf -x "${fontconfng}" -w -f 'Mo5V56do.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-busra-dot-fonts9.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-busra-dot-fonts9.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-busra-dot-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-busra-dot-fonts9.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "sil-busra-dot-fonts9.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-busra-dot-fonts9.list"
done

%check
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-ratanakiri-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-ratanakiri-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-oureang-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-oureang-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-moe-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-moe-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 4
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-dict-fonts4.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-dict-fonts4.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 5
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-high-fonts5.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-high-fonts5.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 6
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-bunong-fonts6.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-bunong-fonts6.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 7
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-xspace-fonts7.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-xspace-fonts7.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 8
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-diagnostic-fonts8.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-diagnostic-fonts8.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 9
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-busra-dot-fonts9.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-busra-dot-fonts9.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-ratanakiri -f sil-ratanakiri-fonts1.list
%files -n fonts-ttf-sil-oureang -f sil-oureang-fonts2.list
%files -n fonts-ttf-sil-busra-moe -f sil-busra-moe-fonts3.list
%files -n fonts-ttf-sil-busra-dict -f sil-busra-dict-fonts4.list
%files -n fonts-ttf-sil-busra-high -f sil-busra-high-fonts5.list
%files -n fonts-ttf-sil-busra-bunong -f sil-busra-bunong-fonts6.list
%files -n fonts-ttf-sil-busra-xspace -f sil-busra-xspace-fonts7.list
%files -n sil-busra-diagnostic -f sil-busra-diagnostic-fonts8.list
%files -n fonts-ttf-sil-busra-dot -f sil-busra-dot-fonts9.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*.pdf

%changelog
* Tue Feb 22 2022 Igor Vlasenko <viy@altlinux.org> 5.300-alt1_6
- new version

