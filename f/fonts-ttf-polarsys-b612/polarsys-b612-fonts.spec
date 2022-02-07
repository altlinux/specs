Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-fonts
BuildRequires: rpm-build-fedora-compat-fonts
# END SourceDeps(oneline)
%define oldname polarsys-b612-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname polarsys-b612-fonts
%global forgeurl https://github.com/polarsys/b612/
Version: 1.008
Release: alt1_9
URL: https://projects.eclipse.org/projects/polarsys.b612

%global tag %{version}
%global foundry PolarSys

# README.md explains, "This program and the accompanying materials are
# made available under the terms of the Eclipse Public License v1.0 and
# Eclipse Distribution License v1.0 and the SIL Open Font License v1.1
# which accompanies this distribution."
%global fontlicense EPL-1.0 and BSD and OFL
%global fontlicenses edl-v10.html epl-v10.html OFL.txt
%global fontdocsex %{fontlicenses}

%global common_description \
Commissioned by Airbus and designed by Intactile Design, B612 is a\
digital font intended to be used in an aeronautical context. B612 is\
built with legibility as its core: every character is designed to be\
highly recognizable even in critical reading conditions. B612 drawing\
has been optimized for screen display, and full hinting has been added\
to all sizes of alpha numeric characters.\


%global fontfamily0 B612
%global fontsummary0 Sans-serif fonts designed for reading comfort and safety in aeroplane cockpits
%global fontpkgheader0    \
Obsoletes: polarsys-b612-fonts-common < 1.008-7\
Obsoletes: polarsys-b612-sans-fonts < 1.008-7\
Provides: polarsys-b612-sans-fonts = %{version}-%{release}\

%global fonts0 fonts/ttf/B612-*.ttf
%global fontdescription0  \
%{common_description}\
\
This packages contains a sans serif font family.

%global fontfamily1 B612 Mono
%global fontsummary1 Monospace fonts designed for reading comfort and safety in aeroplane cockpits
%global fontpkgheader1    \
Obsoletes: polarsys-b612-fonts-common < 1.008-7\

%global fonts1 fonts/ttf/B612Mono-*.ttf
%global fontdescription1  \
%{common_description}\
\
This packages contains a monospace font family.


%global fontname polarsys-b612
%global fontconf 64-%{fontname}


%global forgeurl https://github.com/polarsys/b612/
%global forgesource https://github.com/polarsys/b612//archive/1.008/b612-1.008.tar.gz
%global archivename b612-1.008
%global archiveext tar.gz
%global archiveurl https://github.com/polarsys/b612//archive/1.008/b612-1.008.tar.gz
%global topdir b612-1.008
%global extractdir b612-1.008
%global repo b612
#global owner %nil
#global namespace %nil
%global scm git
%global tag 1.008
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 1.008
#global date %nil
%global distprefix .git1.008


Source0:        %{forgesource}
Source1:        https://www.eclipse.org/legal/epl-v10.html
Source10:       64-polarsys-b612-fonts.conf
Source11:       64-polarsys-b612-mono-fonts.conf
Source20:       %{fontname}.metainfo.xml
Source21:       %{fontname}-mono.metainfo.xml


Name:           fonts-ttf-polarsys-b612
Summary:        %{fontsummary0}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader0}
Source44: import.info
%description
%{?fontdescription0}
%package     -n fonts-ttf-polarsys-b612-mono
Group: System/Fonts/True type
Summary:        %{fontsummary1}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-build-fonts
%{?fontpkgheader1}
%description -n fonts-ttf-polarsys-b612-mono
%{?fontdescription1}
%package   all
Group: System/Fonts/True type
Summary:   All the font packages, generated from %{oldname}
Requires:  fonts-ttf-polarsys-b612 = %EVR
Requires:  fonts-ttf-polarsys-b612-mono = %EVR
BuildArch: noarch
%description all
This meta-package installs all the font packages, generated from the %{oldname}
 source package.

%files all



%package doc
Group: System/Fonts/True type
Summary:        Documentation for B612
BuildArch:      noarch

%description doc
%{common_description}

This package contains a leaflet explaining the design and production of
the fonts.


%prep
%global fontconfs0 %{SOURCE10}
%global fontappstreams0 %{SOURCE20}
%global fontconfs1 %{SOURCE11}
%global fontappstreams1 %{SOURCE21}
%setup -q -n b612-1.008

install -m 0644 -p %{SOURCE1} .


%build
# fontbuild 0
# fontbuild 1


