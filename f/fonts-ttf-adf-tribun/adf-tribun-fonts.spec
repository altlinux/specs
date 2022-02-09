Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname adf-tribun-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname adf-tribun-fonts
# SPDX-License-Identifier: MIT
Version: 1.17
Release: alt1_5
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPLv2+ with exceptions
%global fontlicenses      OTF/COPYING
%global fontdocs          *.txt

%global fontfamily        Tribun
%global fontsummary       ADF Tribun, a newsprint-like serif font family
%global fonts             OTF/*.otf
%global fontdescription   \
Hirwen Harendal started in 1999 the realization of a first font family, aiming\
to create another a.'Times New Romana.'a.. He does not consider this endeavor a huge\
success. However, he transformed Tribun progressively since then to give it its\
own character.\
\
The idea was to achieve newsprint-like rendering. To this effect, the glyph\
bodies, serifs, or even extenders are not normalized and use irregular strokes.\
This is most visible in italics though those variations stay imperceptible at\
small sizes.\
\
Italics proved time-consuming. They are never an easy thing to draw.\
Nevertheless, the designer considers them very close to those of a.'Timesa.', with\
some variations.\
\
The medium weight uses a stronger stroke. It can be used for emphasis, or for\
effects in titles. That being said it has also been used for body copy. It is\
also slightly expanded to complete the face offerings.\
\
The condensed version is a bit unusual, since it stands in for both normal and\
medium condensed. After several trials, Hirwen decided an intermediate weight\
rendered much better both for document display and in print. Secondly, he took\
great care to keep readability excellent, and this even for italics.\
\
This font family is particularly well suited for text, display, or\
presentations. It is also ideal for all Web publications. It can serve as\
alternative to a.'Times New Romana.' and other similar fonts.

%global archivename Tribun-Std-20120228

Source0:  http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:  http://arkandis.tuxfamily.org/docs/Tribun-Cat.pdf
Source10: 60-adf-tribun-fonts.xml

Name:           fonts-ttf-adf-tribun
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%package   doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{oldname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{oldname}.

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE.txt OTF/COPYING

%build
# fontbuild 
fontnames=$(
  for font in 'OTF/TribunADFStd-Bold.otf' 'OTF/TribunADFStd-BoldCond.otf' 'OTF/TribunADFStd-BoldCondItalic.otf' 'OTF/TribunADFStd-BoldItalic.otf' 'OTF/TribunADFStd-Cond.otf' 'OTF/TribunADFStd-CondItalic.otf' 'OTF/TribunADFStd-ExtraBold.otf' 'OTF/TribunADFStd-ExtraBoldItalic.otf' 'OTF/TribunADFStd-Italic.otf' 'OTF/TribunADFStd-Medium.otf' 'OTF/TribunADFStd-MediumItalic.otf' 'OTF/TribunADFStd-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'OTF/TribunADFStd-Bold.otf' 'OTF/TribunADFStd-BoldCond.otf' 'OTF/TribunADFStd-BoldCondItalic.otf' 'OTF/TribunADFStd-BoldItalic.otf' 'OTF/TribunADFStd-Cond.otf' 'OTF/TribunADFStd-CondItalic.otf' 'OTF/TribunADFStd-ExtraBold.otf' 'OTF/TribunADFStd-ExtraBoldItalic.otf' 'OTF/TribunADFStd-Italic.otf' 'OTF/TribunADFStd-Medium.otf' 'OTF/TribunADFStd-MediumItalic.otf' 'OTF/TribunADFStd-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the adf-tribun-fonts appstream file"
cat > "org.altlinux.adf-tribun-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.adf-tribun-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>GPLv2+ with exceptions</project_license>
  <name>ADF Tribun</name>
  <summary><![CDATA[ADF Tribun, a newsprint-like serif font family]]></summary>
  <description>
    <p><![CDATA[Hirwen Harendal started in 1999 the realization of a first font family, aiming]]></p><p><![CDATA[to create another “Times New Roman”… He does not consider this endeavor a huge]]></p><p><![CDATA[success. However, he transformed Tribun progressively since then to give it its]]></p><p><![CDATA[own character.]]></p> The idea was to achieve newsprint-like rendering. To this effect, the glyph bodies, serifs, or even extenders are not normalized and use irregular strokes. This is most visible in italics though those variations stay imperceptible at small sizes. Italics proved time-consuming. They are never an easy thing to draw. Nevertheless, the designer considers them very close to those of “Times”, with some variations. The medium weight uses a stronger stroke. It can be used for emphasis, or for effects in titles. That being said it has also been used for body copy. It is also slightly expanded to complete the face offerings. The condensed version is a bit unusual, since it stands in for both normal and medium condensed. After several trials, Hirwen decided an intermediate weight rendered much better both for document display and in print. Secondly, he took great care to keep readability excellent, and this even for italics. This font family is particularly well suited for text, display, or presentations. It is also ideal for all Web publications. It can serve as alternative to “Times New Roman” and other similar fonts.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://arkandis.tuxfamily.org/adffonts.html</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing adf-tribun-fonts
echo "" > "adf-tribun-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/adf-tribun/
echo "%%dir %_fontsdir/otf/adf-tribun" >> "adf-tribun-fonts.list"
install -m 0644 -vp "OTF/TribunADFStd-Bold.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-Bold.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-BoldCond.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-BoldCond.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-BoldCondItalic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-BoldCondItalic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-BoldItalic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-BoldItalic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-Cond.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-Cond.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-CondItalic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-CondItalic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-ExtraBold.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-ExtraBold.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-ExtraBoldItalic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-Italic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-Italic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-Medium.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-Medium.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-MediumItalic.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-MediumItalic.otf")\" >> 'adf-tribun-fonts.list'
install -m 0644 -vp "OTF/TribunADFStd-Regular.otf" %buildroot%_fontsdir/otf/adf-tribun/
echo \"%_fontsdir/otf/adf-tribun//$(basename "OTF/TribunADFStd-Regular.otf")\" >> 'adf-tribun-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'OTF/TribunADFStd-Bold.otf' 'OTF/TribunADFStd-BoldCond.otf' 'OTF/TribunADFStd-BoldCondItalic.otf' 'OTF/TribunADFStd-BoldItalic.otf' 'OTF/TribunADFStd-Cond.otf' 'OTF/TribunADFStd-CondItalic.otf' 'OTF/TribunADFStd-ExtraBold.otf' 'OTF/TribunADFStd-ExtraBoldItalic.otf' 'OTF/TribunADFStd-Italic.otf' 'OTF/TribunADFStd-Medium.otf' 'OTF/TribunADFStd-MediumItalic.otf' 'OTF/TribunADFStd-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "adf-tribun-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "adf-tribun-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.adf-tribun-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "adf-tribun-fonts.list"
done

for fontdoc in 'NOTICE.txt'; do
  echo %%doc "'${fontdoc}'" >> "adf-tribun-fonts.list"
done

for fontlicense in 'OTF/COPYING'; do
  echo %%doc "'${fontlicense}'" >> "adf-tribun-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'adf-tribun-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'adf-tribun-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-adf-tribun -f adf-tribun-fonts.list

%files doc
%doc --no-dereference OTF/COPYING
%doc *.pdf

%changelog
* Wed Feb 09 2022 Igor Vlasenko <viy@altlinux.org> 1.17-alt1_5
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_13
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_9
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_4
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_3
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- initial release by fcimport

