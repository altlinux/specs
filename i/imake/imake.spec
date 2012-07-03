Name: imake
Version: 1.0.5
Release: alt1

Summary: C preprocessor interface to the make utility
License: MIT/X11
Group: Development/C

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

Patch: imake-1.0.5-alt-tmpdir.patch

BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
Imake is used to generate Makefiles from a template, a set of cpp macro
functions,  and  a  per-directory input file called an Imakefile.  This
allows machine dependencies (such as compiler options,  alternate  com-
mand  names,  and  special  make  rules)  to  be kept separate from the
descriptions of the various items to be built.

%prep
%setup

%patch -p1 -b .orig

%build
%autoreconf
%configure \
	--with-config-dir=%_datadir/X11/config

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Mar 26 2012 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5
- Fix build

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2.1
- Automatic buildreqfix
- Autobuild watchfile added

* Mon Jan 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed config directory

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

