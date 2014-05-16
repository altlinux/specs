Name: ddrutility
Version: 2.4
Release: alt1

Summary: Utility for use with gnuddrescue to aid with data recovery
License: GPLv3+
Group: Archiving/Backup

Url: http://sourceforge.net/projects/ddrutility/
Source0: %name-%version.tar.gz
Source1: %name.watch

%description
%name is meant to be a compliment to gnuddrescue.
It is a set of utilities to help with hard drive data rescue.
It currently contains the following utilities:

ddru_findbad
ddru_ntfsbitmap
ddru_ntfsfindbad

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_infodir/*

%changelog
* Fri May 16 2014 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Sun Apr 27 2014 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Wed Apr 23 2014 Michael Shigorin <mike@altlinux.org> 2.2-alt1
- initial package

