Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname abattis-cantarell-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname abattis-cantarell-fonts
Version: 0.301
Release: alt1_7
URL: https://gitlab.gnome.org/GNOME/cantarell-fonts/

%global	common_description	\
The Cantarell font family is a contemporary Humanist sans serif\
designed for on-screen reading. The fonts were originally designed\
by Dave Crossland.

%global	foundry		abattis
%global	fontlicense	OFL
%global	fontlicenses	COPYING
%global	fontdocs	NEWS README.md
%global	fontdocsex	%{fontlicenses}

%global	fontfamily0	Cantarell
%global	fontsummary0	Humanist sans serif font
%global	fonts0		prebuilt/Cantarell-*.otf
%global	fontsex0	prebuilt/Cantarell-VF.otf
%global	fontdescription0	\
%{common_description}\
\
This package contains the non-variable font version of the Cantarell font.

%global	fontfamily1	Cantarell-VF
%global	fontsummary1	Humanist sans serif font (variable)
%global	fonts1		prebuilt/Cantarell-VF.otf
%global fontdescription1	\
%{common_description}\
\
This package contains the variable font version of the Cantarell font.

Source0: http://download.gnome.org/sources/cantarell-fonts/0.301/cantarell-fonts-%{version}.tar.xz
Source1: 31-cantarell.conf
Source2: 31-cantarell-vf.conf

BuildRequires: gettext gettext-tools
BuildRequires: meson

Name:           fonts-otf-abattis-cantarell
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-otf-abattis-cantarell-vf
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-otf-abattis-cantarell-vf
%{?fontdescription1}

%prep
%global	fontconfs0	%{SOURCE1}
%global	fontconfs1	%{SOURCE2}
%setup -q -n cantarell-fonts-%{version}


%build
%meson
%meson_build
# fontbuild 0
fontnames=$(
  for font in 'prebuilt/Cantarell-Bold.otf' 'prebuilt/Cantarell-ExtraBold.otf' 'prebuilt/Cantarell-Light.otf' 'prebuilt/Cantarell-Regular.otf' 'prebuilt/Cantarell-Thin.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'prebuilt/Cantarell-Bold.otf' 'prebuilt/Cantarell-ExtraBold.otf' 'prebuilt/Cantarell-Light.otf' 'prebuilt/Cantarell-Regular.otf' 'prebuilt/Cantarell-Thin.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the abattis-cantarell-fonts appstream file"
cat > "org.altlinux.abattis-cantarell-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.abattis-cantarell-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>abattis Cantarell</name>
  <summary><![CDATA[Humanist sans serif font]]></summary>
  <description>
    
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://gitlab.gnome.org/GNOME/cantarell-fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'prebuilt/Cantarell-VF.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'prebuilt/Cantarell-VF.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the abattis-cantarell-vf-fonts appstream file"
cat > "org.altlinux.abattis-cantarell-vf-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.abattis-cantarell-vf-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>abattis Cantarell-VF</name>
  <summary><![CDATA[Humanist sans serif font (variable)]]></summary>
  <description>
    <p><![CDATA[The Cantarell font family is a contemporary Humanist sans serif]]></p><p><![CDATA[designed for on-screen reading. The fonts were originally designed]]></p><p><![CDATA[by Dave Crossland.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://gitlab.gnome.org/GNOME/cantarell-fonts/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "abattis-cantarell-fonts
echo "" > "abattis-cantarell-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/abattis-cantarell/
echo "%%dir %_fontsdir/otf/abattis-cantarell" >> "abattis-cantarell-fonts0.list"
install -m 0644 -vp "prebuilt/Cantarell-Bold.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-Bold.otf")\" >> 'abattis-cantarell-fonts0.list'
install -m 0644 -vp "prebuilt/Cantarell-ExtraBold.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-ExtraBold.otf")\" >> 'abattis-cantarell-fonts0.list'
install -m 0644 -vp "prebuilt/Cantarell-Light.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-Light.otf")\" >> 'abattis-cantarell-fonts0.list'
install -m 0644 -vp "prebuilt/Cantarell-Regular.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-Regular.otf")\" >> 'abattis-cantarell-fonts0.list'
install -m 0644 -vp "prebuilt/Cantarell-Thin.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-Thin.otf")\" >> 'abattis-cantarell-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE1' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "abattis-cantarell-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "abattis-cantarell-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.abattis-cantarell-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "abattis-cantarell-fonts0.list"
done

for fontdoc in 'NEWS' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "abattis-cantarell-fonts0.list"
done

for fontlicense in 'COPYING'; do
  echo %%doc "'${fontlicense}'" >> "abattis-cantarell-fonts0.list"
done
echo "Installing "abattis-cantarell-vf-fonts
echo "" > "abattis-cantarell-vf-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/abattis-cantarell/
echo "%%dir %_fontsdir/otf/abattis-cantarell" >> "abattis-cantarell-vf-fonts1.list"
install -m 0644 -vp "prebuilt/Cantarell-VF.otf" %buildroot%_fontsdir/otf/abattis-cantarell/
echo \"%_fontsdir/otf/abattis-cantarell//$(basename "prebuilt/Cantarell-VF.otf")\" >> 'abattis-cantarell-vf-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE2' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "abattis-cantarell-vf-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "abattis-cantarell-vf-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.abattis-cantarell-vf-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "abattis-cantarell-vf-fonts1.list"
done

for fontdoc in 'NEWS' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "abattis-cantarell-vf-fonts1.list"
done

for fontlicense in 'COPYING'; do
  echo %%doc "'${fontlicense}'" >> "abattis-cantarell-vf-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'abattis-cantarell-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'abattis-cantarell-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'abattis-cantarell-vf-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'abattis-cantarell-vf-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-abattis-cantarell -f abattis-cantarell-fonts0.list
%files -n fonts-otf-abattis-cantarell-vf -f abattis-cantarell-vf-fonts1.list

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 0.301-alt1_7
- update

* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 0.301-alt1_5
- update to new release by fcimport

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 0.301-alt1_4
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.301-alt1_1
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.201-alt1_4
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.201-alt1_2
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.111-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.101-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.25-alt1_3
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.18-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.17.2-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.16-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.16-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_2
- update to new release by fcimport

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_0
- new version

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.14-alt1_1
- fc import

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_2
- update to new release by fcimport

* Mon Jun 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_2
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_1
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.11-alt1_1
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.10.1-alt1_1
- update to new release by fcimport

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_1
- update to new release by fcimport

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2_1
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_1
- initial release by fcimport

