Name: libieee1284
Version: 0.2.11
Release: alt2.qa1

Summary: A library for interfacing IEEE 1284-compatible devices

License: GPL
Group: System/Libraries
Url: http://sf.net/projects/libieee1284

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

Requires: common-licenses

# Automatically added by buildreq on Sun Oct 08 2006
BuildRequires: gcc-c++

%description
The libieee1284 library is for communicating with parallel port devices.

%package devel
Summary: Files for developing applications that use libieee1284
Requires: %name = %version
Group: Development/C

%description devel
The header files and man pages for developing applications that use
libieee1284.

%prep
%setup

%build
%configure --disable-static --without-python
%make_build
# xmlto requires big tetex
#xmlto -o doc html-nochunks doc/interface.xml

%install
%makeinstall
ln -s -f /usr/share/license/GPL-2 COPYING

%files
%_bindir/*
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README.* TODO
%doc --no-dereference COPYING

%files devel
%doc doc/interface.xml
#%doc doc/interface.html
%_includedir/ieee1284.h
%_libdir/*.so
%_man3dir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.11-alt2
- cleanup spec

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.11-alt1
- new version 0.2.11 (with rpmrb script)

* Sun Oct 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.10-alt0.1
- new version 0.2.10, fix source URL, update buildreq
- change packager, disable python module, cleanup spec

* Sat Apr 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.2.8-alt1
- new version
- do not build static libs
- do not package .la

* Tue Sep 10 2002 AEN <aen@altlinux.ru> 0.2.1-alt2
- Group name fixed

* Mon Sep 09 2002 AEN <aen@altlinux.ru> 0.2.1-alt1
- first build for Sisyphus

* Sat Aug 24 2002 Tim Waugh <twaugh@redhat.com>
- Ship test program.

* Sat Aug  3 2002 Tim Waugh <twaugh@redhat.com>
- The archive is now distributed in .tar.bz2 format.

* Fri Apr 26 2002 Tim Waugh <twaugh@redhat.com>
- No need to create man page symlinks any more.
- Build requires xmlto now, not docbook-utils.

* Wed Apr 24 2002 Tim Waugh <twaugh@redhat.com>
- The tarball builds its own man pages now; just adjust the symlinks.
- Run ldconfig.

* Mon Jan  7 2002 Tim Waugh <twaugh@redhat.com>
- Ship the PDF file with the devel package.

* Thu Nov 15 2001 Tim Waugh <twaugh@redhat.com>
- Initial specfile.
