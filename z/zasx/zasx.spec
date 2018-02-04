# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           zasx
Version:        1.30
Release:        alt2_24
Summary:        Asteroid like game with powerups
Group:          Games/Other
License:        GPLv2+ and Freely redistributable without restriction
URL:            http://www.bob.allegronetwork.com/zasx/index.html
Source0:        http://www.bob.allegronetwork.com/zasx/zasx130s.zip
Source1:        zasx.desktop
Patch0:         zasx-1.30-fixes.patch
Patch1:         zasx-1.30-datadir.patch
Patch2:         zasx-1.30-format-security.patch
BuildRequires:  dumb-devel ImageMagick-tools desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Shoot the asteroids before they hit your ship and collect power ups to restore
your shields and improve your weapons. The game features single and dualplayer 
mode, joystick, music and sound.


%prep
%setup -q -n Zasx
%patch0 -p1 -z .fix
%patch1 -p1 -z .datadir
%patch2 -p1
sed -i 's/\r//' copying.txt readme.txt docs/index.html docs/%{name}.css
mv docs html

# as-needed
sed -i -e 's,$(CC) $(LDFLAGS) -o $@ $^,$(CC) -o $@ $^ $(LDFLAGS),' Makefile


%build
%make_build PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations"
convert -transparent black %{name}.ico %{name}.png


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%doc copying.txt readme.txt html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_23
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_21
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_15
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_13
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_11
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_10
- initial release by fcimport

