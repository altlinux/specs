# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           quarry
Version:        0.2.0
Release:        alt5_20
Summary:        A multi-purpose board game GUI

Group:          Games/Other
License:        GPLv2+
URL:            http://home.gna.org/quarry/
Source0:        http://download.gna.org/quarry/quarry-%{version}.tar.gz
Patch0:         quarry-format-security.patch

BuildRequires:  desktop-file-utils
BuildRequires:  librsvg-devel librsvg-gir-devel
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:  librarian

%description
Quarry is a multi-purpose GUI for several board games, at present Go, Amazons
and Reversi. It allows users to play against computer players (third-party
programs, e.g. GNU Go or GRhino) or other humans, view and edit game records.
Future versions will also support Internet game servers and provide certain
features for developers of board game-playing engines for enhancing their
programs.

%prep
%setup -q
%patch0 -p1


%build
export CFLAGS="%{optflags} -std=gnu89"
%configure --disable-scrollkeeper-update
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

# desktop file
desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --remove-key Version \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/quarry.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING-DOC NEWS README THANKS TODO
%{_bindir}/quarry
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/quarry.xml
%{_datadir}/pixmaps/quarry.png
%{_datadir}/omf/quarry/
%{_datadir}/quarry/


%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_20
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_12
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_9
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_7
- rebuild with new rpm desktop cleaner

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- rebuild with new librsvg

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- converted from Fedora by srpmconvert script

