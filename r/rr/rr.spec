Name: rr
Version: 1.3
Release: alt1

Summary: retain / recall file and directory paths
License: GPLv2+
Group: File tools

Url: http://retain.sf.net
Source: %name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

%description
rr is a basic command-line utility designed to retain/recall file
and directory paths.  This is done by treating the filename
itself as a unique key to be referenced by for future rr program
calls.  The purpose of this is to assist the user in shorthand
typing and/or not having to remember arbitrary full paths.

%prep
%setup

%build
%configure
%make_build

%install
install -pD -m755 %name  %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*
%doc CHANGES README

%changelog
* Tue Oct 30 2007 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux

