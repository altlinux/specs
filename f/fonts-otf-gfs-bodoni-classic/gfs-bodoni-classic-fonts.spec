Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-bodoni-classic-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-bodoni-classic-fonts
# SPDX-License-Identifier: MIT
Version: 20070415
Release: alt4_33
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Bodoni Classic
%global fontsummary       GFS Bodoni Classic, an 18th century oblique Greek font family
%global fontpkgheader     \
Requires: font(gfsbodoni)\

%global fonts             *.otf
%global fontdescription   \
Giambattista Bodoni was the most prolific Italian type cutter of the 18th\
century. While he worked in the Vatican Press he was involved in the\
type cutting of a.'exotica.' languages for which catholic literature was printed.\
When he established his own press in Parma he did publish many books of the\
classics with his own Greek typefaces in the last quarter of the 18th century.\
He was among the first European type cutters to move away from the byzantine\
cursive tradition with the numerous ligatures which was the norm until then.\
His Greek types influenced many subsequent designers, yet they fell in disuse\
by the middle of the 19th century.\
\
GFS presented Bodonia.'s original Greek typeface in the commemorative edition of\
Pindara.'s Olympian Odes (2004), in digital version by George D. Matthiopoulos,\
and is now available as free ware for the general public. In the OpenType\
features, under ligatures, one may alternately use diphthongs with the accents\
placed in between the characters, as Giambattista Bodoni did when setting\
Greek texts.\


%global archivename GFS_Bodoni_Classic

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

Name:           fonts-otf-gfs-bodoni-classic
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description -n fonts-otf-gfs-bodoni-classic
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
  for font in 'GFSBodoniClassic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSBodoniClassic.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-bodoni-classic-fonts appstream file"
cat > "org.altlinux.gfs-bodoni-classic-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-bodoni-classic-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFSBodoni Classic</name>
  <summary><![CDATA[GFS Bodoni Classic, an 18th century oblique Greek font family]]></summary>
  <description>
    <p><![CDATA[Giambattista Bodoni was the most prolific Italian type cutter of the 18th]]></p><p><![CDATA[century. While he worked in the Vatican Press he was involved in the]]></p><p><![CDATA[type cutting of “exotic” languages for which catholic literature was printed.]]></p><p><![CDATA[When he established his own press in Parma he did publish many books of the]]></p><p><![CDATA[classics with his own Greek typefaces in the last quarter of the 18th century.]]></p><p><![CDATA[He was among the first European type cutters to move away from the byzantine]]></p><p><![CDATA[cursive tradition with the numerous ligatures which was the norm until then.]]></p><p><![CDATA[His Greek types influenced many subsequent designers, yet they fell in disuse]]></p><p><![CDATA[by the middle of the 19th century.]]></p> GFS presented Bodoni’s original Greek typeface in the commemorative edition of Pindar’s Olympian Odes (2004), in digital version by George D. Matthiopoulos, and is now available as free ware for the general public. In the OpenType features, under ligatures, one may alternately use diphthongs with the accents placed in between the characters, as Giambattista Bodoni did when setting
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/18th_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "gfs-bodoni-classic-fonts
echo "" > "gfs-bodoni-classic-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-bodoni-classic/
echo "%%dir %_fontsdir/otf/gfs-bodoni-classic" >> "gfs-bodoni-classic-fonts.list"
install -m 0644 -vp "GFSBodoniClassic.otf" %buildroot%_fontsdir/otf/gfs-bodoni-classic/
echo \"%_fontsdir/otf/gfs-bodoni-classic//$(basename "${font}")\" >> 'gfs-bodoni-classic-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSBodoniClassic.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-bodoni-classic-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-bodoni-classic-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-bodoni-classic-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-bodoni-classic-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt' 'OFL.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-bodoni-classic-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-bodoni-classic-fonts.list"
done

%check
# fontcheck
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-bodoni-classic-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-bodoni-classic-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-bodoni-classic -f gfs-bodoni-classic-fonts.list

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

