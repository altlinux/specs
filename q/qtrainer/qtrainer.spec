Name:		qtrainer
Summary:	Qtrainer is a personal home trainer for Qt4
Version:	0.5.2
Release:	alt2.qa1
Group:		Office
License:	GPLv2+
Packager: 	Mikhail Pokidko <pma@altlinux.ru>
URL:		http://tuxer.ulyssis.be/homepage/qtrainer.html
Source:		%name-%{version}_SRC.tar.gz
Source1:	%name.desktop
Patch0:		%name.patch

BuildRequires: gcc-c++ libqt4-devel libqt4-network libqt4-svg

%description
Qtrainer is a personal home trainer for Qt4 (Windows or KDE3/KDE4(you just need Qt4))
Qtrainer plots your progress, gives you tips and training schedules.
It also lets you plan your trainings.
Qtrainer also has an online database of exercises.


%prep
%setup -q
#patch0 -p1

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
install -Dp -m 0755 bin/%name %buildroot%_bindir/%name
install -Dp -m 0644 src/logo.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop


%files
%_bindir/*
%_iconsdir/hicolor/scalable/apps/*
%_desktopdir/*

%changelog
* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for qtrainer
  * postclean-05-filetriggers for spec file

* Thu Oct 16 2008 Mikhail Pokidko <pma@altlinux.org> 0.5.2-alt2
- spec changes (thx  to drool@); added desktop-file

* Thu Mar 27 2008 Mikhail Pokidko <pma@altlinux.org> 0.5.2-alt1
- version up

* Wed Sep 26 2007 Mikhail Pokidko <pma@altlinux.org> 0.5-alt3
- arch bugfix

* Wed Sep 26 2007 Mikhail Pokidko <pma@altlinux.org> 0.5-alt2
- Little bugfixes

* Mon Sep 10 2007 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- Initial build


