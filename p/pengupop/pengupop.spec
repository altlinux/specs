# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pengupop
Version:        2.2.2
Release:        alt4_19
Summary:        Networked Game in the vein of Move/Puzzle Bobble

Group:          Games/Other
License:        GPLv2+
URL:            http://www.junoplay.com/pengupop
Source0:        http://www.junoplay.com/files/%{name}-%{version}.tar.gz

BuildRequires:  libSDL-devel, zlib-devel, desktop-file-utils
Source44: import.info

%description
Finally a networked multiplayer game in the vein of the puzzle classic Bust a
Move/Puzzle Bobble. Beat your friends in this addictive game, or play against
a random opponent! The purpose of this game is to shoot colored orbs into your
playfield, so they form groups of three or more. You win if you manage to
remove all orbs. You lose if any orb attaches below the white line.


%prep
%setup -q


%build
%configure
%make_build CFLAGS="$CFLAGS -D_FORTIFY_SOURCE=0" LIBS="-lm"

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp pengupop.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        pengupop.desktop


%files
%doc AUTHORS COPYING
%{_bindir}/pengupop
%{_datadir}/applications/pengupop.desktop
%{_datadir}/icons/hicolor/48x48/apps/pengupop.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_19
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_16
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_11
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt2_7
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_7
- converted from Fedora by srpmconvert script

