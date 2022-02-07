Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-philostratos-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-philostratos-fonts
# SPDX-License-Identifier: MIT
Version: 20090902
Release: alt3_22
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Philostratos
%global fontsummary       GFS Philostratos, a 19th century Greek revival of Griechische Antiqua
%global fonts             *.otf
%global fontdescription   \
Griechische Antiqua was one of the historical Greek typefaces of the late 19th\
and early 20th century. It was designed by I'aurice I.duard Pinder, a German\
erudite artist and a member of the Academy of Science in Berlin. This is the\
most popular version which has appeared from 1870 to 1940 in the German\
speaking philological literature and in many classical and Byzantine editions\
by publishers like Teubner (in Leipzig) and Weidmann (in Berlin) such as:\
Anthology of Byzantine Melos by Wilhelm von Christ and Matthaios\
Paranikas (Leipzig 1871), Epicurea, by Heinrich Usener (Leipzig 1887),\
Mitrodorous by Alfred Koerte (Leipzig 1890), Pindar by Otto Schroeder (Leipzig\
1908), I.I.I. Aeschylus by U. von Wilamowitz-Moellendorff (Berlin 1910, 1915),\
Bachylides by Bruno Snell (Leipzig, 1934),  The Vulgata by Alfred Rahlfs\
(Stuttgart 1935), Suidas Lexicon by Ada Adler (Leipzig 1928-1938) etc.\
\
E.J. Kenney lamented the abandonment of the type after the 2nd World War as a\
great loss for Greek typography (a.'From Script to Printa.', Greek Scripts: An\
illustrated Introduction, Society for the Promotion of Hellenic Studies, 2001,\
p. 69).\
\
GFS Philostratos was digitized by George D. Matthiopoulos.

%global archivename GFS_Philostratos

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-gfs-philostratos-fonts.xml

Name:           fonts-otf-gfs-philostratos
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
  for font in 'GFSPhilostratos.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSPhilostratos.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-philostratos-fonts appstream file"
cat > "org.altlinux.gfs-philostratos-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-philostratos-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Philostratos</name>
  <summary><![CDATA[GFS Philostratos, a 19th century Greek revival of Griechische Antiqua]]></summary>
  <description>
    <p><![CDATA[Griechische Antiqua was one of the historical Greek typefaces of the late 19th]]></p><p><![CDATA[and early 20th century. It was designed by Μaurice Εduard Pinder, a German]]></p><p><![CDATA[erudite artist and a member of the Academy of Science in Berlin. This is the]]></p><p><![CDATA[most popular version which has appeared from 1870 to 1940 in the German]]></p><p><![CDATA[speaking philological literature and in many classical and Byzantine editions]]></p><p><![CDATA[by publishers like Teubner (in Leipzig) and Weidmann (in Berlin) such as:]]></p><p><![CDATA[Anthology of Byzantine Melos by Wilhelm von Christ and Matthaios]]></p><p><![CDATA[Paranikas (Leipzig 1871), Epicurea, by Heinrich Usener (Leipzig 1887),]]></p><p><![CDATA[Mitrodorous by Alfred Koerte (Leipzig 1890), Pindar by Otto Schroeder (Leipzig]]></p><p><![CDATA[1908), του Aeschylus by U. von Wilamowitz-Moellendorff (Berlin 1910, 1915),]]></p><p><![CDATA[Bachylides by Bruno Snell (Leipzig, 1934),  The Vulgata by Alfred Rahlfs]]></p><p><![CDATA[(Stuttgart 1935), Suidas Lexicon by Ada Adler (Leipzig 1928-1938) etc.]]></p> E.J. Kenney lamented the abandonment of the type after the 2nd World War as a great loss for Greek typography (“From Script to Print”, Greek Scripts: An illustrated Introduction, Society for the Promotion of Hellenic Studies, 2001, p. 69).
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-philostratos-fonts
echo "" > "gfs-philostratos-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-philostratos/
echo "%%dir %_fontsdir/otf/gfs-philostratos" >> "gfs-philostratos-fonts.list"
install -m 0644 -vp "GFSPhilostratos.otf" %buildroot%_fontsdir/otf/gfs-philostratos/
echo \"%_fontsdir/otf/gfs-philostratos//$(basename "GFSPhilostratos.otf")\" >> 'gfs-philostratos-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSPhilostratos.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-philostratos-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-philostratos-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-philostratos-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-philostratos-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-philostratos-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-philostratos-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-philostratos-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-philostratos-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-philostratos -f gfs-philostratos-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20090902-alt3_22
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_4
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20090902-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090902-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090902-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090902-alt1_2
- initial release by fcimport

