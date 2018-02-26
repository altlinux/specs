Name: lndir
Version: 1.0.3
Release: alt1

Summary: create a shadow directory of symbolic links to another directory tree
License: MIT/X11
Group: Development/C

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
The lndir program makes  a  shadow  copy  todir  of  a  directory  tree
fromdir,  except  that  the shadow is not populated with real files but
instead with symbolic links pointing at the real files in  the  fromdir
directory tree.  This is usually useful for maintaining source code for
different machine architectures.  You create a  shadow  directory  con-
taining  links  to the real source, which you will have usually mounted
from a remote machine.  You can build  in  the  shadow  tree,  and  the
object files will be in the shadow directory, while the source files in
the shadow directory are just symlinks to the real files.

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
* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

