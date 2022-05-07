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
Version:            2.242
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/JetBrains/JetBrainsMono
%global forgesource https://github.com/JetBrains/JetBrainsMono/archive/2.242/JetBrainsMono-2.242.tar.gz
%global archivename JetBrainsMono-2.242
%global archiveext tar.gz
%global archiveurl https://github.com/JetBrains/JetBrainsMono/archive/2.242/JetBrainsMono-2.242.tar.gz
%global topdir JetBrainsMono-2.242
%global extractdir JetBrainsMono-2.242
%global repo JetBrainsMono
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 2.242
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

Release: alt1_1
URL:     https://jetbrains.com/mono/

%global foundry           JetBrains
%global fontlicense       OFL 1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.md

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
#Suggests:  font(jetbrainsmononl)\

%global fonts0            fonts/otf/*.otf
%global fontdescription0  \
%{common_description}\
\
The first font family published by the project, JetBrains Mono, includes coding\
ligatures. They will enhance the rendering of source code but may be\
problematic for other use cases.

%global fontfamily1       JetBrains Mono NL
%global fontsummary1      A mono-space coding font family
%global fonts1            fonts/ttf/*MonoNL*.ttf
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
%setup -q -n JetBrainsMono-2.242

%build
# fontbuild 0
fontnames=$(
  for font in 'fonts/otf/JetBrainsMono-Bold.otf' 'fonts/otf/JetBrainsMono-BoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraBold.otf' 'fonts/otf/JetBrainsMono-ExtraBoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraLight.otf' 'fonts/otf/JetBrainsMono-ExtraLightItalic.otf' 'fonts/otf/JetBrainsMono-Italic.otf' 'fonts/otf/JetBrainsMono-Light.otf' 'fonts/otf/JetBrainsMono-LightItalic.otf' 'fonts/otf/JetBrainsMono-Medium.otf' 'fonts/otf/JetBrainsMono-MediumItalic.otf' 'fonts/otf/JetBrainsMono-Regular.otf' 'fonts/otf/JetBrainsMono-SemiBold.otf' 'fonts/otf/JetBrainsMono-SemiBoldItalic.otf' 'fonts/otf/JetBrainsMono-Thin.otf' 'fonts/otf/JetBrainsMono-ThinItalic.otf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/otf/JetBrainsMono-Bold.otf' 'fonts/otf/JetBrainsMono-BoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraBold.otf' 'fonts/otf/JetBrainsMono-ExtraBoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraLight.otf' 'fonts/otf/JetBrainsMono-ExtraLightItalic.otf' 'fonts/otf/JetBrainsMono-Italic.otf' 'fonts/otf/JetBrainsMono-Light.otf' 'fonts/otf/JetBrainsMono-LightItalic.otf' 'fonts/otf/JetBrainsMono-Medium.otf' 'fonts/otf/JetBrainsMono-MediumItalic.otf' 'fonts/otf/JetBrainsMono-Regular.otf' 'fonts/otf/JetBrainsMono-SemiBold.otf' 'fonts/otf/JetBrainsMono-SemiBoldItalic.otf' 'fonts/otf/JetBrainsMono-Thin.otf' 'fonts/otf/JetBrainsMono-ThinItalic.otf'; do
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
  <project_license>OFL 1.1</project_license>
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
  for font in 'fonts/ttf/JetBrainsMonoNL-Bold.ttf' 'fonts/ttf/JetBrainsMonoNL-BoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBold.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLight.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Italic.ttf' 'fonts/ttf/JetBrainsMonoNL-Light.ttf' 'fonts/ttf/JetBrainsMonoNL-LightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Medium.ttf' 'fonts/ttf/JetBrainsMonoNL-MediumItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Regular.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBold.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Thin.ttf' 'fonts/ttf/JetBrainsMonoNL-ThinItalic.ttf'; do
    fc-scan "${font}" -f "    <font>%%{fullname[0]}</font>\n"
  done | sort -u
)
if [[ -n "${fontnames}" ]] ; then
  fontnames=$'\n'"  <provides>"$'\n'"${fontnames}"$'\n'"  </provides>"
fi
fontlangs=$(
  for font in 'fonts/ttf/JetBrainsMonoNL-Bold.ttf' 'fonts/ttf/JetBrainsMonoNL-BoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBold.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLight.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Italic.ttf' 'fonts/ttf/JetBrainsMonoNL-Light.ttf' 'fonts/ttf/JetBrainsMonoNL-LightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Medium.ttf' 'fonts/ttf/JetBrainsMonoNL-MediumItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Regular.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBold.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Thin.ttf' 'fonts/ttf/JetBrainsMonoNL-ThinItalic.ttf'; do
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
  <project_license>OFL 1.1</project_license>
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
install -m 0755 -vd %buildroot%_fontsdir/otf/jetbrains-mono/
echo "%%dir %_fontsdir/otf/jetbrains-mono" >> "jetbrains-mono-fonts0.list"
install -m 0644 -vp "fonts/otf/JetBrainsMono-Bold.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Bold.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-BoldItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-BoldItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-ExtraBold.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-ExtraBold.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-ExtraBoldItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-ExtraBoldItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-ExtraLight.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-ExtraLight.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-ExtraLightItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-ExtraLightItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-Italic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Italic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-Light.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Light.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-LightItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-LightItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-Medium.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Medium.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-MediumItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-MediumItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-Regular.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Regular.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-SemiBold.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-SemiBold.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-SemiBoldItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-SemiBoldItalic.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-Thin.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-Thin.otf\" >> 'jetbrains-mono-fonts0.list'
install -m 0644 -vp "fonts/otf/JetBrainsMono-ThinItalic.otf" %buildroot%_fontsdir/otf/jetbrains-mono/
echo \"%_fontsdir/otf/jetbrains-mono/JetBrainsMono-ThinItalic.otf\" >> 'jetbrains-mono-fonts0.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE10'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/otf/JetBrainsMono-Bold.otf' 'fonts/otf/JetBrainsMono-BoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraBold.otf' 'fonts/otf/JetBrainsMono-ExtraBoldItalic.otf' 'fonts/otf/JetBrainsMono-ExtraLight.otf' 'fonts/otf/JetBrainsMono-ExtraLightItalic.otf' 'fonts/otf/JetBrainsMono-Italic.otf' 'fonts/otf/JetBrainsMono-Light.otf' 'fonts/otf/JetBrainsMono-LightItalic.otf' 'fonts/otf/JetBrainsMono-Medium.otf' 'fonts/otf/JetBrainsMono-MediumItalic.otf' 'fonts/otf/JetBrainsMono-Regular.otf' 'fonts/otf/JetBrainsMono-SemiBold.otf' 'fonts/otf/JetBrainsMono-SemiBoldItalic.otf' 'fonts/otf/JetBrainsMono-Thin.otf' 'fonts/otf/JetBrainsMono-ThinItalic.otf'
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

for fontdoc in 'Changelog.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "jetbrains-mono-fonts0.list"
done

for fontlicense in 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "jetbrains-mono-fonts0.list"
done
echo Installing jetbrains-mono-nl-fonts
echo "" > "jetbrains-mono-nl-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/jetbrains-mono/
echo "%%dir %_fontsdir/ttf/jetbrains-mono" >> "jetbrains-mono-nl-fonts1.list"
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Bold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Bold.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-BoldItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-BoldItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-ExtraBold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-ExtraBold.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-ExtraBoldItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-ExtraBoldItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-ExtraLight.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-ExtraLight.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-ExtraLightItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-ExtraLightItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Italic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Italic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Light.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Light.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-LightItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-LightItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Medium.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Medium.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-MediumItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-MediumItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Regular.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Regular.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-SemiBold.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-SemiBold.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-SemiBoldItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-SemiBoldItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-Thin.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-Thin.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
install -m 0644 -vp "fonts/ttf/JetBrainsMonoNL-ThinItalic.ttf" %buildroot%_fontsdir/ttf/jetbrains-mono/
echo \"%_fontsdir/ttf/jetbrains-mono/JetBrainsMonoNL-ThinItalic.ttf\" >> 'jetbrains-mono-nl-fonts1.list'
(

  IFS= lines=$(
    for fontconfng in '%SOURCE11'; do
      gen-fontconf -x "${fontconfng}" -w -f 'fonts/ttf/JetBrainsMonoNL-Bold.ttf' 'fonts/ttf/JetBrainsMonoNL-BoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBold.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLight.ttf' 'fonts/ttf/JetBrainsMonoNL-ExtraLightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Italic.ttf' 'fonts/ttf/JetBrainsMonoNL-Light.ttf' 'fonts/ttf/JetBrainsMonoNL-LightItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Medium.ttf' 'fonts/ttf/JetBrainsMonoNL-MediumItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Regular.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBold.ttf' 'fonts/ttf/JetBrainsMonoNL-SemiBoldItalic.ttf' 'fonts/ttf/JetBrainsMonoNL-Thin.ttf' 'fonts/ttf/JetBrainsMonoNL-ThinItalic.ttf'
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

for fontdoc in 'Changelog.md' 'README.md'; do
  echo %%doc "'${fontdoc}'" >> "jetbrains-mono-nl-fonts1.list"
done

for fontlicense in 'OFL.txt'; do
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
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.242-alt1_1
- update to new release by fcimport

* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt1_5
- new version

