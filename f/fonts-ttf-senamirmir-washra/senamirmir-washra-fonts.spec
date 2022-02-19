Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname senamirmir-washra-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname senamirmir-washra-fonts
# SPDX-License-Identifier: MIT
%global archivename washra_fonts4-1

Version: 4.1
Release: alt3_32
URL:     http://www.senamirmir.org/projects/typography/typeface.html

%global foundry           Senamirmir
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description \
A set of high quality Unicode fonts for the  GeE.ez (Ethiopic) script published\
by the Senamirmir project. They can be used to write Ethiopic and Eritrean\
languages (Amharic, Blin, GeE.ez, Harari, MeE.en, Tigre, Tigrinyaa..).

%global fontsummary a font family for the GeE.ez (Ethiopic) script

%global fontfamily0       WashRa
%global fontsummary0      Senamirmir WashRa, %{fontsummary}
%global fontpkgheader0    \
Obsoletes: senamirmir-washra-fonts-common < %{version}-%{release}\

%global fonts0            washrab.ttf washrasb.ttf
%global fontdescription   %{common_description}

%global fontfamily1       Fantuwua
%global fontsummary1      Senamirmir Fantuwua, %{fontsummary}
%global fontpkgheader1    \
Obsoletes: senamirmir-washra-fantuwua-fonts < %{version}-%{release}\

%global fonts1            fantuwua.ttf
%global fontdescription1  \
%{common_description}\
This package consists of the a.'Ethiopic Fantuwuaa.' font family.

%global fontfamily2       Hiwua
%global fontsummary2      Senamirmir Hiwua, %{fontsummary}
%global fontpkgheader2    \
Obsoletes: senamirmir-washra-hiwua-fonts < %{version}-%{release}\

%global fonts2            hiwua.ttf
%global fontdescription2  \
%{common_description}\
This package consists of the a.'Ethiopic Hiwuaa.' font family.

%global fontfamily3       Jiret
%global fontsummary3      Senamirmir Jiret, %{fontsummary}
%global fontpkgheader3    \
Obsoletes: senamirmir-washra-jiret-fonts < %{version}-%{release}\

%global fonts3            jiret.ttf
%global fontdescription3  \
%{common_description}\
This package consists of the a.'Ethiopic Jireta.' font family.

%global fontfamily4       Tint
%global fontsummary4      Senamirmir Tint, %{fontsummary}
%global fontpkgheader4    \
Obsoletes: senamirmir-washra-tint-fonts < %{version}-%{release}\

%global fonts4            tint.ttf
%global fontdescription4  \
%{common_description}\
This package consists of the a.'Ethiopic Tinta.' font family.

%global fontfamily5       Wookianos
%global fontsummary5      Senamirmir Wookianos, %{fontsummary}
%global fontpkgheader5    \
Obsoletes: senamirmir-washra-wookianos-fonts < %{version}-%{release}\

%global fonts5            wookianos.ttf
%global fontdescription5  \
%{common_description}\
This package consists of the a.'Ethiopic Wookianosa.' font family.

%global fontfamily6       Yebse
%global fontsummary6      Senamirmir Yebse, %{fontsummary}
%global fontpkgheader6    \
Obsoletes: senamirmir-washra-yebse-fonts < %{version}-%{release}\

%global fonts6            yebse.ttf
%global fontdescription6  \
%{common_description}\
This package consists of the a.'Ethiopic Yebsea.' font family.

%global fontfamily7       Yigezu Bisrat Goffer
%global fontsummary7      Senamirmir Yigezu Bisrat Goffer, %{fontsummary}
%global fontpkgheader7    \
Obsoletes: senamirmir-washra-yigezu-bisrat-goffer-fonts < %{version}-%{release}\

%global fonts7            goffer.ttf
%global fontdescription7  \
%{common_description}\
This package consists of the a.'Ethiopic Yigezu Bisrat Goffera.' font, a a.'Gothic\
Goffera.' decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book\
a.'Ye-Ethiopia khine tsehifeta.' (Ethiopian Typography) provided the original\
design that served as inspiration for this work.

