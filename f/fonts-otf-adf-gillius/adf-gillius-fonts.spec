Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname adf-gillius-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname adf-gillius-fonts
# SPDX-License-Identifier: MIT
Version: 1.009
Release: alt1_3
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPLv2+ with exceptions
%global fontlicenses      OTF/COPYING
%global fontdocs          NOTICE

%global common_description \
The Gillius family from the Arkandis Digital Foundry is a set of sans-serif\
typefaces intended as an alternative to Gill Sans. Its two widths, regular and\
condensed, both feature a roman and an italic, and each includes a regular and\
bold weight.\


%global fontfamily0       Gillius
%global fontsummary0      ADF Gillius sans-serif typeface family, a GillSans alternative
%global fontpkgheader0    \
Obsoletes: adf-gillius-fonts-common < %{version}-%{release}\

%global fonts0            OTF/GilliusADF-*
%global fontdescription0  \
%{common_description}\
\
This is the base variant.

%global fontfamily2       Gillius-2
%global fontsummary2      ADF Gillius No2 sans-serif typeface family. a GillSans alternative
%global fonts2            OTF/GilliusADFNo2-*
%global fontdescription2  \
%{common_description}\
\
A slightly rounder variant, which features the same set of weights,\
widths, and slopes.


%global archivename Gillius-Collection-20110312

Source0:   http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:   http://arkandis.tuxfamily.org/docs/%{fontfamily0}-cat.pdf
Source10:  69-adf-gillius-fonts.conf
Source12:  69-adf-gillius-2-fonts.conf



Name:           fonts-otf-adf-gillius
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-adf-gillius-2
Group: System/Fonts/True type
Summary:        %{fontsummary2}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader2}
%description -n fonts-ttf-adf-gillius-2
%{?fontdescription2}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-otf-adf-gillius = %EVR
Requires:  fonts-ttf-adf-gillius-2 = %EVR
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
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE OTF/COPYING

%build
# fontbuild 0
fontnames=$(
  for font in 'OTF/GilliusADF-Bold.otf' 'OTF/GilliusADF-BoldCond.otf' 'OTF/GilliusADF-BoldCondItalic.otf' 'OTF/GilliusADF-BoldItalic.otf' 'OTF/GilliusADF-Cond.otf' 'OTF/GilliusADF-CondItalic.otf' 'OTF/GilliusADF-Italic.otf' 'OTF/GilliusADF-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/GilliusADF-Bold.otf' 'OTF/GilliusADF-BoldCond.otf' 'OTF/GilliusADF-BoldCondItalic.otf' 'OTF/GilliusADF-BoldItalic.otf' 'OTF/GilliusADF-Cond.otf' 'OTF/GilliusADF-CondItalic.otf' 'OTF/GilliusADF-Italic.otf' 'OTF/GilliusADF-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-gillius-fonts appstream file"
cat > "org.altlinux.adf-gillius-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-gillius-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Gillius</name>
  <summary><![CDATA[ADF Gillius sans-serif typeface family, a GillSans alternative]]></summary>
  <description>
    <p><![CDATA[The Gillius family from the Arkandis Digital Foundry is a set of sans-serif]]></p><p><![CDATA[typefaces intended as an alternative to Gill Sans. Its two widths, regular and]]></p><p><![CDATA[condensed, both feature a roman and an italic, and each includes a regular and]]></p><p><![CDATA[bold weight.]]></p>
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
  for font in 'OTF/GilliusADFNo2-Bold.otf' 'OTF/GilliusADFNo2-BoldCond.otf' 'OTF/GilliusADFNo2-BoldCondItalic.otf' 'OTF/GilliusADFNo2-BoldItalic.otf' 'OTF/GilliusADFNo2-Cond.otf' 'OTF/GilliusADFNo2-CondItalic.otf' 'OTF/GilliusADFNo2-Italic.otf' 'OTF/GilliusADFNo2-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/GilliusADFNo2-Bold.otf' 'OTF/GilliusADFNo2-BoldCond.otf' 'OTF/GilliusADFNo2-BoldCondItalic.otf' 'OTF/GilliusADFNo2-BoldItalic.otf' 'OTF/GilliusADFNo2-Cond.otf' 'OTF/GilliusADFNo2-CondItalic.otf' 'OTF/GilliusADFNo2-Italic.otf' 'OTF/GilliusADFNo2-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-gillius-2-fonts appstream file"
cat > "org.altlinux.adf-gillius-2-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-gillius-2-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Gillius-2</name>
  <summary><![CDATA[ADF Gillius No2 sans-serif typeface family. a GillSans alternative]]></summary>
  <description>
    <p><![CDATA[The Gillius family from the Arkandis Digital Foundry is a set of sans-serif]]></p><p><![CDATA[typefaces intended as an alternative to Gill Sans. Its two widths, regular and]]></p><p><![CDATA[condensed, both feature a roman and an italic, and each includes a regular and]]></p><p><![CDATA[bold weight.]]></p> A slightly rounder variant, which features the same set of weights,
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://arkandis.tuxfamily.org/adffonts.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "adf-gillius-fonts
echo "" > "adf-gillius-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-gillius/
echo "%%dir %_fontsdir/otf/adf-gillius" >> "adf-gillius-fonts0.list"
install -m 0644 -vp "OTF/GilliusADF-Bold.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-Bold.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-BoldCond.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-BoldCond.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-BoldCondItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-BoldCondItalic.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-BoldItalic.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-Cond.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-Cond.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-CondItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-CondItalic.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-Italic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-Italic.otf")\" >> 'adf-gillius-fonts0.list'
install -m 0644 -vp "OTF/GilliusADF-Regular.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADF-Regular.otf")\" >> 'adf-gillius-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-gillius-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-gillius-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-gillius-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-gillius-fonts0.list"
done

for fontdoc in 'NOTICE'; do
  echo %%doc "'${fontdoc}'" >> "adf-gillius-fonts0.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-gillius-fonts0.list"
done
echo "Installing "adf-gillius-2-fonts
echo "" > "adf-gillius-2-fonts2.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-gillius/
echo "%%dir %_fontsdir/otf/adf-gillius" >> "adf-gillius-2-fonts2.list"
install -m 0644 -vp "OTF/GilliusADFNo2-Bold.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-Bold.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-BoldCond.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-BoldCond.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-BoldCondItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-BoldCondItalic.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-BoldItalic.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-Cond.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-Cond.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-CondItalic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-CondItalic.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-Italic.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-Italic.otf")\" >> 'adf-gillius-2-fonts2.list'
install -m 0644 -vp "OTF/GilliusADFNo2-Regular.otf" %buildroot%_fontsdir/otf/adf-gillius/
echo \"%_fontsdir/otf/adf-gillius//$(basename "OTF/GilliusADFNo2-Regular.otf")\" >> 'adf-gillius-2-fonts2.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE12' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-gillius-2-fonts2.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-gillius-2-fonts2.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-gillius-2-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-gillius-2-fonts2.list"
done

for fontdoc in 'NOTICE'; do
  echo %%doc "'${fontdoc}'" >> "adf-gillius-2-fonts2.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-gillius-2-fonts2.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-gillius-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-gillius-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 2
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-gillius-2-fonts2.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-gillius-2-fonts2.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-adf-gillius -f adf-gillius-fonts0.list
%files -n fonts-ttf-adf-gillius-2 -f adf-gillius-2-fonts2.list

%files doc
%doc --no-dereference OTF/COPYING
%doc *.pdf 


%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.009-alt1_3
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_11
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_10
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_6
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.008-alt3_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.008-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.008-alt2_4
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.008-alt1_4
- initial release by fcimport

