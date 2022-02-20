Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-didot-display-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-didot-display-fonts
# SPDX-License-Identifier: MIT
Version: 20160225
Release: alt1_4
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Didot Display
%global fontsummary       GFS Didot Display, a 20th century Greek decorative font family
%global fontpkgheader     \
Requires: font(gfsdidot)\

%global fonts             *.otf
%global fontdescription \
GFS Didot Display is a fat version of the Greek Didot. Found in several\
publications, mainly as a headline font since the 1840s. At certain occasions\
it was used in text columns for newspaper typesetting. The typeface was\
digitized by George Triantafyllakos based on samples found in Greek newspapers\
from the a.'50s and from the Specimens Catalogue of Linotype Co.

%global archivename GFS_Didot_Display

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 65-gfs-didot-display-fonts.xml

Name:           fonts-otf-gfs-didot-display
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
  for font in 'GFS_Didot_Display.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFS_Didot_Display.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-didot-display-fonts appstream file"
cat > "org.altlinux.gfs-didot-display-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-didot-display-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Didot Display</name>
  <summary><![CDATA[GFS Didot Display, a 20th century Greek decorative font family]]></summary>
  <description>
    <p><![CDATA[GFS Didot Display is a fat version of the Greek Didot. Found in several]]></p><p><![CDATA[publications, mainly as a headline font since the 1840s. At certain occasions]]></p><p><![CDATA[it was used in text columns for newspaper typesetting. The typeface was]]></p><p><![CDATA[digitized by George Triantafyllakos based on samples found in Greek newspapers]]></p><p><![CDATA[from the ’50s and from the Specimens Catalogue of Linotype Co.]]></p>
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing gfs-didot-display-fonts
echo "" > "gfs-didot-display-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-didot-display/
echo "%%dir %_fontsdir/otf/gfs-didot-display" >> "gfs-didot-display-fonts.list"
install -m 0644 -vp "GFS_Didot_Display.otf" %buildroot%_fontsdir/otf/gfs-didot-display/
echo \"%_fontsdir/otf/gfs-didot-display//$(basename "GFS_Didot_Display.otf")\" >> 'gfs-didot-display-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFS_Didot_Display.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-didot-display-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-didot-display-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-didot-display-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-didot-display-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-didot-display-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-didot-display-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-didot-display-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-didot-display-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-didot-display -f gfs-didot-display-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 20160225-alt1_4
- new version

