Name:           wordwarvi
Version:        0.25
Release:        alt2_8
Summary:        Side-scrolling shoot 'em up '80s style arcade game
Group:          Games/Other
License:        GPLv2+ and CC-BY and CC-BY-SA
URL:            http://wordwarvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRequires:  gtk2-devel libportaudio2-devel libvorbis-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Word War vi is your basic side-scrolling shoot 'em up '80s style arcade game.
You pilot your "vi"per craft through core memory, rescuing lost .swp files,
avoiding OS defenses, and wiping out those memory hogging emacs processes.
When all the lost .swp files are rescued, head for the socket which will take
you to the next node in the cluster.

Note: Obviously, emacs is a fine editor and this is all very tongue in cheek,
so don't be getting all bent out of shape because you like emacs better than
vi, mmm-kay?


%prep
%setup -q


%build
make %{?_smp_mflags} PREFIX=%{_prefix} OPTIMIZE_FLAG="$RPM_OPT_FLAGS"


%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install           \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps


%files
%doc AUTHORS COPYING README changelog.txt sounds/Attribution.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_6
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_5
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_4
- converted from Fedora by srpmconvert script

