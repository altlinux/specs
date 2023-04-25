# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: widelands
Version: 1.1
Release: alt1.1
Epoch: 1

Summary: Open source realtime-strategy game
License: GPLv2+
Group: Games/Strategy

Url: http://www.widelands.org
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: boost-program_options-devel >= 1.48.0
BuildRequires: boost-signals-devel
BuildRequires: boost-asio-devel
BuildRequires: ctags
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libglew-devel
BuildRequires: libpng-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: asio-devel
BuildRequires: ctest
BuildRequires: python3
BuildRequires: doxygen

%description
Widelands is an open source (GPLed), realtime-strategy game, using SDL and
other free libraries, which is still under development. Widelands is inspired
by Settlers II (Bluebyte) and is partly similar to it, so if you know it,
you perhaps will have a thought what Widelands is all about.

%prep
%setup
%autopatch -p1
%ifarch %e2k
# unsupported as of lcc 1.26.18 (mcst#7644)
sed -i '/-fno-elide-constructors/d' CMakeLists.txt
%endif

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DWL_INSTALL_BINDIR=%_bindir \
    -DWL_INSTALL_BASEDIR=%_datadir/%name \
    -DWL_INSTALL_DATADIR=%_datadir/%name \
    -DOPTION_BUILD_WEBSITE_TOOLS=OFF

%cmake_build

%install
%cmake_install

# Validate desktop file (provided by upstream)
desktop-file-validate %buildroot%_desktopdir/*.desktop

# Validate appdata (provided by upstream)
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.appdata.xml

%files
%doc ChangeLog CREDITS
%_man6dir/widelands.6.*
%_bindir/%name
%_iconsdir/hicolor/*/apps/*.png
%_datadir/metainfo/*.appdata.xml
%_desktopdir/*.desktop
%_datadir/%name

%changelog
* Tue Apr 25 2023 Michael Shigorin <mike@altlinux.org> 1:1.1-alt1.1
- E2K: avoid lcc-unsupported option (mcst#7644)
- minor spec cleanup

* Sun Oct 23 2022 Anton Midyukov <antohami@altlinux.org> 1:1.1-alt1
- New version 1.1

* Wed Jul 20 2022 Anton Midyukov <antohami@altlinux.org> 1:1.0-alt1.20220719
- New snapshot

* Mon Jun 06 2022 Anton Midyukov <antohami@altlinux.org> 1:1.0-alt1.20220605
- New snapshot version 1.0
- use embedded fonts

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0-alt8_0.77.build20
- Rebuilt with boost-1.73.0.

* Sun Mar 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:0-alt7_0.77.build20
- update

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
