Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname impallari-dancing-script-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname impallari-dancing-script-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/impallari/DancingScript
%global commit      f7f54bc1b8836601dae8696666bfacd306f77e34
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/impallari/DancingScript
%global forgesource https://github.com/impallari/DancingScript/archive/f7f54bc1b8836601dae8696666bfacd306f77e34/DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34.tar.gz
%global archivename DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34
%global archiveext tar.gz
%global archiveurl https://github.com/impallari/DancingScript/archive/f7f54bc1b8836601dae8696666bfacd306f77e34/DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34.tar.gz
%global topdir DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34
%global extractdir DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34
%global repo DancingScript
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit f7f54bc1b8836601dae8696666bfacd306f77e34
#global shortcommit %nil
#global branch %nil
%global version 2.000
#global date %nil
%global distprefix .gitf7f54bc
# FedoraForgeMeta2ALT: end generated meta

Version: 2.000
Release: alt1_8
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md *.html
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dancing Script
%global fontsummary       Dancing Script, a friendly, informal and spontaneous cursive font family
%global fonts             fonts/otf/*otf
%global fontdescription   \
Dancing Script is a lively casual script where the letters bounce and change\
size slightly. Caps are big, and goes below the baseline.\
\
Dancing Script references popular scripts typefaces from the 50a.'s. It relates\
to Murray Hill (Emil Klumpp. 1956) in his weight distribution, and to Mistral\
(Roger Excoffon. 1953) in his lively bouncing effect.\
\
Use it when you want a friendly, informal and spontaneous look.

Source0:  %{forgesource}
Source10: 57-impallari-dancing-script-fonts.xml

Name:           fonts-otf-impallari-dancing-script
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader}
Source44: import.info
%description
%{?fontdescription}

%prep
%global fontconfngs       %{SOURCE10}
%setup -q -n DancingScript-f7f54bc1b8836601dae8696666bfacd306f77e34
%linuxtext %{fontdocs}
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/DancingScript-Bold.otf' 'fonts/otf/DancingScript-Regular.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/DancingScript-Bold.otf' 'fonts/otf/DancingScript-Regular.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the impallari-dancing-script-fonts appstream file"
cat > "org.altlinux.impallari-dancing-script-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.impallari-dancing-script-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>Impallari Dancing Script</name>
  <summary><![CDATA[Dancing Script, a friendly, informal and spontaneous cursive font family]]></summary>
  <description>
    <p><![CDATA[Dancing Script is a lively casual script where the letters bounce and change]]></p><p><![CDATA[size slightly. Caps are big, and goes below the baseline.]]></p> Dancing Script references popular scripts typefaces from the 50’s. It relates to Murray Hill (Emil Klumpp. 1956) in his weight distribution, and to Mistral (Roger Excoffon. 1953) in his lively bouncing effect. Use it when you want a friendly, informal and spontaneous look.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing impallari-dancing-script-fonts
echo "" > "impallari-dancing-script-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/impallari-dancing-script/
echo "%%dir %_fontsdir/otf/impallari-dancing-script" >> "impallari-dancing-script-fonts.list"
install -m 0644 -vp "fonts/otf/DancingScript-Bold.otf" %buildroot%_fontsdir/otf/impallari-dancing-script/
echo \"%_fontsdir/otf/impallari-dancing-script//$(basename "fonts/otf/DancingScript-Bold.otf")\" >> 'impallari-dancing-script-fonts.list'
install -m 0644 -vp "fonts/otf/DancingScript-Regular.otf" %buildroot%_fontsdir/otf/impallari-dancing-script/
echo \"%_fontsdir/otf/impallari-dancing-script//$(basename "fonts/otf/DancingScript-Regular.otf")\" >> 'impallari-dancing-script-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/DancingScript-Bold.otf' 'fonts/otf/DancingScript-Regular.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "impallari-dancing-script-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "impallari-dancing-script-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.impallari-dancing-script-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "impallari-dancing-script-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'FONTLOG.txt' 'README.md' 'DESCRIPTION.en_us.html'; do
  echo %%doc "'${fontdoc}'" >> "impallari-dancing-script-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "impallari-dancing-script-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'impallari-dancing-script-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'impallari-dancing-script-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-impallari-dancing-script -f impallari-dancing-script-fonts.list

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 2.000-alt1_8
- new version

