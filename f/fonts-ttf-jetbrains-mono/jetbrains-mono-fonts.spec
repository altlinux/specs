Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname jetbrains-mono-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname jetbrains-mono-fonts
# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/JetBrains/JetBrainsMono
Version:            1.0.4
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/JetBrains/JetBrainsMono
%global forgesource https://github.com/JetBrains/JetBrainsMono/archive/1.0.4/JetBrainsMono-1.0.4.tar.gz
%global archivename JetBrainsMono-1.0.4
%global archiveext tar.gz
%global archiveurl https://github.com/JetBrains/JetBrainsMono/archive/1.0.4/JetBrainsMono-1.0.4.tar.gz
%global topdir JetBrainsMono-1.0.4
%global extractdir JetBrainsMono-1.0.4
%global repo JetBrainsMono
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 1.0.4
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

Release: alt1_5
URL:     https://jetbrains.com/mono/

%global foundry           JetBrains
%global fontlicense       ASL 2.0
%global fontlicenses      LICENSE
%global fontdocs          *md

%global common_description \
The JetBrains Mono project publishes developer-oriented font families.\
\
Their forms are simple and free from unnecessary details. Rendered in small\
sizes, the text looks crisper. The easier the forms, the faster the eye\
perceives them and the less effort the brain needs to process them.\
\
The shape of ovals approaches that of rectangular symbols. This makes the whole\
pattern of the text more clear-N.ut. The outer sides of ovals ensure there are\
no additional obstacles for your eyes as they scan the text vertically.\
\
Characters remain standard in width, but the height of the lowercase is\
maximized. This approach keeps code lines to the length that developers expect,\
and it helps improve rendering since each letter occupies more pixels.\
\
They use a 9A. italic angle; this maintains the optimal contrast to minimize\
distraction and eye strain. The usual angle is about 11A.a..12A..

%global fontfamily0       JetBrains Mono
%global fontsummary0      A mono-space font family containing coding ligatures
%global fontpkgheader0    \
Requires:  font(jetbrainsmononl)\

