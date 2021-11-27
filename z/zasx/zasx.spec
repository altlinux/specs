Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           zasx
Version:        1.30
Release:        alt2_33
Summary:        Asteroid like game with powerups
License:        GPLv2+ and Freely redistributable without restriction
URL:            https://www.allegro.cc/depot/Zasx/
# Original link (down): http://www.bob.allegronetwork.com/zasx/zasx130s.zip
Source0:        zasx130s.zip
Source1:        zasx.desktop
Source2:        zasx.appdata.xml
Patch0:         zasx-1.30-fixes.patch
Patch1:         zasx-1.30-datadir.patch
Patch2:         zasx-1.30-format-security.patch
Patch3:         zasx-1.30-locale-fix.patch
BuildRequires:  gcc
BuildRequires:  dumb-devel ImageMagick-tools desktop-file-utils libappstream-glib
Requires:       icon-theme-hicolor
Source44: import.info
Patch33: zasx-1.30-alt-allegro-4.4.patch

%description
Shoot the asteroids before they hit your ship and collect power ups to restore
your shields and improve your weapons. The game features single and dualplayer 
mode, joystick, music and sound.


%prep
%setup -q -n Zasx
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i 's/\r//' copying.txt readme.txt docs/index.html docs/%{name}.css
mv docs html

# as-needed
sed -i -e 's,$(CC) $(LDFLAGS) -o $@ $^,$(CC) -o $@ $^ $(LDFLAGS),' Makefile

%patch33 -p1

%build
%make_build PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DALLEGRO_FIX_ALIASES -Wno-deprecated-declarations"
convert -transparent black -resize 64x64 %{name}.ico %{name}.png


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc readme.txt html
%doc --no-dereference copying.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 1.30-alt2_33
- fixed build

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_27
- update to new release by fcimport

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

