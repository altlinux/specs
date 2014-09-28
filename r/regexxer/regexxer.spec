Name: regexxer
Version: 0.11
Release: alt1.git20140920

Summary: regexxer is a nifty search/replace tool for the desktop user.
Group: Text tools
URL: http://regexxer.sourceforge.net/
# git://git.gnome.org/regexxer
Source: %name-%version.tar.gz
License: GPL

# Automatically added by buildreq on Sun May 06 2007
BuildRequires: gcc-c++ GConf libgconfmm2-devel libglademm-devel libpcre-devel perl-XML-Parser

BuildPreReq: intltool libgtkmm3-devel libgtksourceviewmm3-devel

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

%build
%autoreconf
%configure 
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%dir %_datadir/%name
%_datadir/%name/*
#_sysconfdir/gconf/schemas/%name.schemas
%_datadir/glib-2.0/schemas/org.regexxer.gschema.xml

%changelog
* Sun Sep 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20140920
- Version 0.11

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9-alt0.2.qa1
- NMU: rebuilt for updated dependencies.

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt0.2
- Fixed build

* Sun May 06 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9-alt0.1
- first build

