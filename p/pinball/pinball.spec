Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install cppunit-devel gcc-c++ imake libSDL-devel libX11-devel liballegro-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pinball
Version:        0.3.2
Release:        alt1_8
Summary:        Emilia 3D Pinball Game
# core license is GPL+
# gnu table licenses are (GFDL or Free Art or CC-BY-SA) and GPLv3 and CC-BY-SA
# hurd table license is GPLv2+
License: GPL+ and (GFDL or Free Art or CC-BY-SA) and GPLv3 and CC-BY-SA and GPLv2+
URL:            http://pinball.sourceforge.net
Source0:        https://github.com/sergiomb2/pinball/archive/%{version}.tar.gz
Source1:        %{name}.appdata.xml
BuildRequires:  libXt-devel libfreeglut-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires:  libpng-devel libvorbis-devel libltdl7-devel
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires:  autoconf automake libtool
Requires:       icon-theme-hicolor opengl-games-utils timidity-instruments
Source44: import.info

%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release features a number of tables:
tux, professor, professor2, gnu and hurd and is very addictive.


%prep
%setup -q
sed -i 's/Exec=pinball/Exec=pinball-wrapper/' pinball.desktop
autoreconf -fiv


%build
%configure --without-included-ltdl
make


%install
%makeinstall_std INSTALL="install -p"
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
# remove unused global higescorefiles:
rm -r $RPM_BUILD_ROOT%{_localstatedir}
# remove unused test module
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
# .la files are needed for ltdl
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.{a,so}
# remove bogus development files
rm $RPM_BUILD_ROOT%{_bindir}/%{name}-config
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --set-key='Keywords' --set-value='Game;Arcade;Pinball;' \
  pinball.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pinball.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README ChangeLog
%doc --no-dereference COPYING
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
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

