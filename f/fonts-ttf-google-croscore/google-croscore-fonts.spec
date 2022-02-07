Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname google-croscore-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname google-croscore-fonts
BuildArch: noarch

Version:        1.31.0
Release:        alt1_12
License:        ASL 2.0
#URL:            

%global foundry           google
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE-2.0.txt

%global common_description \
This package contains a collections of fonts that offers improved on-screen\
readability characteristics and the pan-European WGL character set and solves\
the needs of developers looking for width-compatible fonts to address document\
portability across platforms.

%global fontsummary The width-compatible fonts for improved on-screen readability

%global archivename croscorefonts-%{version}

%global fontfamily1       Arimo
%global fontsummary1      The croscore Arimo family fonts
%global fontpkgheader1    \
Provides:  google-croscore-arimo-fonts = %{version}-%{release}\
Obsoletes: google-croscore-arimo-fonts < %{version}-%{release}\

%global fonts1            Arimo*.ttf
%global fontdescription1  \
%{common_description}\
\
Arimo was designed by Steve Matteson as an innovative, refreshing sans serif\
design that is metrically compatible with Arial. Arimo offers improved \
on-screen readability characteristics and the pan-European WGL character set \
and solves the needs of developers looking for width-compatible fonts to \
address document portability across platforms.

%global fontfamily2       Cousine
%global fontsummary2      The croscore Cousine family fonts
%global fontpkgheader2    \
Provides:  google-croscore-cousine-fonts = %{version}-%{release}\
Obsoletes: google-croscore-cousine-fonts < %{version}-%{release}\

%global fonts2            Cousine*.ttf
%global fontdescription2  \
%{common_description}\
\
Cousine was designed by Steve Matteson as an innovative, refreshing sans serif\
design that is metrically compatible with Courier New. Cousine offers improved\
on-screen readability characteristics and the pan-European WGL character set\
and solves the needs of developers looking for width-compatible fonts to \
address document portability across platforms.

%global fontfamily3       Tinos
%global fontsummary3      The croscore Tinos family fonts
%global fontpkgheader3    \
Provides:  google-croscore-tinos-fonts = %{version}-%{release}\
Obsoletes: google-croscore-tinos-fonts < %{version}-%{release}\

%global fonts3            Tinos*.ttf
%global fontdescription3  \
%{common_description}\
\
Tinos was designed by Steve Matteson as an innovative, refreshing serif design\
that is metrically compatible with Times New Roman. Tinos offers improved\
on-screen readability characteristics and the pan-European WGL character set\
and solves the needs of developers looking for width-compatible fonts to\
address document portability across platforms.


Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.bz2

Source1:        62-google-arimo-fonts.conf
Source2:        62-google-cousine-fonts.conf
Source3:        62-google-tinos-fonts.conf
Source4:        30-0-google-arimo-fonts.conf
Source5:        30-0-google-cousine-fonts.conf
Source6:        30-0-google-tinos-fonts.conf

# Upstream has not provided license text in their tarball release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

Name: fonts-ttf-google-croscore
Summary: The width-compatible fonts for improved on-screen readability
Source44: import.info

%description
%common_description

%package     -n fonts-ttf-google-croscore-arimo
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-google-croscore-arimo
%{?fontdescription1}
%package     -n fonts-ttf-google-croscore-cousine
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-google-croscore-cousine
%{?fontdescription2}
%package     -n fonts-ttf-google-croscore-tinos
Group: System/Fonts/True type
Summary:        %{fontsummary3}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader3}
%description -n fonts-ttf-google-croscore-tinos
%{?fontdescription3}

