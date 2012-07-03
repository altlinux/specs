# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           arrows
Version:        0.6
Release:        alt3_11
Summary:        Neat little maze game
Group:          Games/Other
License:        GPLv2+
URL:            http://noreason.ca/?file=software
Source0:        http://noreason.ca/data/arrows-%{version}.tar.gz
Source1:        arrows.desktop
Source2:        arrows.png
Patch0:         arrows-level-5.patch 
BuildRequires:  libgtk+2-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
It's a maze game of sorts. Guide the spinning blue thing through
the maze of arrows, creating and destroying arrows as necessary
to collect the green things.


%prep
%setup -q
%patch0 -p1
make clean


%build
make %{?_smp_mflags} CCOPTS="$RPM_OPT_FLAGS"


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 644 arrfl.? $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps


%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_11
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_11
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_10
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_9
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_9
- converted from Fedora by srpmconvert script

