Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname sil-gentium-basic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname sil-gentium-basic-fonts
# SPDX-License-Identifier: MIT
Version: 1.102
Release: alt1_3
URL:     https://software.sil.org/gentium/

%global foundry           SIL
%global fontlicense       OFL
%global fontlicenses      OFL.txt

%global common_description \
Gentium Basic and Gentium Book Basic are font families based on the\
original Gentium design, but with additional weights. Both families come\
with a complete regular, bold, italic and bold italic set of fonts.\
These "Basic" fonts support only the Basic Latin and Latin-1 Supplement\
Unicode ranges, plus a selection of the more commonly used extended Latin\
characters, with miscellaneous diacritical marks, symbols and punctuation.\


%global fontfamily0       Gentium Basic
%global fontsummary0      SIL Gentium Basic font family
%global fontpkgheader0    \
Obsoletes: sil-gentium-basic-fonts-common < %{version}-%{release}\

%global fonts0            GenBas*
%global fontdescription0  \
%{common_description}\
\
This is the base variant.

%global fontfamily2       Gentium Basic Book
%global fontsummary2      SIL Gentium Book Basic font family
%global fonts2            GenBkBas*
%global fontdescription2  \
%global fontpkgname2       sil-gentium-basic-book-fonts\
%{common_description}\
\
The "Book" family is slightly heavier.


%global archivename GentiumBasic_1102

Source0:   https://software.sil.org/downloads/r/gentium/%{archivename}.zip
Source10:  59-sil-gentium-basic-fonts.conf
Source12:  59-sil-gentium-basic-book-fonts.conf


Name:           fonts-ttf-sil-gentium-basic
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-sil-gentium-basic-book
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-sil-gentium-basic-book
%{?fontdescription2}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-sil-gentium-basic = %EVR
Requires:  fonts-ttf-sil-gentium-basic-book = %EVR
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
%global fontconfs0        %{SOURCE10}
%global fontconfs2        %{SOURCE12}
%setup -q -n %{archivename}
%linuxtext *.txt

%build
# fontbuild 0
fontnames=$(
  for font in 'GenBasB.ttf' 'GenBasBI.ttf' 'GenBasI.ttf' 'GenBasR.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GenBasB.ttf' 'GenBasBI.ttf' 'GenBasI.ttf' 'GenBasR.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-gentium-basic-fonts appstream file"
cat > "org.altlinux.sil-gentium-basic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-gentium-basic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Gentium Basic</name>
  <summary><![CDATA[SIL Gentium Basic font family]]></summary>
  <description>
    <p><![CDATA[Gentium Basic and Gentium Book Basic are font families based on the]]></p><p><![CDATA[original Gentium design, but with additional weights. Both families come]]></p><p><![CDATA[with a complete regular, bold, italic and bold italic set of fonts.]]></p><p><![CDATA[These "Basic" fonts support only the Basic Latin and Latin-1 Supplement]]></p><p><![CDATA[Unicode ranges, plus a selection of the more commonly used extended Latin]]></p><p><![CDATA[characters, with miscellaneous diacritical marks, symbols and punctuation.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/gentium/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 2
fontnames=$(
  for font in 'GenBkBasB.ttf' 'GenBkBasBI.ttf' 'GenBkBasI.ttf' 'GenBkBasR.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GenBkBasB.ttf' 'GenBkBasBI.ttf' 'GenBkBasI.ttf' 'GenBkBasR.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the sil-gentium-basic-book-fonts appstream file"
cat > "org.altlinux.sil-gentium-basic-book-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.sil-gentium-basic-book-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>SIL Gentium Basic Book</name>
  <summary><![CDATA[SIL Gentium Book Basic font family]]></summary>
  <description>
     fontpkgname2       sil-gentium-basic-book-fonts<p><![CDATA[Gentium Basic and Gentium Book Basic are font families based on the]]></p><p><![CDATA[original Gentium design, but with additional weights. Both families come]]></p><p><![CDATA[with a complete regular, bold, italic and bold italic set of fonts.]]></p><p><![CDATA[These "Basic" fonts support only the Basic Latin and Latin-1 Supplement]]></p><p><![CDATA[Unicode ranges, plus a selection of the more commonly used extended Latin]]></p><p><![CDATA[characters, with miscellaneous diacritical marks, symbols and punctuation.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://software.sil.org/gentium/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "sil-gentium-basic-fonts
echo "" > "sil-gentium-basic-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo "%%dir %_fontsdir/ttf/sil-gentium-basic" >> "sil-gentium-basic-fonts0.list"
install -m 0644 -vp "GenBasB.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBasB.ttf")\" >> 'sil-gentium-basic-fonts0.list'
install -m 0644 -vp "GenBasBI.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBasBI.ttf")\" >> 'sil-gentium-basic-fonts0.list'
install -m 0644 -vp "GenBasI.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBasI.ttf")\" >> 'sil-gentium-basic-fonts0.list'
install -m 0644 -vp "GenBasR.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBasR.ttf")\" >> 'sil-gentium-basic-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-gentium-basic-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-gentium-basic-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-gentium-basic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-gentium-basic-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-gentium-basic-fonts0.list"
done
echo "Installing "sil-gentium-basic-book-fonts
echo "" > "sil-gentium-basic-book-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo "%%dir %_fontsdir/ttf/sil-gentium-basic" >> "sil-gentium-basic-book-fonts2.list"
install -m 0644 -vp "GenBkBasB.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBkBasB.ttf")\" >> 'sil-gentium-basic-book-fonts2.list'
install -m 0644 -vp "GenBkBasBI.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBkBasBI.ttf")\" >> 'sil-gentium-basic-book-fonts2.list'
install -m 0644 -vp "GenBkBasI.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBkBasI.ttf")\" >> 'sil-gentium-basic-book-fonts2.list'
install -m 0644 -vp "GenBkBasR.ttf" %buildroot%_fontsdir/ttf/sil-gentium-basic/
echo \"%_fontsdir/ttf/sil-gentium-basic//$(basename "GenBkBasR.ttf")\" >> 'sil-gentium-basic-book-fonts2.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE12' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "sil-gentium-basic-book-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "sil-gentium-basic-book-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.sil-gentium-basic-book-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "sil-gentium-basic-book-fonts2.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "sil-gentium-basic-book-fonts2.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-gentium-basic-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-gentium-basic-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'sil-gentium-basic-book-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'sil-gentium-basic-book-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-sil-gentium-basic -f sil-gentium-basic-fonts0.list
%files -n fonts-ttf-sil-gentium-basic-book -f sil-gentium-basic-book-fonts2.list

%files doc
%doc --no-dereference OFL.txt
%doc FONTLOG.txt GENTIUM-FAQ.txt OFL-FAQ.txt

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.102-alt1_3
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_16
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_12
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7
- rebuild to get rid of #27020

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_6
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- initial release by fcimport

