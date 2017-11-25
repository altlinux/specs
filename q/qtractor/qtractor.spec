# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/qmake-qt4 gcc-c++ libX11-devel libXext-devel lv2-devel pkgconfig(ogg) pkgconfig(zlib)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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
Version:       0.8.4
Release:       alt1_1
License:       GPLv2+
Group:         Sound
URL:           http://qtractor.sourceforge.net/
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Source20:      qmake-qt5.sh

Patch3:        qtractor-0.6.4-secondary.patch

BuildRequires: libalsa-devel
BuildRequires: desktop-file-utils
BuildRequires: dssi-devel
# for plugin GUI support:
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires: libjack-devel
BuildRequires: ladspa_sdk
BuildRequires: liblo-devel
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-designer qt5-tools
BuildRequires: qt5-x11extras-devel
BuildRequires: librubberband-devel
BuildRequires: libsuil-devel
BuildRequires: liblilv-devel
BuildRequires: autoconf
BuildRequires: automake

Requires:      icon-theme-hicolor
Source44: import.info

%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++ 
around the Qt4 toolkit using Qt Designer. The initial target platform will be
Linux, where the Jack Audio Connection Kit (JACK) for audio, and the Advanced
Linux Sound Architecture (ALSA) for MIDI, are the main infrastructures to 
evolve as a fairly-featured Linux Desktop Audio Workstation GUI, specially 
dedicated to the personal home-studio.

%prep
%setup -q -n %{name}-%{version}
#patch3 -p1 -b .second

# configure hard-codes prepending searches of /usr (already implicit, causes problems),
# and /usr/local (not needed here), so force it's non-use -- rex
sed -i.ac_with_paths -e "s|^ac_with_paths=.*|ac_with_paths=|g" configure configure.ac
# fedora uses appdata
sed -i -e 's|/metainfo|/appdata|g' src/src.pro

# Fix odd permissions
chmod -x src/qtractorMmcEvent.*

%build
autoreconf

CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS

# force use of custom/local qmake, to inject proper build flags (above)
install -m755 -D %{SOURCE20} bin/qmake-qt5
PATH=`pwd`/bin:%{_qt5_bindir}:$PATH; export PATH

%configure \
   --enable-lilv --enable-suil \
%if %{without_sse}
   --enable-sse=no
%endif

%make_build QMAKE=`pwd`/bin/qmake-qt5


%install
make install DESTDIR=%{buildroot}
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_bindir}/%{name}
%{_bindir}/%{name}_vst_scan
%{_datadir}/man/man1/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
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
