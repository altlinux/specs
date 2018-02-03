# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 6beed311c2ecb3f9662f35ecc06948bd89ed9455
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wordwarvi
Version:        1.1
Release:        alt1_6.git%{shortcommit}
Summary:        Side-scrolling shoot 'em up '80s style arcade game
Group:          Games/Other
License:        GPLv2+ and CC-BY and CC-BY-SA
URL:            https://smcameron.github.io/wordwarvi/
# The 1.1 release never got a tag in git, so we use the commit-id
Source0:        https://github.com/smcameron/wordwarvi/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel libportaudio2-devel libvorbis-devel
BuildRequires:  desktop-file-utils libappstream-glib
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
%setup -qn %{name}-%{commit}


%build
%make_build PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS"


%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS COPYING README changelog.txt sounds/Attribution.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6.git6beed31
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5.git6beed31
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3.git6beed31
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2.git6beed31
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_9
- update to new release by fcimport

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

