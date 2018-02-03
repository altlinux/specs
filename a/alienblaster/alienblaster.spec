# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           alienblaster
Version:        1.1.0
Release:        alt2_21
Summary:        Action-loaded 2D arcade shooter game
Group:          Games/Other
License:        GPLv2+
URL:            http://www.schwardtnet.de/alienblaster/
Source0:        http://www.schwardtnet.de/%{name}/archives/%{name}-%{version}.tgz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}-16x16.png
Source4:        %{name}-32x32.png
Source5:        %{name}-48x48.png
Patch0:         alienblaster-1.1.0-64bit.patch
Patch1:         alienblaster-1.1.0-fullscreen.patch
BuildRequires:  libSDL_mixer-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Alien Blaster is an action-loaded 2D arcade shooter game. Your mission in the 
game is simple: stop the invasion of the aliens by blasting them. 
Simultaneous two-player mode is available.

%prep
%setup -q -n %{name}
%patch0 -p1 -z .64bit
%patch1 -p1 -z .fs

# link with --as-needed
sed -i -e 's,$(GAME_LIBS) -o $(GAME_NAME) $(OBJECT_FILES),-o $(GAME_NAME) $(OBJECT_FILES) $(GAME_LIBS),' src/Makefile

%build
%make_build OPTIMIZATION="$RPM_OPT_FLAGS"

%install
# no make install, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 755 alienBlaster $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
cp -a images sound cfg $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc LICENSE CHANGELOG AUTHORS
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_21
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_20
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_18
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_12
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7
- initial release by fcimport

