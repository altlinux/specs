Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-complutum-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-complutum-fonts
# SPDX-License-Identifier: MIT
Version: 20070413
Release: alt3_34
URL:     http://www.greekfontsociety-gfs.gr/typefaces/16th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Complutum
%global fontsummary       GFS Complutum, a 16th century Greek font family
%global fonts             *.otf
%global fontdescription   \
The ancient Greek alphabet evolved during the millennium of the Byzantine era\
from majuscule to minuscule form and gradually incorporated a wide array of\
ligatures, flourishes and other decorative nuances which defined its\
extravagant cursive character. Until the late 15th century, typographers who\
had to deal with Greek text avoided emulating this complicated hand; instead\
they would use only the twenty four letters of the alphabet separately, often\
without accents and other diacritics.\
\
A celebrated example is the type cut and cast for the typesetting of the New\
Testament in the so-called Complutensian Polyglot Bible (1512), edited by the\
Greek scholar, Demetrios Doukas. The type was cut by Arnaldo GuillA.n de Brocar\
and the whole edition was a commission by cardinal Francisco XimA.nez, in the\
University of AlcalA. (Complutum), Spain. It is one of the best and most\
representative models of this early tradition in Greek typography which was\
revived in the early 20th century by the eminent bibliographer of the British\
Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book\
was printed using the new type. The original type had no capitals so Proctor\
added his own, which were rather large and ill-fitted. The early death of\
Proctor, the big size of the font and the different aesthetic notions of the\
time were the reasons that Otter Greek was destined to oblivion, as a\
curiosity.\
\
Greek Font Society incorporated Brocara.'s famous and distinctive type in the\
commemorative edition of Pindara.'s Odes for the Athens Olympics (2004) and the\
type with a new set of capitals, revived digitally by George D. Matthiopoulos,\
is now available for general use.

%global archivename GFS_Complutum

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-complutum
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-complutum
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
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build

fontnames=$(
  for font in 'GFSPolyglot.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSPolyglot.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-complutum-fonts appstream file"
cat > "org.altlinux.gfs-complutum-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-complutum-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSComplutum</name>
  <summary><![CDATA[GFS Complutum, a 16th century Greek font family]]></summary>
  <description>
    <p><![CDATA[The ancient Greek alphabet evolved during the millennium of the Byzantine era]]></p><p><![CDATA[from majuscule to minuscule form and gradually incorporated a wide array of]]></p><p><![CDATA[ligatures, flourishes and other decorative nuances which defined its]]></p><p><![CDATA[extravagant cursive character. Until the late 15th century, typographers who]]></p><p><![CDATA[had to deal with Greek text avoided emulating this complicated hand; instead]]></p><p><![CDATA[they would use only the twenty four letters of the alphabet separately, often]]></p><p><![CDATA[without accents and other diacritics.]]></p> A celebrated example is the type cut and cast for the typesetting of the New Testament in the so-called Complutensian Polyglot Bible (1512), edited by the Greek scholar, Demetrios Doukas. The type was cut by Arnaldo Guillén de Brocar and the whole edition was a commission by cardinal Francisco Ximénez, in the University of Alcalá (Complutum), Spain. It is one of the best and most representative models of this early tradition in Greek typography which was revived in the early 20th century by the eminent bibliographer of the British Library, Richard Proctor. A font named Otter Greek was cut in 1903 and a book was printed using the new type. The original type had no capitals so Proctor added his own, which were rather large and ill-fitted. The early death of Proctor, the big size of the font and the different aesthetic notions of the time were the reasons that Otter Greek was destined to oblivion, as a curiosity. Greek Font Society incorporated Brocar’s famous and distinctive type in the commemorative edition of Pindar’s Odes for the Athens Olympics (2004) and the type with a new set of capitals, revived digitally by George D. Matthiopoulos,
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/16th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-complutum-fonts
echo "" > "gfs-complutum-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-complutum-fonts/
echo "%%dir %_fontsdir/otf/gfs-complutum-fonts" >> "gfs-complutum-fonts.list"
install -m 0644 -vp "GFSPolyglot.otf" %buildroot%_fontsdir/otf/gfs-complutum-fonts/
echo \"%_fontsdir/otf/gfs-complutum-fonts//$(basename "${font}")\" >> 'gfs-complutum-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSPolyglot.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-complutum-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-complutum-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-complutum-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-complutum-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "${fontdoc}" >> "gfs-complutum-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "${fontlicense}" >> "gfs-complutum-fonts.list"
done

%check

grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-complutum-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-complutum-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-complutum -f gfs-complutum-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070413-alt3_34
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_24
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_21
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_20
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_19
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070413-alt3_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070413-alt2_15
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070413-alt2_14
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070413-alt1_14
- initial release by fcimport

