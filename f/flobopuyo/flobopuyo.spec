Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           flobopuyo
Version:        0.20
Release:        alt4_23
Summary:        2-player falling bubbles game

License:        GPLv2+
URL:            http://www.fovea.cc/flobopuyo-en
Source0:        http://www.fovea.cc/files/flobopuyo/%{name}-%{version}.tgz
Source1:        %{name}.desktop
# Fix building on 64bit
# Patch by Michael Thomas aka Wart <wart at kobold dot org>
# https://lists.fedoraproject.org/archives/list/games@lists.fedoraproject.org/thread/ECMVJBXDAITOV35723OMGQSF3CLXKLZK/
Patch0:         %{name}-0.20-64bit.patch
# Patch by Andrea Musuruane
Patch1:         %{name}-0.20-Makefile.patch
# Fix segfaults on Fedora 24
# Patches by Sebastian Ott
# https://bugzilla.redhat.com/show_bug.cgi?id=1352557
# https://bugzilla.redhat.com/show_bug.cgi?id=1380525
Patch2:         %{name}-0.20-segfaults.patch
# Set proper window title
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=537352
Patch3:         %{name}-0.20-set_window_title.patch
# Fix a typo
# Patch taken from Debian
Patch4:         %{name}-0.20-fix_typo.patch

BuildRequires:  flex 
BuildRequires:  bison 
BuildRequires:  libSDL_mixer-devel 
BuildRequires:  libSDL_image-devel 
BuildRequires:  libicns-utils
BuildRequires:  desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info


%description
A two-player falling bubbles game.  The goal is to make groups of four or more
Puyos (colored bubbles) to make them explode and send bad ghost Puyos to your
opponent.  You win the game if your opponent reaches the top of the board. You
can play against computer or another human.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

# Fix end-of-line-encoding
sed -i 's/\r//' COPYING

# Remove AppleDouble files
rm data/sfx/._bi


%build
export CFLAGS="$RPM_OPT_FLAGS"
%make_build PREFIX=%{_prefix}


%install
%makeinstall_std PREFIX=%{_prefix}

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man6
install -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6

# Install desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

# Extract Mac OS X icons
icns2png -x mac/icon.icns

# Install icon
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 icon_128x128x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files
%doc TODO Changelog
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_23
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_20
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_19
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_18
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_12
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3_8
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3_7
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_7
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_7
- converted from Fedora by srpmconvert script

