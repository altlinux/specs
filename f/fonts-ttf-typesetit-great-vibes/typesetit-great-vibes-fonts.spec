Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname typesetit-great-vibes-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname typesetit-great-vibes-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/GreatVibesFont
%global commit      a82e16d27e13b0d1337abeab05fdfd99a51d044c
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/googlefonts/GreatVibesFont
%global forgesource https://github.com/googlefonts/GreatVibesFont/archive/a82e16d27e13b0d1337abeab05fdfd99a51d044c/GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c.tar.gz
%global archivename GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c
%global archiveext tar.gz
%global archiveurl https://github.com/googlefonts/GreatVibesFont/archive/a82e16d27e13b0d1337abeab05fdfd99a51d044c/GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c.tar.gz
%global topdir GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c
%global extractdir GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c
%global repo GreatVibesFont
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit a82e16d27e13b0d1337abeab05fdfd99a51d044c
#global shortcommit %nil
#global branch %nil
%global version 1.101
#global date %nil
%global distprefix .gita82e16d
# FedoraForgeMeta2ALT: end generated meta

Version: 1.101
Release: alt1_4
URL:     %{forgeurl}

%global foundry           TypeSETit
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Great Vibes
%global fontsummary       Great Vibes, a beautifully flowing cursive font family
%global fonts             fonts/*ttf
%global fontdescription   \
Great Vibes is a beautifully flowing connecting cursive font family. It has\
cleanly looping ascenders and descenders as well as elegant uppercase forms.

Source0:  %{forgesource}
Source10: 57-typesetit-great-vibes-fonts.xml

Name:           fonts-ttf-typesetit-great-vibes
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
%setup -q -n GreatVibesFont-a82e16d27e13b0d1337abeab05fdfd99a51d044c

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/GreatVibes-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/GreatVibes-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the typesetit-great-vibes-fonts appstream file"
cat > "org.altlinux.typesetit-great-vibes-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.typesetit-great-vibes-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>TypeSETit Great Vibes</name>
  <summary><![CDATA[Great Vibes, a beautifully flowing cursive font family]]></summary>
  <description>
    <p><![CDATA[Great Vibes is a beautifully flowing connecting cursive font family. It has]]></p><p><![CDATA[cleanly looping ascenders and descenders as well as elegant uppercase forms.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing typesetit-great-vibes-fonts
echo "" > "typesetit-great-vibes-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/typesetit-great-vibes/
echo "%%dir %_fontsdir/ttf/typesetit-great-vibes" >> "typesetit-great-vibes-fonts.list"
install -m 0644 -vp "fonts/GreatVibes-Regular.ttf" %buildroot%_fontsdir/ttf/typesetit-great-vibes/
echo \"%_fontsdir/ttf/typesetit-great-vibes//$(basename "fonts/GreatVibes-Regular.ttf")\" >> 'typesetit-great-vibes-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/GreatVibes-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "typesetit-great-vibes-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "typesetit-great-vibes-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.typesetit-great-vibes-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "typesetit-great-vibes-fonts.list"
done

for fontdoc in 'AUTHORS.txt' 'CONTRIBUTORS.txt' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "typesetit-great-vibes-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "typesetit-great-vibes-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'typesetit-great-vibes-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'typesetit-great-vibes-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-typesetit-great-vibes -f typesetit-great-vibes-fonts.list

%changelog
* Tue Feb 15 2022 Igor Vlasenko <viy@altlinux.org> 1.101-alt1_4
- new version