%install
echo "Installing "polarsys-b612-fonts
echo "" > "polarsys-b612-fonts0.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/polarsys-b612/
echo "%%dir %_fontsdir/ttf/polarsys-b612" >> "polarsys-b612-fonts0.list"
install -m 0644 -vp "fonts/ttf/B612-Bold.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612-Bold.ttf")\" >> 'polarsys-b612-fonts0.list'
install -m 0644 -vp "fonts/ttf/B612-BoldItalic.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612-BoldItalic.ttf")\" >> 'polarsys-b612-fonts0.list'
install -m 0644 -vp "fonts/ttf/B612-Italic.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612-Italic.ttf")\" >> 'polarsys-b612-fonts0.list'
install -m 0644 -vp "fonts/ttf/B612-Regular.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612-Regular.ttf")\" >> 'polarsys-b612-fonts0.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE10' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "polarsys-b612-fonts0.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "polarsys-b612-fonts0.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in '%SOURCE20'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "polarsys-b612-fonts0.list"
done

for fontlicense in 'edl-v10.html' 'epl-v10.html' 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "polarsys-b612-fonts0.list"
done
echo "Installing "polarsys-b612-mono-fonts
echo "" > "polarsys-b612-mono-fonts1.list"
install -m 0755 -vd %buildroot%_fontsdir/ttf/polarsys-b612/
echo "%%dir %_fontsdir/ttf/polarsys-b612" >> "polarsys-b612-mono-fonts1.list"
install -m 0644 -vp "fonts/ttf/B612Mono-Bold.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612Mono-Bold.ttf")\" >> 'polarsys-b612-mono-fonts1.list'
install -m 0644 -vp "fonts/ttf/B612Mono-BoldItalic.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612Mono-BoldItalic.ttf")\" >> 'polarsys-b612-mono-fonts1.list'
install -m 0644 -vp "fonts/ttf/B612Mono-Italic.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612Mono-Italic.ttf")\" >> 'polarsys-b612-mono-fonts1.list'
install -m 0644 -vp "fonts/ttf/B612Mono-Regular.ttf" %buildroot%_fontsdir/ttf/polarsys-b612/
echo \"%_fontsdir/ttf/polarsys-b612//$(basename "fonts/ttf/B612Mono-Regular.ttf")\" >> 'polarsys-b612-mono-fonts1.list'
(

  install -m 0755 -vd "%{buildroot}%{_fontconfig_templatedir}" \
                    "%{buildroot}%{_fontconfig_confdir}"
  for fontconf in '%SOURCE11' "${newfontconfs[@]}"; do
    if [[ -n $fontconf ]] ; then
      install -m 0644 -vp "${fontconf}" "%{buildroot}%{_fontconfig_templatedir}"
      echo \"%{_fontconfig_templatedir}/$(basename "${fontconf}")\"                  >> "polarsys-b612-mono-fonts1.list"
      ln -vsr "%{buildroot}%{_fontconfig_templatedir}/$(basename "${fontconf}")" "%{buildroot}%{_fontconfig_confdir}"
      echo "%%config(noreplace)" \"%{_fontconfig_confdir}/$(basename "${fontconf}")\" >> "polarsys-b612-mono-fonts1.list"
    fi
  done
)

install -m 0755 -vd "%{buildroot}%{_metainfodir}"
for fontappstream in '%SOURCE21'; do
  install -m 0644 -vp "${fontappstream}" "%{buildroot}%{_metainfodir}"
  echo \"%{_metainfodir}/$(basename "${fontappstream}")\" >> "polarsys-b612-mono-fonts1.list"
done

for fontlicense in 'edl-v10.html' 'epl-v10.html' 'OFL.txt'; do
  echo %%doc "'${fontlicense}'" >> "polarsys-b612-mono-fonts1.list"
done


%check
# fontcheck 0
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'polarsys-b612-fonts0.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'polarsys-b612-fonts0.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'
# fontcheck 1
grep -E '^"%{_fontconfig_templatedir}/.+\.conf"' 'polarsys-b612-mono-fonts1.list' \
  | xargs -I{} -- sh -c "xmllint --loaddtd --valid     --nonet '%{buildroot}{}' >/dev/null && echo %{buildroot}{}: OK"
grep -E '^"%{_datadir}/metainfo/.+\.xml"'        'polarsys-b612-mono-fonts1.list' \
  | xargs -I{} --        appstream-util validate-relax --nonet '%{buildroot}{}'


%files -n fonts-ttf-polarsys-b612 -f polarsys-b612-fonts0.list
%files -n fonts-ttf-polarsys-b612-mono -f polarsys-b612-mono-fonts1.list

%files doc
%doc docs/B612-Leaflet.pdf


%changelog
* Mon Feb 07 2022 Igor Vlasenko <viy@altlinux.org> 1.008-alt1_9
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1_5.20171129gitbd14fde
- new version

