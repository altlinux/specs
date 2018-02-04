# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ perl(Archive/Tar.pm) perl(Archive/Zip.pm)
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           magicmaze
Version:        1.0.2
Release:        alt2_21
Summary:        Board game featuring a maze which the players change each turn
Group:          Games/Other
License:        zlib and Redistributable, no modification permitted
URL:            http://www.helixsoft.nl/project_page.php?file_name=magicmaze.proj
Source0:        http://www.helixsoft.nl/download/%{name}-%{version}_src.tar.gz
Source1:        %{name}.desktop
Patch0:         maze-1.0-gcc4.patch
Patch1:         maze-1.0-no-sound.patch
Patch2:         maze-1.0-fhs.patch
Patch3:         magicmaze-1.0.2-license-clarification.patch
Patch4:         magicmaze-1.0.2-trademarks.patch
Patch5:         magicmaze-1.0.2-format-security.patch
BuildRequires:  libgstream-devel dumb-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
The board of the game is a complicated maze. You see reddish squares, which are
walls, and black lanes, which are walkable. Also you see brightly coloured
(humanoid) figures and little circles. The figures are the players, and the
rounds are coins which the players must collect.

Each player gets a turn. In the beginning of your turn, you get to change the
maze. You can see a small piece of maze "sticking out" of the board. You can
make that piece move around the board an rotate it. When you are done the
piece is pushed in the maze, thus making a whole column or row of the maze
shift. If you do this in a clever way, new passages open up, hopefully leading
you to a coin in your players color.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
chmod -x `find -type f`


%build
%make_build -f makefile.unx PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -I/usr/include/gstream"


%install
make -f makefile.unx install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
              \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%doc license.txt docs/readme.txt docs/todo.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_21
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_20
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_18
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_11
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_10
- fc update

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_7
- update to new release by fcimport

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_6
- initial release by fcimport

