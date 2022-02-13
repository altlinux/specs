Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname impallari-raleway-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname impallari-raleway-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/alexeiva/Raleway
%global commit      98add575720aa077b7d253477e26c463a55e71da
%global forgeurl https://github.com/alexeiva/Raleway
%global forgesource https://github.com/alexeiva/Raleway/archive/98add575720aa077b7d253477e26c463a55e71da/Raleway-98add575720aa077b7d253477e26c463a55e71da.tar.gz
%global archivename Raleway-98add575720aa077b7d253477e26c463a55e71da
%global archiveext tar.gz
%global archiveurl https://github.com/alexeiva/Raleway/archive/98add575720aa077b7d253477e26c463a55e71da/Raleway-98add575720aa077b7d253477e26c463a55e71da.tar.gz
%global topdir Raleway-98add575720aa077b7d253477e26c463a55e71da
%global extractdir Raleway-98add575720aa077b7d253477e26c463a55e71da
%global repo Raleway
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 98add575720aa077b7d253477e26c463a55e71da
#global shortcommit %nil
#global branch %nil
%global version 4.025
#global date %nil
%global distprefix .git98add57

Version: 4.025
Release: alt1_9
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Raleway
%global fontsummary       Raleway, an elegant sans-serif font family
%global fonts             fonts/TTF/*ttf
%global fontdescription   \
Raleway is an elegant sans-serif font family intended for headings and other\
large size usage.\
\
It features both old style and lining numerals, standard and discretionary\
ligatures, a pretty complete set of diacritics, as well as a stylistic\
alternate inspired by more geometric sans-serif typefaces than its\
neo-grotesque inspired default character set.

Source0:  %{forgesource}
Source10: 58-impallari-raleway-fonts.xml

Name:           fonts-ttf-impallari-raleway
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%package doc
Group: System/Fonts/True type
Summary:   Optional documentation files of %{fontpkgname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{fontpkgname}.

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n Raleway-98add575720aa077b7d253477e26c463a55e71da
%linuxtext %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/TTF/Raleway-Black.ttf' 'fonts/TTF/Raleway-BlackItalic.ttf' 'fonts/TTF/Raleway-Bold.ttf' 'fonts/TTF/Raleway-BoldItalic.ttf' 'fonts/TTF/Raleway-ExtraBold.ttf' 'fonts/TTF/Raleway-ExtraBoldItalic.ttf' 'fonts/TTF/Raleway-ExtraLight.ttf' 'fonts/TTF/Raleway-ExtraLightItalic.ttf' 'fonts/TTF/Raleway-Italic.ttf' 'fonts/TTF/Raleway-Light.ttf' 'fonts/TTF/Raleway-LightItalic.ttf' 'fonts/TTF/Raleway-Medium.ttf' 'fonts/TTF/Raleway-MediumItalic.ttf' 'fonts/TTF/Raleway-Regular.ttf' 'fonts/TTF/Raleway-SemiBold.ttf' 'fonts/TTF/Raleway-SemiBoldItalic.ttf' 'fonts/TTF/Raleway-Thin.ttf' 'fonts/TTF/Raleway-ThinItalic.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/TTF/Raleway-Black.ttf' 'fonts/TTF/Raleway-BlackItalic.ttf' 'fonts/TTF/Raleway-Bold.ttf' 'fonts/TTF/Raleway-BoldItalic.ttf' 'fonts/TTF/Raleway-ExtraBold.ttf' 'fonts/TTF/Raleway-ExtraBoldItalic.ttf' 'fonts/TTF/Raleway-ExtraLight.ttf' 'fonts/TTF/Raleway-ExtraLightItalic.ttf' 'fonts/TTF/Raleway-Italic.ttf' 'fonts/TTF/Raleway-Light.ttf' 'fonts/TTF/Raleway-LightItalic.ttf' 'fonts/TTF/Raleway-Medium.ttf' 'fonts/TTF/Raleway-MediumItalic.ttf' 'fonts/TTF/Raleway-Regular.ttf' 'fonts/TTF/Raleway-SemiBold.ttf' 'fonts/TTF/Raleway-SemiBoldItalic.ttf' 'fonts/TTF/Raleway-Thin.ttf' 'fonts/TTF/Raleway-ThinItalic.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the impallari-raleway-fonts appstream file"
cat > "org.altlinux.impallari-raleway-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.impallari-raleway-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Impallari Raleway</name>
  <summary><![CDATA[Raleway, an elegant sans-serif font family]]></summary>
  <description>
    <p><![CDATA[Raleway is an elegant sans-serif font family intended for headings and other]]></p><p><![CDATA[large size usage.]]></p> It features both old style and lining numerals, standard and discretionary ligatures, a pretty complete set of diacritics, as well as a stylistic alternate inspired by more geometric sans-serif typefaces than its neo-grotesque inspired default character set.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing impallari-raleway-fonts
echo "" > "impallari-raleway-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/impallari-raleway/
echo "%%dir %_fontsdir/ttf/impallari-raleway" >> "impallari-raleway-fonts.list"
install -m 0644 -vp "fonts/TTF/Raleway-Black.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Black.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-BlackItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-BlackItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Bold.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Bold.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-BoldItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-BoldItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-ExtraBold.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-ExtraBold.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-ExtraBoldItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-ExtraBoldItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-ExtraLight.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-ExtraLight.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-ExtraLightItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-ExtraLightItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Italic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Italic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Light.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Light.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-LightItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-LightItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Medium.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Medium.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-MediumItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-MediumItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Regular.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Regular.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-SemiBold.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-SemiBold.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-SemiBoldItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-SemiBoldItalic.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-Thin.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-Thin.ttf")\" >> 'impallari-raleway-fonts.list'
install -m 0644 -vp "fonts/TTF/Raleway-ThinItalic.ttf" %buildroot%_fontsdir/ttf/impallari-raleway/
echo \"%_fontsdir/ttf/impallari-raleway//$(basename "fonts/TTF/Raleway-ThinItalic.ttf")\" >> 'impallari-raleway-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/TTF/Raleway-Black.ttf' 'fonts/TTF/Raleway-BlackItalic.ttf' 'fonts/TTF/Raleway-Bold.ttf' 'fonts/TTF/Raleway-BoldItalic.ttf' 'fonts/TTF/Raleway-ExtraBold.ttf' 'fonts/TTF/Raleway-ExtraBoldItalic.ttf' 'fonts/TTF/Raleway-ExtraLight.ttf' 'fonts/TTF/Raleway-ExtraLightItalic.ttf' 'fonts/TTF/Raleway-Italic.ttf' 'fonts/TTF/Raleway-Light.ttf' 'fonts/TTF/Raleway-LightItalic.ttf' 'fonts/TTF/Raleway-Medium.ttf' 'fonts/TTF/Raleway-MediumItalic.ttf' 'fonts/TTF/Raleway-Regular.ttf' 'fonts/TTF/Raleway-SemiBold.ttf' 'fonts/TTF/Raleway-SemiBoldItalic.ttf' 'fonts/TTF/Raleway-Thin.ttf' 'fonts/TTF/Raleway-ThinItalic.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "impallari-raleway-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "impallari-raleway-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.impallari-raleway-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "impallari-raleway-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'FONTLOG.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "impallari-raleway-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "impallari-raleway-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'impallari-raleway-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'impallari-raleway-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-impallari-raleway -f impallari-raleway-fonts.list
%files doc
%doc --no-dereference OFL.txt
%doc documents/*

%changelog
* Sun Feb 13 2022 Igor Vlasenko <viy@altlinux.org> 4.025-alt1_9
- new version, switched to ttf

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_3.git20161116.6c67ab1
- update to new release by fcimport

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2.git20161116.6c67ab1.1
- new version

