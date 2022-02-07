Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-theokritos-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-theokritos-fonts
# SPDX-License-Identifier: MIT
Version: 20070415
Release: alt3_36
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Theokritos
%global fontsummary       GFS Theokritos, a 20th century decorative Greek font family
%global fonts             *.otf
%global fontdescription   \
Yannis Kefallinos (1894a..1958) was one of the most innovative engravers of his\
generation and the first who researched methodically the aesthetics of book and\
typographic design in Greece. He taught at the Fine Arts School of Athens and\
established the first book design workshop from which many practicing artists\
of the 60a.'s and 70a.'s had graduated.\
\
In the late 50a.'s Kefallinos designed and published an exquisite book with\
engraved illustrations of the ancient white funerary pottery in Attica in\
collaboration with Varlamos, Montesanto, Damianakis. For the text of\
Kefallinosa.' I.I.I.I. I.I.I.I.I.I. I.I.I.I.I.I.I. (1956) the artist used a typeface which he\
himself had designed a few years before for an unrealized edition of\
Theocritosa.' Idyls. Its complex and heavily decorative design does point to\
aesthetic codes which preoccupied his artistic expression and, although\
impractical for contemporary text setting, it remains an original display\
face, or it can be used as initials.\
\
The book design workshop of the Fine Arts School of Athens has been recently\
reorganized, under the direction of professor Leoni Vidali, and with her\
collaboration George D. Matthiopoulos has redesigned digitally this historical\
font which is now available as GFS Theokritos.

%global archivename GFS_Theokritos

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 65-gfs-theokritos-fonts.xml

Name:           fonts-otf-gfs-theokritos
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
  for font in 'GFSTheokritos.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSTheokritos.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-theokritos-fonts appstream file"
cat > "org.altlinux.gfs-theokritos-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-theokritos-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Theokritos</name>
  <summary><![CDATA[GFS Theokritos, a 20th century decorative Greek font family]]></summary>
  <description>
    <p><![CDATA[Yannis Kefallinos (1894–1958) was one of the most innovative engravers of his]]></p><p><![CDATA[generation and the first who researched methodically the aesthetics of book and]]></p><p><![CDATA[typographic design in Greece. He taught at the Fine Arts School of Athens and]]></p><p><![CDATA[established the first book design workshop from which many practicing artists]]></p><p><![CDATA[of the 60’s and 70’s had graduated.]]></p> In the late 50’s Kefallinos designed and published an exquisite book with engraved illustrations of the ancient white funerary pottery in Attica in collaboration with Varlamos, Montesanto, Damianakis. For the text of Kefallinos’ Δέκα λευκαί λήκυθοι (1956) the artist used a typeface which he himself had designed a few years before for an unrealized edition of Theocritos’ Idyls. Its complex and heavily decorative design does point to aesthetic codes which preoccupied his artistic expression and, although impractical for contemporary text setting, it remains an original display face, or it can be used as initials. The book design workshop of the Fine Arts School of Athens has been recently reorganized, under the direction of professor Leoni Vidali, and with her collaboration George D. Matthiopoulos has redesigned digitally this historical
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-theokritos-fonts
echo "" > "gfs-theokritos-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-theokritos/
echo "%%dir %_fontsdir/otf/gfs-theokritos" >> "gfs-theokritos-fonts.list"
install -m 0644 -vp "GFSTheokritos.otf" %buildroot%_fontsdir/otf/gfs-theokritos/
echo \"%_fontsdir/otf/gfs-theokritos//$(basename "GFSTheokritos.otf")\" >> 'gfs-theokritos-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSTheokritos.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-theokritos-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-theokritos-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-theokritos-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-theokritos-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-theokritos-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-theokritos-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-theokritos-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-theokritos-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-theokritos -f gfs-theokritos-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20070415-alt3_36
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_26
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_24
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_23
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_22
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_21
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_17
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_16
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt2_16
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070415-alt2_15
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070415-alt1_15
- initial release by fcimport

