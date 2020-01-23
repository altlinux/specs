Name: makedepend
Version: 1.0.6
Release: alt1

Summary: create dependencies in makefiles
License: MIT/X11
Group: Development/C

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: xorg-xproto-devel xorg-util-macros

%description
The makedepend program reads each sourcefile in sequence and parses  it
like  a  C-preprocessor,  processing  all  #include,  #define,  #undef,
\#ifdef, #ifndef, #endif, #if, #elif and #else directives so that it can
correctly  tell  which #include, directives would be used in a compila-
tion.  Any  #include,  directives  can  reference  files  having  other
\#include directives, and parsing will occur in these files as well.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Mon Mar 11 2013 Fr. Br. George <george@altlinux.ru> 1.0.4-alt2
- Rebuild with new buildreq

* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

