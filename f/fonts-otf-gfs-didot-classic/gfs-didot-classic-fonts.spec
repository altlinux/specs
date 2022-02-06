Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-didot-classic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-didot-classic-fonts
# SPDX-License-Identifier: MIT
Version: 20080702
Release: alt4_28
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Didot Classic
%global fontsummary       GFS Didot Classic, a 19th century Greek font family
%global fontpkgheader     \
Requires: font(gfsdidot)\

%global fonts             *.otf
%global fontdescription   \
Under the influence of the neoclassical ideals of the late 18th century, the\
famous French type cutter Firmin Didot in Paris designed a new Greek typeface\
(1805) which was immediately used in the publishing program of Adamantios\
Korai, the prominent intellectual figure of the Greek diaspora and leading\
scholar of the Greek Enlightenment. The typeface eventually arrived in Greece,\
with the field press which came with Didota.'s grandson Ambroise Firmin Didot,\
during the Greek Revolution in 1821. Since then the typeface has enjoyed an\
unrivaled success as the type of choice for almost every kind of publication\
until the last decades of the 20th century.\
\
Didota.'s original type design, as it is documented in publications during the\
first decades of the 19th century, was digitized and revived by George D.\
Matthiopoulos in 2006 for a project of the Department of Literature in the\
School of Philosophy at the University of Thessaloniki, and is now available\
for general use.

%global archivename GFS_Didot_Classic

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-didot-classic
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-didot-classic
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
  for font in 'GFSDidot_Classic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSDidot_Classic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-didot-classic-fonts appstream file"
cat > "org.altlinux.gfs-didot-classic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-didot-classic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSDidot Classic</name>
  <summary><![CDATA[GFS Didot Classic, a 19th century Greek font family]]></summary>
  <description>
    <p><![CDATA[Under the influence of the neoclassical ideals of the late 18th century, the]]></p><p><![CDATA[famous French type cutter Firmin Didot in Paris designed a new Greek typeface]]></p><p><![CDATA[(1805) which was immediately used in the publishing program of Adamantios]]></p><p><![CDATA[Korai, the prominent intellectual figure of the Greek diaspora and leading]]></p><p><![CDATA[scholar of the Greek Enlightenment. The typeface eventually arrived in Greece,]]></p><p><![CDATA[with the field press which came with Didot’s grandson Ambroise Firmin Didot,]]></p><p><![CDATA[during the Greek Revolution in 1821. Since then the typeface has enjoyed an]]></p><p><![CDATA[unrivaled success as the type of choice for almost every kind of publication]]></p><p><![CDATA[until the last decades of the 20th century.]]></p> Didot’s original type design, as it is documented in publications during the first decades of the 19th century, was digitized and revived by George D. Matthiopoulos in 2006 for a project of the Department of Literature in the School of Philosophy at the University of Thessaloniki, and is now available
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-didot-classic-fonts
echo "" > "gfs-didot-classic-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-didot-classic/
echo "%%dir %_fontsdir/otf/gfs-didot-classic" >> "gfs-didot-classic-fonts.list"
install -m 0644 -vp "GFSDidot_Classic.otf" %buildroot%_fontsdir/otf/gfs-didot-classic/
echo \"%_fontsdir/otf/gfs-didot-classic//$(basename "${font}")\" >> 'gfs-didot-classic-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSDidot_Classic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-didot-classic-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-didot-classic-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-didot-classic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-didot-classic-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-didot-classic-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-didot-classic-fonts.list"
done

%check
# fontcheck
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-didot-classic-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-didot-classic-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-didot-classic -f gfs-didot-classic-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20080702-alt4_28
- use short alt-style fontdir name

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20080702-alt3_28
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_18
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_15
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_14
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_10
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080702-alt3_9
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080702-alt2_9
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20080702-alt2_8
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20080702-alt1_8
- initial release by fcimport

