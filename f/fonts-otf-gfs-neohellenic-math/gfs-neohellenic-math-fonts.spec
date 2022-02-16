Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts unzip
# END SourceDeps(oneline)
%define oldname gfs-neohellenic-math-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname gfs-neohellenic-math-fonts
# SPDX-License-Identifier: MIT
Version: 20180227
Release: alt1_4
URL:     https://www.greekfontsociety-gfs.gr/typefaces/Math

%global foundry           GFS
%global fontlicense       OFL
# GFS already forgot about providing clean licensing texts
%global fontlicenses      README
%global fontdocs          README

%global fontfamily        NeoHellenic Math
%global fontsummary       GFS NeoHellenic Math, an almost Sans Serif Math font family
%global fontpkgheader     \
Requires:    fonts-otf-gfs-neohellenic\

%global fonts             *.otf
%global fontdescription   \
GFS NeoHellenic Math is an almost Sans Serif font family. One of its main uses\
is for presentations, an area where (we believe) a commercial grade sans math\
font was not available up to now.\
\
The font family contains an extended glyph set including more than the standard\
math symbols such as vertically extended integrals, chess symbols, etc.\
\
It was commissioned to the Greek Font Society (GFS) by the Graduate Studies\
program a.'Studies in Mathematicsa.' of the Department of Mathematics of the\
University of the Aegean, located on the Samos island, Greece.\
\
The design copyright belongs to the main designer of GFS, George Matthiopoulos.\
The OpenType Math Table embedded in the font was developed by the Mathematics\
Professor Antonis Tsolomitis.

%global archivename GFS_NeoHellenic_Math

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-gfs-neohellenic-math-fonts.xml

Name:           fonts-otf-gfs-neohellenic-math
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
%linuxtext README

%build
# fontbuild 
fontnames=$(
  for font in 'GFSNeohellenicMath.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'GFSNeohellenicMath.otf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the gfs-neohellenic-math-fonts appstream file"
cat > "org.altlinux.gfs-neohellenic-math-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.gfs-neohellenic-math-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>OFL</project_license>
  <name>GFS NeoHellenic Math</name>
  <summary><![CDATA[GFS NeoHellenic Math, an almost Sans Serif Math font family]]></summary>
  <description>
    <p><![CDATA[GFS NeoHellenic Math is an almost Sans Serif font family. One of its main uses]]></p><p><![CDATA[is for presentations, an area where (we believe) a commercial grade sans math]]></p><p><![CDATA[font was not available up to now.]]></p> The font family contains an extended glyph set including more than the standard math symbols such as vertically extended integrals, chess symbols, etc. It was commissioned to the Greek Font Society (GFS) by the Graduate Studies program “Studies in Mathematics” of the Department of Mathematics of the University of the Aegean, located on the Samos island, Greece. The design copyright belongs to the main designer of GFS, George Matthiopoulos. The OpenType Math Table embedded in the font was developed by the Mathematics Professor Antonis Tsolomitis.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://www.greekfontsociety-gfs.gr/typefaces/Math</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing gfs-neohellenic-math-fonts
echo "" > "gfs-neohellenic-math-fonts.list"
install -m 0755 -vd %buildroot%_fontsdir/otf/gfs-neohellenic-math/
echo "%%dir %_fontsdir/otf/gfs-neohellenic-math" >> "gfs-neohellenic-math-fonts.list"
install -m 0644 -vp "GFSNeohellenicMath.otf" %buildroot%_fontsdir/otf/gfs-neohellenic-math/
echo \"%_fontsdir/otf/gfs-neohellenic-math//$(basename "GFSNeohellenicMath.otf")\" >> 'gfs-neohellenic-math-fonts.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'GFSNeohellenicMath.otf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "gfs-neohellenic-math-fonts.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "gfs-neohellenic-math-fonts.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.gfs-neohellenic-math-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "gfs-neohellenic-math-fonts.list"
done

for fontdoc in 'README'; do
  echo %%doc "'${fontdoc}'" >> "gfs-neohellenic-math-fonts.list"
done

for fontlicense in 'README'; do
  echo %%doc "'${fontlicense}'" >> "gfs-neohellenic-math-fonts.list"
done

%check
# fontcheck 
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'gfs-neohellenic-math-fonts.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'gfs-neohellenic-math-fonts.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-otf-gfs-neohellenic-math -f gfs-neohellenic-math-fonts.list

%files doc
%doc --no-dereference README
%doc *.pdf *.sty

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 20180227-alt1_4
- new version

