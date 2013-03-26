# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config gcc-c++ libX11-devel libXext-devel libmad-devel libogg-devel lv2core zlib-devel
# END SourceDeps(oneline)
%ifarch %{ix86}
%global without_sse %{!?_without_sse:0}%{?_without_sse:1}
%endif
%ifarch ia64 x86_64
%global without_sse 0
%endif
%ifnarch %{ix86} ia64 x86_64
%global without_sse 1
%endif

Summary:       Audio/MIDI multi-track sequencer
Name:          qtractor
Version:       0.5.8
Release:       alt1
License:       GPLv2+
Group:         Sound
URL:           http://qtractor.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: libalsa-devel
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
BuildRequires: libjack-devel
BuildRequires: ladspa_sdk
BuildRequires: liblo-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: qt4-devel
BuildRequires: librubberband-devel
BuildRequires: suil-devel
BuildRequires: lilv-devel
BuildRequires: autoconf
BuildRequires: automake

%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++ 
around the Qt4 toolkit using Qt Designer. The initial target platform will be
Linux, where the Jack Audio Connection Kit (JACK) for audio, and the Advanced
Linux Sound Architecture (ALSA) for MIDI, are the main infrastructures to 
evolve as a fairly-featured Linux Desktop Audio Workstation GUI, specially 
dedicated to the personal home-studio.

%prep
%setup -q -n %{name}-%{version}
sed -i -e 's|archive|archive;|' src/qtractor.desktop.in

# Fix odd permissions
chmod -x src/qtractorMmcEvent.*

%build
autoreconf
export PATH=${PATH}:%{_libdir}/qt4/bin
%configure \
   --enable-lilv --enable-suil \
%if %{without_sse}
   --enable-sse=no
%endif

%make_build

%install
make install DESTDIR=%{buildroot}
# %_datadir/locale/ is not appropriate!
mkdir -p %buildroot%_datadir/qt4/translations
mv %buildroot%_datadir/locale/*.qm %buildroot%_datadir/qt4/translations/

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}*.png
%{_datadir}/icons/hicolor/32x32/mimetypes/application*.png
%{_datadir}/mime/packages/%{name}.xml
%{_bindir}/%{name}

%changelog
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
