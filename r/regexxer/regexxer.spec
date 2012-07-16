Name: regexxer
Version: 0.9
Release: alt0.2

Summary: regexxer is a nifty search/replace tool for the desktop user.
Group: Text tools
Source: %name-%version.tar.gz
Patch: regexxer-0.9-alt-glib2.patch
License: GPL
Packager: Eugene Ostapets <eostapets@altlinux.org>

# Automatically added by buildreq on Sun May 06 2007
BuildRequires: gcc-c++ GConf libgconfmm2-devel libglademm-devel libpcre-devel perl-XML-Parser

%description
regexxer is a nifty search/replace tool for the desktop user.  It features
recursive search through directory trees and Perl-style regular expressions
(using libpcre).

regexxer is written in C++ and uses gtkmm (the C++ wrapper for GTK+) for
the GUI.  The user interface is similar to the project-wide search/replace
dialog in the Sniff+ IDE, but regexxer aims to surpass it.

The primary audience of this tool are Linux/Unix users who are tired of
typing find/grep/sed/awk/perl command lines.

%prep
%setup
%patch -p2

%build
%configure 
%make_build

%install
%make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%dir %_datadir/%name
%_datadir/%name/*
%_sysconfdir/gconf/schemas/%name.schemas

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt0.2
- Fixed build

* Sun May 06 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9-alt0.1
- first build

