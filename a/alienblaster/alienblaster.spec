# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           alienblaster
Version:        1.1.0
Release:        alt2_9
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
make %{?_smp_mflags} OPTIMIZATION="$RPM_OPT_FLAGS"


%install
# no make install, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 755 alienBlaster $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
cp -a images sound cfg $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
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
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7
- initial release by fcimport

