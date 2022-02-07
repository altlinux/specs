Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ht-alegreya-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ht-alegreya-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/huertatipografica/Alegreya
Version: 2.008
%global forgeurl https://github.com/huertatipografica/Alegreya
%global forgesource https://github.com/huertatipografica/Alegreya/archive/2.008/Alegreya-2.008.tar.gz
%global archivename Alegreya-2.008
%global archiveext tar.gz
%global archiveurl https://github.com/huertatipografica/Alegreya/archive/2.008/Alegreya-2.008.tar.gz
%global topdir Alegreya-2.008
%global extractdir Alegreya-2.008
%global repo Alegreya
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 2.008
#global date %nil
#global distprefix %nil

Release: alt1_9
URL:     https://www.huertatipografica.com/en/fonts/alegreya-ht-pro

%global foundry           HT
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Alegreya
%global fontsummary       Alegreya, a dynamic and varied serif font family
%global fontpkgheader     \
# Small Caps are accessible in the main family using OpenType features\
Obsoletes: ht-alegreya-smallcaps-fonts < %{version}-%{release}\

%global fonts             fonts/otf/*otf
%global fontsex           fonts/otf/*SC*otf
%global fontdescription   \
Alegreya is a font family originally intended for literature. Among its\
crowning characteristics, it conveys a dynamic and varied rhythm which\
facilitates the reading of long texts. Also, it provides freshness to the page\
while referring to the calligraphic letter, not as a literal interpretation,\
but rather in a contemporary typographic language.\
\
The italic has just as much care and attention to detail in the design as the\
roman. The bold weights are strong, and the Black weights are really\
experimental for the genre.\
\
Not only does Alegreya provide great performance, but also achieves a strong\
and harmonious text by means of elements designed in an atmosphere of\
diversity.\
\
Alegreya was chosen as one of 53 a.'Fonts of the Decadea.' at the ATypI Letter2\
competition in September 2011, and one of the top 14 text type systems. It was\
also selected in the 2nd Bienal Iberoamericana de DiseA.o, competition held in\
Madrid in 2010.

Source0:  %{forgesource}
Source10: 58-ht-alegreya-fonts.conf

Name:           fonts-otf-ht-alegreya
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfs         %{SOURCE10}
%setup -q -n Alegreya-2.008

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/Alegreya-Black.otf' 'fonts/otf/Alegreya-BlackItalic.otf' 'fonts/otf/Alegreya-Bold.otf' 'fonts/otf/Alegreya-BoldItalic.otf' 'fonts/otf/Alegreya-ExtraBold.otf' 'fonts/otf/Alegreya-ExtraBoldItalic.otf' 'fonts/otf/Alegreya-Italic.otf' 'fonts/otf/Alegreya-Medium.otf' 'fonts/otf/Alegreya-MediumItalic.otf' 'fonts/otf/Alegreya-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Alegreya-Black.otf' 'fonts/otf/Alegreya-BlackItalic.otf' 'fonts/otf/Alegreya-Bold.otf' 'fonts/otf/Alegreya-BoldItalic.otf' 'fonts/otf/Alegreya-ExtraBold.otf' 'fonts/otf/Alegreya-ExtraBoldItalic.otf' 'fonts/otf/Alegreya-Italic.otf' 'fonts/otf/Alegreya-Medium.otf' 'fonts/otf/Alegreya-MediumItalic.otf' 'fonts/otf/Alegreya-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ht-alegreya-fonts appstream file"
cat > "org.altlinux.ht-alegreya-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ht-alegreya-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>HT Alegreya</name>
  <summary><![CDATA[Alegreya, a dynamic and varied serif font family]]></summary>
  <description>
    <p><![CDATA[Alegreya is a font family originally intended for literature. Among its]]></p><p><![CDATA[crowning characteristics, it conveys a dynamic and varied rhythm which]]></p><p><![CDATA[facilitates the reading of long texts. Also, it provides freshness to the page]]></p><p><![CDATA[while referring to the calligraphic letter, not as a literal interpretation,]]></p><p><![CDATA[but rather in a contemporary typographic language.]]></p> The italic has just as much care and attention to detail in the design as the roman. The bold weights are strong, and the Black weights are really experimental for the genre. Not only does Alegreya provide great performance, but also achieves a strong and harmonious text by means of elements designed in an atmosphere of diversity. Alegreya was chosen as one of 53 “Fonts of the Decade” at the ATypI Letter2 competition in September 2011, and one of the top 14 text type systems. It was also selected in the 2nd Bienal Iberoamericana de Diseño, competition held in
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.huertatipografica.com/en/fonts/alegreya-ht-pro</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo "Installing "ht-alegreya-fonts
echo "" > "ht-alegreya-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ht-alegreya/
echo "%%dir %_fontsdir/otf/ht-alegreya" >> "ht-alegreya-fonts.list"
install -m 0644 -vp "fonts/otf/Alegreya-Black.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-Black.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-BlackItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-BlackItalic.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-Bold.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-Bold.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-BoldItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-BoldItalic.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-ExtraBold.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-ExtraBold.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-ExtraBoldItalic.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-Italic.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-Italic.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-Medium.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-Medium.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-MediumItalic.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-MediumItalic.otf")\" >> 'ht-alegreya-fonts.list'
install -m 0644 -vp "fonts/otf/Alegreya-Regular.otf" %buildroot%_fontsdir/otf/ht-alegreya/
echo \"%_fontsdir/otf/ht-alegreya//$(basename "fonts/otf/Alegreya-Regular.otf")\" >> 'ht-alegreya-fonts.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ht-alegreya-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ht-alegreya-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ht-alegreya-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ht-alegreya-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'LICENSE.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "ht-alegreya-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "ht-alegreya-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ht-alegreya-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ht-alegreya-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ht-alegreya -f ht-alegreya-fonts.list

%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 2.008-alt1_9
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_5
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_4
- update to new release by fcimport

* Wed Apr 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_2
- converted for ALT Linux by srpmconvert tools

* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_1
- fc import

