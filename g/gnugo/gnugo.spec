Name: gnugo
Version: 3.8
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GNU Go is a free program that plays the game of Go
License: GPLv3+
Group: Games/Boards

URL: http://www.gnu.org/software/gnugo/
Source0: http://ftp.gnu.org/gnu/gnugo/gnugo-%version.tar.gz
Source1: gnugo.desktop

# Automatically added by buildreq on Tue Jun 30 2009
BuildRequires: libncurses-devel

%description
GNU Go is a free program that plays the game of Go. GNU Go has played thousands
of games on the NNGS Go server. GNU Go is now also playing regularly on the
Legend Go Server in Taiwan and the WING server in Japan.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/gnugo.desktop

%files
%_bindir/*
%_desktopdir/*
%_man6dir/*
%_infodir/gnugo.*

%changelog
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
