Name: trowser
Version: 1.3
Release: alt1

Summary: a browser for large line-oriented text files
License: GPLv3
Group: File tools

Url: http://www.nefkom.net/tomzo/prj/trowser/
Source0: %url/%name-%version.tar.gz
Source1: %name.desktop
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
Trowser is a browser for large line-oriented text files (such as debug traces).
It's meant as an alternative to "less". Compared to less, trowser adds color
highlighting, persistent search history, graphical bookmarking, separate
search result windows, and flexible skipping of input from pipes to STDIN.
Trowser has graphical interface, but is designed to allow browsing via the
keyboard at least to the same extent as less. Key bindings and the cursor
positioning concept are derived from vim.

%prep
%setup

%install
install -pDm755 trowser.tcl %buildroot%_bindir/%name
install -pDm644 trowser.1 %buildroot%_man1dir/%name.1
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%doc README trowser.pod

%changelog
* Wed Apr 01 2009 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux

