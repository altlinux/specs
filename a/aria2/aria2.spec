Name: aria2
Version: 1.29.0
Release: alt1

Summary: aria2 - a simple utility for downloading files faster
License: GPLv2+ with exceptions
Group: Networking/File transfer
Url: http://aria2.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.xz

# Automatically added by buildreq on Thu Mar 23 2006
BuildRequires: gcc-c++ libssl-devel libstdc++-devel
BuildRequires: bison
BuildRequires: cppunit-devel
BuildRequires: gettext libasprintf-devel
BuildRequires: libcares-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgnutls-devel libgnutls-openssl-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel


%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent. It also supports Metalink
version 3.0.

Currently it has following features:
- HTTP/HTTPS GET support
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- FTP support (active, passive mode)
- FTP through HTTP proxy (GET command or tunneling)
- Segmented download
- Cookie support
- It can run as a daemon process.
- BitTorrent protocol support with fast extension.
- Selective download in multi-file torrent
- Metalink version 3.0 support (HTTP/FTP/BitTorrent).
- Limiting download/upload speed

%prep
%setup -n %name-%version
#set_gcc_version 4.7


%build


%configure --enable-bittorrent \
           --enable-metalink \
           --enable-epoll\
           --disable-rpath \
           --with-gnutls \
           --with-libcares \
           --with-libxml2 \
           --with-openssl \
           --with-libz \
           --with-sqlite3


%make

%install
#mkdir -p %buildroot%_bindir
#__install -pD -m755 src/aria2c %buildroot%_bindir/aria2c

%makeinstall
%find_lang aria2 --all-name
#find_lang aria2 --with-man --all-name

ln -s aria2c  %buildroot%_bindir/%name

#sed -i -e '1 s/^/.\\" -*- mode: troff; coding: utf8 -*-\n/;' doc/manual-src/ru/_build/man/aria2c.1

bzip2 doc/manual-src/en/_build/man/aria2c.1
bzip2 doc/manual-src/ru/_build/man/aria2c.1
bzip2 doc/manual-src/pt/_build/man/aria2c.1
rm -f %buildroot%_man1dir/aria2c.1.bz2
install -pD -m644 doc/manual-src/en/_build/man/aria2c.1.bz2 %buildroot%_man1dir/aria2c.1.bz2
install -pD -m644 doc/manual-src/en/_build/man/aria2c.1.bz2 %buildroot%_mandir/en/man1/aria2c.1.bz2
install -pD -m644 doc/manual-src/ru/_build/man/aria2c.1.bz2 %buildroot%_mandir/ru/man1/aria2c.1.bz2
install -pD -m644 doc/manual-src/pt/_build/man/aria2c.1.bz2 %buildroot%_mandir/pt/man1/aria2c.1.bz2

mkdir %buildroot%_docdir/%name-%version
mv %buildroot%_docdir/aria2/* %buildroot%_docdir/%name-%version
#mkdir %buildroot%_docdir/%name-%version/bash_completion
#mv %buildroot%_docdir/aria2/bash_completion/* %buildroot%_docdir/%name-%version/bash_completion
#mkdir %buildroot%_docdir/%name-%version/xmlrpc
#mv %buildroot%_docdir/aria2/xmlrpc/* %buildroot%_docdir/%name-%version/xmlrpc


%files -f aria2.lang
#doc AUTHORS ChangeLog README*
%dir %_docdir/aria2-%version
%_bindir/%name
%_bindir/aria2c
%_man1dir/aria2c.1.bz2
%_mandir/*/man1/aria2c.1.xz
%_docdir/%name-%version/*
%_docdir/%name-%version/bash_completion/*
%_docdir/%name-%version/xmlrpc/*

#_datadir/locale/*/LC_MESSAGES/aria2.mo


%changelog
* Tue Nov 15 2016 Ilya Mashkin <oddity@altlinux.ru> 1.29.0-alt1
- 1.29.0

* Thu Sep 22 2016 Ilya Mashkin <oddity@altlinux.ru> 1.27.1-alt1
- 1.27.1

* Sat Sep 03 2016 Ilya Mashkin <oddity@altlinux.ru> 1.26.1-alt1
- 1.26.1

* Thu Aug 04 2016 Ilya Mashkin <oddity@altlinux.ru> 1.25.0-alt1
- 1.25.0

* Thu Jun 16 2016 Ilya Mashkin <oddity@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Thu Jun 02 2016 Ilya Mashkin <oddity@altlinux.ru> 1.23.0-alt1
- 1.23.0

* Sun Apr 17 2016 Ilya Mashkin <oddity@altlinux.ru> 1.22.0-alt1
- 1.22.0

