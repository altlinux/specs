%define origname wxRemind

Name: wxremind
Version: 101
Release: alt1

Summary: wxRemind is a graphical front-end to Remind
License: GPLv2+
Group: Office

Url: http://www.duke.edu/~dgraham/wxRemind/
Source0: %url/%origname-src-%version.tgz
Source1: wxremind.desktop
Packager: Michael Shigorin <mike@altlinux.org>

AutoReq: yes, noshell
BuildArch: noarch

# Automatically added by buildreq on Thu Jun 21 2007 (-bi)
BuildRequires: zip

Requires: python-module-wx
Requires: python-module-dateutil
Requires: remind

%description
wxRemind is a graphical front-end to Remind, a remarkably
sophisticated calendar and alarm system.

The display features a calendar and daily event list suitable
for visualizing your schedule at a glance. Dates and associated
events can be quickly selected either with the mouse or cursor
keys, and dates in the calendar are color coded to reflect the
total duration of scheduled events. wxRemind integrates with an
external editor of your choice to make editing of reminder files
more efficient, provides hotkeys to quickly access the most
common Remind options, allows popup, sound and/or spoken alerts
and can display a postscript calendar of the selected month
suitable for printing.

NB: requires UTF8-encoded ~/.reminders!

%prep
%setup
sed -i 's,\.\./\(wxremind-dist\),\1,g' make_dist.sh
sed -i 's,^\(version=\).*$,\1%version,g' make_dist.sh

%build
mkdir -p wxremind-dist/{docs-wxRemind,wxremind-%version}
./make_dist.sh

%install
install -d %buildroot%_bindir
install -pm755 wxremalert wxremdata wxremind wxremhints \
	%buildroot%_bindir/
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_desktopdir/*

# TODO
# - just drop *.py properly, no need to zip things up
#   (macosish crap looks awful)

%changelog
* Tue Apr 12 2011 Michael Shigorin <mike@altlinux.org> 101-alt1
- 101 (reworked installation, argh)
- added missing dependencies (see #25426)
- fixed desktop file
- added warning regarding unicode data file requirement

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt2.1
- Rebuilt with python 2.6

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.9.6-alt2
- applied repocop patch

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 0.9.6-alt1.1
- Rebuilt with python-2.5.

* Thu Jun 21 2007 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- built for ALT Linux
- added initial desktop file

