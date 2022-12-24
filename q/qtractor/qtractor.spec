# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: /usr/bin/desktop-file-install gcc-c++ pkgconfig(aubio) pkgconfig(lv2) pkgconfig(ogg) pkgconfig(samplerate) pkgconfig(xcb) pkgconfig(zlib)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		qtractor
Version:	0.9.29
Release:	alt1_1
Summary:	An Audio/MIDI multi-track sequencer
License:	GPLv2+
Group:		Sound
URL:		https://qtractor.sourceforge.io/
Source0:	https://www.rncbc.org/archive/%{name}-%{version}.tar.gz

BuildRequires:	qt6-base-devel
BuildRequires:	qt6-base-devel
BuildRequires:	qt6-svg-devel
BuildRequires:	qt6-base-devel
BuildRequires:	qt6-tools-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(rubberband)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(suil-0)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	ladspa_sdk
BuildRequires:	qt5-tools qt6-designer qt6-tools
BuildRequires:	ccmake cmake ctest

Requires:	dssi dssi-examples
Requires:	ladspa_sdk
Source44: import.info

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 or Qt5 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup -q
# E2K: fixed SSE detection code (ilyakurdyukov@)
%ifarch %e2k
sed -i "/#if defined(__GNUC__)/s|#|#ifdef __e2k__\nreturn true;\n#el|" \
  src/qtractor{AudioEngine,AudioMonitor,InsertPlugin,WsolaTimeStretcher}.cpp
%endif



%build
%{mageia_cmake}
%mageia_cmake_build

%install
%mageia_cmake_install

desktop-file-install \
	--remove-key="X-SuSE-translate" \
	--remove-key="Version" \
	--set-key=Exec --set-value="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop

%find_lang %{name} --with-man --with-qt

%files -f %{name}.lang
%doc README LICENSE TRANSLATORS ChangeLog
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}_plugin_scan
%{_datadir}/mime/packages/org.rncbc.%{name}.xml
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_datadir}/icons/hicolor/32x32/mimetypes/org.rncbc.%{name}.application-x-%{name}*.png
%{_datadir}/icons/hicolor/scalable/mimetypes/org.rncbc.%{name}.application-x-%{name}*.svg
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_datadir}/man/man1/%{name}.1*


%changelog
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