* Thu Mar 17 2016 Ilya Mashkin <oddity@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Fri Feb 19 2016 Ilya Mashkin <oddity@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Fri Dec 11 2015 Ilya Mashkin <oddity@altlinux.ru> 1.19.3-alt2
- spec updates

* Wed Dec 09 2015 Ilya Mashkin <oddity@altlinux.ru> 1.19.3-alt1
- 1.19.3

* Tue Oct 06 2015 Ilya Mashkin <oddity@altlinux.ru> 1.19.2-alt1
- 1.19.2

* Mon May 25 2015 Ilya Mashkin <oddity@altlinux.ru> 1.19.0-alt1
- 1.19.0

* Sat Feb 21 2015 Ilya Mashkin <oddity@altlinux.ru> 1.18.9-alt2
- fix Russian man encoding (Thanks to Dmitry Levin)

* Wed Feb 04 2015 Ilya Mashkin <oddity@altlinux.ru> 1.18.9-alt1
- 1.18.9

* Wed Sep 17 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.8-alt1
- 1.18.8

* Tue Jul 22 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.7-alt1
- 1.18.7

* Mon Jul 14 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.6-alt1
- 1.18.6
- fix GnuTLS 2.x compatibility

* Mon Mar 03 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.3-alt3
- fix locales man pages

* Thu Feb 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.3-alt2
- Enable more aria2 features (Closes: #29853) Thanks to Andrey Cherepanov

* Mon Jan 20 2014 Ilya Mashkin <oddity@altlinux.ru> 1.18.3-alt1
- 1.18.3
- add aria2c as binary (Closes: #29742)
- add man and locales files

* Sun Dec 29 2013 Ilya Mashkin <oddity@altlinux.ru> 1.18.2-alt1
- 1.18.2

* Mon Oct 28 2013 Ilya Mashkin <oddity@altlinux.ru> 1.18.1-alt1
- 1.18.1

* Sat Sep 14 2013 Ilya Mashkin <oddity@altlinux.ru> 1.18.0-alt1
- 1.18.0

* Tue May 28 2013 Ilya Mashkin <oddity@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Tue Mar 26 2013 Ilya Mashkin <oddity@altlinux.ru> 1.16.5-alt1
- 1.16.5

* Sat Feb 09 2013 Ilya Mashkin <oddity@altlinux.ru> 1.16.3-alt1
- 1.16.3

* Fri Jan 04 2013 Ilya Mashkin <oddity@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Sun Dec 09 2012 Ilya Mashkin <oddity@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Tue Oct 02 2012 Ilya Mashkin <oddity@altlinux.ru> 1.15.2-alt1
- 1.15.2

* Wed May 30 2012 Ilya Mashkin <oddity@altlinux.ru> 1.15.1-alt1
- 1.15.1
- Update description

* Wed Feb 29 2012 Ilya Mashkin <oddity@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Tue Dec 27 2011 Ilya Mashkin <oddity@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Wed Aug 03 2011 Ilya Mashkin <oddity@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Thu Jun 16 2011 Ilya Mashkin <oddity@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Sat Apr 02 2011 Ilya Mashkin <oddity@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.8-alt1
- 1.10.8

* Wed Dec 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.7-alt1
- 1.10.7

* Thu Nov 04 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Sat Oct 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.5-alt1
- 1.10.5

* Fri Oct 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.4-alt1
- 1.10.4

* Thu Sep 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Tue Aug 31 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Sun Aug 29 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Jul 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.5-alt1
- 1.9.5

* Sat Jun 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.4-alt1
- 1.9.4

* Sat May 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Sun May 02 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Fri Apr 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Mon Mar 29 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Wed Feb 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Feb 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sun Jan 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Jan 07 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Dec 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Sun Nov 15 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Mon Oct 12 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Wed Oct 07 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Thu Jul 29 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Jul 21 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Jun 16 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon May 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Apr 28 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Apr 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sat Feb 21 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed Nov 26 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Thu Oct 09 2008 Ilya Mashkin <oddity@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Sat Sep 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.15.3-alt1
- 0.15.3

* Fri Aug 29 2008 Ilya Mashkin <oddity@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Thu Jul 03 2008 Ilya Mashkin <oddity@altlinux.ru> 0.14.0-alt1
- 0.14.0+1

* Mon May 26 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.2-alt1
- 0.13.2

* Tue Mar 20 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.1-alt1
- 0.13.1+1

* Wed Mar 05 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Sun Feb 17 2008 Ilya Mashkin <oddity@altlinux.ru> 0.12.1-alt1
- 0.12.1+1

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.0-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Jul 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jun 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Jun 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat May 27 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue May 02 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Wed Apr 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Mar 23 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Fri Feb 24 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Mon Feb 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.1.0-alt1
- First version

