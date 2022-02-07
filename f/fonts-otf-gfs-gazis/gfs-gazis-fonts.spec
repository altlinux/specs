Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-gazis-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-gazis-fonts
# SPDX-License-Identifier: MIT
Version: 20091008
Release: alt3_21
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gazis
%global fontsummary       GFS Gazis, an 18th century oblique Greek font family
%global fonts             *.otf
%global fontdescription   \
During the whole of the 18th century the old tradition of using Greek types\
designed to conform to the Byzantine cursive hand with many ligatures and\
abbreviations a.. as it was originated by Aldus Manutius in Venice and\
consolidated by Claude Garamont (Grecs du Roy) a.. was still much in practice,\
although clearly on the wane.\
\
GFS Gazis is a typical German example of this practice as it appeared at the\
end of that era in the 1790a.'s. Its name pays tribute to Anthimos Gazis\
(1758-1828), one of the most prolific Greek thinkers of the period, who was\
responsible for writing, translating and editing numerous books, including the\
editorship of the important Greek periodical I.I.I.I.I. I. I.I.I.I.I.I. (Litterary Hermes)\
in Wien.\
\
GFS Gazis has been digitally designed by George D. Matthiopoulos.

%global archivename GFS_Gazis

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-gfs-gazis-fonts.xml

Name:           fonts-otf-gfs-gazis
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
  for font in 'GFSGazis.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSGazis.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-gazis-fonts appstream file"
cat > "org.altlinux.gfs-gazis-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-gazis-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Gazis</name>
  <summary><![CDATA[GFS Gazis, an 18th century oblique Greek font family]]></summary>
  <description>
    <p><![CDATA[During the whole of the 18th century the old tradition of using Greek types]]></p><p><![CDATA[designed to conform to the Byzantine cursive hand with many ligatures and]]></p><p><![CDATA[abbreviations — as it was originated by Aldus Manutius in Venice and]]></p><p><![CDATA[consolidated by Claude Garamont (Grecs du Roy) — was still much in practice,]]></p><p><![CDATA[although clearly on the wane.]]></p> GFS Gazis is a typical German example of this practice as it appeared at the end of that era in the 1790’s. Its name pays tribute to Anthimos Gazis (1758-1828), one of the most prolific Greek thinkers of the period, who was responsible for writing, translating and editing numerous books, including the editorship of the important Greek periodical Ερμής ο Λόγιος (Litterary Hermes) in Wien.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/18th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-gazis-fonts
echo "" > "gfs-gazis-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-gazis/
echo "%%dir %_fontsdir/otf/gfs-gazis" >> "gfs-gazis-fonts.list"
install -m 0644 -vp "GFSGazis.otf" %buildroot%_fontsdir/otf/gfs-gazis/
echo \"%_fontsdir/otf/gfs-gazis//$(basename "GFSGazis.otf")\" >> 'gfs-gazis-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSGazis.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-gazis-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-gazis-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-gazis-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-gazis-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-gazis-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-gazis-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-gazis-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-gazis-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-gazis -f gfs-gazis-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20091008-alt3_21
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_8
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20091008-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20091008-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20091008-alt2_2
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20091008-alt1_2
- initial release by fcimport

