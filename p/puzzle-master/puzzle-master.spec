Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate gcc-c++ pkgconfig(x11) qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           puzzle-master
Version:        2.5.3
Release:        alt2_7
Summary:        Fun jigsaw puzzle game

License:        GPLv2+
URL:            https://github.com/Venemo/puzzle-master

Source0:        https://github.com/Venemo/puzzle-master/archive/v%{version}.tar.gz

BuildRequires: pkgconfig(Qt5Core), pkgconfig(Qt5Gui), pkgconfig(Qt5Quick)
BuildRequires: desktop-file-utils
Source44: import.info

%description
%{name} is a jigsaw puzzle game that lets you use your own
images (and contains some built-in ones) for generating puzzles.
You can decide the size and the difficulty of the puzzle.

%prep
%setup -q
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.hpp' -o -name '*.cc' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
# These flags ensure that the files will be placed to the correct location
QMAKEFLAGS=''
QMAKEFLAGS+=' -after target.path=%{_bindir}'
QMAKEFLAGS+=' -after desktopfile.path=%{_datadir}/applications'
QMAKEFLAGS+=' -after iconfile.path=%{_datadir}/icons/hicolor/scalable/apps'
QMAKEFLAGS+=' -after appdatafile.path=%{_datadir}/appdata'

qmake-qt5 $QMAKEFLAGS
%make_build

%install
%{makeinstall_std} INSTALL_ROOT=$RPM_BUILD_ROOT
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%attr(644,root,root) %{_datadir}/appdata/%{name}.appdata.xml
%doc LICENSE
%doc LICENSE-DOCS

%changelog
* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_7
- merged e2k patch

* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 2.5.3-alt2_3
- E2K: strip UTF-8 BOM for lcc < 1.24

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_3
- update to new release by fcimport

* Thu Jul 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt3_8
- Fixed build with new toolchain

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_2
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_3
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- converted from Fedora by srpmconvert script

