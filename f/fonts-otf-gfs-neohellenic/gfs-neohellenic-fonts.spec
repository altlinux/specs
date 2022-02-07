Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-neohellenic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-neohellenic-fonts
# SPDX-License-Identifier: MIT
Version: 20090918
Release: alt3_22
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        NeoHellenic
%global fontsummary       GFS NeoHellenic, a 20th century round Greek font family
%global fonts             *.otf
%global fontdescription   \
The design of new Greek typefaces always followed the growing needs of the\
Classical Studies in the major European Universities. Furthermore, by the end\
of the 19th century bibliology had become an established section of Historical\
Studies, and, as John Bowman commented, the prevailing attitude was that Greek\
types should adhere to a lost idealized, yet undefined, Greekness of yore.\
Especially in Great Britain this tendency remained unchallenged in the first\
decades of the 20th century, both by Richard Proctor, curator of the incunabula\
section in the British Museum Library and his successor Victor Scholderer.\
\
In 1927, Scholderer, on behalf of the Society for the Promotion of Greek\
Studies, got involved in choosing and consulting the design and production of a\
Greek type called New Hellenic cut by the Lanston Monotype Corporation. He\
chose the revival of a round, and almost mono-line type which had first appeared\
in 1492 in the edition of Macrobius, ascribable to the printing shop of\
Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful\
typeface in Great Britain after the introduction of Porson Greek well over a\
century before. The type, since to 1930a.'s, was also well received in Greece,\
albeit with a different design for Ksi and Omega.\
\
GFS digitized the typeface (1993-1994) funded by the Athens Archeological\
Society with the addition of a new set of epigraphical symbols. Later (2000)\
more weights were added (italic, bold and bold italic) as well as a Latin\
version.

%global archivename GFS_NeoHellenic

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-gfs-neohellenic-fonts.xml

Name:           fonts-otf-gfs-neohellenic
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
  for font in 'GFSNeohellenic.otf' 'GFSNeohellenicBold.otf' 'GFSNeohellenicBoldIt.otf' 'GFSNeohellenicIt.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSNeohellenic.otf' 'GFSNeohellenicBold.otf' 'GFSNeohellenicBoldIt.otf' 'GFSNeohellenicIt.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-neohellenic-fonts appstream file"
cat > "org.altlinux.gfs-neohellenic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-neohellenic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS NeoHellenic</name>
  <summary><![CDATA[GFS NeoHellenic, a 20th century round Greek font family]]></summary>
  <description>
    <p><![CDATA[The design of new Greek typefaces always followed the growing needs of the]]></p><p><![CDATA[Classical Studies in the major European Universities. Furthermore, by the end]]></p><p><![CDATA[of the 19th century bibliology had become an established section of Historical]]></p><p><![CDATA[Studies, and, as John Bowman commented, the prevailing attitude was that Greek]]></p><p><![CDATA[types should adhere to a lost idealized, yet undefined, Greekness of yore.]]></p><p><![CDATA[Especially in Great Britain this tendency remained unchallenged in the first]]></p><p><![CDATA[decades of the 20th century, both by Richard Proctor, curator of the incunabula]]></p><p><![CDATA[section in the British Museum Library and his successor Victor Scholderer.]]></p> In 1927, Scholderer, on behalf of the Society for the Promotion of Greek Studies, got involved in choosing and consulting the design and production of a Greek type called New Hellenic cut by the Lanston Monotype Corporation. He chose the revival of a round, and almost mono-line type which had first appeared in 1492 in the edition of Macrobius, ascribable to the printing shop of Giovanni Rosso (Joannes Rubeus) in Venice. New Hellenic was the only successful typeface in Great Britain after the introduction of Porson Greek well over a century before. The type, since to 1930’s, was also well received in Greece, albeit with a different design for Ksi and Omega. GFS digitized the typeface (1993-1994) funded by the Athens Archeological Society with the addition of a new set of epigraphical symbols. Later (2000) more weights were added (italic, bold and bold italic) as well as a Latin
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-neohellenic-fonts
echo "" > "gfs-neohellenic-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-neohellenic/
echo "%%dir %_fontsdir/otf/gfs-neohellenic" >> "gfs-neohellenic-fonts.list"
install -m 0644 -vp "GFSNeohellenic.otf" %buildroot%_fontsdir/otf/gfs-neohellenic/
echo \"%_fontsdir/otf/gfs-neohellenic//$(basename "GFSNeohellenic.otf")\" >> 'gfs-neohellenic-fonts.list'
install -m 0644 -vp "GFSNeohellenicBold.otf" %buildroot%_fontsdir/otf/gfs-neohellenic/
echo \"%_fontsdir/otf/gfs-neohellenic//$(basename "GFSNeohellenicBold.otf")\" >> 'gfs-neohellenic-fonts.list'
install -m 0644 -vp "GFSNeohellenicBoldIt.otf" %buildroot%_fontsdir/otf/gfs-neohellenic/
echo \"%_fontsdir/otf/gfs-neohellenic//$(basename "GFSNeohellenicBoldIt.otf")\" >> 'gfs-neohellenic-fonts.list'
install -m 0644 -vp "GFSNeohellenicIt.otf" %buildroot%_fontsdir/otf/gfs-neohellenic/
echo \"%_fontsdir/otf/gfs-neohellenic//$(basename "GFSNeohellenicIt.otf")\" >> 'gfs-neohellenic-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSNeohellenic.otf' 'GFSNeohellenicBold.otf' 'GFSNeohellenicBoldIt.otf' 'GFSNeohellenicIt.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-neohellenic-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-neohellenic-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-neohellenic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-neohellenic-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-neohellenic-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-neohellenic-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-neohellenic-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-neohellenic-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-neohellenic -f gfs-neohellenic-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20090918-alt3_22
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_4
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20090918-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090918-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090918-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090918-alt1_2
- initial release by fcimport

