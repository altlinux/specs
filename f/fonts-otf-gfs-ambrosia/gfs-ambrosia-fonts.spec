Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-ambrosia-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-ambrosia-fonts
# SPDX-License-Identifier: MIT
Version: 20080624
Release: alt4_27
URL:     http://www.greekfontsociety-gfs.gr/typefaces/majuscule

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Ambrosia
%global fontsummary       GFS Ambrosia, a Greek majuscule font family
%global fonts             *.otf
%global fontdescription   \
As it is known, the Greek alphabet was used in majuscule form for over a\
millennium before the minuscule letters gradually replaced it until they became\
the official script in the 9th century A.D. Thereafter, majuscule letters were\
confined to sparse use as initials or elaborate titles until the Italian\
Renaissance.\
\
The new art of Typography, as well as the need of the humanists to mimic the\
ancient Greco-Roman period brought back the extensive use of the majuscule\
letter-forms in both Latin and Greek typography. Greek books of the time were\
printed using the contemporary Byzantine hand with which they combined capital\
letters modeled on the Roman antiquity, i.e. with thick and thin strokes and\
serifs. At the same time the Byzantine majuscule tradition, principally used on\
theological editions, remained alive until the early 19th century.\
\
GFS Ambrosia has the main characteristics of the majuscule forms of the early\
Christian tradition.\
\
It has been designed by George D. Matthiopoulos.

%global archivename GFS_Ambrosia

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-ambrosia
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-ambrosia
%{?fontdescription}

%prep
%global fontconfngs       %{SOURCE10}
%setup -n %{oldname}-%{version} -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build

fontnames=$(
  for font in 'GFSAmbrosia.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSAmbrosia.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-ambrosia-fonts appstream file"
cat > "org.altlinux.gfs-ambrosia-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-ambrosia-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSAmbrosia</name>
  <summary><![CDATA[GFS Ambrosia, a Greek majuscule font family]]></summary>
  <description>
    <p><![CDATA[As it is known, the Greek alphabet was used in majuscule form for over a]]></p><p><![CDATA[millennium before the minuscule letters gradually replaced it until they became]]></p><p><![CDATA[the official script in the 9th century A.D. Thereafter, majuscule letters were]]></p><p><![CDATA[confined to sparse use as initials or elaborate titles until the Italian]]></p><p><![CDATA[Renaissance.]]></p> The new art of Typography, as well as the need of the humanists to mimic the ancient Greco-Roman period brought back the extensive use of the majuscule letter-forms in both Latin and Greek typography. Greek books of the time were printed using the contemporary Byzantine hand with which they combined capital letters modeled on the Roman antiquity, i.e. with thick and thin strokes and serifs. At the same time the Byzantine majuscule tradition, principally used on theological editions, remained alive until the early 19th century. GFS Ambrosia has the main characteristics of the majuscule forms of the early Christian tradition.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/majuscule</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-ambrosia-fonts
echo "" > "gfs-ambrosia-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-ambrosia/
echo "%%dir %_fontsdir/otf/gfs-ambrosia" >> "gfs-ambrosia-fonts.list"
install -m 0644 -vp "GFSAmbrosia.otf" %buildroot%_fontsdir/otf/gfs-ambrosia/
echo \"%_fontsdir/otf/gfs-ambrosia//$(basename "${font}")\" >> 'gfs-ambrosia-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSAmbrosia.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-ambrosia-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-ambrosia-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-ambrosia-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-ambrosia-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-ambrosia-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-ambrosia-fonts.list"
done

%check
# fontcheck
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-ambrosia-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-ambrosia-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-ambrosia -f gfs-ambrosia-fonts.list

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20080624-alt4_27
- use short alt-style fontdir name

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20080624-alt3_27
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_17
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_14
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080624-alt3_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080624-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20080624-alt2_7
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20080624-alt1_7
- initial release by fcimport

