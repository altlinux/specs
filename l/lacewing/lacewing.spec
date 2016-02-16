# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
%define fedora 23
Name:           lacewing
Version:        1.10
Release:        alt2_26
Summary:        Arcade-style shoot-em-up
Group:          Games/Other
License:        GPLv2+
URL:            http://users.olis.net.au/zel/
Source0:        http://users.olis.net.au/zel/lwsrc.zip
Source1:        http://users.olis.net.au/zel/lwdata.zip
Source2:        lacewing.desktop
Source3:        lacewing.png
Patch0:         lacewing.patch
Patch1:         lacewing-fullscreen.patch
Patch2:         lacewing-nicecpu.patch
Patch3:         lacewing-warn.patch
Patch4:         lacewing-format-security.patch
Patch5:         lacewing-rhbz1045111.patch
BuildRequires:  liballegro-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info
Patch33: lacewing-1.10-alt-as-needed.patch

%description
Arcade-style shoot-em-up where you can choose a type of ship and depending on
the type of ship can pickup a number of upgrades during the game.

Lacewing is an arcade-style shoot-em-up which plays a little bit like a cross
between Spacewar and Centipede. It has a decidedly retro style to it. It has
a single-player mode, and also co-operative and duel modes for two players
(split-screen).


%prep
%setup -q -c
unzip -qqo %{SOURCE1}
%patch0 -p1 -z .unix
%patch1 -p1 -z .fullscreen
%patch2 -p1 -z .nicecpu
%patch3 -p1 -z .warn
%patch4 -p1
%patch5 -p1
sed -i 's/\r//' readme.txt licence.txt
chmod 644 readme.txt licence.txt
%patch33 -p1


%build
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations"


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
              \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%files
%doc readme.txt licence.txt
%{_bindir}/lacewing
%{_datadir}/lacewing
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/lacewing.desktop
%else
%{_datadir}/applications/lacewing.desktop
%endif
%{_datadir}/icons/hicolor/48x48/apps/lacewing.png


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_26
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_25
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_24
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_23
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_21
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_20
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_19
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_18
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_17
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_17
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_16
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_15
- initial release by fcimport

