Name: gnugo
Version: 3.8
Release: alt2.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GNU Go is a free program that plays the game of Go
License: GPLv3+
Group: Games/Boards
Url: http://www.gnu.org/software/gnugo/

Requires: %name-core

Source0: http://ftp.gnu.org/gnu/gnugo/gnugo-%version.tar.gz
Source1: gnugo.desktop
Source2: gnugo.svg
# fedora
Patch1: gnugo-3.8-format-security.patch

# Automatically added by buildreq on Tue Jun 30 2009
BuildRequires: libncurses-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
GNU Go is a free program that plays the game of Go. GNU Go has played thousands
of games on the NNGS Go server. GNU Go is now also playing regularly on the
Legend Go Server in Taiwan and the WING server in Japan.

%package core
Summary: %name core package
Group: System/Libraries
Conflicts: %name < 3.8-alt2.1
%description core
%{description}

%prep
%setup
%patch1 -p1

%build
%add_optflags -fcommon
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/gnugo.desktop
install -pD -m644 %SOURCE2 %buildroot/%_iconsdir/hicolor/scalable/apps/gnugo.svg

%files
%_desktopdir/*
%_iconsdir/*/*/apps/gnugo.*

%files core
%_bindir/*
%_man6dir/*
%_infodir/gnugo.*

%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 3.8-alt2.1
- NMU: add patch for printf format security
- NMU: add desktop icon
- NMU: split desktop-file to separate package

* Fri Mar 26 2021 Grigory Ustinov <grenka@altlinux.org> 3.8-alt2
- Fixed FTBFS with -fcommon

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1.qa1.1
- NMU: added BR: texinfo

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 3.8-alt1
- 3.8

* Wed Dec 31 2008 Victor Forsyuk <force@altlinux.org> 3.6-alt3
- Remove obsolete desktop menu updating.

* Mon Jun 11 2007 Victor Forsyuk <force@altlinux.org> 3.6-alt2
- Small spec cleanups and corrections.
- Refresh build requirements.
- Switch to freedesktop-style menu.
- Really install .info files.

* Wed Oct 26 2005 Ivan Evtuhovich <brun@altlinux.ru> 3.6-alt1
- New version

* Tue Feb 10 2004 Ivan Evtuhovich <brun@altlinux.ru> 3.4-alt1
- New version

* Wed Apr 02 2003 Ivan Evtuhovich <brun@altlinux.ru> 3.2-alt0.1
- Initial build.
