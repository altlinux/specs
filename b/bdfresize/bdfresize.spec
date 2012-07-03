# spec file for package bdfresize (Version 1.5)
# Copyright (c) 2005 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
# Please submit bugfixes or comments via http://www.suse.de/feedback/

Name: bdfresize
Version: 1.5
Release: alt2

Summary: A Tool for Resizing BDF Format Fonts
License: GPL
Group: System/X11

Url: http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/
#Original source: http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/bdfresize-1.5.tar.gz
Source: http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/%name-%version.tar.bz2
Patch: http://developer.momonga-linux.org/viewcvs/*checkout*/trunk/pkgs/bdfresize/bdfresize-1.5-gcc34.patch

Packager: Michael Shigorin <mike@altlinux.org>

#set_gcc_version 3.3

%description
Bdfresize is a command for magnifying or shrinking fonts which are
described in the standard BDF format.

Authors:
--------
    Hiroto Kagotani <kagotani@cs.titech.ac.jp>
    Kazuhiko <kazuhiko@ring.gr.jp>
    Masao Uebayashi <uebayasi@soum.co.jp>

%prep
%setup
%patch -p1 -b .gcc34

%build
%__rm -f config.cache
CFLAGS="%optflags" %configure
%make

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%_man1dir/*

%changelog -n bdfresize
* Thu Oct 20 2005 Michael Shigorin <mike@altlinux.org> 1.5-alt2
- applied gcc34 patch from Momonga Linux
- removed INSTALL file

* Fri May 13 2005 Michael Shigorin <mike@altlinux.ru> 1.5-alt1
- built for ALT Linux (efont-unicode build dep)
- based on SuSE 9.3 package
- spec cleanup

* Sun Jan 11 2004 - adrian@suse.de
- build as user
* Wed Nov 14 2001 - mfabian@suse.de
- new package: bdfresize-1.5
