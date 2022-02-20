Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-galatea-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-galatea-fonts
# SPDX-License-Identifier: MIT
Version: 20191205
Release: alt1_4
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Galatea
%global fontsummary       GFS Galatea, a 20th century Greek font family
%global fonts             *.otf
%global fontdescription   \
GFS Galatea Bold revives in digital form an older hot metal typeface from the\
1920a.'s, which can be found in older Greek type specimens named simply as FAT\
type. The font was used as a bold companion of Didot Greek (Apla/Monotype 92).\
It has many similarities with Didot Greek (I.I.I.I.) in design, but it differs in\
its reduced stroke contrast, the use of a lunar lower case epsilon (reminiscent\
of the similar epsilon in Porson Greek) and in sturdier stems and slab serifs.\
An experimental projection of these characteristics to a lighter version has\
led to the introduction of GFS Galatea Regular. The name Galatea is a tribute\
to the author and feminist Galatea Kazantzakis (1881a..1962) as samples of the\
typeface were found in several of her books.\
\
Both typefaces were designed by George Triantafyllakos and are freely available\
for use.

%global archivename GFS_Galatea

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-gfs-galatea-fonts.xml

Name:           fonts-otf-gfs-galatea
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
  for font in 'GFS_Galatea.otf' 'GFS_Galatea_Bold.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFS_Galatea.otf' 'GFS_Galatea_Bold.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-galatea-fonts appstream file"
cat > "org.altlinux.gfs-galatea-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-galatea-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS Galatea</name>
  <summary><![CDATA[GFS Galatea, a 20th century Greek font family]]></summary>
  <description>
    <p><![CDATA[GFS Galatea Bold revives in digital form an older hot metal typeface from the]]></p><p><![CDATA[1920’s, which can be found in older Greek type specimens named simply as FAT]]></p><p><![CDATA[type. The font was used as a bold companion of Didot Greek (Apla/Monotype 92).]]></p><p><![CDATA[It has many similarities with Didot Greek (Απλά) in design, but it differs in]]></p><p><![CDATA[its reduced stroke contrast, the use of a lunar lower case epsilon (reminiscent]]></p><p><![CDATA[of the similar epsilon in Porson Greek) and in sturdier stems and slab serifs.]]></p><p><![CDATA[An experimental projection of these characteristics to a lighter version has]]></p><p><![CDATA[led to the introduction of GFS Galatea Regular. The name Galatea is a tribute]]></p><p><![CDATA[to the author and feminist Galatea Kazantzakis (1881–1962) as samples of the]]></p><p><![CDATA[typeface were found in several of her books.]]></p> Both typefaces were designed by George Triantafyllakos and are freely available for use.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing gfs-galatea-fonts
echo "" > "gfs-galatea-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-galatea/
echo "%%dir %_fontsdir/otf/gfs-galatea" >> "gfs-galatea-fonts.list"
install -m 0644 -vp "GFS_Galatea.otf" %buildroot%_fontsdir/otf/gfs-galatea/
echo \"%_fontsdir/otf/gfs-galatea//$(basename "GFS_Galatea.otf")\" >> 'gfs-galatea-fonts.list'
install -m 0644 -vp "GFS_Galatea_Bold.otf" %buildroot%_fontsdir/otf/gfs-galatea/
echo \"%_fontsdir/otf/gfs-galatea//$(basename "GFS_Galatea_Bold.otf")\" >> 'gfs-galatea-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFS_Galatea.otf' 'GFS_Galatea_Bold.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-galatea-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-galatea-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-galatea-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-galatea-fonts.list"
done

for fontdoc in 'OFL-FAQ.txt'; do
  echo %%doc "'${fontdoc}'" >> "gfs-galatea-fonts.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "gfs-galatea-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-galatea-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-galatea-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-galatea -f gfs-galatea-fonts.list

%files doc
%doc --no-dereference OFL.txt
%doc *.pdf

%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 20191205-alt1_4
- new version