%prep
%global fontconfs1        %{SOURCE1} %{SOURCE4}
%global fontconfs2        %{SOURCE2} %{SOURCE5}
%global fontconfs3        %{SOURCE3} %{SOURCE6}
%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build
# fontbuild 1
fontnames=$(
  for font in 'Arimo-Bold.ttf' 'Arimo-BoldItalic.ttf' 'Arimo-Italic.ttf' 'Arimo-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Arimo-Bold.ttf' 'Arimo-BoldItalic.ttf' 'Arimo-Italic.ttf' 'Arimo-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-arimo-fonts appstream file"
cat > "org.altlinux.google-arimo-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-arimo-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>google Arimo</name>
  <summary><![CDATA[The croscore Arimo family fonts]]></summary>
  <description>
    <p><![CDATA[This package contains a collections of fonts that offers improved on-screen]]></p><p><![CDATA[readability characteristics and the pan-European WGL character set and solves]]></p><p><![CDATA[the needs of developers looking for width-compatible fonts to address document]]></p><p><![CDATA[portability across platforms.]]></p> Arimo was designed by Steve Matteson as an innovative, refreshing sans serif design that is metrically compatible with Arial. Arimo offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'Cousine-Bold.ttf' 'Cousine-BoldItalic.ttf' 'Cousine-Italic.ttf' 'Cousine-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Cousine-Bold.ttf' 'Cousine-BoldItalic.ttf' 'Cousine-Italic.ttf' 'Cousine-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-cousine-fonts appstream file"
cat > "org.altlinux.google-cousine-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-cousine-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>google Cousine</name>
  <summary><![CDATA[The croscore Cousine family fonts]]></summary>
  <description>
    <p><![CDATA[This package contains a collections of fonts that offers improved on-screen]]></p><p><![CDATA[readability characteristics and the pan-European WGL character set and solves]]></p><p><![CDATA[the needs of developers looking for width-compatible fonts to address document]]></p><p><![CDATA[portability across platforms.]]></p> Cousine was designed by Steve Matteson as an innovative, refreshing sans serif design that is metrically compatible with Courier New. Cousine offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 3
fontnames=$(
  for font in 'Tinos-Bold.ttf' 'Tinos-BoldItalic.ttf' 'Tinos-Italic.ttf' 'Tinos-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'Tinos-Bold.ttf' 'Tinos-BoldItalic.ttf' 'Tinos-Italic.ttf' 'Tinos-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the google-tinos-fonts appstream file"
cat > "org.altlinux.google-tinos-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.google-tinos-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>google Tinos</name>
  <summary><![CDATA[The croscore Tinos family fonts]]></summary>
  <description>
    <p><![CDATA[This package contains a collections of fonts that offers improved on-screen]]></p><p><![CDATA[readability characteristics and the pan-European WGL character set and solves]]></p><p><![CDATA[the needs of developers looking for width-compatible fonts to address document]]></p><p><![CDATA[portability across platforms.]]></p> Tinos was designed by Steve Matteson as an innovative, refreshing serif design that is metrically compatible with Times New Roman. Tinos offers improved on-screen readability characteristics and the pan-European WGL character set and solves the needs of developers looking for width-compatible fonts to
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo %{fontpkgname}
echo "Installing "google-arimo-fonts
echo "" > "google-arimo-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-croscore/
echo "%%dir %_fontsdir/ttf/google-croscore" >> "google-arimo-fonts1.list"
install -m 0644 -vp "Arimo-Bold.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Arimo-Bold.ttf")\" >> 'google-arimo-fonts1.list'
install -m 0644 -vp "Arimo-BoldItalic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Arimo-BoldItalic.ttf")\" >> 'google-arimo-fonts1.list'
install -m 0644 -vp "Arimo-Italic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Arimo-Italic.ttf")\" >> 'google-arimo-fonts1.list'
install -m 0644 -vp "Arimo-Regular.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Arimo-Regular.ttf")\" >> 'google-arimo-fonts1.list'

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-arimo-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-arimo-fonts1.list"
done

for fontlicense in 'LICENSE-2.0.txt'; do
  echo %%doc "'${fontlicense}'" >> "google-arimo-fonts1.list"
done
echo "Installing "google-cousine-fonts
echo "" > "google-cousine-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-croscore/
echo "%%dir %_fontsdir/ttf/google-croscore" >> "google-cousine-fonts2.list"
install -m 0644 -vp "Cousine-Bold.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Cousine-Bold.ttf")\" >> 'google-cousine-fonts2.list'
install -m 0644 -vp "Cousine-BoldItalic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Cousine-BoldItalic.ttf")\" >> 'google-cousine-fonts2.list'
install -m 0644 -vp "Cousine-Italic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Cousine-Italic.ttf")\" >> 'google-cousine-fonts2.list'
install -m 0644 -vp "Cousine-Regular.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Cousine-Regular.ttf")\" >> 'google-cousine-fonts2.list'

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-cousine-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-cousine-fonts2.list"
done

for fontlicense in 'LICENSE-2.0.txt'; do
  echo %%doc "'${fontlicense}'" >> "google-cousine-fonts2.list"
done
echo "Installing "google-tinos-fonts
echo "" > "google-tinos-fonts3.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/google-croscore/
echo "%%dir %_fontsdir/ttf/google-croscore" >> "google-tinos-fonts3.list"
install -m 0644 -vp "Tinos-Bold.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Tinos-Bold.ttf")\" >> 'google-tinos-fonts3.list'
install -m 0644 -vp "Tinos-BoldItalic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Tinos-BoldItalic.ttf")\" >> 'google-tinos-fonts3.list'
install -m 0644 -vp "Tinos-Italic.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Tinos-Italic.ttf")\" >> 'google-tinos-fonts3.list'
install -m 0644 -vp "Tinos-Regular.ttf" %buildroot%_fontsdir/ttf/google-croscore/
echo \"%_fontsdir/ttf/google-croscore//$(basename "Tinos-Regular.ttf")\" >> 'google-tinos-fonts3.list'

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.google-tinos-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "google-tinos-fonts3.list"
done

for fontlicense in 'LICENSE-2.0.txt'; do
  echo %%doc "'${fontlicense}'" >> "google-tinos-fonts3.list"
done

%check
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-arimo-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-arimo-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-cousine-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-cousine-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 3
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'google-tinos-fonts3.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'google-tinos-fonts3.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-google-croscore-arimo -f google-arimo-fonts1.list
%files -n fonts-ttf-google-croscore-cousine -f google-cousine-fonts2.list
%files -n fonts-ttf-google-croscore-tinos -f google-tinos-fonts3.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.31.0-alt1_12
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.31.0-alt1_2
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_2
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt2_1
- applied repocop patches

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.23.0-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.21.0-alt1_4
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.21.0-alt1_3
- fc import

