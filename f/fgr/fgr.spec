Name: fgr
Version: 4.7.4
Release: alt1

Summary: File content search command
License: GPL
Group: File tools
Url: http://xffm.sourceforge.net/fgr.html

Source: %name-%version.tar.gz

BuildPreReq: glib2-devel
# Automatically added by buildreq on Sat Jan 19 2008
BuildRequires: gcc-c++ intltool perl-XML-Parser

%description
Fgr is a command find tool which combines the power of "find" with the
versatility of "grep".
The Xffm-find GUI uses this simple program for seaching into the
contents of files.
The ability to use fgr from either a GUI or the command line provides
this application with great versatility.

%prep
%setup

%build
intltoolize --force
libtoolize --force --copy
aclocal -I m4
automake -f -a -c
autoconf
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.4-alt1
- Version 4.7.4

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.5.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Jan 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt2
- fix build with new autotools

* Mon Nov 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt1
- First version for AltLinux Team.
