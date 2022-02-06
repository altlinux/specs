Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-baskerville-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-baskerville-fonts
# SPDX-License-Identifier: MIT
Version: 20070327
Release: alt4_34
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Baskerville
%global fontsummary       GFS Baskerville, an 18th century oblique Greek font family
%global fonts             *.otf
%global fontdescription   \
John Baskerville (1706-1775) got involved in typography late in his career but\
his contribution was significant. He was a successful entrepreneur and\
possessed an inquiring mind which he applied to produce many aesthetic and\
technical innovations in printing. He invented a new ink formula, a new type\
of smooth paper and made various improvements in the printing press. He was\
also involved in type design which resulted in a Latin typeface which was used\
for the edition of Virgil, in 1757. The quality of the type was admired\
throughout of Europe and America and was revived with great success in the\
early 20th century.\
\
Baskerville was also involved in the design of a Greek typeface which he used\
in an edition of the New Testament for Oxford University, in 1763. He adopted\
the practice of avoiding the excessive number of ligatures which Alexander\
Wilson had started a few years earlier but his Greek types were rather narrow\
in proportion and did not win the sympathy of the philologists and other\
scholars of his time. They did influence, however, the Greek types of\
Giambattista Bodoni. and through him Didota.'s Greek in Paris.\
\
The typeface has been digitally revived as GFS Baskerville Classic by Sophia\
Kalaitzidou and George D. Matthiopoulos and is now available as part of GFSa.'\
type library.

%global archivename GFS_Baskerville

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-baskerville
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-baskerville
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
  for font in 'GFSBaskerville.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSBaskerville.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-baskerville-fonts appstream file"
cat > "org.altlinux.gfs-baskerville-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-baskerville-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSBaskerville</name>
  <summary><![CDATA[GFS Baskerville, an 18th century oblique Greek font family]]></summary>
  <description>
    <p><![CDATA[John Baskerville (1706-1775) got involved in typography late in his career but]]></p><p><![CDATA[his contribution was significant. He was a successful entrepreneur and]]></p><p><![CDATA[possessed an inquiring mind which he applied to produce many aesthetic and]]></p><p><![CDATA[technical innovations in printing. He invented a new ink formula, a new type]]></p><p><![CDATA[of smooth paper and made various improvements in the printing press. He was]]></p><p><![CDATA[also involved in type design which resulted in a Latin typeface which was used]]></p><p><![CDATA[for the edition of Virgil, in 1757. The quality of the type was admired]]></p><p><![CDATA[throughout of Europe and America and was revived with great success in the]]></p><p><![CDATA[early 20th century.]]></p> Baskerville was also involved in the design of a Greek typeface which he used in an edition of the New Testament for Oxford University, in 1763. He adopted the practice of avoiding the excessive number of ligatures which Alexander Wilson had started a few years earlier but his Greek types were rather narrow in proportion and did not win the sympathy of the philologists and other scholars of his time. They did influence, however, the Greek types of Giambattista Bodoni. and through him Didot’s Greek in Paris. The typeface has been digitally revived as GFS Baskerville Classic by Sophia Kalaitzidou and George D. Matthiopoulos and is now available as part of GFS’
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/18th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-baskerville-fonts
echo "" > "gfs-baskerville-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-baskerville/
echo "%%dir %_fontsdir/otf/gfs-baskerville" >> "gfs-baskerville-fonts.list"
install -m 0644 -vp "GFSBaskerville.otf" %buildroot%_fontsdir/otf/gfs-baskerville/
echo \"%_fontsdir/otf/gfs-baskerville//$(basename "${font}")\" >> 'gfs-baskerville-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSBaskerville.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-baskerville-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-baskerville-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-baskerville-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-baskerville-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-baskerville-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-baskerville-fonts.list"
done

%check
# fontcheck
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-baskerville-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-baskerville-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-baskerville -f gfs-baskerville-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070327-alt4_34
- use short alt-style fontdir name

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 20070327-alt3_34
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_24
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_21
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_20
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_19
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_18
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070327-alt3_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 20070327-alt2_15
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 20070327-alt2_14
- rebuild with new rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 20070327-alt1_14
- initial release by fcimport

