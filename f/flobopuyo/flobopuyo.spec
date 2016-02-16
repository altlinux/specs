# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
Name:           flobopuyo
Version:        0.20
Release:        alt4_17
Summary:        2-player falling bubbles game

Group:          Games/Other
License:        GPLv2+
URL:            http://www.ios-software.com/?page=projet&quoi=29
# The upstream source link is a php script that sends the file.  This
# works fine for wget and curl, but confuses rpmbuild when it wants to unpack
# the source tarball.
#Source0:        http://www.ios-software.com/download.php3?what=20151&lg=AN
Source0:        %{name}-%{version}.tgz
Source1:        %{name}.desktop
# Icon converted with icns2png
Source2:        %{name}.png
# Wart
Patch0:         %{name}-0.20-64bit.patch
# Andrea Musuruane
Patch1:         %{name}-0.20-Makefile.patch

BuildRequires:  flex 
BuildRequires:  bison 
BuildRequires:  libSDL_mixer-devel 
BuildRequires:  libSDL_image-devel 
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
%patch0
%patch1 -p1

# Fix end-of-line-encoding
sed -i 's/\r//' COPYING

# Remove AppleDouble files
rm data/sfx/._bi


%build
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} PREFIX=%{_prefix}


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man6
install -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6

# Install desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/


%files
%doc COPYING TODO Changelog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
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

