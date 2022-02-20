Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname ossobuffo-jura-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname ossobuffo-jura-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/ossobuffo/jura
%global commit      6e2614af65721fe74167b1f74b90e7bf5c0d0260
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/ossobuffo/jura
%global forgesource https://github.com/ossobuffo/jura/archive/6e2614af65721fe74167b1f74b90e7bf5c0d0260/jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260.tar.gz
%global archivename jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260
%global archiveext tar.gz
%global archiveurl https://github.com/ossobuffo/jura/archive/6e2614af65721fe74167b1f74b90e7bf5c0d0260/jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260.tar.gz
%global topdir jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260
%global extractdir jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260
%global repo jura
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 6e2614af65721fe74167b1f74b90e7bf5c0d0260
#global shortcommit %nil
#global branch %nil
%global version 5.103
#global date %nil
%global distprefix .git6e2614a
# FedoraForgeMeta2ALT: end generated meta

Version: 5.103
Release: alt1_7
URL:     %{forgeurl}

%global foundry           ossobuffo
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *html *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Jura
%global fontsummary       Jura, a sans-serif font family in the Eurostile vein
%global fonts             fonts/otf/*otf
%global fontdescription   \
Jura is a sans-serif font family in the Eurostile vein.

Source0:  %{forgesource}
Source10: 60-ossobuffo-jura-fonts.xml

Name:           fonts-otf-ossobuffo-jura
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
%setup -q -n jura-6e2614af65721fe74167b1f74b90e7bf5c0d0260
%linuxtext %{fontdocs} %{fontlicenses}
chmod 644 %{fontdocs} %{fontlicenses}

%build
# fontbuild 
fontnames=$(
  for font in 'fonts/otf/Jura-Bold.otf' 'fonts/otf/Jura-Light.otf' 'fonts/otf/Jura-Medium.otf' 'fonts/otf/Jura-Regular.otf' 'fonts/otf/Jura-SemiBold.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/Jura-Bold.otf' 'fonts/otf/Jura-Light.otf' 'fonts/otf/Jura-Medium.otf' 'fonts/otf/Jura-Regular.otf' 'fonts/otf/Jura-SemiBold.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the ossobuffo-jura-fonts appstream file"
cat > "org.altlinux.ossobuffo-jura-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.ossobuffo-jura-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>ossobuffo Jura</name>
  <summary><![CDATA[Jura, a sans-serif font family in the Eurostile vein]]></summary>
  <description>
    <p><![CDATA[Jura is a sans-serif font family in the Eurostile vein.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">%{forgeurl}</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing ossobuffo-jura-fonts
echo "" > "ossobuffo-jura-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/ossobuffo-jura/
echo "%%dir %_fontsdir/otf/ossobuffo-jura" >> "ossobuffo-jura-fonts.list"
install -m 0644 -vp "fonts/otf/Jura-Bold.otf" %buildroot%_fontsdir/otf/ossobuffo-jura/
echo \"%_fontsdir/otf/ossobuffo-jura//$(basename "fonts/otf/Jura-Bold.otf")\" >> 'ossobuffo-jura-fonts.list'
install -m 0644 -vp "fonts/otf/Jura-Light.otf" %buildroot%_fontsdir/otf/ossobuffo-jura/
echo \"%_fontsdir/otf/ossobuffo-jura//$(basename "fonts/otf/Jura-Light.otf")\" >> 'ossobuffo-jura-fonts.list'
install -m 0644 -vp "fonts/otf/Jura-Medium.otf" %buildroot%_fontsdir/otf/ossobuffo-jura/
echo \"%_fontsdir/otf/ossobuffo-jura//$(basename "fonts/otf/Jura-Medium.otf")\" >> 'ossobuffo-jura-fonts.list'
install -m 0644 -vp "fonts/otf/Jura-Regular.otf" %buildroot%_fontsdir/otf/ossobuffo-jura/
echo \"%_fontsdir/otf/ossobuffo-jura//$(basename "fonts/otf/Jura-Regular.otf")\" >> 'ossobuffo-jura-fonts.list'
install -m 0644 -vp "fonts/otf/Jura-SemiBold.otf" %buildroot%_fontsdir/otf/ossobuffo-jura/
echo \"%_fontsdir/otf/ossobuffo-jura//$(basename "fonts/otf/Jura-SemiBold.otf")\" >> 'ossobuffo-jura-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/Jura-Bold.otf' 'fonts/otf/Jura-Light.otf' 'fonts/otf/Jura-Medium.otf' 'fonts/otf/Jura-Regular.otf' 'fonts/otf/Jura-SemiBold.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "ossobuffo-jura-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "ossobuffo-jura-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.ossobuffo-jura-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "ossobuffo-jura-fonts.list"
done

for fontdoc in 'FONTLOG.txt' 'OFL-FAQ.txt' 'DESCRIPTION.en_us.html' 'COPYRIGHT.md' 'FONTLOG.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "ossobuffo-jura-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "ossobuffo-jura-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'ossobuffo-jura-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'ossobuffo-jura-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-ossobuffo-jura -f ossobuffo-jura-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc documentation/*

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 5.103-alt1_7
- new version

