Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-decker-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-decker-fonts
# SPDX-License-Identifier: MIT
Version: 20090618
Release: alt3_24
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Decker
%global fontsummary       GFS Decker, a 19th century Greek font family
%global fonts             *.otf
%global fontdescription   \
This typeface is a product of Deckersche SchriftgieA.ere type foundry owned by\
Rudolf Ludwig Decker (1804-1877) in Berlin, but it was frequently used in\
Greek editions by both Oxford and Cambridge University Press during the last\
decades of the 19th century. It was designed and cut before 1864, according to\
John Bowman, when a set of matrices was bought by OUP, although the type was\
not cast and used in England until 1882.\
\
The typeface is an uncial design containing a case of capitals, and small\
capitals, too. The letters lack any serifs although they retain their thick\
and thin strokes. It appeared as an alternate type of Byzantine tradition in\
mostly Patristic texts.\
\
The font was digitally designed by George D. Matthiopoulos and is freely\
available by GFS.

%global archivename GFS_Decker

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-decker
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-decker
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
  for font in 'GFSDecker.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSDecker.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-decker-fonts appstream file"
cat > "org.altlinux.gfs-decker-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-decker-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSDecker</name>
  <summary><![CDATA[GFS Decker, a 19th century Greek font family]]></summary>
  <description>
    <p><![CDATA[This typeface is a product of Deckersche Schriftgießere type foundry owned by]]></p><p><![CDATA[Rudolf Ludwig Decker (1804-1877) in Berlin, but it was frequently used in]]></p><p><![CDATA[Greek editions by both Oxford and Cambridge University Press during the last]]></p><p><![CDATA[decades of the 19th century. It was designed and cut before 1864, according to]]></p><p><![CDATA[John Bowman, when a set of matrices was bought by OUP, although the type was]]></p><p><![CDATA[not cast and used in England until 1882.]]></p> The typeface is an uncial design containing a case of capitals, and small capitals, too. The letters lack any serifs although they retain their thick and thin strokes. It appeared as an alternate type of Byzantine tradition in mostly Patristic texts. The font was digitally designed by George D. Matthiopoulos and is freely
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-decker-fonts
echo "" > "gfs-decker-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-decker-fonts/
echo "%%dir %_fontsdir/otf/gfs-decker-fonts" >> "gfs-decker-fonts.list"
install -m 0644 -vp "GFSDecker.otf" %buildroot%_fontsdir/otf/gfs-decker-fonts/
echo \"%_fontsdir/otf/gfs-decker-fonts//$(basename "${font}")\" >> 'gfs-decker-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSDecker.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-decker-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-decker-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-decker-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-decker-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "${fontdoc}" >> "gfs-decker-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "${fontlicense}" >> "gfs-decker-fonts.list"
done

%check

grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-decker-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-decker-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-decker -f gfs-decker-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20090618-alt3_24
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_11
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_10
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_6
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090618-alt3_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20090618-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20090618-alt2_4
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20090618-alt1_4
- initial release by fcimport

