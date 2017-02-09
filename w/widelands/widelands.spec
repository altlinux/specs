Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install /usr/bin/doxygen gcc-c++ libGL-devel libGLU-devel libminizip-devel python-devel rpm-build-python zlib-devel
# END SourceDeps(oneline)
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global buildno 18
%global buildid build%{buildno}
%global build_id build-%{buildno}

Name:           widelands
Version:        0
Release:        alt6_0.55.%{buildid}
Summary:        Open source realtime-strategy game

Group:          Games/Other
License:        GPLv2+
URL:            http://www.widelands.org
Source0:        http://launchpad.net/widelands/%{buildid}/%{build_id}/+download/widelands-%{buildid}-src.tar.bz2

BuildRequires: libSDL-devel >= 1.2.11
BuildRequires: libSDL_gfx-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_mixer-devel >= 1.2.6
BuildRequires: libSDL_net-devel
BuildRequires: libSDL_sound-devel
BuildRequires: libSDL_ttf-devel >= 2.0.0
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires: boost-devel-static >= 1.47.0
BuildRequires: ctest cmake
BuildRequires: ctags
BuildRequires: desktop-file-utils
BuildRequires: gettext gettext-tools
BuildRequires: ggz-base-libs-devel
BuildRequires: libGLEW-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel libtiffxx-devel
BuildRequires: optipng
%if 0%{?fedora} >= 20
BuildRequires: liblua5.1-devel
%else
BuildRequires: lua-devel
%endif
Requires:      fonts-otf-drehatlas-widelands
Requires:      fonts-ttf-gnu-freefont-serif
Requires:      fonts-ttf-gnu-freefont-sans
Requires:      icon-theme-hicolor

%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it, you
perhaps will have a thought, what Widelands is all about.


%prep
%setup -q -n widelands-%{buildid}-src


%build
mkdir -p build/compile
pushd build/compile
# We need to set CMAKE_INCLUDE_PATH to /usr for FindLua51.cmake
%{fedora_cmake} \
    -DCMAKE_INCLUDE_PATH=%{_prefix} \
    -DWL_INSTALL_PREFIX=%{_prefix} \
    -DWL_INSTALL_BINDIR=%{_bindir} \
    -DWL_INSTALL_DATADIR=share/%{name} \
    ../..
%make_build
popd


%install
pushd build/compile
%makeinstall_std
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
cp -a pics/wl-logo-64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > widelands.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Widelands
GenericName=Realtime Strategy Game
Comment=Build a growing settlement and rule the world
Icon=widelands
Exec=widelands
Categories=Game;StrategyGame;
EOF

desktop-file-install  \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ %{name}.desktop

pushd $RPM_BUILD_ROOT
rm usr/share/widelands/fonts/FreeSans.ttf
rm usr/share/widelands/fonts/FreeSerif.ttf
rm usr/share/widelands/fonts/Widelands/*
ln -s /usr/share/fonts/ttf/gnu-free/FreeSans.ttf usr/share/widelands/fonts/FreeSans.ttf
ln -s /usr/share/fonts/ttf/gnu-free/FreeSerif.ttf usr/share/widelands/fonts/FreeSerif.ttf
ln -s /usr/share/fonts/otf/drehatlas-widelands/Widelands.otf usr/share/widelands/fonts/Widelands/Widelands.ttf
find usr/share/widelands/locale/ -maxdepth 1 -type d -name \*_\* | sed -n 's#\(usr/share/widelands/locale/\(.*\)_.*\)#%lang(\2) /\1#p' > %{_builddir}/widelands-%{buildid}-src/%{name}.files
find usr/share/widelands/locale/ -maxdepth 1 -type d ! -name "*_*" | sed -n -e 's#\(usr/share/widelands/locale/\(.\+\)\)#%lang(\2) /\1#p' >> %{_builddir}/widelands-%{buildid}-src/%{name}.files
find usr/share/widelands/ -mindepth 1 -maxdepth 1 -not -name locale | sed -n 's#\(usr/share/widelands/*\)#/\1#p' >> %{_builddir}/widelands-%{buildid}-src/%{name}.files
popd


%pre
cat << EOF | while read name; do rm -rf "%{_datadir}/widelands/maps/${name}.wmf"; done
Checkmate
Dry Riverbed
Elven Forests
Enemy in sight
Finlakes
Firegames
Four Castles
Glacier Lake
Golden Peninsula
Lake of tranquility
Plateau
Riverlands
The Oasis Triangle
The big lake
The long way
Two frontiers
War of the Valleys
EOF


%files -f %{name}.files
%doc ChangeLog COPYING CREDITS
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale


%changelog
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

