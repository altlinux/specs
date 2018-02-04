# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install imake libX11-devel libXext-devel perl(find.pl) xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xgalaxy
Version:        2.0.34
Release:        alt2_27
Summary:        Arcade game: shoot down the space ships attacking the planet
Group:          Games/Other
License:        GPL+
URL:            http://sourceforge.net/projects/xgalaga/
Source0:        http://downloads.sourceforge.net/xgalaga/xgalaga_%{version}.orig.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-hyperspace.desktop
Patch0:         http://ftp.debian.org/debian/pool/main/x/xgalaga/xgalaga_2.0.34-44.diff.gz
Patch1:         %{name}-2.0.34-fullscreen.patch
Patch2:         %{name}-2.0.34-%{name}.patch
Patch3:         %{name}-2.0.34-joy.patch
Patch4:         %{name}-2.0.34-fullscreen-viewport.patch
Patch5:         %{name}-2.0.34-alsa.patch
Patch6:         %{name}-2.0.34-dga-compile-fix.patch
BuildRequires:  libXt-devel libXpm libXpm-devel libXmu-devel libXxf86vm-devel
BuildRequires:  libalsa-devel desktop-file-utils ImageMagick-tools 
Requires:       icon-theme-hicolor
Obsoletes:      xgalaga <= %{version}
Provides:       xgalaga = %{version}-%{release}
Source44: import.info

%description
Arcade game for the X Window System where you have to shoot down the space
ships attacking the planet.
 

%prep
%setup -q -n xgalaga-%{version}
# many thanks to Debian for all their excellent work on xgalala
%patch0 -p1 -z .deb
%patch1 -p1 -z .fs
%patch2 -p1 -z .%{name}
%patch3 -p1 -z .joy
%patch4 -p1 -z .viewport
%patch5 -p1 -z .alsa
%patch6 -p1 -z .no-dga
sed -e 's/Debian/Fedora/g' debian/README.Debian > README.fedora
cat >> README.fedora << EOF

The latest Fedora %{name} package also includes fullscreen support, start
%{name} with -window to get the old windowed behavior. You can switch on the
fly between window and fullscreen mode with alt+enter.
EOF

# Change the name everywhere as upstreams name has already been used for a game
# much like this one in the past, upstreams use of this is a legal gray area.
sed -i 's/xgalaga/xgalaxy/g' `grep -rls xgalaga .`
sed -i 's/XGalaga/XGalaxy/g' `grep -rls XGalaga .`


%build
sed -i 's,LIBS = @LIBS@ libsprite/libsprite.a @X_LIBS@,LIBS = libsprite/libsprite.a @LIBS@ @X_LIBS@,' Makefile.in
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DXF86VIDMODE"
export X_LIBS=-lXxf86vm
./configure --libdir=%{_libdir} --exec-prefix=%{_bindir} \
  --prefix=%{_datadir}/%{name}
sed -i s/xgal.sndsrv.oss/xgal.sndsrv.alsa/ Makefile
%make_build SOUNDLIBS=-lasound
convert images/player3.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# move the sound-server binary out of %{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_bindir}
ln -s ../../bin/xgal.sndsrv.alsa \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/xgal.sndsrv.alsa
# fix useless exec bit
chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/*/*
# make install doesn't install the manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 xgal.6x $RPM_BUILD_ROOT%{_mandir}/man6/%{name}.6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
desktop-file-install        \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps

%files
%doc CHANGES COPYING README README.fedora
%{_bindir}/%{name}*
%{_bindir}/xgal.sndsrv.alsa
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_27
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_26
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_24
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_23
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_22
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_19
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_17
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt2_16
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt1_16
- update to new release by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.34-alt1_15
- initial release by fcimport