%global fontfamily8       Yigezu Bisrat Gothic
%global fontsummary8      Senamirmir Yigezu Bisrat Gothic, %{fontsummary}
%global fontpkgheader8    \
Obsoletes: senamirmir-washra-yigezu-bisrat-gothic-fonts < %{version}-%{release}\

%global fonts8            yigezubisratgothic.ttf
%global fontdescription8  \
%{common_description}\
This package consists of the a.'Ethiopic Yigezu Bisrat Gothica.' font, a a.'Gothica.'\
decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book\
a.'Ye-Ethiopia khine tsehifeta.' (Ethiopian Typography) provided inspiration for\
this work.

%global fontfamily9       Zelan
%global fontsummary9      Senamirmir Zelan, %{fontsummary}
%global fontpkgheader9    \
Obsoletes: senamirmir-washra-zelan-fonts < %{version}-%{release}\

%global fonts9            zelan.ttf
%global fontdescription9  \
%{common_description}\
This package consists of the a.'Ethiopic Zelana.' font.

Source0: http://www.senamirmir.org/downloads/%{archivename}.zip
# We need upstream or someone who knows local Ethiopian usage to suggest a
# classification we could relay to fontconfig. In the meanwhile, only three
# font families classified
Source10: 65-senamirmir-washra-fonts.xml
Source11: 65-senamirmir-fantuwua-fonts.xml
Source12: 65-senamirmir-hiwua-fonts.xml
Source13: 65-senamirmir-jiret-fonts.xml
Source14: 65-senamirmir-tint-fonts.xml
Source15: 65-senamirmir-wookianos-fonts.xml
Source16: 65-senamirmir-yebse-fonts.xml
Source17: 65-senamirmir-yigezu-bisrat-goffer-fonts.xml
Source18: 65-senamirmir-yigezu-bisrat-gothic-fonts.xml
Source19: 65-senamirmir-zelan-fonts.xml

