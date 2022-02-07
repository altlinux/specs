Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-porson-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-porson-fonts
# SPDX-License-Identifier: MIT
Version: 20060908
Release: alt3_32
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Porson
%global fontsummary       GFS Porson, a 19th century Greek font family
%global fonts             *.otf
%global fontdescription   \
In England, during the 1790a.'s, Cambridge University Press decided to procure a\
new set of Greek types. The universitya.'s great scholar of Classics, Richard\
Porson was asked to produce a typeface based on his handsome handwriting and\
Richard Austin was commissioned to cut the types. The type was completed in\
1808, after the untimely death of Porson the previous year. Its success was\
immediate and since then the classical editions in Great Britain and the\
U.S.A. use it, almost invariably.\
\
In 1913, Monotype released the typeface with some corrections, notably\
replacing the upright capitals suggested by Porson with inclined ones. In\
Greece the typeface was used under the name Pelasgika type.\
\
GFS Porson is based on the Monotype version, though using upright capitals, as\
in the original.

%global archivename GFS_Porson

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-gfs-porson-fonts.xml

Name:           fonts-otf-gfs-porson
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
  for font in 'GFSPorson.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSPorson.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-porson-fonts appstream file"
cat > "org.altlinux.gfs-porson-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-porson-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Porson</name>
  <summary><![CDATA[GFS Porson, a 19th century Greek font family]]></summary>
  <description>
    <p><![CDATA[In England, during the 1790’s, Cambridge University Press decided to procure a]]></p><p><![CDATA[new set of Greek types. The university’s great scholar of Classics, Richard]]></p><p><![CDATA[Porson was asked to produce a typeface based on his handsome handwriting and]]></p><p><![CDATA[Richard Austin was commissioned to cut the types. The type was completed in]]></p><p><![CDATA[1808, after the untimely death of Porson the previous year. Its success was]]></p><p><![CDATA[immediate and since then the classical editions in Great Britain and the]]></p><p><![CDATA[U.S.A. use it, almost invariably.]]></p> In 1913, Monotype released the typeface with some corrections, notably replacing the upright capitals suggested by Porson with inclined ones. In Greece the typeface was used under the name Pelasgika type. GFS Porson is based on the Monotype version, though using upright capitals, as
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/19th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-porson-fonts
echo "" > "gfs-porson-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-porson/
echo "%%dir %_fontsdir/otf/gfs-porson" >> "gfs-porson-fonts.list"
install -m 0644 -vp "GFSPorson.otf" %buildroot%_fontsdir/otf/gfs-porson/
echo \"%_fontsdir/otf/gfs-porson//$(basename "GFSPorson.otf")\" >> 'gfs-porson-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSPorson.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-porson-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-porson-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-porson-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-porson-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-porson-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-porson-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-porson-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-porson-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-porson -f gfs-porson-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 20060908-alt3_32
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_23
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_20
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_19
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_16
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 20060908-alt3_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20060908-alt2_15
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20060908-alt2_14
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20060908-alt1_14
- initial release by fcimport

