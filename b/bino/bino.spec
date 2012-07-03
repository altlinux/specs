# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtk-update-icon-cache /usr/bin/update-desktop-database gcc-c++ libXNVCtrl-devel pkgconfig(Equalizer) pkgconfig(QtOpenGL) pkgconfig(gl) pkgconfig(libavcodec) pkgconfig(libavdevice) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(liblircclient0) pkgconfig(libswscale)
# END SourceDeps(oneline)
Summary(ru): Видеоплеер с поддержкой 3D и многомониторных конфигураций
Summary(ru): Видеоплеер с поддержкой 3D и многомониторных конфигураций
Summary(ru): Видеоплеер с поддержкой 3D и многомониторных конфигураций
Summary(ru): Видеоплеер с поддержкой 3D и многомониторных конфигураций
Name:               bino
Version:            1.3.4
Release:            alt1_1
Summary:            Video Player with 3D and Multi-Display Video Support
Summary(ru):        Видеоплеер с поддержкой 3D и многомониторных конфигураций

Source:             http://download.savannah.nongnu.org/releases-noredirect/%{name}/%{name}-%{version}.tar.xz
Source1:            bino.desktop
Source100:          README.RFRemix
URL:                http://bino.nongnu.org/
Group:              Video
License:            GPLv2

BuildRequires:      qt4-devel
BuildRequires:      libglew-devel >= 1.5.0
BuildRequires:      libopenal-devel
BuildRequires:      autoconf automake libtool
BuildRequires:      desktop-file-utils
BuildRequires:      texinfo
BuildRequires:      libass-devel
BuildRequires:      libX11-devel
BuildRequires:      libglewmx1.7
Source44: import.info


%description
Bino is a video player with two special features:
* support for 3D videos, with a wide variety of input and output formats.
* support for multi-display video, e.g. for powerwalls, Virtual Reality
  installations and other multi-projector setups.

%description -l ru
Bino это видеоплеер с двумя специальными возможностями:
* поддержка 3D видео с широким спектром выходных и выходных форматов.
* поддержка многомониторного видео, т.е. для стен, устройств
  виртуальной реальности и других многопроекторных установок.


%prep
%setup -q

%build
autoreconf -i
%configure --disable-silent-rules

make %{?_smp_mflags}
cp %{SOURCE100} .


%install
%makeinstall

install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -r %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README README.RFRemix
%doc doc/*.html doc/*.jpg doc/*.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_1
- update to new release by fcimport

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_1.R
- rebuild with fixed Equalizer

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1.R
- update to new release by fcimport

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_2.R
- excluded mimeinfo.cache

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2.R
- converted by srpmconvert script

