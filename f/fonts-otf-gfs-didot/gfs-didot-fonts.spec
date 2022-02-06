Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-didot-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-didot-fonts
# SPDX-License-Identifier: MIT
Version: 20070616
Release: alt3_33
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Didot
%global fontsummary       GFS Didot, a 20th century Greek font family
%global fonts             *.otf
%global fontdescription   \
Didota.'s type was the base for a new font, GFS Didot (1994) which was designed\
by Takis Katsoulidis, and digitized by George Matthiopoulos. The typeface is\
accompanied by a matching Latin alphabet based on Hermann Zapfa.'s PaLatino.

%global archivename GFS_Didot

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

Name:           fonts-otf-gfs-didot
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-didot
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
  for font in 'GFSDidot.otf' 'GFSDidotBold.otf' 'GFSDidotBoldItalic.otf' 'GFSDidotItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSDidot.otf' 'GFSDidotBold.otf' 'GFSDidotBoldItalic.otf' 'GFSDidotItalic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-didot-fonts appstream file"
cat > "org.altlinux.gfs-didot-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-didot-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSDidot</name>
  <summary><![CDATA[GFS Didot, a 20th century Greek font family]]></summary>
  <description>
    <p><![CDATA[Didot’s type was the base for a new font, GFS Didot (1994) which was designed]]></p><p><![CDATA[by Takis Katsoulidis, and digitized by George Matthiopoulos. The typeface is]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-didot-fonts
echo "" > "gfs-didot-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-didot-fonts/
echo "%%dir %_fontsdir/otf/gfs-didot-fonts" >> "gfs-didot-fonts.list"
install -m 0644 -vp "GFSDidot.otf" %buildroot%_fontsdir/otf/gfs-didot-fonts/
echo \"%_fontsdir/otf/gfs-didot-fonts//$(basename "${font}")\" >> 'gfs-didot-fonts.list'
install -m 0644 -vp "GFSDidotBold.otf" %buildroot%_fontsdir/otf/gfs-didot-fonts/
echo \"%_fontsdir/otf/gfs-didot-fonts//$(basename "${font}")\" >> 'gfs-didot-fonts.list'
install -m 0644 -vp "GFSDidotBoldItalic.otf" %buildroot%_fontsdir/otf/gfs-didot-fonts/
echo \"%_fontsdir/otf/gfs-didot-fonts//$(basename "${font}")\" >> 'gfs-didot-fonts.list'
install -m 0644 -vp "GFSDidotItalic.otf" %buildroot%_fontsdir/otf/gfs-didot-fonts/
echo \"%_fontsdir/otf/gfs-didot-fonts//$(basename "${font}")\" >> 'gfs-didot-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSDidot.otf' 'GFSDidotBold.otf' 'GFSDidotBoldItalic.otf' 'GFSDidotItalic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-didot-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-didot-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-didot-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-didot-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "${fontdoc}" >> "gfs-didot-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "${fontlicense}" >> "gfs-didot-fonts.list"
done

%check

grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-didot-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-didot-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-didot -f gfs-didot-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070616-alt3_33
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_23
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_20
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_19
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_15
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070616-alt3_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070616-alt2_14
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070616-alt2_13
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070616-alt1_13
- initial release by fcimport

