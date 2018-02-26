%define _optlevel s

Name: rtorrent
Version: 0.8.7
Release: alt1

Summary: rTorrent - rakshasa's ncurses BitTorrent client using librTorrent
Group: Networking/File transfer
License: GPL2
Url: http://libtorrent.rakshasa.no/
Packager: Alexey Morsov <swi@altlinux.ru>

Source0: %name-%version.tar
Patch0: %name-man-alt.patch

BuildRequires: gcc-c++ libcurl-devel libidn-devel libncursesw-devel libsigc++2.0-devel libssl-devel libstdc++-devel libtinfo-devel zlib-devel libgssapi-devel
BuildRequires: cppunit-devel
BuildRequires: libxmlrpc-devel >= 0.12.2 libxml2-devel

BuildRequires: libtorrent-devel >= 0.12.6-alt1
Requires: libtorrent0.12 >= 0.12.7-alt1

%description
rTorrent is a ncurses based client and is therefor ideal to use with
screen. rTorrent features:

* Use an URL or file path to add torrents at runtime.
* Emacs'ish find-file support for opening torrents.
* Stop/delete/resume torrents.
* Optionally loads/saves/deletes torrents automatically in a session
  directory.
* Safe fast resume support.
* Shows lots of information about peers and the torrent.
* Only one torrent at a time is checked.

%prep
%setup -q
%patch0 -p1
mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING


%build
%autoreconf
%configure --with-xmlrpc-c
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS TODO doc/rtorrent.rc

%_bindir/%name
%_man1dir/*

%changelog
* Sat Nov 13 2010 Alexey Morsov <swi@altlinux.ru> 0.8.7-alt1
- new version
- clean spec-file
- put man back (patch)

* Fri Jan 15 2010 Alexey Morsov <swi@altlinux.ru> 0.8.6-alt1
- new version

* Tue Aug 04 2009 Alexey Morsov <swi@altlinux.ru> 0.8.5-alt2
- remove unnecessary doc files (bug #19029)

* Wed Jul 15 2009 Alexey Morsov <swi@altlinux.ru> 0.8.5-alt1
- new version

* Mon May 11 2009 Alexey Morsov <swi@altlinux.ru> 0.8.4-alt2
- fix build with gcc4.4

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 0.8.4-alt1
- new version

* Thu Nov 06 2008 Alexey Morsov <swi@altlinux.ru> 0.8.3-alt1
- new version

* Fri Jul 25 2008 Alexey Morsov <swi@altlinux.ru> 0.8.2-alt3
[ Alexey Morsov ]
- spec fix
  + change librtorrent to libtorrent

* Sat May 31 2008 Alexey Morsov <swi@altlinux.ru> 0.8.2-alt2
- fix BuildRequires for libxmlrpc

* Tue May 20 2008 Alexey Morsov <swi@altlinux.ru> 0.8.2-alt1
- new version
- enable scgi support (#15686)

* Wed Jan 30 2008 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1
- version 0.8.0
- new with DHT support

* Tue Dec 11 2007 Alexey Morsov <swi@altlinux.ru> 0.7.9-alt1
- version 0.7.9

* Sun Oct 14 2007 Alexey Morsov <swi@altlinux.ru> 0.7.8-alt1
- version 0.7.8
- Added Peer Exchange support, enable with the "peer_exchange=yes" 
option.
- Fixed the wrong tracker requests being sent when finishing a torrent.
- Renamed all commands to from e.g "get_d_*" to "d.get_*". Remember to 
update your rc file.
- Improved XMLRPC support, including support for 64bit ints, removed 
defective FastCGI support

* Tue Aug 07 2007 Alexey Morsov <swi@altlinux.ru> 0.7.5-alt1
- version 0.7.5
- now compile over libncursesw (thanks to thresh)
- Fixed a bug that caused piped requests to be lost.
- The old option handler has been rewritten.

* Tue Aug 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7.4-alt1.1
- Build with libncursesw-devel.

* Mon Apr 09 2007 Alexey Morsov <swi@altlinux.ru> 0.7.4-alt1
- new version
- remove patch (now use subst)
- fix spec and buildrequires

* Mon Feb 12 2007 Alexey Morsov <swi@altlinux.ru> 0.6.4-alt3
- add libgssapi-devel (new libcurl?)

* Tue Jan 09 2007 Alexey Morsov <swi@altlinux.ru> 0.6.4-alt2
- fix for librtorrent (rename libtorrent)

* Mon Nov 13 2006 Andrei Bulava <abulava@altlinux.ru> 0.6.4-alt1
- 0.6.4
- built with "-Os" instead of "-O2" as suggested by upstream
  (thanks to reporters of #10248 for pointing at random segfaults)

* Mon Sep 11 2006 Andrei Bulava <abulava@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Thu May 04 2006 Andrei Bulava <abulava@altlinux.ru> 0.4.5-alt1
- 0.4.5
- replaced COPYING with a symlink to the system-wide GPL-2 text

* Fri Nov 18 2005 Andrei Bulava <abulava@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Fri Oct 28 2005 Andrei Bulava <abulava@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Mon Sep 26 2005 Andrei Bulava <abulava@altlinux.ru> 0.3.0-alt1
- 0.3.0
- minor spec fixes regarding build process

* Mon Jun 13 2005 Andrei Bulava <abulava@altlinux.ru> 0.2.4-alt1
- initial build for ALT Linux