Name:           fonts-ttf-senamirmir-washra
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription}
%package     -n fonts-ttf-senamirmir-washra-fantuwua
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-senamirmir-washra-fantuwua
%{?fontdescription1}
%package     -n fonts-ttf-senamirmir-washra-hiwua
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-senamirmir-washra-hiwua
%{?fontdescription2}
%package     -n fonts-ttf-senamirmir-washra-jiret
Group: System/Fonts/True type
Summary:        %{fontsummary3}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-ttf-senamirmir-washra-jiret
%{?fontdescription3}
%package     -n fonts-ttf-senamirmir-washra-tint
Group: System/Fonts/True type
Summary:        %{fontsummary4}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader4}
%description -n fonts-ttf-senamirmir-washra-tint
%{?fontdescription4}
%package     -n fonts-ttf-senamirmir-washra-wookianos
Group: System/Fonts/True type
Summary:        %{fontsummary5}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader5}
%description -n fonts-ttf-senamirmir-washra-wookianos
%{?fontdescription5}
%package     -n fonts-ttf-senamirmir-washra-yebse
Group: System/Fonts/True type
Summary:        %{fontsummary6}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader6}
%description -n fonts-ttf-senamirmir-washra-yebse
%{?fontdescription6}
%package     -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer
Group: System/Fonts/True type
Summary:        %{fontsummary7}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader7}
%description -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer
%{?fontdescription7}
%package     -n fonts-ttf-senamirmir-yigezu-bisrat-gothic
Group: System/Fonts/True type
Summary:        %{fontsummary8}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader8}
%description -n fonts-ttf-senamirmir-yigezu-bisrat-gothic
%{?fontdescription8}
%package     -n fonts-ttf-senamirmir-washra-zelan
Group: System/Fonts/True type
Summary:        %{fontsummary9}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader9}
%description -n fonts-ttf-senamirmir-washra-zelan
%{?fontdescription9}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-senamirmir-washra = %EVR
Requires:  fonts-ttf-senamirmir-washra-fantuwua = %EVR
Requires:  fonts-ttf-senamirmir-washra-hiwua = %EVR
Requires:  fonts-ttf-senamirmir-washra-jiret = %EVR
Requires:  fonts-ttf-senamirmir-washra-tint = %EVR
Requires:  fonts-ttf-senamirmir-washra-wookianos = %EVR
Requires:  fonts-ttf-senamirmir-washra-yebse = %EVR
Requires:  fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer = %EVR
Requires:  fonts-ttf-senamirmir-yigezu-bisrat-gothic = %EVR
Requires:  fonts-ttf-senamirmir-washra-zelan = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%package doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%global fontconfngs2      %{SOURCE12}
%global fontconfngs3      %{SOURCE13}
%global fontconfngs4      %{SOURCE14}
%global fontconfngs5      %{SOURCE15}
%global fontconfngs6      %{SOURCE16}
%global fontconfngs7      %{SOURCE17}
%global fontconfngs8      %{SOURCE18}
%global fontconfngs9      %{SOURCE19}
%setup -n %{oldname}-%{version} -c -q
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in 'washrab.ttf' 'washrasb.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'washrab.ttf' 'washrasb.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-washra-fonts appstream file"
cat > "org.altlinux.senamirmir-washra-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-washra-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir WashRa</name>
  <summary><![CDATA[a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'fantuwua.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fantuwua.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-fantuwua-fonts appstream file"
cat > "org.altlinux.senamirmir-fantuwua-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-fantuwua-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Fantuwua</name>
  <summary><![CDATA[Senamirmir Fantuwua, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Fantuwua” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'hiwua.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'hiwua.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-hiwua-fonts appstream file"
cat > "org.altlinux.senamirmir-hiwua-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-hiwua-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Hiwua</name>
  <summary><![CDATA[Senamirmir Hiwua, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Hiwua” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'jiret.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'jiret.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-jiret-fonts appstream file"
cat > "org.altlinux.senamirmir-jiret-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-jiret-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Jiret</name>
  <summary><![CDATA[Senamirmir Jiret, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Jiret” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 4
fontnames=$(
  for font in 'tint.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'tint.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-tint-fonts appstream file"
cat > "org.altlinux.senamirmir-tint-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-tint-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Tint</name>
  <summary><![CDATA[Senamirmir Tint, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Tint” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 5
fontnames=$(
  for font in 'wookianos.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'wookianos.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-wookianos-fonts appstream file"
cat > "org.altlinux.senamirmir-wookianos-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-wookianos-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Wookianos</name>
  <summary><![CDATA[Senamirmir Wookianos, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Wookianos” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 6
fontnames=$(
  for font in 'yebse.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'yebse.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-yebse-fonts appstream file"
cat > "org.altlinux.senamirmir-yebse-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-yebse-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Yebse</name>
  <summary><![CDATA[Senamirmir Yebse, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Yebse” font family.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 7
fontnames=$(
  for font in 'goffer.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'goffer.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-yigezu-bisrat-goffer-fonts appstream file"
cat > "org.altlinux.senamirmir-yigezu-bisrat-goffer-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-yigezu-bisrat-goffer-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Yigezu Bisrat Goffer</name>
  <summary><![CDATA[Senamirmir Yigezu Bisrat Goffer, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Yigezu Bisrat Goffer” font, a “Gothic Goffer” decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book “Ye-Ethiopia khine tsehifet” (Ethiopian Typography) provided the original design that served as inspiration for this work.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 8
fontnames=$(
  for font in 'yigezubisratgothic.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'yigezubisratgothic.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-yigezu-bisrat-gothic-fonts appstream file"
cat > "org.altlinux.senamirmir-yigezu-bisrat-gothic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-yigezu-bisrat-gothic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Yigezu Bisrat Gothic</name>
  <summary><![CDATA[Senamirmir Yigezu Bisrat Gothic, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Yigezu Bisrat Gothic” font, a “Gothic” decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book “Ye-Ethiopia khine tsehifet” (Ethiopian Typography) provided inspiration for this work.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 9
fontnames=$(
  for font in 'zelan.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'zelan.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the senamirmir-zelan-fonts appstream file"
cat > "org.altlinux.senamirmir-zelan-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.senamirmir-zelan-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Senamirmir Zelan</name>
  <summary><![CDATA[Senamirmir Zelan, a font family for the Geʼez (Ethiopic) script]]></summary>
  <description>
    <p><![CDATA[A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published]]></p><p><![CDATA[by the Senamirmir project. They can be used to write Ethiopic and Eritrean]]></p><p><![CDATA[languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).]]></p> This package consists of the “Ethiopic Zelan” font.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.senamirmir.org/projects/typography/typeface.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing senamirmir-washra-fonts
echo "" > "senamirmir-washra-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-washra-fonts0.list"
install -m 0644 -vp "washrab.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "washrab.ttf")\" >> 'senamirmir-washra-fonts0.list'
install -m 0644 -vp "washrasb.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "washrasb.ttf")\" >> 'senamirmir-washra-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'washrab.ttf' 'washrasb.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-washra-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-washra-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-washra-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-washra-fonts0.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-washra-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-washra-fonts0.list"
done
echo Installing senamirmir-fantuwua-fonts
echo "" > "senamirmir-fantuwua-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-fantuwua-fonts1.list"
install -m 0644 -vp "fantuwua.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "fantuwua.ttf")\" >> 'senamirmir-fantuwua-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fantuwua.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-fantuwua-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-fantuwua-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-fantuwua-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-fantuwua-fonts1.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-fantuwua-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-fantuwua-fonts1.list"
done
echo Installing senamirmir-hiwua-fonts
echo "" > "senamirmir-hiwua-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-hiwua-fonts2.list"
install -m 0644 -vp "hiwua.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "hiwua.ttf")\" >> 'senamirmir-hiwua-fonts2.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE12'; do
      gen-fontconf -x "${fontconfng}" -w -f 'hiwua.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-hiwua-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-hiwua-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-hiwua-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-hiwua-fonts2.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-hiwua-fonts2.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-hiwua-fonts2.list"
done
echo Installing senamirmir-jiret-fonts
echo "" > "senamirmir-jiret-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-jiret-fonts3.list"
install -m 0644 -vp "jiret.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "jiret.ttf")\" >> 'senamirmir-jiret-fonts3.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE13'; do
      gen-fontconf -x "${fontconfng}" -w -f 'jiret.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-jiret-fonts3.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-jiret-fonts3.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-jiret-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-jiret-fonts3.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-jiret-fonts3.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-jiret-fonts3.list"
done
echo Installing senamirmir-tint-fonts
echo "" > "senamirmir-tint-fonts4.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-tint-fonts4.list"
install -m 0644 -vp "tint.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "tint.ttf")\" >> 'senamirmir-tint-fonts4.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE14'; do
      gen-fontconf -x "${fontconfng}" -w -f 'tint.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-tint-fonts4.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-tint-fonts4.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-tint-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-tint-fonts4.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-tint-fonts4.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-tint-fonts4.list"
done
echo Installing senamirmir-wookianos-fonts
echo "" > "senamirmir-wookianos-fonts5.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-wookianos-fonts5.list"
install -m 0644 -vp "wookianos.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "wookianos.ttf")\" >> 'senamirmir-wookianos-fonts5.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE15'; do
      gen-fontconf -x "${fontconfng}" -w -f 'wookianos.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-wookianos-fonts5.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-wookianos-fonts5.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-wookianos-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-wookianos-fonts5.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-wookianos-fonts5.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-wookianos-fonts5.list"
done
echo Installing senamirmir-yebse-fonts
echo "" > "senamirmir-yebse-fonts6.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-yebse-fonts6.list"
install -m 0644 -vp "yebse.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "yebse.ttf")\" >> 'senamirmir-yebse-fonts6.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE16'; do
      gen-fontconf -x "${fontconfng}" -w -f 'yebse.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-yebse-fonts6.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-yebse-fonts6.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-yebse-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-yebse-fonts6.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-yebse-fonts6.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-yebse-fonts6.list"
done
echo Installing senamirmir-yigezu-bisrat-goffer-fonts
echo "" > "senamirmir-yigezu-bisrat-goffer-fonts7.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
install -m 0644 -vp "goffer.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "goffer.ttf")\" >> 'senamirmir-yigezu-bisrat-goffer-fonts7.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE17'; do
      gen-fontconf -x "${fontconfng}" -w -f 'goffer.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-yigezu-bisrat-goffer-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-yigezu-bisrat-goffer-fonts7.list"
done
echo Installing senamirmir-yigezu-bisrat-gothic-fonts
echo "" > "senamirmir-yigezu-bisrat-gothic-fonts8.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
install -m 0644 -vp "yigezubisratgothic.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "yigezubisratgothic.ttf")\" >> 'senamirmir-yigezu-bisrat-gothic-fonts8.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE18'; do
      gen-fontconf -x "${fontconfng}" -w -f 'yigezubisratgothic.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-yigezu-bisrat-gothic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-yigezu-bisrat-gothic-fonts8.list"
done
echo Installing senamirmir-zelan-fonts
echo "" > "senamirmir-zelan-fonts9.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/senamirmir-washra/
echo "%%dir %_fontsdir/ttf/senamirmir-washra" >> "senamirmir-zelan-fonts9.list"
install -m 0644 -vp "zelan.ttf" %buildroot%_fontsdir/ttf/senamirmir-washra/
echo \"%_fontsdir/ttf/senamirmir-washra//$(basename "zelan.ttf")\" >> 'senamirmir-zelan-fonts9.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE19'; do
      gen-fontconf -x "${fontconfng}" -w -f 'zelan.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "senamirmir-zelan-fonts9.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "senamirmir-zelan-fonts9.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.senamirmir-zelan-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "senamirmir-zelan-fonts9.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "senamirmir-zelan-fonts9.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "senamirmir-zelan-fonts9.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-washra-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-washra-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-fantuwua-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-fantuwua-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-hiwua-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-hiwua-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-jiret-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-jiret-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 4
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-tint-fonts4.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-tint-fonts4.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 5
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-wookianos-fonts5.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-wookianos-fonts5.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 6
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-yebse-fonts6.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-yebse-fonts6.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 7
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-yigezu-bisrat-goffer-fonts7.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-yigezu-bisrat-goffer-fonts7.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 8
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-yigezu-bisrat-gothic-fonts8.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-yigezu-bisrat-gothic-fonts8.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 9
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'senamirmir-zelan-fonts9.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'senamirmir-zelan-fonts9.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-senamirmir-washra -f senamirmir-washra-fonts0.list
%files -n fonts-ttf-senamirmir-washra-fantuwua -f senamirmir-fantuwua-fonts1.list
%files -n fonts-ttf-senamirmir-washra-hiwua -f senamirmir-hiwua-fonts2.list
%files -n fonts-ttf-senamirmir-washra-jiret -f senamirmir-jiret-fonts3.list
%files -n fonts-ttf-senamirmir-washra-tint -f senamirmir-tint-fonts4.list
%files -n fonts-ttf-senamirmir-washra-wookianos -f senamirmir-wookianos-fonts5.list
%files -n fonts-ttf-senamirmir-washra-yebse -f senamirmir-yebse-fonts6.list
%files -n fonts-ttf-senamirmir-washra-yigezu-bisrat-goffer -f senamirmir-yigezu-bisrat-goffer-fonts7.list
%files -n fonts-ttf-senamirmir-yigezu-bisrat-gothic -f senamirmir-yigezu-bisrat-gothic-fonts8.list
%files -n fonts-ttf-senamirmir-washra-zelan -f senamirmir-zelan-fonts9.list

%files doc
%doc --no-dereference OFL.txt
%doc *.doc *.pdf

%changelog
* Sat Feb 19 2022 Igor Vlasenko <viy@altlinux.org> 4.1-alt3_32
- new version

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_16
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt3_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_6
- initial release by fcimport

