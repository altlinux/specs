Name: cutecom
Version: 0.22.0
Release: alt1.qa1

Summary: A graphical serial terminal
License: GPLv2
Group: Communications

Url: http://cutecom.sourceforge.net
Source: %url/%name-%version.tar.gz
Patch: cutecom-0.22.0-alt-desktop.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Nov 05 2008
BuildRequires: cmake gcc-c++ kdelibs libqt4-devel

Summary(pl):	Graficzny terminal szeregowy
BuildRequires: desktop-file-utils

%description
Cutecom is a graphical serial terminal, like minicom. It is aimed
mainly at hardware developers or other people who need a terminal to
talk to their devices.

%description -l pl
Cutecom to graficzny terminal szeregowy podobny do minicoma. Jest
przeznaczony g³ównie dla twórców sprzêtu i innych ludzi potrzebuj±cych
terminala do komunikacji ze swoimi urz±dzeniami.

%prep
%setup
%patch -p1

%build
PATH=$PATH:%_libdir/qt4/bin
cmake .
%configure
%make_build

%install
install -pD %name %buildroot%_bindir/%name
install -pD %name.desktop %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/cutecom.desktop

%files
%doc Changelog README
%_bindir/*
%_desktopdir/*

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.22.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cutecom

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 0.22.0-alt1
- 0.22.0
- fixed desktop file (repocop)

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 0.20.0-alt2
- applied repocop patch

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.20.0-alt1
- 0.20.0 (qt4)
- buildreq

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.14.2-alt1
- 0.14.2

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.14.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for cutecom
 * update_menus for cutecom

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 0.14.1-alt1
- 0.14.1
- buildreq

* Wed Mar 01 2006 Michael Shigorin <mike@altlinux.org> 0.13.2-alt1
- initial build for ALT Linux Sisyphus (spec from PLD Team)
  + these PLD people worked on it: blekot, qboosh, bszx
  + they can be reached at <cvs_login>@pld-linux.org
- spec cleanup
- buildreq
