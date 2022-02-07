Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-solomos-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-solomos-fonts
# SPDX-License-Identifier: MIT
Version: 20071114
Release: alt3_32
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Solomos
%global fontsummary       GFS Solomos, a 19th century italic Greek font family
%global fonts             *.otf
%global fontdescription   \
From the middle of the 19th century an italic font with many calligraphic\
overtones was introduced into Greek printing. Its source is unknown, but it\
almost certainly was the product of a German or Italian foundry. In the first\
type specimen printed in Greece by the type cutter K. Miliadis (1850), the font\
was listed anonymously along others of 11pts and in the Gr. Doumasa.' undated\
specimen appeared as a.'11pt Greek inclineda.'. For most of the second half of the\
century the type was used extensively as an italic for emphasis in words,\
sentences or excerpts. In 1889, the folio size Type Specimen of Anestis\
Konstantinidisa.' publishing, printing and type founding establishment also\
included the type as a.'Greek inclined [9 & 12 pt]a.'.\
\
Nevertheless, the excessively calligraphic style of the characters, combined\
with the steep and uncomfortable obliqueness of the capitals, was out of\
favor in the 20th century and the type did not survive the conformity of the\
mechanical type cutting and casting.\
\
The font has been digitally revived, as part of our typographic tradition, by\
George D. Matthiopoulos and is part of GFSa.' type library under the name GFS\
Solomos, in commemoration of the great Greek poet of the 19th century,\
Dionisios Solomos.

%global archivename GFS_Solomos

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-gfs-solomos-fonts.xml

Name:           fonts-otf-gfs-solomos
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
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
# fontbuild 
fontnames=$(
  for font in 'GFSSolomos.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSSolomos.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-solomos-fonts appstream file"
cat > "org.altlinux.gfs-solomos-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-solomos-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Solomos</name>
  <summary><![CDATA[GFS Solomos, a 19th century italic Greek font family]]></summary>
  <description>
    <p><![CDATA[From the middle of the 19th century an italic font with many calligraphic]]></p><p><![CDATA[overtones was introduced into Greek printing. Its source is unknown, but it]]></p><p><![CDATA[almost certainly was the product of a German or Italian foundry. In the first]]></p><p><![CDATA[type specimen printed in Greece by the type cutter K. Miliadis (1850), the font]]></p><p><![CDATA[was listed anonymously along others of 11pts and in the Gr. Doumas’ undated]]></p><p><![CDATA[specimen appeared as “11pt Greek inclined”. For most of the second half of the]]></p><p><![CDATA[century the type was used extensively as an italic for emphasis in words,]]></p><p><![CDATA[sentences or excerpts. In 1889, the folio size Type Specimen of Anestis]]></p><p><![CDATA[Konstantinidis’ publishing, printing and type founding establishment also]]></p><p><![CDATA[included the type as “Greek inclined [9 & 12 pt]”.]]></p> Nevertheless, the excessively calligraphic style of the characters, combined with the steep and uncomfortable obliqueness of the capitals, was out of favor in the 20th century and the type did not survive the conformity of the mechanical type cutting and casting. The font has been digitally revived, as part of our typographic tradition, by George D. Matthiopoulos and is part of GFS’ type library under the name GFS Solomos, in commemoration of the great Greek poet of the 19th century,
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-solomos-fonts
echo "" > "gfs-solomos-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-solomos/
echo "%%dir %_fontsdir/otf/gfs-solomos" >> "gfs-solomos-fonts.list"
install -m 0644 -vp "GFSSolomos.otf" %buildroot%_fontsdir/otf/gfs-solomos/
echo \"%_fontsdir/otf/gfs-solomos//$(basename "GFSSolomos.otf")\" >> 'gfs-solomos-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSSolomos.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-solomos-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-solomos-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-solomos-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-solomos-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-solomos-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-solomos-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-solomos-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-solomos-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-solomos -f gfs-solomos-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20071114-alt3_32
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_22
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_15
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20071114-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20071114-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20071114-alt2_13
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20071114-alt1_13
- initial release by fcimport

