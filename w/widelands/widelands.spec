Epoch: 1
Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install /usr/bin/doxygen boost-devel libGLU-devel libX11-devel libglvnd-devel libicu-devel python-devel rpm-build-python zlib-devel
# END SourceDeps(oneline)

%filter_from_requires /^.usr.share.fonts.ttf./d
Requires: fonts-ttf-amiri
Requires: fonts-ttf-lklug
Requires: fonts-ttf-wqy-microhei
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global buildno 19
%global buildid build%{buildno}

Name:           widelands
Version:        0
Release:        alt7_0.69.%{buildid}
Summary:        Open source realtime-strategy game

License:        GPLv2+
URL:            http://www.widelands.org
Source0:        https://launchpad.net/widelands/%{buildid}/%{buildid}/+download/widelands-%{buildid}-src-gcc7.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         widelands-build19-ppc64le.patch
Patch1:         widelands-build19-gcc82.patch

BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libSDL2_net-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: boost-complete >= 1.48.0
BuildRequires: ctest cmake
BuildRequires: ctags
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: gettext gettext-tools
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libGLEW-devel
BuildRequires: libpng-devel
Requires:      icon-theme-hicolor
# The game contains a copy of these fonts, we replaces these with system fonts
Requires:      fonts-ttf-amiri
Requires:      fonts-ttf-dejavu
Requires:      fonts-ttf-dejavu
Requires:      fonts-ttf-dejavu
Requires:      fonts-otf-drehatlas-widelands
Requires:      fonts-ttf-lklug
Requires:      fonts-ttf-wqy-microhei
Source44: import.info

%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it, you
perhaps will have a thought, what Widelands is all about.


%prep
%setup -q -n widelands-%{buildid}-src-gcc7
%patch0 -p1
%patch1 -p1


%build
mkdir build
pushd build
# We need to set CMAKE_INCLUDE_PATH to /usr for FindLua51.cmake
%{fedora_cmake} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_bindir} \
    -DWL_INSTALL_BASEDIR=%{_prefix}/share/%{name} \
    -DWL_INSTALL_DATADIR=%{_prefix}/share/%{name} \
    -DOPTION_BUILD_WEBSITE_TOOLS=OFF \
    ..
%make_build
popd


%install
pushd build
%makeinstall_std
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
ln -s /usr/share/%{name}/images/logos/wl-logo-64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

pushd $RPM_BUILD_ROOT
# We don't want this development tool / utility
rm usr/bin/wl_render_richtext

# Replace fonts with system fonts
rm -r usr/share/%{name}/i18n/fonts/amiri
rm -r usr/share/%{name}/i18n/fonts/DejaVu
rm -r usr/share/%{name}/i18n/fonts/MicroHei
rm -r usr/share/%{name}/i18n/fonts/Sinhala
rm -r usr/share/%{name}/i18n/fonts/Widelands/*
ln -s /usr/share/fonts/ttf/amiri usr/share/%{name}/i18n/fonts/amiri
ln -s /usr/share/fonts/ttf/dejavu usr/share/%{name}/i18n/fonts/DejaVu
ln -s /usr/share/fonts/ttf/wqy-microhei usr/share/%{name}/i18n/fonts/MicroHei
ln -s /usr/share/fonts/ttf/lklug usr/share/%{name}/i18n/fonts/Sinhala
ln -s /usr/share/fonts/otf/drehatlas-widelands/Widelands.otf usr/share/%{name}/i18n/fonts/Widelands/Widelands.ttf

# Scripting magic to add proper %%lang() markings to the locale files
find usr/share/widelands/locale/ -maxdepth 1 -type d -name \*_\* | sed -n 's#\(usr/share/widelands/locale/\(.*\)_.*\)#%lang(\2) /\1#p' > %{_builddir}/widelands-%{buildid}-src-gcc7/%{name}.files
find usr/share/widelands/locale/ -maxdepth 1 -type d ! -name "*_*" | sed -n -e 's#\(usr/share/widelands/locale/\(.\+\)\)#%lang(\2) /\1#p' >> %{_builddir}/widelands-%{buildid}-src-gcc7/%{name}.files
find usr/share/widelands/ -mindepth 1 -maxdepth 1 -not -name locale | sed -n 's#\(usr/share/widelands/*\)#/\1#p' >> %{_builddir}/widelands-%{buildid}-src-gcc7/%{name}.files
popd


%files -f %{name}.files
%doc ChangeLog CREDITS
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale


%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 1:0-alt7_0.69.build19
- update to new release by fcimport

* Sun Sep 23 2018 Igor Vlasenko <viy@altlinux.ru> 1:0-alt7_0.67.build19
- rebuild with new libicu/ical

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 1:0-alt7_0.62.build19
- use boost-complete

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0-alt6_0.62.build19.1
- NMU: rebuilt with boost-1.67.0

* Sun May 27 2018 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.62.build19
- build19

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.59.build18
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.57.build18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.56.build18
- update to new release by fcimport

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.55.build18
- rebuild new lua

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt6_0.39.build17
- rebuild with new SDL

* Tue Nov 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:0-alt5_0.39.build17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:0-alt5_0.38.build17
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1:0-alt5_0.35.build17
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt5_0.34.build17
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt5_0.33.build17
- gcc46 build

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.33.build17
- new release

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.30.build16
- fixed build

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt3_0.30.build16
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt3_0.29.build16
- rebuild with fixed sourcedep analyser (#27020)

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.29.build16
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.28.build16
- update to new release by fcimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.26.build16
- initial release by fedoraimport

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.26.build16
- new version by fcimport

* Mon Mar 16 2009 Eugene Ostapets <eostapets@altlinux.ru> b13-alt1
- new version

* Mon Apr 21 2008 Eugene Ostapets <eostapets@altlinux.ru> b12-alt1
- First build for ALTLinux

