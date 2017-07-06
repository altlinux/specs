# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel
# END SourceDeps(oneline)
Name:           puzzle-master
Version:        2.0.0
Release:        alt3_8
Summary:        Fun and addictive jigsaw puzzle game

Group:          Games/Other
License:        GPLv2+
URL:            http://puzzle-master.colorful.hu/

Source0:        %{name}-%{version}.tar.gz
# This package is generated from upstream's SCM, in the following way;
# %{name} refers to the package name and %{version} to the release version.
#
# git clone git://gitorious.org/colorful-apps/%{name}.git; cd %{name};
# git archive --format=tar --prefix=%{name}-%{version}/ v%{version} | gzip -n > %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(QtCore) pkgconfig(QtGui) pkgconfig(QtOpenGL) pkgconfig(QtDeclarative)
BuildRequires: desktop-file-utils
Source44: import.info
Patch1:     %name-%version-alt-build.patch

%description
%{name} is a jigsaw puzzle game that lets you use your own
images (and contains some built-in ones) for generating puzzles.
You can decide the size and the difficulty of the puzzle.

%prep
%setup -q
%patch1 -p2

%build
# This ensures that the files will be placed to the correct location
QMAKEFLAGS=''
QMAKEFLAGS+=' -after target.path=%{_bindir}'
QMAKEFLAGS+=' -after desktopfile.path=%{_datadir}/applications'
QMAKEFLAGS+=' -after iconfile.path=%{_datadir}/icons/hicolor/scalable/apps'
# This will find qmake on both Fedora and MeeGo
qmake-qt4 $QMAKEFLAGS || qmake $QMAKEFLAGS
make %{?_smp_mflags}

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%doc LICENSE
%doc LICENSE-DOCS

%changelog
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

