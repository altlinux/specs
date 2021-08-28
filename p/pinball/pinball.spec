Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install cppunit-devel imake libSDL-devel libX11-devel liballegro-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pinball
Version:        0.3.4
Release:        alt1_8
Summary:        Emilia 3D Pinball Game
# core license is GPLv2+
# gnu table licenses are (GFDL or Free Art or CC-BY-SA) and GPLv3 and CC-BY-SA
# hurd table license is GPLv2+
License: GPLv2+ and (GFDL or Free Art or CC-BY-SA) and GPLv3 and CC-BY-SA
URL:            http://pinball.sourceforge.net
Source0:        https://github.com/sergiomb2/pinball/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libXt-devel
BuildRequires:  libfreeglut-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libpng-devel libpng17-tools
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libltdl7-devel
BuildRequires:  gettext-tools libasprintf-devel
Requires:   icon-theme-hicolor
Requires:   opengl-games-utils
Requires:   timidity-instruments
Source44: import.info

%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release features a number of tables:
tux, professor, professor2, gnu and hurd and is very addictive.

%package devel
Group: Games/Other
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains files for development with %{name}.
May be used in pinball-pinedit.


%prep
%setup -q
sed -i 's/Exec=pinball/Exec=pinball-wrapper/' pinball.desktop
./bootstrap


%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%configure --disable-static
%make_build


%install
%makeinstall_std
%find_lang %{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
# remove unused test module
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
# .la files are needed for ltdl

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --set-key='Keywords' --set-value='Game;Arcade;Pinball;' \
  pinball.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pinball.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 pinball.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc README ChangeLog
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*so.*
%{_libdir}/%{name}/*la
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files devel
%{_bindir}/%{name}-config
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.a
%{_includedir}/%{name}


%changelog
* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 0.3.4-alt1_8
- fixed build

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_1
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_27
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_25
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_23
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_22
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_21
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_20
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_19
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_18
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_18
- update to new release by fcimport

* Sun Jul 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_17
- initial release by fcimport

