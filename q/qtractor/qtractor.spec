Name: qtractor
Version: 0.9.90
Release: alt2

Summary: Audio/MIDI multi-track sequencer
License: GPLv2
Group: Sound
Url: https://qtractor.org/

Source: %name-%version-%release.tar

ExcludeArch: ppc64le

BuildRequires: cmake gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: ladspa_sdk
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(aubio)
BuildRequires: pkgconfig(dssi)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(zlib)

%description
Qtractor is an audio/MIDI multi-track sequencer application written
in C++ with the Qt framework [1]. Target platform is Linux, where the
Jack Audio Connection Kit (JACK) for audio and the Advanced Linux
Sound Architecture (ALSA) for MIDI are the main infrastructures
to evolve as a fairly-featured Linux desktop audio workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup
%ifarch %e2k
sed -i "/#if defined(__GNUC__)/s|#|#ifdef __e2k__\nreturn true;\n#el|" \
  src/qtractor{AudioEngine,AudioMonitor,InsertPlugin,WsolaTimeStretcher}.cpp
sed -i "s/'\\\\0'/QChar(&)/" src/qtractorPluginForm.cpp
%endif

%build
%cmake -DCONFIG_CLAP=NO -DCONFIG_VST2=NO -DCONFIG_VST3=NO
%cmake_build

%install
%cmakeinstall_std
desktop-file-edit \
	--remove-key=X-SuSE-translate \
        --remove-key=Version \
        --set-key=Exec --set-value=%name \
	%buildroot%_desktopdir/*.desktop

%files
%doc LICENSE README

%_bindir/qtractor
%_libdir/qtractor
%_datadir/qtractor

%_datadir/metainfo/*.xml
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg

%_man1dir/qtractor.1*

%changelog
* Sun Jun 09 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.9.90-alt2
- fix e2k build

* Fri Apr 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.90-alt1
- 0.9.90 released

* Mon Jan 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.39-alt1
- 0.9.39 released

* Tue Jan  2 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.38-alt1
- 0.9.38 released
- fixed build with pw jack substitute (closes: 48991)

* Mon Oct 02 2023 Igor Vlasenko <viy@altlinux.org> 0.9.35-alt1_1
- update by mgaimport

* Thu Sep 14 2023 Igor Vlasenko <viy@altlinux.org> 0.9.34-alt1_1
- update by mgaimport

* Wed Sep  6 2023 Artyom Bystrov <arbars@altlinux.org> 0.9.31-alt1_2
- Fix FTBFS (thanks to aris@)

* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 0.9.31-alt1_1
- update by mgaimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.29-alt1_1
- update by mgaimport

* Fri Sep 30 2022 Igor Vlasenko <viy@altlinux.org> 0.9.28-alt1_1
- update by mgaimport

* Fri Jun 25 2021 Igor Vlasenko <viy@altlinux.org> 0.9.22-alt1_1
- new version

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 0.9.21-alt1_1
- update by mgaimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 0.9.20-alt1_1
- update by mgaimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.19-alt1_1
- update by mgaimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.18-alt1_1
- update by mgaimport

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.17-alt1_1
- new version

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_1
- update to new release by fcimport

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_1
- new version

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_2
- update to new release by fcimport

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_1
- new version

* Thu Jun 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1.1
- Rebuild with new version liblo

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1
- manual update to 0.5.8

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_2
- update from fc import

* Mon Sep 12 2011 Egor Glukhov <kaman@altlinux.org> 0.5.0.44-alt1
- fixed build
- 0.5.0.44

* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.4.9-alt1
- 0.4.9

* Sun Feb 13 2011 Egor Glukhov <kaman@altlinux.org> 0.4.8.18-alt1
- 0.4.8.18

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 0.4.6-alt1
- initial build for Sisyphus
