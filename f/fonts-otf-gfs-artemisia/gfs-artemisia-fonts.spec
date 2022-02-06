Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-artemisia-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-artemisia-fonts
# SPDX-License-Identifier: MIT
Version: 20070415
Release: alt4_33
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.rtf
%global fontdocsex        %{fontlicenses}

%global fontfamily        Artemisia
%global fontsummary       GFS Artemisia, a Greek font family
%global fonts             *.otf
%global fontdescription   \
The type family GFS Artemisia was designed by the painter-engraver Takis\
Katsoulidis and reflects his style and typographic acumen. It is largely his\
effort to offer, from a different perspective, a type face which, like Times\
Greek, would be applicable to a wide spectrum of uses and equally agreeable and\
legible.\
\
The typeface has been digitized by George D. Matthiopoulos.

%global archivename GFS_Artemisia

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

Name:           fonts-otf-gfs-artemisia
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-artemisia
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
chmod 644 %{fontdocs} %{fontlicenses}

%build

fontnames=$(
  for font in 'GFSArtemisia.otf' 'GFSArtemisiaBold.otf' 'GFSArtemisiaBoldIt.otf' 'GFSArtemisiaIt.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSArtemisia.otf' 'GFSArtemisiaBold.otf' 'GFSArtemisiaBoldIt.otf' 'GFSArtemisiaIt.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-artemisia-fonts appstream file"
cat > "org.altlinux.gfs-artemisia-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-artemisia-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSArtemisia</name>
  <summary><![CDATA[GFS Artemisia, a Greek font family]]></summary>
  <description>
    <p><![CDATA[The type family GFS Artemisia was designed by the painter-engraver Takis]]></p><p><![CDATA[Katsoulidis and reflects his style and typographic acumen. It is largely his]]></p><p><![CDATA[effort to offer, from a different perspective, a type face which, like Times]]></p><p><![CDATA[Greek, would be applicable to a wide spectrum of uses and equally agreeable and]]></p><p><![CDATA[legible.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-artemisia-fonts
echo "" > "gfs-artemisia-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-artemisia/
echo "%%dir %_fontsdir/otf/gfs-artemisia" >> "gfs-artemisia-fonts.list"
install -m 0644 -vp "GFSArtemisia.otf" %buildroot%_fontsdir/otf/gfs-artemisia/
echo \"%_fontsdir/otf/gfs-artemisia//$(basename "${font}")\" >> 'gfs-artemisia-fonts.list'
install -m 0644 -vp "GFSArtemisiaBold.otf" %buildroot%_fontsdir/otf/gfs-artemisia/
echo \"%_fontsdir/otf/gfs-artemisia//$(basename "${font}")\" >> 'gfs-artemisia-fonts.list'
install -m 0644 -vp "GFSArtemisiaBoldIt.otf" %buildroot%_fontsdir/otf/gfs-artemisia/
echo \"%_fontsdir/otf/gfs-artemisia//$(basename "${font}")\" >> 'gfs-artemisia-fonts.list'
install -m 0644 -vp "GFSArtemisiaIt.otf" %buildroot%_fontsdir/otf/gfs-artemisia/
echo \"%_fontsdir/otf/gfs-artemisia//$(basename "${font}")\" >> 'gfs-artemisia-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSArtemisia.otf' 'GFSArtemisiaBold.otf' 'GFSArtemisiaBoldIt.otf' 'GFSArtemisiaIt.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-artemisia-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-artemisia-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-artemisia-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-artemisia-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt' 'readme.rtf'; do
  echo %%doc "'${fontdoc}'" >> "gfs-artemisia-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-artemisia-fonts.list"
done

%check
# fontcheck
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-artemisia-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-artemisia-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-artemisia -f gfs-artemisia-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070415-alt4_33
- use short alt-style fontdir name

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070415-alt3_33
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_23
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_20
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_15
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070415-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070415-alt2_13
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070415-alt1_13
- initial release by fcimport

