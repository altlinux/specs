# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize
# END SourceDeps(oneline)
Name:           gamazons
Version:        0.83
Release:        alt4_16
Summary:        GNOME Amazons

Group:          Games/Other
License:        GPLv2
URL:            http://www.yorgalily.org/gamazons/
Source0:        http://www.yorgalily.org/gamazons/src/gamazons-%{version}.tar.gz

BuildRequires:  libgnomeui-devel desktop-file-utils
Source44: import.info

%description
Amazons is a game played on a 10x10 chess board. Each side has four
pieces (amazons) that move like chess queens (in a straight line in
any direction). Instead of capturing pieces like in chess, the game is
determined based on who moves last.

Each move consists of two parts. First an amazon moves to a new square
and then fires an arrow to another square (the arrow is fired in a
straight line in any direction from the square the amazon landed
on). The square the arrow lands on becomes a permenant block for the
rest of the game. No one can move over it, or fire an arrow over
it. Every turn an amazon must move and fire an arrow, so every turn
there is one less square available on the board. Try and block in your
opponent or section off a good chunk of the board for yourself.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
                     --delete-original \
                     --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
                     --remove-key=OnlyShowIn \
  $RPM_BUILD_ROOT%{_datadir}/applications/gamazons.desktop


%files
%doc COPYING src/gamazon.bugs src/thots
%{_bindir}/gamazons
%{_datadir}/applications/gamazons.desktop
%{_datadir}/gnome/help
%{_datadir}/gamazons
%{_datadir}/pixmaps/gamazons
%{_datadir}/pixmaps/gnome-gamazons.png



%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_12
- update to new release by fcimport

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.83-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_8
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1_6
- converted from Fedora by srpmconvert script