%global fonts0            ttf/*ttf
%global fontsex0          %{fonts1}
%global fontdescription0  \
%{common_description}\
\
The first font family published by the project, JetBrains Mono, includes coding\
ligatures. They will enhance the rendering of source code but may be\
problematic for other use cases.

%global fontfamily1       JetBrains Mono NL
%global fontsummary1      A mono-space coding font family
%global fonts1            ttf/*MonoNL*ttf
%global fontdescription1  \
%{common_description}\
\
The second font family published by the project, JetBrains Mono NL, is general\
purpose and free of coding ligatures.

Source0:  %{forgesource}
Source10: 60-jetbrains-mono-fonts.xml
Source11: 58-jetbrains-mono-nl-fonts.xml

Name:           fonts-ttf-jetbrains-mono
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-jetbrains-mono-nl
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-jetbrains-mono-nl
%{?fontdescription1}

%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-jetbrains-mono = %EVR
Requires:  fonts-ttf-jetbrains-mono-nl = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all


%prep
%global fontconfngs0      %{SOURCE10}
%global fontconfngs1      %{SOURCE11}
%setup -q -n JetBrainsMono-1.0.4

%build
# fontbuild 0
fontnames=$(
  for font in 'ttf/JetBrainsMono-Bold-Italic.ttf' 'ttf/JetBrainsMono-Bold.ttf' 'ttf/JetBrainsMono-ExtraBold-Italic.ttf' 'ttf/JetBrainsMono-ExtraBold.ttf' 'ttf/JetBrainsMono-Italic.ttf' 'ttf/JetBrainsMono-Medium-Italic.ttf' 'ttf/JetBrainsMono-Medium.ttf' 'ttf/JetBrainsMono-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'ttf/JetBrainsMono-Bold-Italic.ttf' 'ttf/JetBrainsMono-Bold.ttf' 'ttf/JetBrainsMono-ExtraBold-Italic.ttf' 'ttf/JetBrainsMono-ExtraBold.ttf' 'ttf/JetBrainsMono-Italic.ttf' 'ttf/JetBrainsMono-Medium-Italic.ttf' 'ttf/JetBrainsMono-Medium.ttf' 'ttf/JetBrainsMono-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the jetbrains-mono-fonts appstream file"
cat > "org.altlinux.jetbrains-mono-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.jetbrains-mono-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>JetBrains JetBrains Mono</name>
  <summary><![CDATA[A mono-space font family containing coding ligatures]]></summary>
  <description>
    <p><![CDATA[The JetBrains Mono project publishes developer-oriented font families.]]></p> Their forms are simple and free from unnecessary details. Rendered in small sizes, the text looks crisper. The easier the forms, the faster the eye perceives them and the less effort the brain needs to process them. The shape of ovals approaches that of rectangular symbols. This makes the whole pattern of the text more clear-сut. The outer sides of ovals ensure there are no additional obstacles for your eyes as they scan the text vertically. Characters remain standard in width, but the height of the lowercase is maximized. This approach keeps code lines to the length that developers expect, and it helps improve rendering since each letter occupies more pixels. They use a 9° italic angle; this maintains the optimal contrast to minimize distraction and eye strain. The usual angle is about 11°–12°. The first font family published by the project, JetBrains Mono, includes coding ligatures. They will enhance the rendering of source code but may be problematic for other use cases.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://jetbrains.com/mono/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM
# fontbuild 1
fontnames=$(
  for font in 'ttf/JetBrainsMonoNL-Bold-Italic.ttf' 'ttf/JetBrainsMonoNL-Bold.ttf' 'ttf/JetBrainsMonoNL-ExtraBold-Italic.ttf' 'ttf/JetBrainsMonoNL-ExtraBold.ttf' 'ttf/JetBrainsMonoNL-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium.ttf' 'ttf/JetBrainsMonoNL-Regular.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'ttf/JetBrainsMonoNL-Bold-Italic.ttf' 'ttf/JetBrainsMonoNL-Bold.ttf' 'ttf/JetBrainsMonoNL-ExtraBold-Italic.ttf' 'ttf/JetBrainsMonoNL-ExtraBold.ttf' 'ttf/JetBrainsMonoNL-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium.ttf' 'ttf/JetBrainsMonoNL-Regular.ttf'; do
    fc-scan "${font}" -f "%%{[]lang{    <lang>%%{lang}</lang>\n}}"
  done | sort -u
)
if [[ -n "${fontlangs}" ]] ; then
  fontlangs=$'\n'"  <languages>"$'\n'"${fontlangs}"$'\n'"  </languages>"
fi

echo "Generating the jetbrains-mono-nl-fonts appstream file"
cat > "org.altlinux.jetbrains-mono-nl-fonts.metainfo.xml" << EOF_APPSTREAM
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-License-Identifier: MIT -->
<component type="font">
  <id>org.altlinux.jetbrains-mono-nl-fonts</id>
  <metadata_license>MIT</metadata_license>
  <project_license>ASL 2.0</project_license>
  <name>JetBrains JetBrains Mono NL</name>
  <summary><![CDATA[A mono-space coding font family]]></summary>
  <description>
    <p><![CDATA[The JetBrains Mono project publishes developer-oriented font families.]]></p> Their forms are simple and free from unnecessary details. Rendered in small sizes, the text looks crisper. The easier the forms, the faster the eye perceives them and the less effort the brain needs to process them. The shape of ovals approaches that of rectangular symbols. This makes the whole pattern of the text more clear-сut. The outer sides of ovals ensure there are no additional obstacles for your eyes as they scan the text vertically. Characters remain standard in width, but the height of the lowercase is maximized. This approach keeps code lines to the length that developers expect, and it helps improve rendering since each letter occupies more pixels. They use a 9° italic angle; this maintains the optimal contrast to minimize distraction and eye strain. The usual angle is about 11°–12°. The second font family published by the project, JetBrains Mono NL, is general purpose and free of coding ligatures.
  </description>
  <updatecontact>devel@lists.altlinux.org</updatecontact>
  <url type="homepage">https://jetbrains.com/mono/</url>
  <releases>
    <release version="%{version}-%{release}" date="$(date -d @$SOURCE_DATE_EPOCH -u --rfc-3339=d)"/>
  </releases>${fontnames}${fontlangs}
</component>
EOF_APPSTREAM

%install
echo Installing jetbrains-mono-fonts
echo "" > "jetbrains-mono-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/jetbrains-mono/
echo "%%dir %_fontsdir/ttf/jetbrains-mono" >> "jetbrains-mono-fonts0.list"
install -m 0644 -vp "ttf/JetBrainsMono-Bold-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Bold-Italic.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-Bold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Bold.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-ExtraBold-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-ExtraBold-Italic.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-ExtraBold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-ExtraBold.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Italic.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-Medium-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Medium-Italic.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-Medium.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Medium.ttf")\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "ttf/JetBrainsMono-Regular.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMono-Regular.ttf")\" >> 'jetbrains-mono-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'ttf/JetBrainsMono-Bold-Italic.ttf' 'ttf/JetBrainsMono-Bold.ttf' 'ttf/JetBrainsMono-ExtraBold-Italic.ttf' 'ttf/JetBrainsMono-ExtraBold.ttf' 'ttf/JetBrainsMono-Italic.ttf' 'ttf/JetBrainsMono-Medium-Italic.ttf' 'ttf/JetBrainsMono-Medium.ttf' 'ttf/JetBrainsMono-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "jetbrains-mono-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "jetbrains-mono-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.jetbrains-mono-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "jetbrains-mono-fonts0.list"
done

for fontdoc in 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "jetbrains-mono-fonts0.list"
done

for fontlicense in 'LICENSE'; do
  echo %%doc "'${fontlicense}'" >> "jetbrains-mono-fonts0.list"
done
echo Installing jetbrains-mono-nl-fonts
echo "" > "jetbrains-mono-nl-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/jetbrains-mono/
echo "%%dir %_fontsdir/ttf/jetbrains-mono" >> "jetbrains-mono-nl-fonts1.list"
install -m 0644 -vp "ttf/JetBrainsMonoNL-Bold-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Bold-Italic.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-Bold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Bold.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-ExtraBold-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-ExtraBold-Italic.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-ExtraBold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-ExtraBold.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Italic.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-Medium-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Medium-Italic.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-Medium.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Medium.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "ttf/JetBrainsMonoNL-Regular.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono//$(basename "ttf/JetBrainsMonoNL-Regular.ttf")\" >> 'jetbrains-mono-nl-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'ttf/JetBrainsMonoNL-Bold-Italic.ttf' 'ttf/JetBrainsMonoNL-Bold.ttf' 'ttf/JetBrainsMonoNL-ExtraBold-Italic.ttf' 'ttf/JetBrainsMonoNL-ExtraBold.ttf' 'ttf/JetBrainsMonoNL-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium-Italic.ttf' 'ttf/JetBrainsMonoNL-Medium.ttf' 'ttf/JetBrainsMonoNL-Regular.ttf'
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
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "jetbrains-mono-nl-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "jetbrains-mono-nl-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in 'org.altlinux.jetbrains-mono-nl-fonts.metainfo.xml'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "jetbrains-mono-nl-fonts1.list"
done

for fontdoc in 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "jetbrains-mono-nl-fonts1.list"
done

for fontlicense in 'LICENSE'; do
  echo %%doc "'${fontlicense}'" >> "jetbrains-mono-nl-fonts1.list"
done

%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'jetbrains-mono-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'jetbrains-mono-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'jetbrains-mono-nl-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'jetbrains-mono-nl-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'

%files -n fonts-ttf-jetbrains-mono -f jetbrains-mono-fonts0.list
%files -n fonts-ttf-jetbrains-mono-nl -f jetbrains-mono-nl-fonts1.list

%changelog
* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt1_5
- new version

