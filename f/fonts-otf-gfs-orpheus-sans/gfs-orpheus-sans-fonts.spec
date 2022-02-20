Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-orpheus-sans-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-orpheus-sans-fonts
# SPDX-License-Identifier: MIT
Version: 20161102
Release: alt1_4
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Orpheus Sans
%global fontsummary       GFS Orpheus Sans, a 21st century mono-linear Greek font family
%global fontpkgheader     \
#Suggests: font(gfsorpheus)\

%global fonts             *.otf
%global fontdescription   \
GFS Orpheus Sans is a mono-linear version of GFS Orpheus. The experiment of\
designing a mono-linear typeface based on the original, contrasted typeface,\
clearly shows the innovative design ideas that were incorporated in the\
original typeface; ideas similar to those of a modern sans serif typeface with\
clean mono-linear strokes and balanced proportions.\
\
GFS Orpheus Sans was designed by George Triantafyllakos.

%global archivename GFS_Orpheus_Sans

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-gfs-orpheus-sans-fonts.xml

Name:           fonts-otf-gfs-orpheus-sans
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
  for font in 'GFS_Orpheus_Sans.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFS_Orpheus_Sans.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-orpheus-sans-fonts appstream file"
cat > "org.altlinux.gfs-orpheus-sans-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-orpheus-sans-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Orpheus Sans</name>
  <summary><![CDATA[GFS Orpheus Sans, a 21st century mono-linear Greek font family]]></summary>
  <description>
    <p><![CDATA[GFS Orpheus Sans is a mono-linear version of GFS Orpheus. The experiment of]]></p><p><![CDATA[designing a mono-linear typeface based on the original, contrasted typeface,]]></p><p><![CDATA[clearly shows the innovative design ideas that were incorporated in the]]></p><p><![CDATA[original typeface; ideas similar to those of a modern sans serif typeface with]]></p><p><![CDATA[clean mono-linear strokes and balanced proportions.]]></p> GFS Orpheus Sans was designed by George Triantafyllakos.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing gfs-orpheus-sans-fonts
echo "" > "gfs-orpheus-sans-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-orpheus-sans/
echo "%%dir %_fontsdir/otf/gfs-orpheus-sans" >> "gfs-orpheus-sans-fonts.list"
install -m 0644 -vp "GFS_Orpheus_Sans.otf" %buildroot%_fontsdir/otf/gfs-orpheus-sans/
echo \"%_fontsdir/otf/gfs-orpheus-sans//$(basename "GFS_Orpheus_Sans.otf")\" >> 'gfs-orpheus-sans-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFS_Orpheus_Sans.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-orpheus-sans-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-orpheus-sans-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-orpheus-sans-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-orpheus-sans-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-orpheus-sans-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-orpheus-sans-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-orpheus-sans-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-orpheus-sans-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-orpheus-sans -f gfs-orpheus-sans-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 20161102-alt1_4
- new version

