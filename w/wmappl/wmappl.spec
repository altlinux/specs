Name: wmappl
Version: 0.71
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A simple application launcher for the WindowMaker
License: GPLv2+
Group: Graphical desktop/Window Maker

URL: http://wmappl.sourceforge.net/
Source: http://dl.sourceforge.net/wmappl/wmappl-%version.tar.gz

# Automatically added by buildreq on Tue Oct 06 2009
BuildRequires: imake imlib2-devel libXext-devel libXpm-devel libXt-devel xorg-cf-files

%description
WMAppl is a simple application launcher for the Window Maker dock. It displays
up to six application icons at a time and two scroll arrows. The scroll arrows
will scroll the displayed application icons through the list of configured
applications. When an application icon is pressed, the configured command line
is executed.

%prep
%setup

%build
%configure --enable-Imlib2
%make ICONDIR=%_iconsdir/wmappl

%install
%makeinstall_std pkgdatadir=%_iconsdir/wmappl

%files
%_bindir/*
%_iconsdir/wmappl
%_man1dir/*
%_man5dir/*

%changelog
* Tue Oct 06 2009 Victor Forsyuk <force@altlinux.org> 0.71-alt2
- Refreshed BuildRequires to fix repocop warning.

* Wed Apr 06 2005 Victor Forsyuk <force@altlinux.ru> 0.71-alt1
- Fix URL.
- Build with enabled Imlib2.
- Package man pages.

* Mon Apr 28 2003 Ott Alex <ott@altlinux.ru> 0.61-alt1
- Initial build

